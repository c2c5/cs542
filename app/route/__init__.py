from flask import Blueprint, render_template, request, flash
from util import database
from app.accounts.session import require_oneof_roles
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/RoutePictures'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

routes = Blueprint('routes', __name__,
                        template_folder='view')

@routes.route('/routes')
def Route():
    db = database.get_db()
    with db.cursor() as cursor:
        get_routes_query = "SELECT routeid, set_by, difficulty, picture, student_name from Route, User WHERE Route.set_by = User.userid"
        cursor.execute(get_routes_query)
        result = cursor.fetchall()
    return render_template('Route.html', routes=result)


@routes.route('/SetRoutes',methods=["GET","POST"])
@require_oneof_roles("setter")
def SetRoutes():
    if request.method == "POST":
        db = database.get_db()
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with db.cursor() as cursor:
            difficulty = request.form["Difficulty"]
            picture = file.filename
            set_by = request.form["SetBy"]
            add_route_query = "INSERT INTO Route (set_by, difficulty, picture) VALUES " + \
                              "(%s, %s, %s);"
            cursor.execute(add_route_query, (set_by, difficulty, picture))
            db.commit()
            flash('Created a route', 'success')
            return render_template('SetRoute.html')
    else:
        return render_template('SetRoute.html')

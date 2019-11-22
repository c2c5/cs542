from flask import Blueprint, render_template, request, flash
from util import database
from app.accounts.session import require_oneof_roles, current_user, current_user_roles
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import uuid

UPLOAD_FOLDER = 'static/RoutePictures'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

routes = Blueprint('routes', __name__,
                        template_folder='view')

@routes.route('/routes', methods=["GET", "POST"])
def Route():
    db = database.get_db()
    with db.cursor() as cursor:
        get_routes_query = "SELECT routeid, set_by, difficulty, picture, student_name from Route, User WHERE Route.set_by = User.userid"
        cursor.execute(get_routes_query)
        result = cursor.fetchall()

    if request.method == "POST":
        if ("delete" in request.form):
            with db.cursor() as cursor:
                routedel = "DELETE FROM Route WHERE routeid=%s"
                cursor.execute(routedel, (request.form["delete"]))
            db.commit()
            return redirect(url_for('routes.Route', **request.args))

    return render_template('Route.html', routes=result)

@routes.route('/SetRoutes',methods=["GET","POST"])
@require_oneof_roles("setter", "admin")
def SetRoutes():
    db = database.get_db()
    with db.cursor() as cursor:
        get_name_query = "SELECT U.userid, role, student_name from User U, UserRoles R WHERE R.role = %s AND U.userid=R.userid"
        cursor.execute(get_name_query, "setter")
        entries = cursor.fetchall()

    if request.method == "POST":
        file = request.files['file']
        picture = ""
        if file and allowed_file(file.filename):
            strs = file.filename.split(".")[-1]
            picture = str(uuid.uuid1()) + "." + strs
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], picture))
        with db.cursor() as cursor:
            difficulty = request.form["Difficulty"]
            if ("admin" not in current_user_roles()):
                set_by = current_user()["userid"]
            else:
                set_by = request.form["SetBy"]

            if(int(difficulty) < 10):
                add_route_query = "INSERT INTO Route (set_by, difficulty, picture) VALUES " + \
                                  "(%s, %s, %s);"
                cursor.execute(add_route_query, (set_by, difficulty, picture))
                db.commit()
                flash('Created a route', 'success')
            else:
                flash('Difficulty should in 1-10', 'danger')
            return render_template('SetRoute.html',entries = entries)
    else:
        return render_template('SetRoute.html',entries = entries)


@routes.route('/Edit/<id>',methods=["GET","POST"])
@require_oneof_roles("setter", "admin")
def EditRoutes(id):
    db = database.get_db()
    with db.cursor() as cursor:
        get_name_query = "SELECT U.userid, role,student_name from User U, UserRoles R WHERE R.role = %s AND U.userid=R.userid"
        cursor.execute(get_name_query, "setter")
        setters = cursor.fetchall()

        get_old_data = "SELECT * FROM Route WHERE routeid=%s"
        cursor.execute(get_old_data, id)
        old_data = cursor.fetchone()

    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            strs = filename.split(".")[-1]
            picture = str(uuid.uuid1()) + "." + strs
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], picture))
        with db.cursor() as cursor:
            difficulty = request.form["Difficulty"]

            if ("admin" not in current_user_roles()):
                set_by = current_user()["userid"]
            else:
                set_by = request.form["SetBy"]

            if file:
                add_route_query = "UPDATE Route SET set_by=%s, difficulty=%s, picture= %s WHERE routeid = %s;"
                cursor.execute(add_route_query, (set_by, difficulty, picture, id))
            else:
                add_route_query = "UPDATE Route SET set_by=%s, difficulty=%s WHERE routeid = %s;"
                cursor.execute(add_route_query, (set_by, difficulty, id))

            if (int(difficulty) < 10):
                db.commit()
                flash('Updated a route', 'success')
                return redirect(url_for('routes.Route'))
            else:
                flash('Difficulty should in 1-10', 'danger')

        return render_template('Edit.html',setters = setters, old_data=old_data)

    else:
        return render_template('Edit.html',setters = setters, old_data=old_data)

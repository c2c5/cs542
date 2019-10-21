from flask import Blueprint, render_template, request, flash
from util import database
from app.accounts.session import require_oneof_roles

routes = Blueprint('routes', __name__,
                        template_folder='view')

@routes.route('/routes')
def Route():
    db = database.get_db()
    with db.cursor() as cursor:
        get_routes_query = "SELECT routeid, set_by, difficulty from Route"
        cursor.execute(get_routes_query)
        result = cursor.fetchall()
    return render_template('Route.html', routes=result)


@routes.route('/routes/routespicture')
def RoutePicture():
    db = database.get_db()
    with db.cursor() as cursor:
        get_routespic_query = "SELECT picture from Route WHERE routeid = %s"
        ##cursor.execute(get_routespic_query,request.args.get("routeid"))
        cursor.execute(get_routespic_query,request.args.get("routeid"))
        result = cursor.fetchone()
    return render_template('RoutePicture.html', routepic=result)

@routes.route('/SetRoutes',methods=["GET","POST"])
@require_oneof_roles("setter")
def SetRoutes():
    if request.method == "POST":
        db = database.get_db()
        with db.cursor() as cursor:
            routeid = request.form["RouteID"]
            difficulty = request.form["Difficulty"]
            picture = request.form["PictureURL"]
            set_by = request.form["SetBy"]
            add_route_query = "INSERT INTO Route (routeid, set_by, difficulty, picture) VALUES " + \
                              "(%s, %s, %s, %s);"
            cursor.execute(add_route_query, (routeid, set_by, difficulty, picture))
            db.commit()
            flash('Created a route', 'success')
            return render_template('SetRoute.html')
    else:
        flash("Please ReEnter")
        return render_template('SetRoute.html')

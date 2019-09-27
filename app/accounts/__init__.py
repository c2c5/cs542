from flask import Blueprint, render_template, abort, request, redirect, url_for, flash, make_response
from jinja2 import TemplateNotFound
from util import database
from app.accounts.session import current_user, invalidate_token, CS542_TOKEN_COOKIE, CS542_TOKEN_COOKIE_EXPIRY
import bcrypt
import hashlib
import secrets

accounts = Blueprint('accounts', __name__,
                        template_folder='view')

@accounts.route('/')
def show():
    try:
        user = current_user()
        if (user is not None):
            return render_template('user.html', user=user)
        else:
            return redirect(url_for('accounts.signup'))
    except TemplateNotFound:
        abort(500)

@accounts.route('/login', methods=["GET","POST"])
def signin():
    user = current_user()
    if (request.method == "GET"):
        return render_template('login.html')
    elif (request.method == "POST"):

        db = database.get_db()
        with db.cursor() as cursor:
            #studentIDHash = hashlib.sha512(request.form["studentID"].encode('utf-8')).hexdigest()
            studentIDHash = request.form["studentID"]
            get_user_login = "SELECT password_hash, userid, student_name FROM User WHERE student_id=%s;"
            cursor.execute(get_user_login, studentIDHash)
            result = cursor.fetchone()
            #if (cursor.rowcount == 1 and bcrypt.checkpw(request.form["password"].encode('utf-8'), result['password_hash'].encode('utf-8'))):
            if (cursor.rowcount == 1 and request.form["password"] == result['password_hash']):
                ## User successfuly authenticated, make the session for the user.
                session_token = secrets.token_hex(30)
                make_user_session = "INSERT INTO LoginSession (userid, token) VALUES (%s, %s);"
                cursor.execute(make_user_session, (result['userid'], session_token))
                if (cursor.rowcount == 1):
                    db.commit()
                    resp = make_response(redirect('/'))
                    resp.set_cookie(CS542_TOKEN_COOKIE, session_token)

                    flash('Welcome, %s.' % result['student_name'], 'success')
                    return resp
                else:
                    flash('Login Failed.', 'danger')
                    return render_template('login.html')
            else:
                flash('Login Failed.', 'danger')
                return render_template('login.html')
            return ""

@accounts.route('/logout', methods=["GET","POST"])
def signout():
    if (current_user() is not None):
        invalidate_token(current_user()['session_token'])
        resp = make_response(redirect('/'))
        resp.set_cookie(CS542_TOKEN_COOKIE, '', 0)
        flash('Logged Out', 'success')
        return resp
    else:
        abort(500)

@accounts.route('/new', methods=["GET","POST"])
def signup():
    if request.method == "POST":
        ## Post method, process data
        for _, v in request.form.items():
            if v is None or v.strip() == "":
                flash('Make sure that you fill in every field', 'danger')
                return redirect(url_for('accounts.signup', **request.args))

        if (request.form["password"] != request.form["confirmpassword"]):
            flash('Make sure that your passwords match', 'danger')
            return redirect(url_for('accounts.signup', **request.args))
        
        db = database.get_db()
        with db.cursor() as cursor:
            salt = bcrypt.gensalt()
            #studentIDHash = hashlib.sha512(request.form["studentID"].encode('utf-8')).hexdigest()
            studentIDHash = request.form["studentID"]
            add_user_query = "INSERT INTO User (student_id, student_name, join_date, password_hash) VALUES " + \
                             "(%s, %s, CURDATE(), %s);"
            #cursor.execute(add_user_query, (studentIDHash, request.form["name"], bcrypt.hashpw(request.form["password"].encode('utf-8'), salt)))
            cursor.execute(add_user_query, (studentIDHash, request.form["name"], request.form["password"]))
            if (cursor.rowcount == 1):
                db.commit()
                flash('Created user account', 'success')
                return redirect(url_for('accounts.signup', **request.args))
            else:
                flash('Error creating user. Does one already exist?', 'danger')
                return redirect(url_for('accounts.signup', **request.args))
    else:
        ## Get method, show the form
        try:
            # Pre-fill id if supplied.
            id = ''
            if ('id' in request.args.keys()):
                id = request.args["id"]
            return render_template('register.html', id=id)

        except TemplateNotFound:
            abort(500)


@accounts.route('/routes')
def Route():
    db = database.get_db()
    with db.cursor() as cursor:
        get_routes_query = "SELECT routeid, set_by from Route"
        cursor.execute(get_routes_query)
        result = cursor.fetchall()
    return render_template('Route.html', routes=result)


@accounts.route('/routes/routespicture')
def RoutePicture():
    db = database.get_db()
    with db.cursor() as cursor:
        get_routespic_query = "SELECT picture from Route WHERE routeid = %s"
        cursor.execute(get_routespic_query,request.args.get("routeid"))
        result = cursor.fetchone()
    return render_template('RoutePicture.html', routepic=result)


@accounts.route('/scores')
def Scores():
    db = database.get_db()
    with db.cursor() as cursor:
        get_scores_query = "SELECT eventid, score from TournamentParticipants"
        cursor.execute(get_scores_query)
        result = cursor.fetchall()
    return render_template('TournamentParticipants.html', records=result)

@accounts.route('/SetRoutes',methods=["GET","POST"])
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

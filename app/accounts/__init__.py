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
            studentIDHash = hashlib.sha512(request.form["studentID"].encode('utf-8')).hexdigest()
            get_user_login = "SELECT password_hash, userid, student_name FROM User WHERE student_id=%s;"
            cursor.execute(get_user_login, studentIDHash)
            result = cursor.fetchone()
            if (cursor.rowcount == 1 and bcrypt.checkpw(request.form["password"].encode('utf-8'), result['password_hash'].encode('utf-8'))):
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
            studentIDHash = hashlib.sha512(request.form["studentID"].encode('utf-8')).hexdigest()
            add_user_query = "INSERT INTO User (student_id, student_name, join_date, password_hash) VALUES " + \
                             "(%s, %s, CURDATE(), %s);"
            cursor.execute(add_user_query, (studentIDHash, request.form["name"], bcrypt.hashpw(request.form["password"].encode('utf-8'), salt)))
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
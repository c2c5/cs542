from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from util import database
import bcrypt

accounts = Blueprint('accounts', __name__,
                        template_folder='view')

@accounts.route('/')
def show():
    try:
        return render_template('test.html')
    except TemplateNotFound:
        abort(500)

@accounts.route('/login', methods=["GET","POST"])
def signin():
    return 0

@accounts.route('/logout', methods=["GET","POST"])
def signout():
    return 0

@accounts.route('/new', methods=["GET","POST"])
def signup():
    if request.method == "POST":
        ## Post method, process data
        for k, v in request.form.items():
            if v is None or v.strip() == "":
                flash('Make sure that you fill in every field', 'danger')
                return redirect(url_for('accounts.signup', **request.args))

        if (request.form["password"] != request.form["confirmpassword"]):
            flash('Make sure that your passwords match', 'danger')
            return redirect(url_for('accounts.signup', **request.args))
        
        db = database.get_db()
        with db.cursor() as cursor:
            salt = bcrypt.gensalt()
            print(len(salt))
            add_user_query = "INSERT INTO User (student_id, student_name, join_date, password_hash) VALUES " + \
                             "(%s, %s, CURDATE(), %s);"
            cursor.execute(add_user_query, (request.form["studentID"], request.form["name"], bcrypt.hashpw(request.form["password"].encode('utf-8'), salt)))
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
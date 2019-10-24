from flask import Blueprint, render_template, redirect, abort, url_for, request, flash
from app.accounts.session import current_user
from jinja2 import TemplateNotFound
from util import database

events = Blueprint('events', __name__, template_folder='view')

@events.route('/')
def show():
    try:
        user = current_user()
        if (user is not None):
            db = database.get_db()
            with db.cursor() as cursor:
                get_event = "SELECT eventid, name, start, end FROM event;"
                cursor.execute(get_event)
                entries = cursor.fetchall()
                return render_template('events.html', entries=entries)
        else:
            return redirect(url_for('accounts.signup'))
    except TemplateNotFound:
        abort(500)

@events.route('/detail/<id>')
def show_info(id):
    db = database.get_db()
    with db.cursor() as cursor:
        get_event_info = "SELECT name, start, end, description, max_participants, cost, paid_members_only FROM event WHERE eventid=%s;"
        cursor.execute(get_event_info, id)
        entries = cursor.fetchall()
        get_opener = "SELECT student_name FROM user AS u, event AS e WHERE u.userid = e.opener and e.eventid=%s;"
        cursor.execute(get_opener, id)
        openers = cursor.fetchall()
        return render_template('event_info.html', entries=entries, openers=openers)

@events.route('/edit/<id>', methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        db = database.get_db()
        with db.cursor() as cursor:
            get_event_info = "SELECT name, start, end, description, max_participants, cost, paid_members_only FROM event WHERE eventid=%s;"
            cursor.execute(get_event_info, id)
            entries = cursor.fetchall()
            get_opener = "SELECT userid, student_name from userdatawithrole where roles = 'opener' or roles = 'admin'"
            cursor.execute(get_opener)
            openers = cursor.fetchall()
        try:
            return render_template('event_edit.html', entries=entries, openers=openers)
        except TemplateNotFound:
            abort(500)
    else:
        db = database.get_db()
        with db.cursor() as cursor:
            update_event = "UPDATE event SET name=%s, description=%s, start=%s, end=%s, max_participants=%s, cost=%s, paid_members_only=%s, " + \
                "opener=%s WHERE eventid=%s;"
            cursor.execute(update_event, (request.form['event_name'], request.form['description'],
                                             request.form['start'], request.form['end'], request.form['max_participants'],
                                             request.form['cost'], request.form['PMO_Options'], request.form['opener'], id))
            print(cursor.rowcount)
            if (cursor.rowcount == 1):
                db.commit()
                flash('Changed event infomation', 'success')
                return redirect(url_for('events.show_info', id=id, **request.args))

@events.route('/create', methods=["GET", "POST"])
def create():
    db = database.get_db()
    with db.cursor() as cursor:
        get_opener = "SELECT userid, student_name from userdatawithrole where roles = 'opener' or roles = 'admin'"
        cursor.execute(get_opener)
        entries = cursor.fetchall()
    if request.method == "POST":
        db = database.get_db()
        with db.cursor() as cursor:
            add_event_query = "INSERT INTO event(name, description, start, end, max_participants, cost, paid_members_only, opener) VALUES" + \
                              "(%s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(add_event_query, (request.form['event_name'], request.form['description'],
                                             request.form['start'], request.form['end'], request.form['max_participants'],
                                             request.form['cost'], request.form['PMO_Options'], request.form['opener']))
            if (cursor.rowcount == 1):
                db.commit()
                flash('Created event', 'success')
                return redirect(url_for('events.show', **request.args))
            else:
                flash('Error creating user.', 'danger')
                return redirect(url_for('events.show', **request.args))
    else:
        try:
            return render_template('create.html', entries=entries)
        except TemplateNotFound:
            abort(500)

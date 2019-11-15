from flask import Blueprint, render_template, redirect, abort, url_for, request, flash
from app.accounts.session import current_user
from jinja2 import TemplateNotFound
from util import database
import pymysql

events = Blueprint('events', __name__, template_folder='view')

@events.route('/', methods=["GET", "POST"])
def show():
    if request.method == "GET":
        try:
            db = database.get_db()
            with db.cursor() as cursor:
                get_event = "SELECT e.eventid, e.name, e.start, e.end, e.actual_end, e.description, e.max_participants, " \
                            "e.cost, e.paid_members_only, e.opener, u.student_name FROM event AS e LEFT JOIN user AS u ON e.opener=u.userid;"
                cursor.execute(get_event)
                entries = cursor.fetchall()
            return render_template('events.html', entries=entries)
        except TemplateNotFound:
            abort(500)
    else:
        db = database.get_db()
        with db.cursor() as cursor:
            if 'delete' in request.form:
                delete_event = "DELETE FROM event WHERE eventid=%s;"
                cursor.execute(delete_event, request.form['delete'])
                if cursor.rowcount == 1:
                    db.commit()
                    flash('Event has been deleted', 'success')
                    return redirect(url_for('events.show', **request.args))
                else:
                    flash('Event has not been deleted successfully', 'danger')
                    return redirect(url_for('events.show', **request.args))
            else:
                close_event = "UPDATE event SET actual_start=CURRENT_TIMESTAMP() WHERE eventid=%s;"
                cursor.execute(close_event, request.form['eventid'])
                if cursor.rowcount == 1:
                    db.commit()
                    flash('Event has been opened!', 'success')
                    return redirect(url_for('checkin.checkinout', id=request.form['eventid'], **request.args))
                else:
                    flash('Event has not been opened successfully!', 'danger')
                    return redirect(url_for('events.show', **request.args))

@events.route('/detail/<id>')
def show_info(id):
    db = database.get_db()
    with db.cursor() as cursor:
        get_event_info = "SELECT name, start, end, description, max_participants, cost, paid_members_only FROM Event WHERE eventid=%s;"
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
            get_event_info = "SELECT name, start, end, description, max_participants, cost, paid_members_only, opener FROM event WHERE eventid=%s;"
            cursor.execute(get_event_info, id)
            entries = cursor.fetchall()
            get_opener = "SELECT userid, student_name from userdatawithrole where roles LIKE '%opener%'"
            cursor.execute(get_opener)
            openers = cursor.fetchall()
        try:
            return render_template('event_edit.html', entries=entries, openers=openers)
        except TemplateNotFound:
            abort(500)
    else:
        try:
            db = database.get_db()
            with db.cursor() as cursor:
                update_event = "UPDATE event SET name=%s, description=%s, start=%s, end=%s, max_participants=%s, cost=%s, paid_members_only=%s, " + \
                    "opener=%s WHERE eventid=%s;"
                opener = None if (request.form['opener'] == "None") else request.form['opener']
                cursor.execute(update_event, (request.form['event_name'], request.form['description'],
                                                 request.form['start'], request.form['end'], request.form['max_participants'],
                                                 request.form['cost'], request.form['PMO_Options'], opener, id))
                if (cursor.rowcount == 1):
                    db.commit()
                    flash('Event infomation has been changed! ', 'success')
                    return redirect(url_for('events.show_info', id=id, **request.args))
                else:
                    flash('Check if you insert the correct information', 'danger')
                    return redirect(url_for('events.show_info', id=id, **request.args))
        except pymysql.InternalError as e:
            flash(e.args[1], 'danger')
            return redirect(url_for('events.show_info', id=id, **request.args))

@events.route('/create', methods=["GET", "POST"])
def create():
    db = database.get_db()
    with db.cursor() as cursor:
        get_opener = "SELECT userid, student_name from userdatawithrole where roles LIKE '%opener%';"
        cursor.execute(get_opener)
        entries = cursor.fetchall()
    if request.method == "POST":
        try:
            db = database.get_db()
            with db.cursor() as cursor:
                add_event_query = "INSERT INTO event(name, description, start, end, max_participants, cost, paid_members_only, opener) VALUES" + \
                                  "(%s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(add_event_query, (request.form['event_name'], request.form['description'],
                                                 request.form['start'], request.form['end'], request.form['max_participants'],
                                                 request.form['cost'], request.form['PMO_Options'], request.form['opener']))
                if (cursor.rowcount == 1):
                    db.commit()
                    flash('Created event', 'success')
                    return redirect(url_for('events.show', **request.args))
                else:
                    flash('Check if you insert the correct information', 'danger')
                    return redirect(url_for('events.show', **request.args))
        except pymysql.InternalError as e:
            flash(e.args[1], 'danger')
            return redirect(url_for('events.show', **request.args))
    else:
        try:
            return render_template('create.html', entries=entries)
        except TemplateNotFound:
            abort(500)

@events.route('/my_events')
def show_my_events():
    try:
        user = current_user()
        if (user is not None):
            db = database.get_db()
            with db.cursor() as cursor:
                get_event = "SELECT e.name AS name, t.start AS start, t.end AS end, t.total_time AS total_time FROM " + \
                            "timeentry AS t, event AS e WHERE e.eventid=t.eventid and t.userid=%s;"
                cursor.execute(get_event, user['userid'])
                entries = cursor.fetchall()
                return render_template('my_events.html', entries=entries)
        else:
            return redirect(url_for('accounts.signup'))
    except TemplateNotFound:
        abort(500)

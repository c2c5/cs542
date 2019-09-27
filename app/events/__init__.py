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
                get_event = "SELECT name, description, start, end, cost FROM event;"
                cursor.execute(get_event)
                #print(cursor.fetchall())
                #entries = [dict(name=row[0], des=row[1], start=row[2], end=row[3], cost=row[4]) for row in cursor.fetchall()]
                #print(entries)
                entries = cursor.fetchall()
                return render_template('events.html', entries=entries)
        else:
            return redirect(url_for('accounts.signup'))
    except TemplateNotFound:
        abort(500)

@events.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        db = database.get_db()
        with db.cursor() as cursor:
            add_event_query = "INSERT INTO event(name, description, start, end, max_participants, cost, paid_members_only) VALUES" + \
                              "(%s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(add_event_query, (request.form['event_name'], request.form['description'],
                                             request.form['start'], request.form['end'], request.form['max_participants'],
                                             request.form['cost'], request.form['PMO_Options']))
            if (cursor.rowcount == 1):
                db.commit()
                flash('Created user account', 'success')
                return redirect(url_for('events.show', **request.args))
            else:
                flash('Error creating user.', 'danger')
                return redirect(url_for('events.show', **request.args))
    else:
        try:
            return render_template('create.html')
        except TemplateNotFound:
            abort(500)

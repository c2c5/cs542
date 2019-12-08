from flask import Blueprint, render_template, redirect, abort, url_for, request, flash
from app.accounts.session import current_user
from jinja2 import TemplateNotFound
from util import database
import pymysql
import math

events = Blueprint('events', __name__, template_folder='view')

@events.route('/', methods=["GET", "POST"])
def show():
    if request.method == "GET":
        try:
            db = database.get_db()
            with db.cursor() as cursor:

                # Filtration criteria
                query_conditions = []
                for arg, val in request.args.items():
                    if (arg == "free" and val is not "" and int(val) == 1):
                        query_conditions.append("paid_members_only=0 AND cost=0")
                    elif (arg == "free" and val is not "" and int(val) == 0):
                        query_conditions.append("paid_members_only=1 AND cost=0")
                    elif (arg == "tournament" and val is not "" and int(val) == 1):
                        query_conditions.append("tournament_result_unit IS NOT NULL and tournament_result_ordering IS NOT NULL")
                    elif (arg == "tournament" and val is not "" and int(val) == 0):
                        query_conditions.append("tournament_result_unit IS NULL and tournament_result_ordering IS NULL")
                    elif (arg == "maxcost" and val is not "" and val.isnumeric()):
                        query_conditions.append("cost <= %s" % db.escape(val))
                    elif (arg == "start" and val is not ""):
                        query_conditions.append("start >= %s" % db.escape(val))
                    elif (arg == "end" and val is not ""):
                        query_conditions.append("end <= %s" % db.escape(val))

                query = "SELECT COUNT(*) as ct FROM Event"
                if (len(query_conditions) > 0):
                    query += " WHERE " + (" AND ".join(query_conditions))
                print(query)
                cursor.execute(query)
                count = cursor.fetchone()["ct"]
            
                # Pagination calculations
                LIMIT = 9
                page = int(request.args["page"]) if "page" in request.args else 0
                offset = page*LIMIT
                maxpage = math.ceil(count/LIMIT)-1
                pages = []
                if (maxpage >= 2):
                    if (page == 0):
                        pages.append(0)
                        pages.append(1)
                        pages.append(2)
                    elif (page == maxpage):
                        pages.append(maxpage-2)
                        pages.append(maxpage-1)
                        pages.append(maxpage)
                    else:
                        pages.append(page-1)
                        pages.append(page)
                        pages.append(page+1)
                elif (maxpage == 1):
                    pages.append(0)
                    pages.append(1)
                else:
                    pages.append(0)

                get_event = "SELECT e.eventid, e.name, e.start, e.end, e.actual_end, e.description, e.max_participants, " \
                            "e.cost, e.paid_members_only, e.opener, e.display, e.tournament_result_unit, " \
                            "e.tournament_result_ordering, e.display, u.student_name FROM event AS e LEFT JOIN user AS u ON e.opener=u.userid"
                if (len(query_conditions) > 0):
                    get_event += " WHERE " + (" AND ".join(query_conditions))
                get_event += " ORDER BY e.start DESC LIMIT %s OFFSET %s" % (db.escape(LIMIT), db.escape(offset))
                cursor.execute(get_event)
                entries = cursor.fetchall()
                get_result_asc = "SELECT U.student_name as name, T.score as score FROM tournamentparticipants as T, " \
                                 "user as U WHERE U.userid=T.userid and T.eventid=%s ORDER BY score;"
                get_result_desc = "SELECT U.student_name as name, T.score as score FROM tournamentparticipants as T, " \
                                  "user as U WHERE U.userid=T.userid and T.eventid=%s ORDER BY score DESC;"
                for entry in entries:
                    if entry['tournament_result_ordering'] is None:
                        entry['result'] = None
                    elif entry['tournament_result_ordering'] == 1:
                        cursor.execute(get_result_asc, entry['eventid'])
                        results = cursor.fetchall()
                        entry['result'] = results
                    else:
                        cursor.execute(get_result_desc, entry['eventid'])
                        results = cursor.fetchall()
                        entry['result'] = results
            return render_template('events.html',
                entries=entries,
                pages=pages,
                page=page,
                maxpage=maxpage,
                limit=LIMIT,
                count=count,
                start = request.args["start"] if "start" in request.args else "",
                end = request.args["end"] if "end" in request.args else "",
                maxcost = int(request.args["maxcost"]) if "maxcost" in request.args and request.args["maxcost"] and request.args["maxcost"].isnumeric() else "",
                free = int(request.args["free"]) if "free" in request.args and request.args["free"] else 2,
                tournament = int(request.args["tournament"]) if "tournament" in request.args and request.args["tournament"] else 2)
        except TemplateNotFound:
            abort(500)
    else:
        db = database.get_db()
        with db.cursor() as cursor:
            if 'delete' in request.form:
                delete_event = "UPDATE event SET display=0 WHERE eventid=%s;"
                delete_timeentry = "DELETE FROM timeentry WHERE eventid=%s;"
                cursor.execute(delete_event, request.form['delete'])
                if cursor.rowcount == 1:
                    flash('Event has been deleted', 'success')
                    cursor.execute(delete_timeentry, request.form['delete'])
                    db.commit()
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
        get_opener = "SELECT student_name FROM User AS u, Event AS e WHERE u.userid = e.opener and e.eventid=%s;"
        cursor.execute(get_opener, id)
        openers = cursor.fetchall()
        return render_template('event_info.html', entries=entries, openers=openers)

@events.route('/edit/<id>', methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        db = database.get_db()
        with db.cursor() as cursor:
            get_event_info = "SELECT name, start, end, description, max_participants, cost, paid_members_only, opener, " \
                             "tournament_result_unit, tournament_result_ordering FROM Event WHERE eventid=%s;"
            cursor.execute(get_event_info, id)
            entries = cursor.fetchall()
            get_opener = "SELECT userid, student_name from UserDataWithRole where roles LIKE '%opener%'"
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
                update_event = "UPDATE Event SET name=%s, description=%s, start=%s, end=%s, max_participants=%s, cost=%s, paid_members_only=%s, " + \
                    "opener=%s, tournament_result_unit=%s, tournament_result_ordering=%s WHERE eventid=%s;"
                opener = None if (request.form['opener'] == "None") else request.form['opener']
                if request.form['TRO'] == "None":
                    cursor.execute(update_event, (request.form['event_name'], request.form['description'],
                                                     request.form['start'], request.form['end'],
                                                     request.form['max_participants'],
                                                     request.form['cost'], request.form['PMO_Options'],
                                                     request.form['opener'], None, None, id))
                else:
                    cursor.execute(update_event, (request.form['event_name'], request.form['description'],
                                                     request.form['start'], request.form['end'], request.form['max_participants'],
                                                     request.form['cost'], request.form['PMO_Options'], request.form['opener'],
                                                     request.form['TRU'], request.form['TRO'], id))
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
        get_opener = "SELECT userid, student_name from UserDataWithRole where roles LIKE '%opener%';"
        cursor.execute(get_opener)
        entries = cursor.fetchall()
    if request.method == "POST":
        try:
            db = database.get_db()
            with db.cursor() as cursor:
                add_event_query = "INSERT INTO Event(name, description, start, end, max_participants, cost, " \
                                  "paid_members_only, opener, tournament_result_unit, tournament_result_ordering) VALUES" + \
                                  "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                if request.form['TRO'] == "None":
                    cursor.execute(add_event_query, (request.form['event_name'], request.form['description'],
                                                     request.form['start'], request.form['end'],
                                                     request.form['max_participants'],
                                                     request.form['cost'], request.form['PMO_Options'],
                                                     request.form['opener'],
                                                     None, None))
                else:
                    cursor.execute(add_event_query, (request.form['event_name'], request.form['description'],
                                                     request.form['start'], request.form['end'], request.form['max_participants'],
                                                     request.form['cost'], request.form['PMO_Options'], request.form['opener'],
                                                     request.form['TRU'], request.form['TRO']))
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
                            "TimeEntry AS t, Event AS e WHERE e.eventid=t.eventid and t.userid=%s;"
                cursor.execute(get_event, user['userid'])
                entries = cursor.fetchall()
                return render_template('my_events.html', entries=entries)
        else:
            return redirect(url_for('accounts.signup'))
    except TemplateNotFound:
        abort(500)

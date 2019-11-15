from flask import Blueprint, render_template, request, redirect, url_for, flash
from util import database
from app.accounts.session import require_oneof_roles
import pymysql
import hashlib


checkin = Blueprint('checkin', __name__,
                        template_folder='view')

'''PE'''
@checkin.route('/pe', methods=["GET","POST"])
@require_oneof_roles('admin')
def PE():
    flash('Please enter the start date of the current semester/term in order to see the PE student information!', 'danger')
    db = database.get_db()
    result = [{'Name':None, 'TimeSpent':None}]
    if request.method == "POST":
        start_date = request.form['Start Date']
        if start_date == "":
            return render_template('PE.html', records=result)
        else:
            with db.cursor() as cursor:
                get_pe_query = "SELECT Name, SUM(total_time) AS TimeSpent " + \
                               "FROM PE " +\
                               "WHERE start >= %s " +\
                               "GROUP BY Name " +\
                               "ORDER BY Name"
                #get_pe_query = "SELECT student_name AS Name, SUM(total_time) AS TimeSpent " + \
                #              "FROM User U left join (SELECT * from timeentry where start >= %s) AS T " + \
                #               "ON U.userid = T.userid " + \
                #               "WHERE U.pe_credit = 1 " + \
                #               "GROUP BY student_name " + \
                #               "ORDER BY student_name"
                cursor.execute(get_pe_query, start_date)
                result = cursor.fetchall()
            return render_template('PE.html', records=result)
    else:
        return render_template('PE.html', records=result)



'''Checkin/out'''
@checkin.route('/checkinout/<id>', methods=["GET","POST"])
@require_oneof_roles('admin', 'opener')
def checkinout(id):
    db = database.get_db()
    tournament_info = "SELECT tournament_result_unit AS unit FROM event WHERE eventid=%s"
    with db.cursor() as cursor:
        cursor.execute(tournament_info, id)
        tour_infos = cursor.fetchall()
    get_view_query_in = "SELECT Name from checkin where eventid = %s"
    get_view_query_out = "SELECT Name, total_time AS Time from checkout where eventid = %s"
    if request.method == "POST":
        with db.cursor() as cursor:
            for arg in request.form:
                if arg == 'eventid':
                    select = "SELECT userid as id from timeentry WHERE eventid=%s"
                    cursor.execute(select, id)
                    userids = cursor.fetchall()
                    checkout_condition = []
                    if userids:
                        for userid in userids:
                            checkout_condition.append("userid=%s" % db.escape(userid['id']))
                        checkout = "UPDATE timeentry SET end=CURRENT_TIMESTAMP() WHERE eventid=%s AND " + (" OR ".join(checkout_condition))
                        cursor.execute(checkout, id)
                    close_event = "UPDATE event SET actual_end=CURRENT_TIMESTAMP() WHERE eventid=%s;"
                    cursor.execute(close_event, request.form['eventid'])
                    if cursor.rowcount == 1:
                        db.commit()
                        flash('Event has been closed!', 'success')
                        return redirect(url_for('events.show', **request.args))
                    else:
                        flash('Event has not been closed successfully!', 'danger')
                        return redirect(url_for('events.show', **request.args))
                elif arg == 'StudentID':
                    studentIDshash = hashlib.sha512(request.form['StudentID'].encode('utf-8')).hexdigest()
                    find_userid_query = "SELECT userid FROM User WHERE student_id = %s"
                    cursor.execute(find_userid_query, studentIDshash)
                    userid = cursor.fetchall()
                    if userid == ():
                        flash('No account with this studentID, please sign up!', 'danger')
                        #get_view_query = "SELECT student_name AS Name " + \
                        #                 "FROM TimeEntry T, User U " + \
                        #                 "WHERE T.userid = U.userid AND eventid = %s AND T.end is null"
                        cursor.execute(get_view_query_in, id)
                        result = cursor.fetchall()
                        #get_view_query = "SELECT student_name AS Name, total_time AS Time " + \
                        #                 "FROM TimeEntry T, User U " + \
                        #                 "WHERE T.userid = U.userid AND eventid = %s AND T.end is not null"
                        cursor.execute(get_view_query_out, id)
                        check_out = cursor.fetchall()
                        return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)
                    else:
                        userid = userid[0]['userid']
                    check_userid_query = "SELECT count(*) AS c FROM TimeEntry " +\
                                         "WHERE eventid= %s " +\
                                         "AND userid = %s"
                    cursor.execute(check_userid_query, (id, userid))
                    count = cursor.fetchall()
                    count = count[0]['c']
                    if count == 0:
                        cursor.execute(get_view_query_out, id)
                        check_out = cursor.fetchall()
                        try:
                            add_start_query = "INSERT INTO TimeEntry (eventid, userid, start) VALUES(%s, %s, CURRENT_TIMESTAMP());"
                            cursor.execute(add_start_query, (id, userid))
                            if (cursor.rowcount == 1):
                                db.commit()
                                flash('Successfully checked in', 'success')
                                cursor.execute(get_view_query_in, id)
                                result = cursor.fetchall()
                                return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)
                            else:
                                flash('Check in error', 'danger')
                                cursor.execute(get_view_query_in, id)
                                result = cursor.fetchall()
                                return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)
                        except pymysql.InternalError as e:
                            flash(e.args[1], 'danger')
                            cursor.execute(get_view_query_in, id)
                            result = cursor.fetchall()
                            return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)


                    if count != 0:
                        check_checkout_query = "SELECT count(*) AS c FROM TimeEntry " +\
                                               "WHERE eventid =%s AND userid = %s AND end is not null"
                        cursor.execute(check_checkout_query, (id, userid))
                        cc = cursor.fetchall()
                        if cc[0]['c'] == 0:
                            add_end_query = "UPDATE TimeEntry SET end = CURRENT_TIMESTAMP() " +\
                                            "WHERE eventid = %s AND userid = %s"
                            cursor.execute(add_end_query, (id, userid))
                            if (cursor.rowcount == 1):
                                db.commit()
                                flash('Successfully checked out', 'success')
                                cursor.execute(get_view_query_in, id)
                                result = cursor.fetchall()
                                cursor.execute(get_view_query_out, id)
                                check_out = cursor.fetchall()
                                return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)
                            else:
                                flash('Something missing in the account', 'danger')
                                cursor.execute(get_view_query_in, id)
                                result = cursor.fetchall()
                                cursor.execute(get_view_query_out, id)
                                check_out = cursor.fetchall()
                                return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)
                        elif cc[0]['c'] == 1:
                            flash("The student has already checked out", "success")
                            cursor.execute(get_view_query_in, id)
                            result = cursor.fetchall()
                            cursor.execute(get_view_query_out, id)
                            check_out = cursor.fetchall()
                            return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)
    else:
        with db.cursor() as cursor:
            cursor.execute(get_view_query_in, id)
            result = cursor.fetchall()
            cursor.execute(get_view_query_out, id)
            check_out = cursor.fetchall()
        return render_template('checkinout.html', id=id, records=result, check_outs=check_out, tour_infos=tour_infos)

from flask import Blueprint, render_template, abort, request, redirect, url_for, flash, make_response
from jinja2 import TemplateNotFound
from util import database
from app.accounts.session import current_user, current_user_roles, invalidate_token, CS542_TOKEN_COOKIE, CS542_TOKEN_COOKIE_EXPIRY, require_login, require_oneof_roles

import hashlib


checkin = Blueprint('checkin', __name__,
                        template_folder='view')

'''PE'''
@checkin.route('/pe')
@require_oneof_roles('admin')
def PE():
    db = database.get_db()
    with db.cursor() as cursor:
        get_pe_query = "SELECT student_name AS Name, student_id AS ID, SUM(total_time) AS TimeSpent " + \
                       "FROM TimeEntry T, User U " + \
                       "WHERE T.userid = U.userid " + \
                       "AND U.pe_credit = 1 " + \
                       "GROUP BY student_id " +\
                       "ORDER BY student_name"
        cursor.execute(get_pe_query)
        result = cursor.fetchall()
    return render_template('PE.html', records=result)


'''Checkin/out'''
@checkin.route('/checkinout/<id>', methods=["GET","POST"])
@require_oneof_roles('admin', 'opener')
def checkinout(id):
    db = database.get_db()
    with db.cursor() as cursor:
        get_view_query = "SELECT student_name AS Name, student_id AS ID " + \
                       "FROM TimeEntry T, User U " +\
                       "WHERE T.userid = U.userid AND eventid = %s AND T.end is null"
        cursor.execute(get_view_query, id)
        result = cursor.fetchall()

    if request.method == "POST":
        with db.cursor() as cursor:
            studentid = request.form["StudentID"]
            find_userid_query = "SELECT userid FROM User WHERE student_id = %s"
            cursor.execute(find_userid_query, studentid)
            userid = cursor.fetchall()
            userid = userid[0]['userid']

            check_userid_query = "SELECT count(*) AS c FROM TimeEntry " +\
                                 "WHERE eventid= %s " +\
                                 "AND userid = %s"
            cursor.execute(check_userid_query, (id, userid))
            count = cursor.fetchall()
            count = count[0]['c']
            if count == 0:
                add_start_query = "INSERT INTO TimeEntry (eventid, userid, start) VALUES(%s, %s, CURRENT_TIMESTAMP());"
                cursor.execute(add_start_query, (id, userid))
                if (cursor.rowcount == 1):
                    db.commit()
                    flash('Successfully checked in', 'success')
                return render_template('checkinout.html', records=result)

            if count != 0:
                add_end_query = "UPDATE TimeEntry SET end = CURRENT_TIMESTAMP() " +\
                                "WHERE eventid = %s AND userid = %s"
                cursor.execute(add_end_query, (id, userid))
                if (cursor.rowcount == 1):
                    db.commit()
                    flash('Successfully checked out', 'success')
                    return render_template('checkinout.html', records=result)
                else:
                    flash('Something missing in the account', 'danger')
                    return render_template('checkinout.html', records=result)
    else:
        return render_template('checkinout.html', records=result)
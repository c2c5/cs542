from util import database
import flask

CS542_TOKEN_COOKIE = 'CS542_TOKEN_COOKIE'
CS542_TOKEN_COOKIE_EXPIRY = 86400

def current_user():
    if flask.has_request_context() and CS542_TOKEN_COOKIE in flask.request.cookies:
        db = database.get_db()
        if 'current_user' not in flask.g:
            with db.cursor() as cursor:
                get_user_from_token_query = "SELECT U.*, (NOW()- L.start_time) as session_duration_seconds," + \
                    "L.token as session_token FROM User U, LoginSession L WHERE L.token = %s AND U.userid = L.userid;"
                cursor.execute(get_user_from_token_query, flask.request.cookies[CS542_TOKEN_COOKIE])
                result = cursor.fetchone()
                flask.g.current_user = result
                return result
        else:
            return flask.g.current_user
    else:
        return None

def invalidate_token(token):
    db = database.get_db()
    with db.cursor() as cursor:
        delete_session_query = "DELETE FROM LoginSession where LoginSession.token=%s"
        cursor.execute(delete_session_query, token)
        if (cursor.rowcount == 1):
            db.commit()
        return (cursor.rowcount == 1)

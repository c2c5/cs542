from util import database
from functools import wraps
import flask

CS542_TOKEN_COOKIE = 'CS542_TOKEN_COOKIE'
CS542_TOKEN_COOKIE_EXPIRY = 86400

def current_user():
    if flask.has_request_context() and CS542_TOKEN_COOKIE in flask.request.cookies:
        db = database.get_db()
        if 'current_user' not in flask.g:
            with db.cursor() as cursor:
                get_user_from_token_query = "SELECT U.*, (NOW()- L.start_time) as session_duration_seconds," + \
                    "L.token as session_token FROM UserDataWithRole U, LoginSession L WHERE L.token = %s AND U.userid = L.userid;"
                cursor.execute(get_user_from_token_query, flask.request.cookies[CS542_TOKEN_COOKIE])
                result = cursor.fetchone()
                flask.g.current_user = result
                return result
        else:
            return flask.g.current_user
    else:
        return None

def current_user_roles():
    if flask.has_request_context() and CS542_TOKEN_COOKIE in flask.request.cookies:
        if (current_user() is None or current_user()["roles"] == ""):
            return []
        return current_user()["roles"].split(", ")
    else:
        return []

def invalidate_token(token):
    db = database.get_db()
    with db.cursor() as cursor:
        delete_session_query = "DELETE FROM LoginSession where LoginSession.token=%s"
        cursor.execute(delete_session_query, token)
        if (cursor.rowcount == 1):
            db.commit()
        return (cursor.rowcount == 1)

def require_login(api_method):
    @wraps(api_method)

    def check_login(*args, **kwargs):
        if (current_user() is None):
            return flask.redirect(flask.url_for('accounts.signin', redirect=flask.request.path))
        else:
            return api_method(*args, **kwargs) 

    return check_login

def require_oneof_roles(*argv):
    def real_decorator(api_method):
        @wraps(api_method)
        def check_login(*args, **kwargs):
            if (current_user() is None):
                return flask.redirect(flask.url_for('accounts.signin', redirect=flask.request.path))
            else:
                for arg in argv:
                    if (arg in current_user_roles()):
                        return api_method(*args, **kwargs) 
                return flask.abort(403)

        return check_login
    return real_decorator
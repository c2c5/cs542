import pymysql
import pymysql.cursors
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host='localhost',
                user='cs542',
                password='cs542dbmsdatabaseproject',
                db='cs542',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def register_db(app):
    app.teardown_appcontext(close_db)
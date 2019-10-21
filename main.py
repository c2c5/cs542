from flask import Flask, render_template

import util.database as db
import util.assets as assets
from util.octicon import get_octicon_svg
from app.accounts.session import current_user, current_user_roles

# Blueprints
from app.accounts import accounts
from app.events import events
from app.route import routes

app = Flask(__name__)
app.secret_key = 'pWMZ5WDbm3qFo73LyL36ZnFEqATI212t'
db.register_db(app)
assets.register_assets(app)

# Register jinja functions
app.jinja_env.globals.update(current_user=current_user)
app.jinja_env.globals.update(current_user_roles=current_user_roles)
app.jinja_env.globals.update(octicon=get_octicon_svg)

app.register_blueprint(accounts, url_prefix='/user')
app.register_blueprint(events, url_prefix='/event')
app.register_blueprint(routes, url_prefix='/routes')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ =="__main__":
    app.run(debug=True,port=8080)
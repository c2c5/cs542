from flask import Flask, render_template
import util.database as db
import util.assets as assets
from app.accounts.session import current_user

# Blueprints
from app.accounts import accounts
from app.events import events

app = Flask(__name__)
app.secret_key = 'pWMZ5WDbm3qFo73LyL36ZnFEqATI212t'
db.register_db(app)
assets.register_assets(app)
app.jinja_env.globals.update(current_user=current_user)

app.register_blueprint(accounts, url_prefix='/user')
app.register_blueprint(events, url_prefix='/event')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ =="__main__":
    app.run(debug=True,port=8080)
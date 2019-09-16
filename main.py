from flask import Flask
import util.database as db
import util.assets as assets

# Blueprints
from app.accounts import accounts

app = Flask(__name__)
app.secret_key = 'pWMZ5WDbm3qFo73LyL36ZnFEqATI212t'
db.register_db(app)
assets.register_assets(app)

app.register_blueprint(accounts, url_prefix='/user')

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

if __name__ =="__main__":
    app.run(debug=True,port=8080)
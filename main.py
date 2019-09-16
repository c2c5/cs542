from flask import Flask
from app.accounts import accounts

app = Flask(__name__)

# Blueprints
app.register_blueprint(accounts, url_prefix='/user')

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

if __name__ =="__main__":
    app.run(debug=True,port=8080)
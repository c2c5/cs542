from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

accounts = Blueprint('accounts', __name__,
                        template_folder='view')

@accounts.route('/')
def show():
    try:
        return render_template('test.html')
    except TemplateNotFound:
        abort(500)
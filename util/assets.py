from flask_assets import Bundle, Environment

bundles = {
    'app_js': Bundle(
        'bootstrap/js/bootstrap.bundle.js',
        output='gen/app.js'),
    'app_css': Bundle(
        'bootstrap/css/bootstrap.min.css',
        output='gen/app.css'),
}

def register_assets(app):
    assets = Environment(app)
    assets.register(bundles)
from flask_assets import Bundle, Environment

bundles = {
    'app_js': Bundle(
        'jquery.min.js',
        'bootstrap/js/bootstrap.bundle.js',
        'moment/moment.min.js',
        'datetimepicker/js/bootstrap-datetimepicker.min.js',
        output='gen/app.js'),
    'app_css': Bundle(
        'bootstrap/css/bootstrap.min.css',
        'datetimepicker/css/bootstrap-datetimepicker.min.css',
        'font-awesome/css/font-awesome.min.css',
        output='gen/app.css'),
}

def register_assets(app):
    assets = Environment(app)
    assets.register(bundles)
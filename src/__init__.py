import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
    )
    app.config['WTF_CSRF_ENABLED'] = False

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/health-check')
    def health_check():
        return 'Server is running...'

    # Database
    from src.database import db
    db.init_app(app)

    # Route
    from src.route import route
    app.register_blueprint(route.bp)

    return app

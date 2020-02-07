import os

from flask import Flask, render_template, redirect, url_for
import click
from flask.cli import with_appcontext

from .extensions import db
from .commands import create_tables


def create_app(config_file='settings.py'):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    from app.routes import auth
    app.register_blueprint(auth.bp)

    app.cli.add_command(create_tables)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    # There is no need for a homepage.
    def index():
        return redirect(url_for('auth.login'))

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('/error/404.html', title='404'), 404

    return app

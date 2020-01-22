import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    g is a special object that is unique for each request. 
    current_app is another special object that points to the Flask application handling the request.
    sqlite3.connect() establishes a connection to the file pointed at by the DATABASE configuration key. 
    sqlite3.Row tells the connection to return rows that behave like dicts.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """
    close_db checks if a connection was created by checking if g.db was set. 
    If the connection exists, it is closed.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    #returns a database connection, which is used to execute the commands read from the file
    db = get_db()
    """
    opens a file relative to the flaskr package, which is useful since you won’t 
    necessarily know where that location is when deploying the application later.
    """
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """
    app.teardown_appcontext() tells Flask to call that function when cleaning up after returning the response.
    app.cli.add_command() adds a new command that can be called with the flask command.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
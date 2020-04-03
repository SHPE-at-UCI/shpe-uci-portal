import click
from flask.cli import with_appcontext

from .extensions import db
from .models import User


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    print("Creating tables")
    db.drop_all()
    db.create_all()
    print(db)

@with_appcontext
def do():
    db.create_all()

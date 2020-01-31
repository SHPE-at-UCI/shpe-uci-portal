import click
from flask.cli import with_appcontext

from .extensions import db
from .models import User


@click.command()
@with_appcontext
def create_tables():
    db.create_all()
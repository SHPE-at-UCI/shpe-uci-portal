import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User, Logins
from app.extensions import db

from time import time
from sys import platform

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Below should go all our routes dealing with Registration / Login / Session / Logout


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        # first_name = request.form['first_name']
        # last_name = request.form['last_name']
        error = None
        find_one = User.query.filter_by(email=email).first()

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif find_one is not None:
            error = 'User {} is already registered.'.format(email)

        if error is None:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            print(User.query.all())

            return redirect(url_for('dashboard'))

        flash(error)
        # Change later to dashboard.html
    return render_template('/auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        error = None
        user = User.query.filter_by(email=email).first()

        if user is None or not check_password_hash(user.password, password):
            error = 'The username and password you entered did not match our records. Please double-check and try again'

        flash(error)

        if error is None:
            session.clear()
            session['user_id'] = user.id
            logins = (user.id, time(), platform)
            print(logins)
            print("Hi")
            db.session.add(logins)
            db.session.commit()
            print("Here")
            print(Logins.query.all())
            return redirect(url_for('home'))

    return render_template('/auth/login.html')


@bp.before_app_request
# this gets executed before ANY request.
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    print(user_id)
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


def login_required(view):
    # Wrapper function to check if user is logged in.
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

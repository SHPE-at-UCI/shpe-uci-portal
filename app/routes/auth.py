import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User
from app.extensions import db

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
    print(request)
    if request.method == 'POST':
        # Change later to dashboard.html
        return redirect(url_for('dashboard'))
    return render_template('/auth/login.html')

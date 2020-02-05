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

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(User.query.all())

        #Change later to dashboard.html
        return render_template('home.html')
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        print("Loggin in")

        #Change later to dashboard.html
        return render_template('home.html')
    return render_template('login.html')
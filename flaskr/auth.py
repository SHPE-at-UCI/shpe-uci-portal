import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Below should go all our routes dealing with Registration / Login / Session / Logout


@bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html')
import os

from flask import Flask, render_template, redirect, url_for, g, Blueprint, request
from app.routes.auth import login_required #possibly don't need
from app.extensions import db
import app.__init__
# from flask_login import current_user
from flask_recaptcha import ReCaptcha

bp = Blueprint('faq', __name__, url_prefix='/faq')

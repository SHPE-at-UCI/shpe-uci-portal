import os


from flask import Flask, render_template, redirect, url_for, g, Blueprint, request
from app.routes.auth import login_required #possibly don't need
from app.extensions import db
import app.__init__
# from flask_login import current_user
from flask_recaptcha import ReCaptcha

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def login():
    # fetch user information from database
    user = db.child('users').child(g.user['localId']).get().val()
    # fetch user points from database
    userPoints = db.child('points').child(g.user['localId']).get().val()
    # load the dashboard with the user information
    return render_template('/dashboard.html', user=user, points=userPoints)

#@bp.route("upload-pdf", methods=["GET", "POST"])
# not working yet

def upload_pdf():   
    if request.method == "POST":
        if request.files:
            pdf = request.files["pdf_uploader"]

            pdf.save(os.path.join(app.config["PDF_UPLOADS"], pdf.filename))

            return redirect(request.url)

    return "Thank you for putting file"
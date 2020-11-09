import os
from flask import Flask, render_template, redirect, url_for, g, request, flash
from werkzeug import secure_filename
from app.routes.auth import login_required
from app.extensions import db
# from flask_login import current_user
from flask_recaptcha import ReCaptcha

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["PDF_UPLOADS"] = "./app/utils/temp" # Path to save resumes
    PATH_TO_UPLOAD = app.config["PDF_UPLOADS"] #constant term

    # Configure and Start Google recaptcha
    app.config.update(
        RECAPTCHA_ENABLED= True,
        RECAPTCHA_SITE_KEY= os.getenv("GOOGLE_SITE_KEY"),
        RECAPTCHA_SECRET_KEY= os.getenv("GOOGLE_SECRET_KEY")
    )
    recaptcha = ReCaptcha(app=app)

    from app.utils.google_drive_api import google_drive_auth # google drive api functions
    from app.routes import auth, settings
    from app.routes.search import get_all_users, get_user
    from app.routes import dashboard
    from app.routes.dashboard import allowed_file, delete_file
    # Register routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(settings.bp)
    app.register_blueprint(dashboard.bp)

    from app.routes import points
    app.register_blueprint(points.bp)
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

    @app.route('/admin-route')
    def admin():
        return render_template('admin-route.html')

    @app.route('/points')
    @login_required
    def points():
        userPoints = userPoints = db.child(
            'points').child(g.user['localId']).get().val()
        return render_template('points.html', points=userPoints)

    @app.route('/dashboard', methods=["GET","POST"])
    @login_required
    def dashboard():
        if request.method == "POST":
            user_file = request.files['pdf_uploader']
            if not allowed_file(user_file): #checks if file is pdf
                return redirect(request.url)
            else:
                secure_file = secure_filename(user_file.filename) # holds pdf file from form
                user_file.save(os.path.join(PATH_TO_UPLOAD, secure_file)) # create variable here path to new pdf
                myfilepath = os.path.join(PATH_TO_UPLOAD, secure_file) #hold file path for google drive
                google_drive_auth(myfilepath)
                delete_file(myfilepath)

            return redirect(request.url) #returns url and looks for request object
        # if method is GET then render template
        return render_template("dashboard.html")

    @app.route('/team')
    def team():
        return render_template('/team.html')

    @app.route('/settings')
    @login_required
    def settings():
        return render_template('settings.html')

    @app.route('/portfolio/<ucinet>')
    @login_required
    def portfolio(ucinet):
        #print(f"Retrieving Data for {ucinet}")
        userInfo = get_user(ucinet)
        if userInfo == None:
            return page_not_found("User not found")
        return render_template('portfolio.html', userdata=userInfo)

    @app.route('/meetteam')
    def meet_team():
        return 'MeetTeam'

    @app.route('/search')
    def search():
        users = get_all_users()
        # for user in users:
        #     user.print()
        return render_template('search.html', users=users)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('/error/404.html', title='404'), 404

    return app

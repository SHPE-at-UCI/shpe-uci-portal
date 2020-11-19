import os

from flask import Flask, render_template, redirect, url_for, g, Blueprint, request, jsonify
from app.routes.auth import login_required #possibly don't need
from app.extensions import db
import app.__init__
import requests # methods
# from flask_login import current_user

bp = Blueprint('faq', __name__, url_prefix='/faq')

# This is the main page for the FAQ page
# Returns a page with a search bar, filtering 
# the questions in the database
@bp.route('/', methods=['GET'])
def faq():
    if request.method == 'GET':
        return render_template('faq/faq.html')


@bp.route('/post', methods=['GET', 'POST'])
def postQuestion():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass


@bp.route('/api/questions', methods=['GET'])
def getAllQuestions():
    if request.method == 'GET':
        return jsonify(db.child('questions').get().val())


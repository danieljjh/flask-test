"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request  
from flask import render_template
from model.models import db, Survey, Question, Choice  


page = Blueprint('page_bp', __name__,  template_folder='templates')

@page.route('/home')
def home():  
	# return 'home'
    return render_template('hello.html')



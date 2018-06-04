"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request  
from model.models import db, Survey, Question, Choice  


api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):  
    response = { 'msg': "Hello33 {}".format(name) }
    return jsonify(response)

@api.route('/surveys/<int:id>/', methods=('GET', 'PUT'))
def survey(id):  
    if request.method == 'GET':
        survey = Survey.query.get(id)
        return jsonify({ 'survey': survey.to_dict() })
    elif request.method == 'PUT':
        data = request.get_json()
        for q in data['questions']:
            choice = Choice.query.get(q['choice'])
            choice.selected = choice.selected + 1
        db.session.commit()
        survey = Survey.query.get(data['id'])
        return jsonify(survey.to_dict()), 201

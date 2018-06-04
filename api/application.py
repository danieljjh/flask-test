"""
application.py  
- creates a Flask app instance and registers the database object
"""

from flask import Flask

def create_app(app_name='TTX_API'):  
    app = Flask(app_name)
    app.config.from_object('api.config.BaseConfig')

    from api import api
    app.register_blueprint(api, url_prefix="/api")

    from page import page
    app.register_blueprint(page, url_prefix="/page")

    from model.models import db
    db.init_app(app)


    return app
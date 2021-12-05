# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

import os
import config

from flask import (
    Flask, 
    request,
    render_template,
    send_from_directory,
    abort
)

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# Application initialization
app = Flask(__name__, 
            template_folder='views',
            static_folder='public')

app.config.from_object(config.DevelopmentConfig)

api_router = Api(app, prefix='/api/v1')  # API Initialization
db = SQLAlchemy(app)                     # Database Initialization


"""
404 Page not found error default handler
"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', error=e), 404



"""
Controllers and API Resources import
and register blueprints and resources 
"""

from app.controllers import main    # Controllers
from app.api import resources       # API Resources

# Register resources
api_router.add_resource(resources.Example, '/')

# Register Blueprints
app.register_blueprint(main.bp)

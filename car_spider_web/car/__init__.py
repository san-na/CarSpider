# -*- coding: utf-8 -*-

__author__ = "san-na"

from car import settings

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import logging.handlers
import logging

db = None

def create_app():
    global db

    app = Flask(__name__)
    app.config.from_object(settings)

    db = SQLAlchemy(app)
    setup_blueprints(app)
    setup_logger(app)

    return app

def setup_blueprints(app):
    ''' init blueprints
    '''
    from car.common import Common
    app.register_blueprint(Common, url_prefix='')

def setup_logger(app):
    """ init logger of operation.
    """
    log_path = app.config['LOG_PATH']
    handler = logging.handlers.TimedRotatingFileHandler(log_path, when='d',
                                                        interval=1)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

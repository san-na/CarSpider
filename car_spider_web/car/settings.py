# -*- coding: utf-8 -*-

DEBUG = True
TESTING = False

from datetime import timedelta

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/car_spider'
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_RECYCLE=3600

SECRET_KEY = r'\xc0\xafc\x2f\x45WmB\xfa\x92\xc9\x25\xa5\x81\x8d\xa3y[f\xe7w\xd8}'

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASS = ""
MYSQL_DB = 'car_spider'

LOG_PATH = 'log/car_spider.log'

# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

DB_PORT = 3306
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = ''

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SITE_NAME = 'Flask Application'
    SECRET_KEY = 'c219d4e3-3ea8-4dbb-8641-8bbfc644aa18'
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
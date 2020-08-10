import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'KLuieon*&*KLJNSDKSNDBFJh'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # POSTS_PER_PAGE = 25


# Host
# ec2-54-234-44-238.compute-1.amazonaws.com
# Database
# d7s98va9149nli
# User
# gzlfdzlvnwzllk
# Port
# 5432
# Password
# 54b5020450162ff5d9f280a0c130c773a4d734cacaf74de62a03642787ca5082
# URI
# postgres: // gzlfdzlvnwzllk: 54b5020450162ff5d9f280a0c130c773a4d734cacaf74de62a03642787ca5082@ec2-54-234-44-238.compute-1.amazonaws.com: 5432/d7s98va9149nli
# Heroku CLI
# heroku pg: psql postgresql-opaque-01070 - -app leakwall

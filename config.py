#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set st=4 ts=4 sts=4 sw=4 et sta
# Copyright (c)  2017 - 2018 DataCraft Ltd, Nyimbi Odero. All Rights Reserved

import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = '\2\1YestAnotherSecret.KeyDrat\1\2\e\y\y\h'

# The SQLAlchemy connection string.
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
SQLALCHEMY_DATABASE_URI = 'postgresql://nyimbi:abcd1234.d@localhost:5432/iecms'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#------------------------------
# GLOBALS FOR APP Builder
#------------------------------
# Uncomment to setup Your App name
APP_NAME = "IECMS - Kenya"

# Uncomment to setup Setup an App icon
#APP_ICON = "static/img/logo.jpg"

#----------------------------------------------------
# AUTHENTICATION CONFIG
#----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
#AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
#OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
#---------------------------------------------------
# Babel config for translations
#---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for you app
LANGUAGES = {
    'en': {'flag':'ke', 'name':'English'},
    'sw': {'flag':'ke', 'name':'Kiswahili'},
    'luo': {'flag':'ke', 'name':'Luo'},
    'kik': {'flag':'ke', 'name':'Kikuyu'},
    'kam': {'flag':'ke', 'name':'Kamba'},
    'luy': {'flag':'ke', 'name':'Luhya'},
    'teo': {'flag':'ke', 'name':'Ateso'},
    'mer': {'flag':'ke', 'name':'Meru'},

}
#---------------------------------------------------
# Image and file configuration
#---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
#IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
#APP_THEME = "bootstrap-theme.css"  # default bootstrap
APP_THEME = "cerulean.css"
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"
#APP_THEME = "spacelab.css"
#APP_THEME = "united.css"
#APP_THEME = "yeti.css"

# Customized Settings
RECAPTCHA_PUBLIC_KEY='6LcTcRgUAAAAAGQNc6P-IAICSM9O6Ti4NWmHL5x_'
RECAPTCHA_PRIVATE_KEY = '6LcTcRgUAAAAADrZLG8K2NV5qgE46hufXFpXC3bO'

# Config for Flask-Mail necessary for user registration
MAIL_PORT=587
MAIL_USE_SSL=False
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USE_TLS = True
MAIL_USERNAME = 'elimu.bora.emis@gmail.com'
MAIL_PASSWORD = 'Abcd1234.'
MAIL_DEFAULT_SENDER = 'elimu.bora.emis@gmail.com'


# Config for the Mongo Instance
MONGO_URI = "mongo://localhost:27017/docx" # A MongoDB URI which is used in preference of the other configuration variables.
# MONGO_HOST	    # The host name or IP address of your MongoDB server. Default: “localhost”.
# MONGO_PORT	    #The port number of your MongoDB server. Default: 27017.
# MONGO_AUTO_START_REQUEST	# Set to False to disable PyMongo 2.2’s “auto start request” behavior (see MongoClient). Default: True.
# MONGO_MAX_POOL_SIZE	# (optional): The maximum number of idle connections maintained in the PyMongo connection pool. Default: PyMongo default.
# MONGO_SOCKET_TIMEOUT_MS	# (optional): (integer) How long (in milliseconds) a send or receive on a socket can take before timing out. Default: PyMongo default.
# MONGO_CONNECT_TIMEOUT_MS	# (optional): (integer) How long (in milliseconds) a connection can take to be opened before timing out. Default: PyMongo default.
# MONGO_SERVER_SELECTION_TIMEOUT_MS	# (optional) Controls how long (in milliseconds) the driver will wait to find an available, appropriate server to carry out a database operation; while it is waiting, multiple server monitoring operations may be carried out, each controlled by connectTimeoutMS. Default: PyMongo default.
# MONGO_DBNAME	        # The database name to make available as the db attribute. Default: app.name.
# MONGO_USERNAME	    # The user name for authentication. Default: None
# MONGO_PASSWORD	    # The password for authentication. Default: None
# MONGO_AUTH_SOURCE	    # The database to authenticate against. Default: None
# MONGO_AUTH_MECHANISM	# The mechanism to authenticate with. Default: pymongo <3.x MONGODB-CR else SCRAM-SHA-1
# MONGO_REPLICA_SET	    # The name of a replica set to connect to; this must match the internal name of the replica set (as determined by the isMaster command). Default: None.
# MONGO_READ_PREFERENCE	# Determines how read queries are routed to the replica set members. Must be one of the constants defined on pymongo.read_preferences.ReadPreference or the string names thereof.
# MONGO_DOCUMENT_CLASS	# This tells pymongo to return custom objects instead of dicts, for example bson.son.SON. Default: dict
# MONGO_CONNECT	        # (optional): If True (the default), let the MongoClient immediately begin connecting to MongoDB in the background. Otherwise connect on the first operation. This has to be set to False if multiprocessing is desired; see Using PyMongo with Multiprocessing.

# @app.route('/uploads/<path:filename>', methods=['POST'])
# def save_upload(filename):
#     mongo.save_file(filename, request.files['file'])
#     return redirect(url_for('get_upload', filename=filename))

# @app.route('/uploads/<path:filename>')
# def get_upload(filename):
#     return mongo.send_file(filename)

RDB_CONFIG = {
  'host' : os.getenv('RDB_HOST', 'localhost'),
  'port' : os.getenv('RDB_PORT', 28015),
  'db'   : os.getenv('RDB_DB', 'iecms'),
  'table': os.getenv('RDB_TABLE', 'files')
}
RDB_HOST =  os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015
RDB_DB   = 'iecms'
RDB_TBL  = 'file'

# The `Connection` object returned by [`r.connect`](http://www.rethinkdb.com/api/python/connect/)
# is a [context manager](http://docs.python.org/2/library/stdtypes.html#typecontextmanager)
# that can be used with the `with` statements.
# def connection():
#   return r.connect(host=RDB_CONFIG['host'], port=RDB_CONFIG['port'],
#                    db=RDB_CONFIG['db'])

######## MPESA #########
MPESA_B2C_ACCESS_KEY = 'Mpesa b2c access Key'
MPESA_B2C_CONSUMER_SECRET = 'Mpesa b2c consumer secret'
MPESA_C2B_ACCESS_KEY = 'Mpesa c2b access Key'
MPESA_C2B_CONSUMER_SECRET = 'Mpesa c2b consumer secret'
B2C_SECURITY_TOKEN = 'b2c security token'
B2C_INITIATOR_NAME = 'b2c initiator name'
B2C_COMMAND_ID = 'Sb2c command id'
B2C_SHORTCODE = 'b2c shortcode'
B2C_QUEUE_TIMEOUT_URL = 'b2c queue timeout url'
B2C_RESULT_URL = 'b2c result url'

C2B_REGISTER_URL = 'c2b register url'
C2B_VALIDATE_URL = 'c2b validate url'
C2B_CONFIRMATION_URL = 'c2b confirmation url'
C2B_SHORT_CODE = 'c2b short code'
C2B_RESPONSE_TYPE = 'Completed'

C2B_ONLINE_CHECKOUT_URL = 'c2b online checkout url'
C2B_ONLINE_CHECKOUT_CALLBACK_URL = 'online checkout callback url'
C2B_TRANSACTION_TYPE = 'CustomerPayBillOnline'
C2B_ONLINE_PASSKEY = 'c2b online passkey'
C2B_ONLINE_SHORT_CODE = 'c2b online short code'

# Urls
GENERATE_TOKEN_URL = 'auth url'
B2C_URL = 'b2c url'

# number of seconds from the expiry we consider the token expired
# the token expires after an hour
TOKEN_THRESHOLD = 600


#### CELERY
CELERY_RESULT_BACKEND = ''
CELERY_BROKER_URL =''
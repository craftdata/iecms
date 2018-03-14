# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT
import click
click.disable_unicode_literals_warning = True
import logging
import config as cfg
from flask import Flask, g
from celery import Celery
from flask_appbuilder import SQLA, AppBuilder
from flask_debugtoolbar import DebugToolbarExtension
from flask_pymongo import PyMongo
from flask_humanize import Humanize
from flask_ckeditor import CKEditor
from app.index import MyIndexView
from app.sec import MySecurityManager

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
"""
 Logging configuration
"""


### Setup the RethinkDB Connection
def rethinkDbSetup():
    try:
        connection = r.connect(host=cfg.RDB_CONFIG['host'], port=cfg.RDB_CONFIG['port'])
        r.db_create(cfg.RDB_CONFIG['db']).run(connection)
        r.db(cfg.RDB_CONFIG['db']).table_create(cfg.RDB_CONFIG['table']).run(connection)
        print ('Database setup completed. Now run the app without --setup.')
        connection.close()
    except RqlRuntimeError:
        print ('App RethinkDB database already exists. Run the app without --setup.')
    finally:
        pass


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
humanize = Humanize(app)
# ckeditor = CKEditor(app)

# Enable Debug Toolbar
toolbar = DebugToolbarExtension(app)
#mongo = PyMongo(app)

# Now do the RethinkDb setups
rethinkDbSetup()

@app.before_request
def before_request():
    try:
        g.rdb_conn = r.connect(host=cfg.RDB_CONFIG['host'], port=cfg.RDB_CONFIG['port'], db=cfg.RDB_CONFIG['db'])
    except RqlDriverError:
        print(503, "No database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass


db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, security_manager_class=MySecurityManager)



"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
    
    postgresql://nyimbi@localhost:5432/ctmp
"""    

from app import views


# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT
import click
click.disable_unicode_literals_warning = True
import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from flask_debugtoolbar import DebugToolbarExtension
from flask_pymongo import PyMongo
from app.index import MyIndexView
from app.sec import MySecurityManager

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)

# Enable Debug Toolbar
toolbar = DebugToolbarExtension(app)
mongo = PyMongo(app)


app.config.from_object('config')
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


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
from app.index import MyIndexView
from app.sec import MySecurityManager

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

from .sec import MySecurityManager

#
#  Logging configuration
#

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

### Make a celery app
def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
    
    
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



### app Setup
app = Flask(__name__)
app.config.from_object('config')
humanize = Humanize(app)
# Enable Debug Toolbar
toolbar = DebugToolbarExtension(app)
#mongo = PyMongo(app)
celery = make_celery(flask_app)

# Now you can call a celery task like this
# @celery.task()
# def add_together(a, b):
#     return a + b

# In a separate terminal start at the root of the app
#celery -A app.celery worker


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


from app import views

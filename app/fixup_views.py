# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT

import os, sys, string, inspect, importlib, datetime
import inflect
import pprint

infl = inflect.engine()

# execfile('mixins.py')
exec(open("./mixins.py").read())

from IPython.core.debugger import Pdb

view_imports = """# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# Generated on {}


import calendar
from flask import redirect, flash, url_for, Markup, g
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, BaseView, MasterDetailView, MultipleView, RestCRUDView, CompactCRUDMixin
from flask_appbuilder import ModelView, CompactCRUDMixin, aggregate_count, action, expose, BaseView, has_access
from flask_appbuilder.charts.views import ChartView, TimeChartView, GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.widgets import ListThumbnail, ListWidget
from flask_appbuilder.widgets import FormVerticalWidget, FormInlineWidget, FormHorizontalWidget, ShowBlockWidget
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction as FA
from flask_appbuilder.models.group import aggregate_count, aggregate_sum, aggregate_avg
from flask_babel import gettext
from flask_appbuilder.filemanager import get_file_original_name
from flask_appbuilder.models.mixins import AuditMixin, FileColumn

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms_alchemy import ModelForm, ClassMap
from wtforms_alchemy import model_form_factory

# For decoding the md_metadata
import ast

# To Extend the User Model
from flask_appbuilder.security.views import UserDBModelView
#from flask_babelpkg import lazy_gettext

from app import appbuilder, db
from .models import *

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

#To pretty Print from PersonMixin
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)
 
def get_user():
    return g.user
    
def pretty_year(value):
    return str(value.year)

    
# Class of readonly field widgets
class BS3TextFieldROWidget(BS3TextFieldWidget):
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(BS3TextFieldROWidget, self).__call__(field, **kwargs)
        
# Use like this
# class ExampleView(ModelView):
#     datamodel = SQLAInterface(ExampleModel)
#     edit_form_extra_fields = {{'field2': TextField('field2',
#                                 widget=BS3TextFieldROWidget())}}
"""  # .format(datetime)

view_head = """
class {}View(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface({}, db.session)"""  # .format(x,x)

wtf_form = """
class wtf_{}Form(ModelForm):
    class Meta:
        model = {}
        # strip_string_fields = False   # Whether or not to add stripping filter to all string fields.
        # not_null_validator_type_map = ClassMap({{sa.Enum: [DataRequired()]}})
        # include = ['author_id']
        # exclude = ['pgm', 'wsq', 'xyt', 'photo', 'file']
        # exclude = ['page_image']
        # only = ['name', 'content']
        # include_primary_keys = True
        # only_indexed_fields = False # only fields that have an index will be included in the form, Useful for searching
        # field_args = {{'email': {{'validators': [Optional()]}} }} #  for overriding field arguments
        # include_foreign_keys = False
        # include_datetimes_with_default=False # Such as created_at etc
        # validators = {{ 'email': [Email()] }} # Dict of validators
        # datetime_format =  ‘%Y-%m-%d %H:%M:%S’ # default datetime format, which will be assigned to generated datetime fields.
        # date_format = ‘%Y-%m-%d’      # default date format, which will be assigned to generated datetime fields.
        # all_fields_optional = False   # Defines all generated fields as optional (useful for update forms).
        # assign_required =  True       # Whether or not to assign non-nullable fields as required
#     location = ModelFormField(LocationForm)
"""  # .format(x,x)

view_body = """
    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    
    # search_form_query_rel_fields = [('group':[['name',FilterStartsWith,'W']]
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail','doc', 'doc_binary'] + person_exclude_columns + biometric_columns + person_search_exclude_columns
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {{"contact_group":"Contacts Group"}}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = {}
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = {}
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = {}
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 50
    # formatters_columns = {{‘some_date_col’: lambda x: x.isoformat() }}
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets = \
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    
    add_fieldsets =  {}
    edit_fieldsets = {}
    show_fieldsets = {}
    
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    
    # description_columns = {{"name":"your models name column","address":"the address column"}}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # extra_args = None
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {{'group': [['name',FilterStartsWith,'W']] }}
    # edit_form_query_rel_fields = {{'group': [['name',FilterStartsWith,'W']] }}
    # search_form_query_rel_fields = {{'group': [['name',FilterStartsWith,'W']] }}
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    """

chart_head = """
class {}ChartView(GroupByChartView):
    datamodel = SQLAInterface({}, db.session) """  # .format(x,x)

chart_body = """
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = {}View.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {{
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        # (aggregate_avg, 'population'),
                        # (aggregate_avg, 'college')
                       ]
        }},
        {{
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       # (aggregate_avg, 'population'),
                       # (aggregate_avg, 'college')
            ]
        }}
    ]
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail','doc', 'doc_binary'] + person_exclude_columns + biometric_columns + person_search_exclude_columns
"""  # .format(x)

sec_py = """
from flask_appbuilder.security.sqla.manager import SecurityManager
from .sec_models import MyUser
from .sec_views import MyUserDBModelView

class MySecurityManager(SecurityManager):
    user_model = MyUser
    userdbmodelview = MyUserDBModelView
"""

sec_model = """
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, ForeignKey, String, Sequence, Table
from sqlalchemy.orm import relationship, backref
from flask_appbuilder import Model

class MyUser(User):
    extra = Column(String(256))
    another = Column(String(100))
    # Profile picture
    # Phone Number
    # Home address
"""

sec_view = """\
from flask_appbuilder.security.views import UserDBModelView
from flask_babelpkg import lazy_gettext

class MyUserDBModelView(UserDBModelView):
    
    #     View that add DB specifics to User view.
    #     Override to implement your own custom view.
    #     Then override userdbmodelview property on SecurityManager
   

    show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'extra']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
        (lazy_gettext('Audit Info'),
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]

    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'extra']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
    ]

    add_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'extra', 'password', 'conf_password']
    list_columns = ['first_name', 'last_name', 'username', 'email', 'active', 'roles']
    edit_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'extra']
    """

init_py = """\
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
""" # End init_py






jointbl_code = """
class {}View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface({})
    # list_columns = []
"""  # .format(x,x)

jointbl_mv_code = """
class {}MultiView(MultipleView):"""

tail_ent = 'appbuilder.add_view({}View(), "{}", icon="fa-folder-open-o", category="Setup")\n'
chart_ent = 'appbuilder.add_view({}ChartView(), "{} Age Chart", icon="fa-bar-chart", category="Charts")\n'
jointbl_mv_ent = 'appbuilder.add_view({}MultiView(), "{} Multi View", icon="fa-address-card-o", category="MultiViews")\n'

# jointbl_ent = 'appbuilder.add_view_no_menu({}View(), "{}")\n'
jointbl_ent = 'appbuilder.add_view({}View(), "{} Joint View", icon="fa-address-card-o", category="JointViews")\n'

end_notes = """
# appbuilder.add_separator("Setup")
# appbuilder.add_separator("My Views")
# appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)
"""

# Field_sets and columns
f_set = """
{}_{}_field_set = [
    ('Data', {{'fields': {}, 'expanded': True}}),
    # ('Other', {{'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False}})
]
"""
f_column = """
{}_{}_columns = {}
"""

f_exclusions = """
audit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on', 'changed_by_fk','created_by_fk']
add_exclude_columns = edit_exclude_columns = audit_exclude_columns
person_search_exclude_columns = ['photo', 'photo_img', 'photo_img_thumbnail', 'fp_l1', 'fp_l2', 'fp_l3', 'fp_l4',
                                 'fp_l5', 'fp_r1', 'fp_r2', 'fp_r3', 'fp_r4',
                                 'fp_r5'] + ['finger_palm_left', 'finger_palm_right', 'eye_left', 'eye_right']
                                 
biometric_columns = ['fp_lthumb', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5',
                     'fp_rthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5',
                     'palm_left', 'palm_right', 'eye_left', 'eye_right']

"""


# List of all the class name



def get_klass(module):
    klass_names = []
    for name in dir(module):
        obj = getattr(module, name)
        if inspect.isclass(obj):  # or (str(obj.__name__).startswith('t_')):
            # print(obj.__name__)
            t1 = 'ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR, TSVectorType, UserExtensionMixin, '
            t2 = 'MetaData, metadata, FetchedValue, ImageManager, AuditMixin, FileColumn, ImageColumn, UserExtensionMixin, Base, TSVectorType, BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time, text, '
            t3 = 'Enum, BaseQuery, AuditMixinNullable, Float, Interval, Markup, Model, date, datetime, declared_attr, hybrid_property, timedelta, models, CheckConstraint'
            t4 = t1 + t2 + t3
            ta = t4.split(', ')
            if obj.__name__ not in ['Base', 'BigInteger', 'Boolean', 'Column', 'Date', 'DateTime', 'ForeignKey',
                                    'ForeignKeyConstraint', 'Index', 'Integer', 'LargeBinary', 'Numeric', 'String',
                                    'Table', 'Text', 'Time'] + ta and not obj.__name__.endswith('Mixin'):
                klass_names.append(obj.__name__)
    return klass_names



def get_class_names():
    class_names = []
    with open('class_names.txt','r') as f:
        class_names = f.read().splitlines()
    
    return class_names


# Essentially doing this: cat models.py| grep "^t_*" | cut -d "=" -f1
def get_join_tables():
    mdl = []
    jt = []
    with open('join_tables.txt', 'r') as f:
        jt = f.read().splitlines()
    # for i in range(len(mdl)):
    #     if mdl[i].startswith('class T_'):
    #         (s,_,_) = mdl[i].partition('(')
    #         t = s.split(' ') # Left contains class, right contains name
    #         jt.append(t[1].strip())
    return jt



# This is the actual code generator
# Presumption is the
def gen_code(model_filename):
    code = []
    fld_set = []
    
    md_view_list = []
    md_join_view_list =[]
    md_wtf_list = []
    md_table_list = []
    md_join_tables = []
    md_metadata = {}
    
    # For reasons of introspection we import models.py or such other
    modl = importlib.import_module(model_filename)
    
    # The fixup_models.py should have created a class_names.txt
    # where we get these details
    cls_list = get_class_names()
    md_table_list = cls_list
    
    join_tables = get_join_tables()
    md_join_tables = join_tables
    
    def section_preamble(text):
        code.append('#' * 30)
        code.append('# ' + '{:^30}'.format(text))
        code.append('#' * 20)
    
    def space(n):
        code.append('\n' * n)
    
    ##### CODE GENERATION
    code.append(view_imports.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # Generate Views
    
    
    ############## Field Sets ##############
    exclude_list = ['id', 'file', 'photo', 'metadata','photo_img','photo_img_thumbnail'] +\
         ['created_by', 'created_on', 'changed_by', 'changed_on', 'changed_by_fk', 'created_by_fk']
    exclude_list += []
    section_preamble('Field Sets and Columns')
    code.append(f_exclusions)
    
    for x in cls_list:
        # To get the field names for reference we do
        print(x)
        class_ = getattr(modl, str(x))
        filds = [attrname for attrname in dir(class_) if
                 not callable(getattr(class_, attrname)) and not attrname.startswith(
                     # '_') and (attrname not in ['id', 'file', 'photo', 'metadata','photo_img','photo_img_thumbnail'])])
                     '_') and (attrname not in exclude_list)]
        
        # Put name. description, notes first
        if 'notes' in filds:
            filds.insert(0, filds.pop(filds.index('notes')))
        if 'description' in filds:
            filds.insert(0, filds.pop(filds.index('description')))
        if 'name' in filds:
            filds.insert(0, filds.pop(filds.index('name')))
        
        
        # Remove country if country1 is there etc
        for fld in filds:
            if fld+'1' in filds:
                filds.pop(filds.index(fld))
            
        s = str(filds)
        for ed in ['add', 'edit', 'list']:
            code.append(f_column.format(x, ed, s))
        for ed in ['add', 'edit', 'show']:
            code.append(f_set.format(x, ed, s) + '\n')
    code.append('# exec("field_sets.py")')

    ############## Table Views ##############
    section_preamble('Table Views')
    for x in cls_list:
        # To get the field names for reference we do
        class_ = getattr(modl, x)
        s = str([attrname for attrname in dir(class_) if
                 not callable(getattr(class_, attrname))
                 and not attrname.startswith('_')
                 and  (attrname not in ['pgm', 'wsq', 'xyt', 'photo', 'file', 'metadata'])
                 ]
                )
        for ed in ['add', 'edit', 'list']:
            fld_set.append(f_column.format(x, ed, s))
        for ed in ['add', 'edit', 'show']:
            fld_set.append(f_set.format(x, ed, s) + '\n')
        
        code.append('# FIELDS: ' + s)
        md_view_list.append(x+'View')
        md_metadata[x] = s
        code.append(view_head.format(x, x, ))
        # Set the columns and fieldsets in the view
        a = x + '_add_columns'
        b = x + '_edit_columns'
        c = x + '_list_columns'
        d = x + '_add_field_set'
        e = x + '_edit_field_set'
        f = x + '_show_field_set'
        code.append(view_body.format(a, b, c, d, e, f))
        space(2)

    #For Convenience in editing. Edit these to
    code_write(fld_set, 'field_sets.py')

    ############## Join Table Views ##############
    # Not going to be of much use except for reports
    # Generate Join Table Views
    # {}View
    section_preamble('Join Table Views')
    for x in join_tables:
        code.append('# View Table for:' + x)
        code.append(jointbl_code.format(x, x))
        md_join_view_list.append(x+'View')
        space(2)
        

    ############## Join MultiViews ##############
    # {}MultiView
    section_preamble('Join MultipleViews')
    for x in join_tables:
        code.append('\n# MultiView for:' + x)
        code.append(jointbl_mv_code.format(x))
        vws = x.split('_')
        vws.pop(0)
        s = [y.title() + 'View, ' for y in vws if len(y) > 1]
        t = ''.join(s)
        code.append('\tviews = [' + t + ']\n')
        space(2)
    
    
    ############## Charts ##############
    # Generate Charts
    section_preamble('Chart Views')
    for x in cls_list:
        code.append(chart_head.format(x, x))
        code.append(chart_body.format(x))
        space(2)

    ############## WTF FORMS ##############
    # Generate wtfForms
    # wtf_{}Form
    section_preamble('WTForms-Alchemy Forms')
    section_preamble('Just in case we ever need them')
    for x in cls_list:
        code.append(wtf_form.format(x, x))
        md_wtf_list.append('wtf_'+x+'Form')
        space(2)

    ############## WORKFLOWS ##############
    code.append('############## WORKFLOWS ##############')
    space(2)
    code.append('#-X-#### Table-Field Dictionary')
    sx = pprint.pformat(md_metadata, indent=4, depth=1)
    code.append('wz_metadata = \\\n' + sx)  # ('md_metadata = ' + s.getvalue())

    space(3)
    code.append('#-X-#### Table List')
    sx = pprint.pformat(md_table_list)
    code.append('wz_table_list = ' + sx)

    space(3)
    code.append('#-X-#### Join Tables')
    sx = pprint.pformat(md_join_tables)
    code.append('wz_join_tables = \\\n' + sx)

    space(3)
    code.append('#-X-#### View List')
    sx = pprint.pformat(md_view_list)
    code.append('wz_view_list = \\\n' + sx)

    space(3)
    code.append('#-X-#### WTF Form List')
    sx = pprint.pformat(md_wtf_list)
    code.append('wz_wtf_list = \\\n' + sx)

    space(3)
    code.append('#-X-#### Join View List')
    sx = pprint.pformat(md_join_view_list)
    code.append('wz_join_view_list = \\\n' + sx)

    space(3)
    
    ############## REGISTRATIONS ##############
    space(2)
    section_preamble('View Registrations')
    for x in cls_list:
        s = tail_ent.format(x, x)
        if x.endswith('type') or \
                x.endswith('category') or \
                x.endswith('rank') or \
                x.endswith('station') or \
                x.endswith('class') or \
                x.endswith('role') or \
                x.endswith('list') or \
                x.endswith('team') or \
                x.endswith('Ward') or \
                x.endswith('Subcounty') or \
                x.endswith('County') or \
                x.endswith('Country') or \
                x.endswith('Town') or \
                x.endswith('officer'):
            t= s.replace('category="Setup"', 'category="Admin"')
        else:
            t = s
        code.append(t)
    
    # section_preamble('Join Table Registrations')
    # for x in join_tables:
    #     code.append(jointbl_ent.format(x,x))
    
    section_preamble('Register Join Table MultiViews Registrations')
    for x in join_tables:
        vws = x.split('_')
        vws.pop(0)
        s = jointbl_mv_ent.format(x, str(vws).title())
        code.append(s)
    
    section_preamble('Chart View Registrations')
    for x in cls_list:
        code.append(chart_ent.format(x, x))
    
    space(2)
    code.append('appbuilder.security_cleanup()')

  
    ############## END NOTES AND COMMENTS ##############
    code.append('############## END NOTES AND COMMENTS ##############')
    section_preamble('Programming Notes and things of interest')
    code.append(end_notes)
    
    section_preamble('Join Table List')
    for x in join_tables:
        vws = x.split('_')
        vws.pop(0)
        code.append('\n# ' + x + ' -' + str([y.title() for y in vws]))
    
    section_preamble('List of tables')
    for x in cls_list:
        code.append('\n# ' + x)
    
    return code




def code_write(cd, filename):
    thefile = open(filename, 'w')
    for item in cd:
        thefile.write("%s\n" % item)
    thefile.close()


def gen_sec_models():
    thefile = open('sec_models.py', 'w')
    thefile.write(sec_model)
    thefile.close()
    
    thefile = open('sec_views.py', 'w')
    thefile.write(sec_view)
    thefile.close()
    
    thefile = open('sec.py', 'w')
    thefile.write(sec_py)
    thefile.close()
    
    thefile = open('init__.py', 'w')
    thefile.write(init_py)
    thefile.close()


if __name__ == '__main__':
    # modl = sys.argv[1]
    print(sys.argv[1] + ':Building models for this')
    
    
    code = gen_code(sys.argv[1])
    
    code_write(code, 'views.py')
    gen_sec_models()

# import importlib, codeg
# modl = importlib.import_module('mod1')
# code =  codeg.gen_code(modl)
# thefile = open('views.py','w')
# for item in code:
#     thefile.write(item)
# thefile.close()
# gen_sec_models()

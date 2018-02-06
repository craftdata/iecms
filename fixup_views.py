# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT

import os, sys, string, inspect, importlib, datetime

#execfile('mixins.py')
exec(open("app/mixins.py").read())

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
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms_alchemy import ModelForm
from flask_appbuilder.filemanager import get_file_original_name
from flask_appbuilder.models.mixins import AuditMixin, FileColumn

# To Extend the User Model
from flask_appbuilder.security.views import UserDBModelView
#from flask_babelpkg import lazy_gettext

from app import appbuilder, db
from .models import *


audit_exclude_columns = hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on']

#To pretty Print from PersonMixin
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

def get_user():
    return g.user

def pretty_year(value):
    return str(value.year)

def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

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
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
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
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {{"contact_group":"Contacts Group"}}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = {}
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = {}
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = {}
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
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
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        }},
        {{
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }}
    ]

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
         {{'fields': ['username', 'active', 'roles', 'login_count', 'extra']}}),
        (lazy_gettext('Personal Info'),
         {{'fields': ['first_name', 'last_name', 'email'], 'expanded': True}}),
        (lazy_gettext('Audit Info'),
         {{'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}}),
    ]

    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {{'fields': ['username', 'active', 'roles', 'login_count', 'extra']}}),
        (lazy_gettext('Personal Info'),
         {{'fields': ['first_name', 'last_name', 'email'], 'expanded': True}}),
    ]

    add_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'extra', 'password', 'conf_password']
    list_columns = ['first_name', 'last_name', 'username', 'email', 'active', 'roles']
    edit_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'extra']
    """

init_py = """\
import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from flask_humanize import Humanize
from app.index import MyIndexView

from .sec import MySecurityManager

#
#  Logging configuration
#

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
humanize = Humanize(app)
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, security_manager_class=MySecurityManager)


from app import views
"""

jointbl_code = """
class {}View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface({})
    # list_columns = []
"""  # .format(x,x)

jointbl_mv_code = """
class {}MultiView(MultipleView):
    """

tail_ent = 'appbuilder.add_view({}View(), "{}", icon="fa-folder-open-o", category="Setup")\n'
chart_ent = 'appbuilder.add_view({}ChartView(), "{} Age Chart", icon="fa-bar-chart", category="Charts")\n'
jointbl_mv_ent = 'appbuilder.add_view({}MultiView(), "{} Multi View", icon="fa-address-card-o", category="MultiViews")\n'
jointbl_ent = 'appbuilder.add_view_no_menu({}View(), "{}")\n'

end_notes = """
# appbuilder.add_separator("Setup")
# appbuilder.add_separator("My Views")
# appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)
"""

# Field_sets and columns
f_set = """
{}_{}_field_set = [
    ('Data', {{'fields': {}, 'expanded': True}}),
    ('Other', {{'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False}})
]
"""
f_column = """
{}_{}_columns = {}
"""

f_exclusions = """
audit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
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
            ts = 'ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR, TSVectorType, UserExtensionMixin'
            ta = ts.split(', ')
            if obj.__name__ not in ['Base', 'BigInteger', 'Boolean', 'Column', 'Date', 'DateTime', 'ForeignKey',
                                    'ForeignKeyConstraint', 'Index', 'Integer', 'LargeBinary', 'Numeric', 'String',
                                    'Table', 'Text', 'Time'] + ta:
                klass_names.append(obj.__name__)
    return klass_names


def get_join_tables(module):
    jt = []
    for name in dir(module):
        if name.startswith('t_'):
            jt.append(name)
    return jt


def gen_code(modl):
    code = []
    fld_set = []
    cls_list = get_klass(modl)
    join_tables = get_join_tables(modl)

    def section_preamble(text):
        code.append('\n' * 2)
        code.append('#' * 20)
        code.append('# ' + text)
        code.append('#' * 20)

    def space(n):
        code.append('\n' * n)

    ##### CODE GENERATION
    code.append(view_imports.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # Generate Views

    section_preamble('Field Sets and Columns')
    code.append(f_exclusions)
    for x in cls_list:
        # To get the field names for reference we do
        class_ = getattr(modl, x)
        s = str([attrname for attrname in dir(class_) if
                 not callable(getattr(class_, attrname)) and not attrname.startswith('_') and not attrname == 'id' and not attrname == 'file'])
        for ed in ['add', 'edit', 'list']:
            code.append(f_column.format(x, ed, s))
        for ed in ['add', 'edit', 'show']:
            code.append(f_set.format(x, ed, s) + '\n')
    code.append('# exec("field_sets.py")')

    section_preamble('Table Views')
    for x in cls_list:
        # To get the field names for reference we do
        class_ = getattr(modl, x)
        s = str([attrname for attrname in dir(class_) if
                 not callable(getattr(class_, attrname)) and not attrname.startswith('_')])
        for ed in ['add', 'edit', 'list']:
            fld_set.append(f_column.format(x, ed, s))
        for ed in ['add', 'edit', 'show']:
            fld_set.append(f_set.format(x, ed, s) + '\n')

        code.append('# FIELDS: ' + s)
        code.append(view_head.format(x, x, ))
        # Set the columns and fieldsets
        a = x + '_add_columns'
        b = x + '_edit_columns'
        c = x + '_list_columns'
        d = x + '_add_field_set'
        e = x + '_edit_field_set'
        f = x + '_show_field_set'
        code.append(view_body.format(a, b, c, d, e, f))
        space(2)

    code_write(fld_set, 'field_sets.py')


    # Generate Join Table Views
    section_preamble('Join Table Views')
    for x in join_tables:
        code.append('# View Table for:' + x)
        code.append(jointbl_code.format(x, x))
        space(2)

    section_preamble('Join MultipleViews')
    for x in join_tables:
        code.append('\n# MultiView for:' + x)
        code.append(jointbl_mv_code.format(x) + '\n')
        vws = x.split('_')
        vws.pop(0)
        code.append('\tviews = ' + str([y.title() + 'View' for y in vws]) + '\n')
        space(2)

    # Generate Charts
    section_preamble('Chart Views')
    for x in cls_list:
        code.append(chart_head.format(x, x))
        code.append(chart_body.format(x))
        space(2)

    # Generate wtfForms
    section_preamble('WTForms-Alchemy Forms')
    section_preamble('Just in case we ever need them')
    for x in cls_list:
        code.append(wtf_form.format(x, x))
        space(2)

    # Add Tail
    space(2)
    section_preamble('View Registrations')
    for x in cls_list:
        code.append(tail_ent.format(x, x))

    section_preamble('Join Table Registrations')
    for x in join_tables:
        code.append(jointbl_ent.format(x, x))

    section_preamble('Register Join Table MultiViews Registrations')
    for x in join_tables:
        vws = x.split('_')
        vws.pop(0)
        code.append(jointbl_mv_ent.format(x, str(vws).title()))

    section_preamble('Chart View Registrations')
    for x in cls_list:
        code.append(chart_ent.format(x, x))

    space(2)
    code.append('appbuilder.security_cleanup()')
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


imp_add = 0


def fixup_model():
    code = []
    imports = []
    classes = []
    global imp_add

    with open('model.py', 'r') as f:
        code = f.readlines()
        for i in range(len(code)):
            if code[i].startswith('import') or code[i].startswith('from '):
                imports.append(i)
            if code[i].startswith('class '):
                classes.append(i)
        imp_add = max(imports) + 1
        class_count = len(classes)

    def add_imports(impt):
        imp_add += 1
        code.insert(imp_add, impt + '\n')

    def add_mixin(class_name, mix_in):
        # find the ( and replace with ( Mixin,
        for i in range(len(code)):
            if code[i].startswith('class '):
                if code[i].find(class_name) > -1:
                    code[i] = code[i].replace('(', '( ' + mix_in + ', ')

    # We add new code to the top
    def add_field(class_name, field_code):
        for i in range(len(code)):
            if code[i].startswith('class '):
                if code[i].find(class_name) > -1:
                    code[i + 3].insert(field_code)

    # Add Imports: continuum etc

    # Replace Base with Model
    # Add Mixins
    # Rename snake_case fields
    # Manage Show fields
    pass


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
    print(sys.argv[1])
    modl = importlib.import_module(sys.argv[1])

    code = gen_code(modl)

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

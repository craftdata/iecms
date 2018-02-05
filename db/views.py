# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# Generated on 2018-02-05 11:58:07


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
from flask_babel import gettext
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms_alchemy import ModelForm

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
    
# Class of readonly field widgets
class BS3TextFieldROWidget(BS3TextFieldWidget):
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(BS3TextFieldROWidget, self).__call__(field, **kwargs)
        
# Use like this
# class ExampleView(ModelView):
#     datamodel = SQLAInterface(ExampleModel)
#     edit_form_extra_fields = {'field2': TextField('field2',
#                                 widget=BS3TextFieldROWidget())}




##################### Table Views##################### FIELDS: ['id', 'metadata']
class AccounttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Accounttype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date']
class BillView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Bill, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['amount', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']
class BilldetailView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Billdetail, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['economic_class', 'economicclass', 'health_status', 'id', 'metadata', 'photo', 'religion', 'religion1']
class BiodatumView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Biodatum, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['casechecklist', 'courtcase', 'id', 'metadata', 'parent', 'subcategory']
class CasecategoryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Casecategory, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class CasechecklistView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Casechecklist, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class CaselinktypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Caselinktype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class CelltypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Celltype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'id', 'life_imprisonment', 'metadata', 'parent', 'parties', 'party', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']
class CommitalView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Commital, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'maxduration', 'metadata']
class CommitaltypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Commitaltype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']
class ComplaintView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Complaint, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['complaint_category_parent', 'id', 'metadata', 'parent']
class ComplaintcategoryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Complaintcategory, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class ComplaintroleView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Complaintrole, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'name']
class CountryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Country, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['country', 'country1', 'id', 'metadata']
class CountyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(County, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['court_rank', 'court_station', 'courtrank', 'courtstation', 'id', 'judicialofficer', 'metadata', 'town', 'town1']
class CourtView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Court, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'short_code']
class CourtaccountView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtaccount, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'object_of_litigation', 'parent', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']
class CourtcaseView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtcase, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class CourtrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtrank, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class CourtstationView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtstation, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['description', 'id', 'law', 'metadata', 'ref']
class CrimeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Crime, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'investigationdiary', 'metadata']
class CsiEquipmentView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(CsiEquipment, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata']
class DiagramView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Diagram, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'party', 'party1', 'prison_officer', 'prisonofficer']
class DisciplineView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Discipline, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title']
class DoctemplateView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Doctemplate, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_name', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'name', 'page_count', 'paid', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']
class DocumentView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Document, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class DocumenttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Documenttype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class EconomicclasView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Economicclas, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['docx', 'exhibit_no', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'photo', 'seizure', 'seizure1']
class ExhibitView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Exhibit, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata']
class ExpertView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Expert, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']
class ExperttestimonyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Experttestimony, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class ExperttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Experttype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['fee_type', 'id', 'metadata', 'parent']
class FeeclasView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Feeclas, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'unit']
class FeetypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Feetype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['enddate', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'notes', 'party', 'party1', 'prisonofficer', 'reporting_prison_officer', 'startdate']
class HealtheventView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Healthevent, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class HealtheventtypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Healtheventtype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'notes', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']
class HearingView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Hearing, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['hearing_type', 'id', 'metadata', 'parent']
class HearingtypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Hearingtype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['hashable', 'native', 'python_type', 'should_evaluate_none']
class INTERVALView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(INTERVAL, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type']
class InstancecrimeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Instancecrime, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['answer', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated']
class InterviewView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Interview, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['date_assigned', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']
class InvestigatingOfficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(InvestigatingOfficer, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'id', 'location', 'metadata', 'outcome', 'party', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']
class InvestigationdiaryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Investigationdiary, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']
class IssueView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Issue, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['court_station', 'courtstation', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'rank']
class JudicialofficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Judicialofficer, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class JudicialrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Judicialrank, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class JudicialroleView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Judicialrole, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class LawfirmView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Lawfirm, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['bar_date', 'bar_no', 'id', 'law_firm', 'lawfirm', 'metadata', 'party']
class LawyerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Lawyer, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['citation', 'commentary', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim']
class LegalreferenceView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Legalreference, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['metadata']
class ModelView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Model, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['biodata', 'biodatum', 'childunder4', 'id', 'metadata']
class NextofkinView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Nextofkin, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent']
class NotificationView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notification, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count']
class NotificationregisterView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notificationregister, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['description', 'id', 'metadata', 'name']
class NotificationtypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notificationtype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class NotifyeventView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notifyevent, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['create_date', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt']
class PageView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Page, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['active', 'biodata', 'biodatum', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']
class PartyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Party, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class PartytypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Partytype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['amount', 'bill', 'bill1', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated']
class PaymentView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Payment, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory']
class PersonaleffectView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Personaleffect, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class PersonaleffectscategoryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Personaleffectscategory, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']
class PoliceofficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policeofficer, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['description', 'id', 'metadata', 'name', 'sequence']
class PoliceofficerrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policeofficerrank, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']
class PolicestationView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policestation, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class PolicestationrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policestationrank, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'town', 'town1']
class PrisonView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prison, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']
class PrisonofficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prisonofficer, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class PrisonofficerrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prisonofficerrank, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'lawyer', 'lawyer1', 'metadata', 'prosecutor_team', 'prosecutorteam']
class ProsecutorView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prosecutor, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class ProsecutorteamView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prosecutorteam, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class ReleasetypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Releasetype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class ReligionView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Religion, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class SchedulestatustypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Schedulestatustype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']
class SeizureView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Seizure, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['amount', 'complaint', 'complaint1', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms']
class SettlementView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Settlement, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['county', 'county1', 'id', 'metadata']
class SubcountyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Subcounty, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'parent', 'template_type']
class TemplatetypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Templatetype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'ward']
class TownView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Town, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'video']
class TranscriptView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Transcript, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno']
class VehicleView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Vehicle, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata', 'subcounty', 'subcounty1']
class WardView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Ward, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    

# FIELDS: ['id', 'metadata']
class WarranttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Warranttype, db.session)
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
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]}
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {{'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }}
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']]}
    
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
    





##################### Join Table Views##################### View Table for:t_casecategory_courtcase
class t_casecategory_courtcaseView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_casecategory_courtcase)
    # list_columns = []


# View Table for:t_casecategorychecklist
class t_casecategorychecklistView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_casecategorychecklist)
    # list_columns = []


# View Table for:t_complaint_complaintcategory
class t_complaint_complaintcategoryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_complaint_complaintcategory)
    # list_columns = []


# View Table for:t_complaint_courtcase
class t_complaint_courtcaseView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_complaint_courtcase)
    # list_columns = []


# View Table for:t_court_judicialofficer
class t_court_judicialofficerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_court_judicialofficer)
    # list_columns = []


# View Table for:t_courtcase_judicialofficer
class t_courtcase_judicialofficerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_courtcase_judicialofficer)
    # list_columns = []


# View Table for:t_courtcase_lawfirm
class t_courtcase_lawfirmView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_courtcase_lawfirm)
    # list_columns = []


# View Table for:t_csi_equipment_investigationdiary
class t_csi_equipment_investigationdiaryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_csi_equipment_investigationdiary)
    # list_columns = []


# View Table for:t_document_documenttype
class t_document_documenttypeView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_document_documenttype)
    # list_columns = []


# View Table for:t_expert_experttype
class t_expert_experttypeView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_expert_experttype)
    # list_columns = []


# View Table for:t_hearing_issue
class t_hearing_issueView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_issue)
    # list_columns = []


# View Table for:t_hearing_judicialofficer
class t_hearing_judicialofficerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_judicialofficer)
    # list_columns = []


# View Table for:t_hearing_lawfirm
class t_hearing_lawfirmView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_lawfirm)
    # list_columns = []


# View Table for:t_hearing_lawfirm_2
class t_hearing_lawfirm_2View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_lawfirm_2)
    # list_columns = []


# View Table for:t_instancecrime_issue
class t_instancecrime_issueView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_instancecrime_issue)
    # list_columns = []


# View Table for:t_investigating_officer_investigationdiary
class t_investigating_officer_investigationdiaryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_investigating_officer_investigationdiary)
    # list_columns = []


# View Table for:t_investigationdiary_party
class t_investigationdiary_partyView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_investigationdiary_party)
    # list_columns = []


# View Table for:t_investigationdiary_vehicle
class t_investigationdiary_vehicleView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_investigationdiary_vehicle)
    # list_columns = []


# View Table for:t_issue_lawyer
class t_issue_lawyerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_lawyer)
    # list_columns = []


# View Table for:t_issue_legalreference
class t_issue_legalreferenceView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_legalreference)
    # list_columns = []


# View Table for:t_issue_legalreference_2
class t_issue_legalreference_2View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_legalreference_2)
    # list_columns = []


# View Table for:t_issue_party
class t_issue_partyView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_party)
    # list_columns = []


# View Table for:t_issue_party_2
class t_issue_party_2View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_party_2)
    # list_columns = []


# View Table for:t_lawyer_party
class t_lawyer_partyView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_lawyer_party)
    # list_columns = []


# View Table for:t_party_settlement
class t_party_settlementView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_party_settlement)
    # list_columns = []


# View Table for:t_policeofficer_policestation
class t_policeofficer_policestationView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_policeofficer_policestation)
    # list_columns = []


# View Table for:t_town_ward
class t_town_wardView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_town_ward)
    # list_columns = []






##################### Join MultipleViews####################
# MultiView for:t_casecategory_courtcase
class t_casecategory_courtcaseMultiView(MultipleView):
    
	views = ['CasecategoryView', 'CourtcaseView']



# MultiView for:t_casecategorychecklist
class t_casecategorychecklistMultiView(MultipleView):
    
	views = ['CasecategorychecklistView']



# MultiView for:t_complaint_complaintcategory
class t_complaint_complaintcategoryMultiView(MultipleView):
    
	views = ['ComplaintView', 'ComplaintcategoryView']



# MultiView for:t_complaint_courtcase
class t_complaint_courtcaseMultiView(MultipleView):
    
	views = ['ComplaintView', 'CourtcaseView']



# MultiView for:t_court_judicialofficer
class t_court_judicialofficerMultiView(MultipleView):
    
	views = ['CourtView', 'JudicialofficerView']



# MultiView for:t_courtcase_judicialofficer
class t_courtcase_judicialofficerMultiView(MultipleView):
    
	views = ['CourtcaseView', 'JudicialofficerView']



# MultiView for:t_courtcase_lawfirm
class t_courtcase_lawfirmMultiView(MultipleView):
    
	views = ['CourtcaseView', 'LawfirmView']



# MultiView for:t_csi_equipment_investigationdiary
class t_csi_equipment_investigationdiaryMultiView(MultipleView):
    
	views = ['CsiView', 'EquipmentView', 'InvestigationdiaryView']



# MultiView for:t_document_documenttype
class t_document_documenttypeMultiView(MultipleView):
    
	views = ['DocumentView', 'DocumenttypeView']



# MultiView for:t_expert_experttype
class t_expert_experttypeMultiView(MultipleView):
    
	views = ['ExpertView', 'ExperttypeView']



# MultiView for:t_hearing_issue
class t_hearing_issueMultiView(MultipleView):
    
	views = ['HearingView', 'IssueView']



# MultiView for:t_hearing_judicialofficer
class t_hearing_judicialofficerMultiView(MultipleView):
    
	views = ['HearingView', 'JudicialofficerView']



# MultiView for:t_hearing_lawfirm
class t_hearing_lawfirmMultiView(MultipleView):
    
	views = ['HearingView', 'LawfirmView']



# MultiView for:t_hearing_lawfirm_2
class t_hearing_lawfirm_2MultiView(MultipleView):
    
	views = ['HearingView', 'LawfirmView', '2View']



# MultiView for:t_instancecrime_issue
class t_instancecrime_issueMultiView(MultipleView):
    
	views = ['InstancecrimeView', 'IssueView']



# MultiView for:t_investigating_officer_investigationdiary
class t_investigating_officer_investigationdiaryMultiView(MultipleView):
    
	views = ['InvestigatingView', 'OfficerView', 'InvestigationdiaryView']



# MultiView for:t_investigationdiary_party
class t_investigationdiary_partyMultiView(MultipleView):
    
	views = ['InvestigationdiaryView', 'PartyView']



# MultiView for:t_investigationdiary_vehicle
class t_investigationdiary_vehicleMultiView(MultipleView):
    
	views = ['InvestigationdiaryView', 'VehicleView']



# MultiView for:t_issue_lawyer
class t_issue_lawyerMultiView(MultipleView):
    
	views = ['IssueView', 'LawyerView']



# MultiView for:t_issue_legalreference
class t_issue_legalreferenceMultiView(MultipleView):
    
	views = ['IssueView', 'LegalreferenceView']



# MultiView for:t_issue_legalreference_2
class t_issue_legalreference_2MultiView(MultipleView):
    
	views = ['IssueView', 'LegalreferenceView', '2View']



# MultiView for:t_issue_party
class t_issue_partyMultiView(MultipleView):
    
	views = ['IssueView', 'PartyView']



# MultiView for:t_issue_party_2
class t_issue_party_2MultiView(MultipleView):
    
	views = ['IssueView', 'PartyView', '2View']



# MultiView for:t_lawyer_party
class t_lawyer_partyMultiView(MultipleView):
    
	views = ['LawyerView', 'PartyView']



# MultiView for:t_party_settlement
class t_party_settlementMultiView(MultipleView):
    
	views = ['PartyView', 'SettlementView']



# MultiView for:t_policeofficer_policestation
class t_policeofficer_policestationMultiView(MultipleView):
    
	views = ['PoliceofficerView', 'PolicestationView']



# MultiView for:t_town_ward
class t_town_wardMultiView(MultipleView):
    
	views = ['TownView', 'WardView']






##################### Chart Views####################
class AccounttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Accounttype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = AccounttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class BillChartView(GroupByChartView):
    datamodel = SQLAInterface(Bill, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = BillView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class BilldetailChartView(GroupByChartView):
    datamodel = SQLAInterface(Billdetail, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = BilldetailView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class BiodatumChartView(GroupByChartView):
    datamodel = SQLAInterface(Biodatum, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = BiodatumView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CasecategoryChartView(GroupByChartView):
    datamodel = SQLAInterface(Casecategory, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CasecategoryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CasechecklistChartView(GroupByChartView):
    datamodel = SQLAInterface(Casechecklist, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CasechecklistView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CaselinktypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Caselinktype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CaselinktypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CelltypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Celltype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CelltypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CommitalChartView(GroupByChartView):
    datamodel = SQLAInterface(Commital, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CommitalView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CommitaltypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Commitaltype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CommitaltypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ComplaintChartView(GroupByChartView):
    datamodel = SQLAInterface(Complaint, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ComplaintView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ComplaintcategoryChartView(GroupByChartView):
    datamodel = SQLAInterface(Complaintcategory, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ComplaintcategoryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ComplaintroleChartView(GroupByChartView):
    datamodel = SQLAInterface(Complaintrole, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ComplaintroleView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CountryChartView(GroupByChartView):
    datamodel = SQLAInterface(Country, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CountryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CountyChartView(GroupByChartView):
    datamodel = SQLAInterface(County, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CountyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CourtChartView(GroupByChartView):
    datamodel = SQLAInterface(Court, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CourtaccountChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtaccount, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtaccountView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CourtcaseChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtcase, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtcaseView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CourtrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtrank, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CourtstationChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtstation, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtstationView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CrimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Crime, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CrimeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class CsiEquipmentChartView(GroupByChartView):
    datamodel = SQLAInterface(CsiEquipment, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CsiEquipmentView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class DiagramChartView(GroupByChartView):
    datamodel = SQLAInterface(Diagram, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DiagramView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class DisciplineChartView(GroupByChartView):
    datamodel = SQLAInterface(Discipline, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DisciplineView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class DoctemplateChartView(GroupByChartView):
    datamodel = SQLAInterface(Doctemplate, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DoctemplateView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class DocumentChartView(GroupByChartView):
    datamodel = SQLAInterface(Document, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DocumentView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class DocumenttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Documenttype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DocumenttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class EconomicclasChartView(GroupByChartView):
    datamodel = SQLAInterface(Economicclas, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = EconomicclasView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ExhibitChartView(GroupByChartView):
    datamodel = SQLAInterface(Exhibit, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExhibitView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ExpertChartView(GroupByChartView):
    datamodel = SQLAInterface(Expert, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExpertView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ExperttestimonyChartView(GroupByChartView):
    datamodel = SQLAInterface(Experttestimony, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExperttestimonyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ExperttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Experttype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExperttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class FeeclasChartView(GroupByChartView):
    datamodel = SQLAInterface(Feeclas, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = FeeclasView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class FeetypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Feetype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = FeetypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class HealtheventChartView(GroupByChartView):
    datamodel = SQLAInterface(Healthevent, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HealtheventView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class HealtheventtypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Healtheventtype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HealtheventtypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class HearingChartView(GroupByChartView):
    datamodel = SQLAInterface(Hearing, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HearingView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class HearingtypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Hearingtype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HearingtypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class INTERVALChartView(GroupByChartView):
    datamodel = SQLAInterface(INTERVAL, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = INTERVALView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class InstancecrimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Instancecrime, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InstancecrimeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class InterviewChartView(GroupByChartView):
    datamodel = SQLAInterface(Interview, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InterviewView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class InvestigatingOfficerChartView(GroupByChartView):
    datamodel = SQLAInterface(InvestigatingOfficer, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InvestigatingOfficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class InvestigationdiaryChartView(GroupByChartView):
    datamodel = SQLAInterface(Investigationdiary, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InvestigationdiaryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class IssueChartView(GroupByChartView):
    datamodel = SQLAInterface(Issue, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = IssueView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class JudicialofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialofficer, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialofficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class JudicialrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialrank, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class JudicialroleChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialrole, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialroleView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class LawfirmChartView(GroupByChartView):
    datamodel = SQLAInterface(Lawfirm, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LawfirmView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class LawyerChartView(GroupByChartView):
    datamodel = SQLAInterface(Lawyer, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LawyerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class LegalreferenceChartView(GroupByChartView):
    datamodel = SQLAInterface(Legalreference, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LegalreferenceView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ModelChartView(GroupByChartView):
    datamodel = SQLAInterface(Model, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ModelView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class NextofkinChartView(GroupByChartView):
    datamodel = SQLAInterface(Nextofkin, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NextofkinView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class NotificationChartView(GroupByChartView):
    datamodel = SQLAInterface(Notification, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotificationView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class NotificationregisterChartView(GroupByChartView):
    datamodel = SQLAInterface(Notificationregister, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotificationregisterView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class NotificationtypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Notificationtype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotificationtypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class NotifyeventChartView(GroupByChartView):
    datamodel = SQLAInterface(Notifyevent, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotifyeventView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PageChartView(GroupByChartView):
    datamodel = SQLAInterface(Page, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PageView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PartyChartView(GroupByChartView):
    datamodel = SQLAInterface(Party, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PartyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PartytypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Partytype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PartytypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PaymentChartView(GroupByChartView):
    datamodel = SQLAInterface(Payment, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PaymentView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PersonaleffectChartView(GroupByChartView):
    datamodel = SQLAInterface(Personaleffect, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PersonaleffectView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PersonaleffectscategoryChartView(GroupByChartView):
    datamodel = SQLAInterface(Personaleffectscategory, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PersonaleffectscategoryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PoliceofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Policeofficer, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PoliceofficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PoliceofficerrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Policeofficerrank, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PoliceofficerrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PolicestationChartView(GroupByChartView):
    datamodel = SQLAInterface(Policestation, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PolicestationView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PolicestationrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Policestationrank, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PolicestationrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PrisonChartView(GroupByChartView):
    datamodel = SQLAInterface(Prison, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisonView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PrisonofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Prisonofficer, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisonofficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class PrisonofficerrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Prisonofficerrank, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisonofficerrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ProsecutorChartView(GroupByChartView):
    datamodel = SQLAInterface(Prosecutor, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ProsecutorView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ProsecutorteamChartView(GroupByChartView):
    datamodel = SQLAInterface(Prosecutorteam, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ProsecutorteamView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ReleasetypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Releasetype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ReleasetypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class ReligionChartView(GroupByChartView):
    datamodel = SQLAInterface(Religion, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ReligionView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class SchedulestatustypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Schedulestatustype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SchedulestatustypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class SeizureChartView(GroupByChartView):
    datamodel = SQLAInterface(Seizure, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SeizureView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class SettlementChartView(GroupByChartView):
    datamodel = SQLAInterface(Settlement, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SettlementView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class SubcountyChartView(GroupByChartView):
    datamodel = SQLAInterface(Subcounty, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SubcountyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class TemplatetypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Templatetype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = TemplatetypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class TownChartView(GroupByChartView):
    datamodel = SQLAInterface(Town, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = TownView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class TranscriptChartView(GroupByChartView):
    datamodel = SQLAInterface(Transcript, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = TranscriptView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class VehicleChartView(GroupByChartView):
    datamodel = SQLAInterface(Vehicle, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = VehicleView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class WardChartView(GroupByChartView):
    datamodel = SQLAInterface(Ward, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = WardView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    



class WarranttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Warranttype, db.session) 
    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = WarranttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series": [(aggregate_count,"age_today")]
        }
    ]
    






##################### WTForms-Alchemy Forms####################



##################### Just in case we ever need them####################
class wtf_AccounttypeForm(ModelForm):
    class Meta:
        model = Accounttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_BillForm(ModelForm):
    class Meta:
        model = Bill
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_BilldetailForm(ModelForm):
    class Meta:
        model = Billdetail
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_BiodatumForm(ModelForm):
    class Meta:
        model = Biodatum
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CasecategoryForm(ModelForm):
    class Meta:
        model = Casecategory
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CasechecklistForm(ModelForm):
    class Meta:
        model = Casechecklist
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CaselinktypeForm(ModelForm):
    class Meta:
        model = Caselinktype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CelltypeForm(ModelForm):
    class Meta:
        model = Celltype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CommitalForm(ModelForm):
    class Meta:
        model = Commital
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CommitaltypeForm(ModelForm):
    class Meta:
        model = Commitaltype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ComplaintcategoryForm(ModelForm):
    class Meta:
        model = Complaintcategory
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ComplaintroleForm(ModelForm):
    class Meta:
        model = Complaintrole
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CountryForm(ModelForm):
    class Meta:
        model = Country
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CountyForm(ModelForm):
    class Meta:
        model = County
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CourtForm(ModelForm):
    class Meta:
        model = Court
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CourtaccountForm(ModelForm):
    class Meta:
        model = Courtaccount
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CourtcaseForm(ModelForm):
    class Meta:
        model = Courtcase
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CourtrankForm(ModelForm):
    class Meta:
        model = Courtrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CourtstationForm(ModelForm):
    class Meta:
        model = Courtstation
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CrimeForm(ModelForm):
    class Meta:
        model = Crime
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_CsiEquipmentForm(ModelForm):
    class Meta:
        model = CsiEquipment
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_DiagramForm(ModelForm):
    class Meta:
        model = Diagram
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_DoctemplateForm(ModelForm):
    class Meta:
        model = Doctemplate
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_DocumentForm(ModelForm):
    class Meta:
        model = Document
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_DocumenttypeForm(ModelForm):
    class Meta:
        model = Documenttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_EconomicclasForm(ModelForm):
    class Meta:
        model = Economicclas
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ExhibitForm(ModelForm):
    class Meta:
        model = Exhibit
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ExpertForm(ModelForm):
    class Meta:
        model = Expert
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ExperttestimonyForm(ModelForm):
    class Meta:
        model = Experttestimony
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ExperttypeForm(ModelForm):
    class Meta:
        model = Experttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_FeeclasForm(ModelForm):
    class Meta:
        model = Feeclas
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_FeetypeForm(ModelForm):
    class Meta:
        model = Feetype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_HealtheventForm(ModelForm):
    class Meta:
        model = Healthevent
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_HealtheventtypeForm(ModelForm):
    class Meta:
        model = Healtheventtype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_HearingForm(ModelForm):
    class Meta:
        model = Hearing
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_HearingtypeForm(ModelForm):
    class Meta:
        model = Hearingtype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_INTERVALForm(ModelForm):
    class Meta:
        model = INTERVAL
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_InstancecrimeForm(ModelForm):
    class Meta:
        model = Instancecrime
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_InterviewForm(ModelForm):
    class Meta:
        model = Interview
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_InvestigatingOfficerForm(ModelForm):
    class Meta:
        model = InvestigatingOfficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_InvestigationdiaryForm(ModelForm):
    class Meta:
        model = Investigationdiary
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_IssueForm(ModelForm):
    class Meta:
        model = Issue
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_JudicialofficerForm(ModelForm):
    class Meta:
        model = Judicialofficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_JudicialrankForm(ModelForm):
    class Meta:
        model = Judicialrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_JudicialroleForm(ModelForm):
    class Meta:
        model = Judicialrole
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_LawfirmForm(ModelForm):
    class Meta:
        model = Lawfirm
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_LawyerForm(ModelForm):
    class Meta:
        model = Lawyer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_LegalreferenceForm(ModelForm):
    class Meta:
        model = Legalreference
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ModelForm(ModelForm):
    class Meta:
        model = Model
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_NextofkinForm(ModelForm):
    class Meta:
        model = Nextofkin
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_NotificationForm(ModelForm):
    class Meta:
        model = Notification
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_NotificationregisterForm(ModelForm):
    class Meta:
        model = Notificationregister
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_NotificationtypeForm(ModelForm):
    class Meta:
        model = Notificationtype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_NotifyeventForm(ModelForm):
    class Meta:
        model = Notifyevent
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PageForm(ModelForm):
    class Meta:
        model = Page
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PartyForm(ModelForm):
    class Meta:
        model = Party
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PartytypeForm(ModelForm):
    class Meta:
        model = Partytype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PaymentForm(ModelForm):
    class Meta:
        model = Payment
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PersonaleffectForm(ModelForm):
    class Meta:
        model = Personaleffect
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PersonaleffectscategoryForm(ModelForm):
    class Meta:
        model = Personaleffectscategory
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PoliceofficerForm(ModelForm):
    class Meta:
        model = Policeofficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PoliceofficerrankForm(ModelForm):
    class Meta:
        model = Policeofficerrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PolicestationForm(ModelForm):
    class Meta:
        model = Policestation
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PolicestationrankForm(ModelForm):
    class Meta:
        model = Policestationrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PrisonForm(ModelForm):
    class Meta:
        model = Prison
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PrisonofficerForm(ModelForm):
    class Meta:
        model = Prisonofficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_PrisonofficerrankForm(ModelForm):
    class Meta:
        model = Prisonofficerrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ProsecutorForm(ModelForm):
    class Meta:
        model = Prosecutor
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ProsecutorteamForm(ModelForm):
    class Meta:
        model = Prosecutorteam
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ReleasetypeForm(ModelForm):
    class Meta:
        model = Releasetype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_ReligionForm(ModelForm):
    class Meta:
        model = Religion
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_SchedulestatustypeForm(ModelForm):
    class Meta:
        model = Schedulestatustype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_SeizureForm(ModelForm):
    class Meta:
        model = Seizure
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_SettlementForm(ModelForm):
    class Meta:
        model = Settlement
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_SubcountyForm(ModelForm):
    class Meta:
        model = Subcounty
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_TemplatetypeForm(ModelForm):
    class Meta:
        model = Templatetype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_TownForm(ModelForm):
    class Meta:
        model = Town
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_TranscriptForm(ModelForm):
    class Meta:
        model = Transcript
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_WardForm(ModelForm):
    class Meta:
        model = Ward
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)



class wtf_WarranttypeForm(ModelForm):
    class Meta:
        model = Warranttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)








##################### View Registrations####################appbuilder.add_view(AccounttypeView(), "Accounttype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(BillView(), "Bill", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(BilldetailView(), "Billdetail", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(BiodatumView(), "Biodatum", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CasecategoryView(), "Casecategory", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CasechecklistView(), "Casechecklist", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CaselinktypeView(), "Caselinktype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CelltypeView(), "Celltype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CommitalView(), "Commital", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CommitaltypeView(), "Commitaltype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ComplaintView(), "Complaint", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ComplaintcategoryView(), "Complaintcategory", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ComplaintroleView(), "Complaintrole", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CountryView(), "Country", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CountyView(), "County", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CourtView(), "Court", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CourtaccountView(), "Courtaccount", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CourtcaseView(), "Courtcase", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CourtrankView(), "Courtrank", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CourtstationView(), "Courtstation", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CrimeView(), "Crime", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CsiEquipmentView(), "CsiEquipment", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(DiagramView(), "Diagram", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(DisciplineView(), "Discipline", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(DoctemplateView(), "Doctemplate", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(DocumentView(), "Document", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(DocumenttypeView(), "Documenttype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(EconomicclasView(), "Economicclas", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ExhibitView(), "Exhibit", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ExpertView(), "Expert", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ExperttestimonyView(), "Experttestimony", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ExperttypeView(), "Experttype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(FeeclasView(), "Feeclas", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(FeetypeView(), "Feetype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(HealtheventView(), "Healthevent", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(HealtheventtypeView(), "Healtheventtype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(HearingView(), "Hearing", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(HearingtypeView(), "Hearingtype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(INTERVALView(), "INTERVAL", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(InstancecrimeView(), "Instancecrime", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(InterviewView(), "Interview", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(InvestigatingOfficerView(), "InvestigatingOfficer", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(InvestigationdiaryView(), "Investigationdiary", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(IssueView(), "Issue", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(JudicialofficerView(), "Judicialofficer", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(JudicialrankView(), "Judicialrank", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(JudicialroleView(), "Judicialrole", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(LawfirmView(), "Lawfirm", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(LawyerView(), "Lawyer", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(LegalreferenceView(), "Legalreference", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ModelView(), "Model", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(NextofkinView(), "Nextofkin", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(NotificationView(), "Notification", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(NotificationregisterView(), "Notificationregister", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(NotificationtypeView(), "Notificationtype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(NotifyeventView(), "Notifyevent", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PageView(), "Page", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PartyView(), "Party", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PartytypeView(), "Partytype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PaymentView(), "Payment", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PersonaleffectView(), "Personaleffect", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PersonaleffectscategoryView(), "Personaleffectscategory", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PoliceofficerView(), "Policeofficer", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PoliceofficerrankView(), "Policeofficerrank", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PolicestationView(), "Policestation", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PolicestationrankView(), "Policestationrank", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PrisonView(), "Prison", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PrisonofficerView(), "Prisonofficer", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PrisonofficerrankView(), "Prisonofficerrank", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ProsecutorView(), "Prosecutor", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ProsecutorteamView(), "Prosecutorteam", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ReleasetypeView(), "Releasetype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ReligionView(), "Religion", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(SchedulestatustypeView(), "Schedulestatustype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(SeizureView(), "Seizure", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(SettlementView(), "Settlement", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(SubcountyView(), "Subcounty", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(TemplatetypeView(), "Templatetype", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(TownView(), "Town", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(TranscriptView(), "Transcript", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(VehicleView(), "Vehicle", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(WardView(), "Ward", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(WarranttypeView(), "Warranttype", icon="fa-folder-open-o", category="Setup")




##################### Join Table Registrations####################appbuilder.add_view_no_menu(t_casecategory_courtcaseView(), "t_casecategory_courtcase")
appbuilder.add_view_no_menu(t_casecategorychecklistView(), "t_casecategorychecklist")
appbuilder.add_view_no_menu(t_complaint_complaintcategoryView(), "t_complaint_complaintcategory")
appbuilder.add_view_no_menu(t_complaint_courtcaseView(), "t_complaint_courtcase")
appbuilder.add_view_no_menu(t_court_judicialofficerView(), "t_court_judicialofficer")
appbuilder.add_view_no_menu(t_courtcase_judicialofficerView(), "t_courtcase_judicialofficer")
appbuilder.add_view_no_menu(t_courtcase_lawfirmView(), "t_courtcase_lawfirm")
appbuilder.add_view_no_menu(t_csi_equipment_investigationdiaryView(), "t_csi_equipment_investigationdiary")
appbuilder.add_view_no_menu(t_document_documenttypeView(), "t_document_documenttype")
appbuilder.add_view_no_menu(t_expert_experttypeView(), "t_expert_experttype")
appbuilder.add_view_no_menu(t_hearing_issueView(), "t_hearing_issue")
appbuilder.add_view_no_menu(t_hearing_judicialofficerView(), "t_hearing_judicialofficer")
appbuilder.add_view_no_menu(t_hearing_lawfirmView(), "t_hearing_lawfirm")
appbuilder.add_view_no_menu(t_hearing_lawfirm_2View(), "t_hearing_lawfirm_2")
appbuilder.add_view_no_menu(t_instancecrime_issueView(), "t_instancecrime_issue")
appbuilder.add_view_no_menu(t_investigating_officer_investigationdiaryView(), "t_investigating_officer_investigationdiary")
appbuilder.add_view_no_menu(t_investigationdiary_partyView(), "t_investigationdiary_party")
appbuilder.add_view_no_menu(t_investigationdiary_vehicleView(), "t_investigationdiary_vehicle")
appbuilder.add_view_no_menu(t_issue_lawyerView(), "t_issue_lawyer")
appbuilder.add_view_no_menu(t_issue_legalreferenceView(), "t_issue_legalreference")
appbuilder.add_view_no_menu(t_issue_legalreference_2View(), "t_issue_legalreference_2")
appbuilder.add_view_no_menu(t_issue_partyView(), "t_issue_party")
appbuilder.add_view_no_menu(t_issue_party_2View(), "t_issue_party_2")
appbuilder.add_view_no_menu(t_lawyer_partyView(), "t_lawyer_party")
appbuilder.add_view_no_menu(t_party_settlementView(), "t_party_settlement")
appbuilder.add_view_no_menu(t_policeofficer_policestationView(), "t_policeofficer_policestation")
appbuilder.add_view_no_menu(t_town_wardView(), "t_town_ward")




##################### Register Join Table MultiViews Registrations####################appbuilder.add_view(t_casecategory_courtcaseMultiView(), "['Casecategory', 'Courtcase'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_casecategorychecklistMultiView(), "['Casecategorychecklist'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_complaint_complaintcategoryMultiView(), "['Complaint', 'Complaintcategory'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_complaint_courtcaseMultiView(), "['Complaint', 'Courtcase'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_court_judicialofficerMultiView(), "['Court', 'Judicialofficer'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_courtcase_judicialofficerMultiView(), "['Courtcase', 'Judicialofficer'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_courtcase_lawfirmMultiView(), "['Courtcase', 'Lawfirm'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_csi_equipment_investigationdiaryMultiView(), "['Csi', 'Equipment', 'Investigationdiary'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_document_documenttypeMultiView(), "['Document', 'Documenttype'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_expert_experttypeMultiView(), "['Expert', 'Experttype'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_hearing_issueMultiView(), "['Hearing', 'Issue'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_hearing_judicialofficerMultiView(), "['Hearing', 'Judicialofficer'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_hearing_lawfirmMultiView(), "['Hearing', 'Lawfirm'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_hearing_lawfirm_2MultiView(), "['Hearing', 'Lawfirm', '2'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_instancecrime_issueMultiView(), "['Instancecrime', 'Issue'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_investigating_officer_investigationdiaryMultiView(), "['Investigating', 'Officer', 'Investigationdiary'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_investigationdiary_partyMultiView(), "['Investigationdiary', 'Party'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_investigationdiary_vehicleMultiView(), "['Investigationdiary', 'Vehicle'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_issue_lawyerMultiView(), "['Issue', 'Lawyer'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_issue_legalreferenceMultiView(), "['Issue', 'Legalreference'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_issue_legalreference_2MultiView(), "['Issue', 'Legalreference', '2'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_issue_partyMultiView(), "['Issue', 'Party'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_issue_party_2MultiView(), "['Issue', 'Party', '2'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_lawyer_partyMultiView(), "['Lawyer', 'Party'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_party_settlementMultiView(), "['Party', 'Settlement'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_policeofficer_policestationMultiView(), "['Policeofficer', 'Policestation'] Multi View", icon="fa-address-card-o", category="MultiViews")
appbuilder.add_view(t_town_wardMultiView(), "['Town', 'Ward'] Multi View", icon="fa-address-card-o", category="MultiViews")




##################### Chart View Registrations####################appbuilder.add_view(AccounttypeChartView(), "Accounttype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(BillChartView(), "Bill Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(BilldetailChartView(), "Billdetail Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(BiodatumChartView(), "Biodatum Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CasecategoryChartView(), "Casecategory Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CasechecklistChartView(), "Casechecklist Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CaselinktypeChartView(), "Caselinktype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CelltypeChartView(), "Celltype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CommitalChartView(), "Commital Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CommitaltypeChartView(), "Commitaltype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ComplaintChartView(), "Complaint Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ComplaintcategoryChartView(), "Complaintcategory Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ComplaintroleChartView(), "Complaintrole Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CountryChartView(), "Country Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CountyChartView(), "County Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CourtChartView(), "Court Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CourtaccountChartView(), "Courtaccount Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CourtcaseChartView(), "Courtcase Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CourtrankChartView(), "Courtrank Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CourtstationChartView(), "Courtstation Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CrimeChartView(), "Crime Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(CsiEquipmentChartView(), "CsiEquipment Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(DiagramChartView(), "Diagram Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(DisciplineChartView(), "Discipline Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(DoctemplateChartView(), "Doctemplate Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(DocumentChartView(), "Document Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(DocumenttypeChartView(), "Documenttype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(EconomicclasChartView(), "Economicclas Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ExhibitChartView(), "Exhibit Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ExpertChartView(), "Expert Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ExperttestimonyChartView(), "Experttestimony Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ExperttypeChartView(), "Experttype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(FeeclasChartView(), "Feeclas Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(FeetypeChartView(), "Feetype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(HealtheventChartView(), "Healthevent Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(HealtheventtypeChartView(), "Healtheventtype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(HearingChartView(), "Hearing Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(HearingtypeChartView(), "Hearingtype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(INTERVALChartView(), "INTERVAL Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(InstancecrimeChartView(), "Instancecrime Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(InterviewChartView(), "Interview Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(InvestigatingOfficerChartView(), "InvestigatingOfficer Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(InvestigationdiaryChartView(), "Investigationdiary Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(IssueChartView(), "Issue Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(JudicialofficerChartView(), "Judicialofficer Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(JudicialrankChartView(), "Judicialrank Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(JudicialroleChartView(), "Judicialrole Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(LawfirmChartView(), "Lawfirm Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(LawyerChartView(), "Lawyer Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(LegalreferenceChartView(), "Legalreference Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ModelChartView(), "Model Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(NextofkinChartView(), "Nextofkin Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(NotificationChartView(), "Notification Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(NotificationregisterChartView(), "Notificationregister Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(NotificationtypeChartView(), "Notificationtype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(NotifyeventChartView(), "Notifyevent Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PageChartView(), "Page Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PartyChartView(), "Party Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PartytypeChartView(), "Partytype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PaymentChartView(), "Payment Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PersonaleffectChartView(), "Personaleffect Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PersonaleffectscategoryChartView(), "Personaleffectscategory Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PoliceofficerChartView(), "Policeofficer Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PoliceofficerrankChartView(), "Policeofficerrank Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PolicestationChartView(), "Policestation Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PolicestationrankChartView(), "Policestationrank Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PrisonChartView(), "Prison Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PrisonofficerChartView(), "Prisonofficer Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(PrisonofficerrankChartView(), "Prisonofficerrank Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ProsecutorChartView(), "Prosecutor Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ProsecutorteamChartView(), "Prosecutorteam Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ReleasetypeChartView(), "Releasetype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(ReligionChartView(), "Religion Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(SchedulestatustypeChartView(), "Schedulestatustype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(SeizureChartView(), "Seizure Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(SettlementChartView(), "Settlement Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(SubcountyChartView(), "Subcounty Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(TemplatetypeChartView(), "Templatetype Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(TownChartView(), "Town Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(TranscriptChartView(), "Transcript Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(VehicleChartView(), "Vehicle Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(WardChartView(), "Ward Age Chart", icon="fa-bar-chart", category="Charts")
appbuilder.add_view(WarranttypeChartView(), "Warranttype Age Chart", icon="fa-bar-chart", category="Charts")


appbuilder.security_cleanup()



##################### Programming Notes and things of interest####################
# appbuilder.add_separator("Setup")
# appbuilder.add_separator("My Views")
# appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)




##################### Join Table List####################
# t_casecategory_courtcase -['Casecategory', 'Courtcase']
# t_casecategorychecklist -['Casecategorychecklist']
# t_complaint_complaintcategory -['Complaint', 'Complaintcategory']
# t_complaint_courtcase -['Complaint', 'Courtcase']
# t_court_judicialofficer -['Court', 'Judicialofficer']
# t_courtcase_judicialofficer -['Courtcase', 'Judicialofficer']
# t_courtcase_lawfirm -['Courtcase', 'Lawfirm']
# t_csi_equipment_investigationdiary -['Csi', 'Equipment', 'Investigationdiary']
# t_document_documenttype -['Document', 'Documenttype']
# t_expert_experttype -['Expert', 'Experttype']
# t_hearing_issue -['Hearing', 'Issue']
# t_hearing_judicialofficer -['Hearing', 'Judicialofficer']
# t_hearing_lawfirm -['Hearing', 'Lawfirm']
# t_hearing_lawfirm_2 -['Hearing', 'Lawfirm', '2']
# t_instancecrime_issue -['Instancecrime', 'Issue']
# t_investigating_officer_investigationdiary -['Investigating', 'Officer', 'Investigationdiary']
# t_investigationdiary_party -['Investigationdiary', 'Party']
# t_investigationdiary_vehicle -['Investigationdiary', 'Vehicle']
# t_issue_lawyer -['Issue', 'Lawyer']
# t_issue_legalreference -['Issue', 'Legalreference']
# t_issue_legalreference_2 -['Issue', 'Legalreference', '2']
# t_issue_party -['Issue', 'Party']
# t_issue_party_2 -['Issue', 'Party', '2']
# t_lawyer_party -['Lawyer', 'Party']
# t_party_settlement -['Party', 'Settlement']
# t_policeofficer_policestation -['Policeofficer', 'Policestation']
# t_town_ward -['Town', 'Ward']



##################### List of tables####################
# Accounttype
# Bill
# Billdetail
# Biodatum
# Casecategory
# Casechecklist
# Caselinktype
# Celltype
# Commital
# Commitaltype
# Complaint
# Complaintcategory
# Complaintrole
# Country
# County
# Court
# Courtaccount
# Courtcase
# Courtrank
# Courtstation
# Crime
# CsiEquipment
# Diagram
# Discipline
# Doctemplate
# Document
# Documenttype
# Economicclas
# Exhibit
# Expert
# Experttestimony
# Experttype
# Feeclas
# Feetype
# Healthevent
# Healtheventtype
# Hearing
# Hearingtype
# INTERVAL
# Instancecrime
# Interview
# InvestigatingOfficer
# Investigationdiary
# Issue
# Judicialofficer
# Judicialrank
# Judicialrole
# Lawfirm
# Lawyer
# Legalreference
# Model
# Nextofkin
# Notification
# Notificationregister
# Notificationtype
# Notifyevent
# Page
# Party
# Partytype
# Payment
# Personaleffect
# Personaleffectscategory
# Policeofficer
# Policeofficerrank
# Policestation
# Policestationrank
# Prison
# Prisonofficer
# Prisonofficerrank
# Prosecutor
# Prosecutorteam
# Releasetype
# Religion
# Schedulestatustype
# Seizure
# Settlement
# Subcounty
# Templatetype
# Town
# Transcript
# Vehicle
# Ward
# Warranttype
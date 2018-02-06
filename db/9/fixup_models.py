# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT

std_hdr = ''

std_hdrx = """
from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy_utils import aggregated, force_auto_coercion, observes
from sqlalchemy.orm import column_property
from sqlalchemy.event import listens_for
from flask import Markup, url_for

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import INTERVAL
from sqlalchemy.ext.declarative import declarative_base
from flask_appbuilder import Model
from sqlalchemy.event import listens_for
from flask import Markup, url_for
# Versioning Mixin
from sqlalchemy_continuum import make_versioned
#Add __versioned__ = {}

#Searchability look at DocMixin
from sqlalchemy_utils.types import TSVectorType   #Searchability look at DocMixin
from sqlalchemy_searchable import make_searchable

# ActiveRecord Model Features
from sqlalchemy_mixins import AllFeaturesMixin, ActiveRecordMixin

from sqlalchemy.orm import relationship, query, defer, deferred
# IMPORT Postgresql Specific Types
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR )

from sqlalchemy.dialects.postgresql import aggregate_order_by, INTERVAL

from sqlalchemy import (Column, Integer, String, ForeignKey,
    Sequence, Float, Text, BigInteger, Date,
    DateTime, Time, Boolean, Index, CheckConstraint,
    UniqueConstraint,ForeignKeyConstraint, Numeric, LargeBinary , Table)
    
from datetime import timedelta, datetime, date
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.sql import func

# UTILITY CLASSES
import arrow, enum, datetime
from mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')





# Initialize sqlalchemy_utils
#force_auto_coercion()

# Keep versions of all data
make_versioned()
make_searchable()


def future_date(days):
    return datetime.datetime.now() + datetime.timedelta(days=days)
"""
photo_hdr = '' # Temporary Patch

photo_hdrx="""
    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)
    
    mindate = datetime.date(datetime.MINYEAR, 1, 1)

    def ViewName(self):
        return self.__class__.__name__ +'View'
        
    def photo_img(self):
        im = ImageManager()
        vn = self.ViewName()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.ViewName()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.ViewName()
        #pdf = render_pdf(url_for(vn, pk=str(self.id)))
        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))
        #response = make_response(pdf)
        #response.headers['Content-Type'] = 'application/pdf'
        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    
        return Markup(
            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+
            'title="Print">' +
            '<i class="fa fa-edit"></i>' +
            '</a>')
    
    def audio_play(self):
        vn = self.ViewName()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )
                
    def download(self):
        vn = self.ViewName()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')
    
    def file_name(self):
        return get_file_original_name(str(self.file))
        
    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) or self.mindate
    
    def year(self):
        date = self.created_on or self.mindate
        return datetime.datetime(date.year, 1, 1)

"""

imp_add = 0
code = []
imports = []
class_names = []


# Write code to filename
def code_write(filename):
    global code
    thefile = open(filename, 'w')
    for item in code:
        thefile.write("%s\n" % item)
    thefile.close()
    
    
def init_fixup(filename):

    global imp_add, imports, classes, code
    
    with open(filename, 'r') as f:
        code = f.readlines()
        for i in range(len(code)):
            # General Fixups
            code[i] = code[i].replace("nullable=False", "nullable=True",1)
            code[i] = code[i].replace("secondary='","secondary='t_",1)
            
            if code[i].startswith('import') or code[i].startswith('from '):
                imports.append(i)
            if code[i].startswith('class '):
                code[i] = code[i].replace('(Base)', '(Model)',1)
                # Get the classname
                (a, _, _)  = code[i].partition('(')
                b = a.split()
                class_names.append(b[1])
                #code.insert(i+1,'\t__versioned__ = {}\n')
                code.insert(i+2, photo_hdr)
                
        imp_add = max(imports) + 1
        class_count = len(class_names)

def add_imports(impt):
    global imp_add, imports, class_names, code
    
    imp_add += 1
    code.insert(imp_add, impt+ '\n')
    
# TAkes two strings
def add_mixin(class_name, mix_in):
    global imp_add, imports, classes, code
    
    # find the ( and replace with ( Mixin,
    for i in range(len(code)):
        if code[i].startswith('class '):
            (a, _, _) = code[i].partition('(')
            b = a.split()
            if b[1] == class_name:
                code[i] = code[i].replace('(', '( ' + mix_in + ', ')
    




# Returns the line number on which the class declaration is made
def find_class(class_name):
    global code
    for i in range(len(code)):
        if code[i].startswith('class '):
            (a, _, _) = code[i].partition('(')
            b = a.split()
            if b[1] == class_name:
                return i
    return 0
    
# Given line number, finds the next class
def find_next_class(line):
    global code
    for i in range(line, len(code)):
        if code[i].startswith('class '):
            return i
    return 0
    
    
    
    
# We add new code to the top
def add_field_top(class_name, field_code):
    global imp_add, imports, class_names, code
    i = find_class(class_name)
    if i > 0:
        code[i + 2].insert(field_code)


def add_field_below(class_name, field_code):
    global imp_add, imports, class_names, code
    i = find_next_class( find_class(class_name) )
    if i > 0:
        code[i - 2].insert(field_code)



if __name__ == '__main__':
    # Initialize Variables
    init_fixup('mod1.py')
    print("Finished Init Fixup")
    # first we change Base to Model
    
    # Add AuditMixin Across the board
    for x in class_names:
        add_mixin(x,'AuditMixin, AllFeaturesMixin')
    
    
    # it it has the name 'type' or category' add RefTypeMixin
    for x in class_names:
        if x.endswith('type') or \
                x.endswith('category') or\
                x.endswith('rank') or \
                x.endswith('station') or \
                x.endswith('clas') or\
                x.endswith('role') or\
                x.endswith('list') or\
                x.endswith('team'):
            
            add_mixin(x, 'RefTypeMixin')

    for x in class_names:
        if x.endswith('officer'):
            add_mixin(x, 'PersonMixin')
            
    # Adding all the mixin's
    
    # PersonDocMixin
    add_mixin('Nextofkin', 'PersonDocMixin')
    add_mixin('Biodatum',   'PersonDocMixin')
    add_mixin('Biodatum',   'PersonMedicalMixin')
    add_mixin('Biodatum',   'BiometricMixin')
    add_mixin('Biodatum',   'ParentageMixin')
    
    # DocMixin
    add_mixin('Document',  'DocMixin')
    add_mixin('Transcript',  'DocMixin')
    add_mixin('Exhibit',  'DocMixin')
    
    # RefTpeMixin
    add_mixin('Lawfirm',   'RefTypeMixin')
    add_mixin('Discipline','RefTypeMixin')
    
    # PersonMixin
    add_mixin('Party','PersonMixin')
    add_mixin('Lawyer','PersonMixin')
    add_mixin('Nextofkin','PersonMixin')
    add_mixin('Prosecutor','PersonMixin')
    
    # ActivityMixin
    add_mixin('Courtcase','ActivityMixin')
    add_mixin('Hearing','ActivityMixin')
    add_mixin('Commital','ActivityMixin')
    add_mixin('Healthevent','ActivityMixin')
    add_mixin('Investigationdiary','ActivityMixin')
    
    # PlaceMixin
    add_mixin('Court', 'PlaceMixin')
    add_mixin('Prison', 'PlaceMixin')
    add_mixin('Lawfirm', 'PlaceMixin')



    
    # Apply Mixins
    # Also add ContactMixin
    person_mix = ['Party','Lawyer', 'Nextofkin', 'Prosecutor']
    name_mix = []
    activity_mix = ['Courtcase', 'Hearing', 'Investigationdiary', 'Commital']
    place_mix = ['Court', 'Prison', ]
    
    # Add Imports
    add_imports(std_hdr)
            
    code_write('models.py')
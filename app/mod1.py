# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT

import datetime
from datetime import datetime, MINYEAR
from flask_appbuilder import Model
from sqlalchemy.dialects.postgresql.base import INTERVAL
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_appbuilder import Model
from sqlalchemy.event import listens_for
from flask import Markup, url_for

from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.filemanager import get_file_original_name
from sqlalchemy_utils import aggregated, force_auto_coercion, observes
from sqlalchemy.orm import column_property

from flask_appbuilder.filemanager import get_file_original_name
# IMPORT Postgresql Specific Types
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR )

# Versioning and Searchable Mixin
from sqlalchemy_continuum import make_versioned
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable

from .mixins import *

make_versioned()
make_searchable()

# Base = declarative_base()
# metadata = Base.metadata
    
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import INTERVAL
from flask_sqlalchemy import SQLAlchemy

#ENDIMP
# db = SQLAlchemy()


#STARTCLASS
class Accounttype(Model):
    __versioned__ = {}
    __tablename__ = 'accounttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Bill(Model):
    __versioned__ = {}
    __tablename__ = 'bill'
    __table_args__ = (
         ForeignKeyConstraint(['court_account_courts', 'court_account_account__types'], ['courtaccount.courts', 'courtaccount.account__types']),
         Index('idx_bill__court_account_courts_court_account_account__types', 'court_account_courts', 'court_account_account__types')
    )

    id =  Column( Integer, primary_key=True, autoincrement=True)
    assessing_registrar =  Column( ForeignKey('judicialofficer.id'), nullable=False, index=True)
    assess_date =  Column( DateTime)
    receiving_registrar =  Column( ForeignKey('judicialofficer.id'), nullable=False, index=True)
    receive_date =  Column( DateTime)
    lawyer_paying =  Column( ForeignKey('lawyer.id'), index=True)
    party_paying =  Column( ForeignKey('party.id'), index=True)
    documents =  Column( ForeignKey('document.id'), index=True)
    date_of_payment =  Column( DateTime)
    paid =  Column( Boolean)
    bill_code =  Column( String(20), unique=True)
    bill_total =  Column( Numeric(12, 2))
    court =  Column( ForeignKey('court.id'), nullable=False, index=True)
    court_account_courts =  Column( Integer, nullable=False)
    court_account_account__types =  Column( Integer, nullable=False)
    validated =  Column( Boolean)
    validation_date =  Column( DateTime)
    paid_total =  Column( Numeric(12, 2))
    bill_balance =  Column( Numeric(12, 2))
    bill_date =  Column( DateTime)

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Bill.assessing_registrar == Judicialofficer.id', backref='bills')
    court1 =  relationship('Court', primaryjoin='Bill.court == Court.id', backref='bills')
    courtaccount =  relationship('Courtaccount', primaryjoin='and_(Bill.court_account_courts == Courtaccount.courts, Bill.court_account_account__types == Courtaccount.account__types)', backref='bills')
    document =  relationship('Document', primaryjoin='Bill.documents == Document.id', backref='bills')
    lawyer =  relationship('Lawyer', primaryjoin='Bill.lawyer_paying == Lawyer.id', backref='bills')
    party =  relationship('Party', primaryjoin='Bill.party_paying == Party.id', backref='bills')
    judicialofficer1 =  relationship('Judicialofficer', primaryjoin='Bill.receiving_registrar == Judicialofficer.id', backref='bills_52')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Billdetail(Model):
    __versioned__ = {}
    __tablename__ = 'billdetail'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    receipt_id =  Column( ForeignKey('bill.id'), nullable=False, index=True)
    feetype =  Column( ForeignKey('feetype.id'), nullable=False, index=True)
    purpose =  Column( Text, nullable=False)
    unit =  Column( Text)
    qty =  Column( Integer)
    unit_cost =  Column( Numeric(12, 2))
    amount =  Column( Numeric(12, 2))
    bd_date =  Column( DateTime)

    feetype1 =  relationship('Feetype', primaryjoin='Billdetail.feetype == Feetype.id', backref='billdetails')
    receipt =  relationship('Bill', primaryjoin='Billdetail.receipt_id == Bill.id', backref='billdetails')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Biodata(Model):
    __versioned__ = {}
    __tablename__ = 'biodata'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=False, index=True)
    economic_class =  Column( ForeignKey('economicclass.id'), index=True)
    religion =  Column( ForeignKey('religion.id'), index=True)
    photo =  Column( LargeBinary)
    health_status =  Column( Text, nullable=False)

    economicclass =  relationship('Economicclass', primaryjoin='Biodata.economic_class == Economicclass.id', backref='biodatas')
    party1 =  relationship('Party', primaryjoin='Biodata.party == Party.id', backref='biodatas')
    religion1 =  relationship('Religion', primaryjoin='Biodata.religion == Religion.id', backref='biodatas')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Casecategory(Model):
    __versioned__ = {}
    __tablename__ = 'casecategory'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    subcategory =  Column( ForeignKey('casecategory.id'), index=True)

    parent =  relationship('Casecategory', remote_side=[id], primaryjoin='Casecategory.subcategory == Casecategory.id', backref='casecategories')
    casechecklist =  relationship('Casechecklist', secondary='casecategory_casechecklist', backref='casecategories')
    courtcase =  relationship('Courtcase', secondary='casecategory_courtcase', backref='casecategories')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_casecategory_casechecklist =  Table(
    'casecategory_casechecklist', Model.metadata,
     Column('casechecklists',  ForeignKey('casechecklist.id'), primary_key=True, nullable=False),
     Column('casecategories',  ForeignKey('casecategory.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_casecategory_courtcase =  Table(
    'casecategory_courtcase', Model.metadata,
     Column('casecategory',  ForeignKey('casecategory.id'), primary_key=True, nullable=False),
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Casechecklist(Model):
    __versioned__ = {}
    __tablename__ = 'casechecklist'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    check_list_item =  Column( String(100), nullable=False)
    description =  Column( String(100), nullable=False)
    notes =  Column( Text, nullable=False)
    is_mandatory =  Column( Boolean)
    priority =  Column( BigInteger)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Caselinktype(Model):
    __versioned__ = {}
    __tablename__ = 'caselinktype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Celltype(Model):
    __versioned__ = {}
    __tablename__ = 'celltype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Commital(Model):
    __versioned__ = {}
    __tablename__ = 'commital'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    prisons =  Column( ForeignKey('prison.id'), index=True)
    police_station =  Column( ForeignKey('policestation.id'), index=True)
    parties =  Column( ForeignKey('party.id'), nullable=False, index=True)
    casecomplete =  Column( Boolean)
    commit_date =  Column( Date, nullable=False)
    purpose =  Column( Text, nullable=False)
    warrant_type =  Column( ForeignKey('warranttype.id'), nullable=False, index=True)
    warrant_docx =  Column( Text, nullable=False)
    warrant_issue_date =  Column( Date)
    warrant_issued_by =  Column( Text, nullable=False)
    warrant_date_attached =  Column( DateTime)
    duration =  Column( INTERVAL(fields='day to second'))
    commital =  Column( ForeignKey('commital.id'), index=True)
    commital_type =  Column( ForeignKey('commitaltype.id'), nullable=False, index=True)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)
    concurrent =  Column( Boolean)
    life_imprisonment =  Column( Boolean)
    arrival_date =  Column( DateTime)
    sentence_start_date =  Column( DateTime)
    arrest_date =  Column( DateTime)
    remaining_years =  Column( Integer)
    remaining_months =  Column( Integer)
    remaining_days =  Column( Integer)
    cell_number =  Column( Text, nullable=False)
    cell_type =  Column( ForeignKey('celltype.id'), index=True)
    release_date =  Column( DateTime)
    exit_date =  Column( DateTime)
    reason_for_release =  Column( Text, nullable=False)
    with_children =  Column( Boolean)
    release_type =  Column( ForeignKey('releasetype.id'), index=True)
    receiving_officer =  Column( ForeignKey('prisonofficer.id'), nullable=False, index=True)
    releasing_officer =  Column( ForeignKey('prisonofficer.id'), nullable=False, index=True)

    celltype =  relationship('Celltype', primaryjoin='Commital.cell_type == Celltype.id', backref='commitals')
    parent =  relationship('Commital', remote_side=[id], primaryjoin='Commital.commital == Commital.id', backref='commitals')
    commitaltype =  relationship('Commitaltype', primaryjoin='Commital.commital_type == Commitaltype.id', backref='commitals')
    courtcase =  relationship('Courtcase', primaryjoin='Commital.court_case == Courtcase.id', backref='commitals')
    party =  relationship('Party', primaryjoin='Commital.parties == Party.id', backref='commitals')
    policestation =  relationship('Policestation', primaryjoin='Commital.police_station == Policestation.id', backref='commitals')
    prison =  relationship('Prison', primaryjoin='Commital.prisons == Prison.id', backref='commitals')
    prisonofficer =  relationship('Prisonofficer', primaryjoin='Commital.receiving_officer == Prisonofficer.id', backref='commitals')
    releasetype =  relationship('Releasetype', primaryjoin='Commital.release_type == Releasetype.id', backref='commitals')
    prisonofficer1 =  relationship('Prisonofficer', primaryjoin='Commital.releasing_officer == Prisonofficer.id', backref='commitals_97')
    warranttype =  relationship('Warranttype', primaryjoin='Commital.warrant_type == Warranttype.id', backref='commitals')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Commitaltype(Model):
    __versioned__ = {}
    __tablename__ = 'commitaltype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    maxduration =  Column( INTERVAL(fields='day to second'))

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Complaint(Model):
    __versioned__ = {}
    __tablename__ = 'complaint'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    active =  Column( Boolean)
    ob_number =  Column( String(20), nullable=False)
    police_station =  Column( ForeignKey('policestation.id'), nullable=False, index=True)
    daterecvd =  Column( DateTime, nullable=False)
    datefiled =  Column( DateTime)
    datecaseopened =  Column( DateTime)
    casesummary =  Column( String(2000), nullable=False)
    complaintstatement =  Column( Text, nullable=False)
    circumstances =  Column( Text, nullable=False)
    reportingofficer =  Column( ForeignKey('policeofficer.id'), nullable=False, index=True)
    casefileinformation =  Column( Text, nullable=False)
    p_request_help =  Column( Boolean)
    p_instruction =  Column( Text, nullable=False)
    p_submitted =  Column( Boolean)
    p_submission_date =  Column( DateTime)
    p_submission_notes =  Column( Text, nullable=False)
    p_closed =  Column( Text, nullable=False)
    p_evaluation =  Column( Text, nullable=False)
    p_recommend_charge =  Column( Boolean)
    charge_sheet =  Column( Text, nullable=False)
    charge_sheet_docx =  Column( Text, nullable=False)
    evaluating_prosecutor_team =  Column( ForeignKey('prosecutorteam.id'), index=True)
    magistrate_report_date =  Column( DateTime)
    reported_to_judicial_officer =  Column( ForeignKey('judicialofficer.id'), index=True)
    closed =  Column( Boolean)
    close_date =  Column( DateTime)
    close_reason =  Column( Text, nullable=False)

    prosecutorteam =  relationship('Prosecutorteam', primaryjoin='Complaint.evaluating_prosecutor_team == Prosecutorteam.id', backref='complaints')
    policestation =  relationship('Policestation', primaryjoin='Complaint.police_station == Policestation.id', backref='complaints')
    judicialofficer =  relationship('Judicialofficer', primaryjoin='Complaint.reported_to_judicial_officer == Judicialofficer.id', backref='complaints')
    policeofficer =  relationship('Policeofficer', primaryjoin='Complaint.reportingofficer == Policeofficer.id', backref='complaints')
    complaintcategory =  relationship('Complaintcategory', secondary='complaint_complaintcategory', backref='complaints')
    courtcase =  relationship('Courtcase', secondary='complaint_courtcase', backref='complaints')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_complaint_complaintcategory =  Table(
    'complaint_complaintcategory', Model.metadata,
     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=False),
     Column('complaintcategory',  ForeignKey('complaintcategory.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_complaint_courtcase =  Table(
    'complaint_courtcase', Model.metadata,
     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=False),
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Complaintcategory(Model):
    __versioned__ = {}
    __tablename__ = 'complaintcategory'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    complaint_category_parent =  Column( ForeignKey('complaintcategory.id'), index=True)

    parent =  relationship('Complaintcategory', remote_side=[id], primaryjoin='Complaintcategory.complaint_category_parent == Complaintcategory.id', backref='complaintcategories')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Complaintrole(Model):
    __versioned__ = {}
    __tablename__ = 'complaintrole'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Country(Model):
    __versioned__ = {}
    __tablename__ = 'country'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    code =  Column( String(4))
    name =  Column( String(50), nullable=False)
    dial_prefix =  Column( String(6))
    capital =  Column( String(100), nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class County(Model):
    __versioned__ = {}
    __tablename__ = 'county'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    code =  Column( String(10), nullable=False)
    country =  Column( ForeignKey('country.id'), nullable=False, index=True)

    country1 =  relationship('Country', primaryjoin='County.country == Country.id', backref='counties')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Court(Model):
    __versioned__ = {}
    __tablename__ = 'court'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    court_rank =  Column( ForeignKey('courtrank.id'), nullable=False, index=True)
    court_station =  Column( ForeignKey('courtstation.id'), nullable=False, index=True)
    town =  Column( ForeignKey('town.id'), nullable=False, index=True)
    till_number =  Column( Text, nullable=False)

    courtrank =  relationship('Courtrank', primaryjoin='Court.court_rank == Courtrank.id', backref='courts')
    courtstation =  relationship('Courtstation', primaryjoin='Court.court_station == Courtstation.id', backref='courts')
    town1 =  relationship('Town', primaryjoin='Court.town == Town.id', backref='courts')
    judicialofficer =  relationship('Judicialofficer', secondary='court_judicialofficer', backref='courts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_court_judicialofficer =  Table(
    'court_judicialofficer', Model.metadata,
     Column('court',  ForeignKey('court.id'), primary_key=True, nullable=False),
     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Courtaccount(Model):
    __versioned__ = {}
    __tablename__ = 'courtaccount'

    courts =  Column( ForeignKey('court.id'), primary_key=True, nullable=False)
    account__types =  Column( ForeignKey('accounttype.id'), primary_key=True, nullable=False, index=True)
    account_number =  Column( Text, nullable=False)
    account_name =  Column( Text, nullable=False)
    short_code =  Column( Text, nullable=False)
    bank_name =  Column( Text, nullable=False)

    accounttype =  relationship('Accounttype', primaryjoin='Courtaccount.account__types == Accounttype.id', backref='courtaccounts')
    court =  relationship('Court', primaryjoin='Courtaccount.courts == Court.id', backref='courtaccounts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Courtcase(Model):
    __versioned__ = {}
    __tablename__ = 'courtcase'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    docket_number =  Column( String(200), nullable=False)
    case_number =  Column( Text, nullable=False)
    adr =  Column( Boolean)
    mediation_proposal =  Column( Text, nullable=False)
    case_received_date =  Column( Date)
    case_filed_date =  Column( Date)
    case_summary =  Column( Text, nullable=False)
    filing_prosecutor =  Column( ForeignKey('prosecutor.id'), index=True)
    fast_track =  Column( Boolean)
    priority =  Column( Integer)
    object_of_litigation =  Column( Text, nullable=False)
    grounds =  Column( Text, nullable=False)
    prosecution_prayer =  Column( Text, nullable=False)
    pretrial_date =  Column( Date)
    pretrial_notes =  Column( Text, nullable=False)
    pretrial_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)
    case_admissible =  Column( Boolean)
    indictment_date =  Column( Text, nullable=False)
    judgement =  Column( Text, nullable=False)
    judgement_docx =  Column( Text, nullable=False)
    case_link_type =  Column( ForeignKey('caselinktype.id'), index=True)
    linked_cases =  Column( ForeignKey('courtcase.id'), index=True)
    appealed =  Column( Boolean)
    appeal_number =  Column( Text, nullable=False)
    inventory_of_docket =  Column( Text, nullable=False)
    next_hearing_date =  Column( Date)
    interlocutory_judgement =  Column( Text, nullable=False)
    reopen =  Column( Boolean)
    reopen_reason =  Column( Text, nullable=False)
    combined_case =  Column( Boolean)
    value_in_dispute =  Column( Numeric(12, 2))
    award =  Column( Numeric(12, 2))
    govt_liability =  Column( Text, nullable=False)
    active =  Column( Boolean)
    active_date =  Column( DateTime)

    caselinktype =  relationship('Caselinktype', primaryjoin='Courtcase.case_link_type == Caselinktype.id', backref='courtcases')
    prosecutor =  relationship('Prosecutor', primaryjoin='Courtcase.filing_prosecutor == Prosecutor.id', backref='courtcases')
    parent =  relationship('Courtcase', remote_side=[id], primaryjoin='Courtcase.linked_cases == Courtcase.id', backref='courtcases')
    judicialofficer =  relationship('Judicialofficer', primaryjoin='Courtcase.pretrial_registrar == Judicialofficer.id', backref='courtcases')
    judicialofficer1 =  relationship('Judicialofficer', secondary='courtcase_judicialofficer', backref='courtcases_100')
    lawfirm =  relationship('Lawfirm', secondary='courtcase_lawfirm', backref='courtcases')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_courtcase_judicialofficer =  Table(
    'courtcase_judicialofficer', Model.metadata,
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=False),
     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_courtcase_lawfirm =  Table(
    'courtcase_lawfirm', Model.metadata,
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=False),
     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Courtrank(Model):
    __versioned__ = {}
    __tablename__ = 'courtrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Courtstation(Model):
    __versioned__ = {}
    __tablename__ = 'courtstation'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    till_number =  Column( Text, nullable=False)
    pay_bill =  Column( Text, nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Crime(Model):
    __versioned__ = {}
    __tablename__ = 'crime'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    law =  Column( Text, nullable=False)
    description =  Column( Text, nullable=False)
    ref =  Column( Text, nullable=False)
    ref_law =  Column( ForeignKey('law.id'), index=True)
    min_sentence =  Column( Text, nullable=False)
    max_sentence =  Column( Text, nullable=False)
    max_fine =  Column( Numeric(12, 2))

    law1 =  relationship('Law', primaryjoin='Crime.ref_law == Law.id', backref='crimes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Csiequipment(Model):
    __versioned__ = {}
    __tablename__ = 'csiequipment'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    investigationdiary =  relationship('Investigationdiary', secondary='csiequipment_investigationdiary', backref='csiequipments')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_csiequipment_investigationdiary =  Table(
    'csiequipment_investigationdiary', Model.metadata,
     Column('csiequipment',  ForeignKey('csiequipment.id'), primary_key=True, nullable=False),
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Diagram(Model):
    __versioned__ = {}
    __tablename__ = 'diagram'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_diary =  Column( ForeignKey('investigationdiary.id'), nullable=False, index=True)
    image =  Column( Text, nullable=False)
    description =  Column( Text, nullable=False)
    docx =  Column( Text, nullable=False)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Diagram.investigation_diary == Investigationdiary.id', backref='diagrams')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Discipline(Model):
    __versioned__ = {}
    __tablename__ = 'discipline'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=False, index=True)
    prison_officer =  Column( ForeignKey('prisonofficer.id'), nullable=False, index=True)

    party1 =  relationship('Party', primaryjoin='Discipline.party == Party.id', backref='disciplines')
    prisonofficer =  relationship('Prisonofficer', primaryjoin='Discipline.prison_officer == Prisonofficer.id', backref='disciplines')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Docpart(Model):
    __versioned__ = {}
    __tablename__ = 'docpart'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    document =  Column( ForeignKey('document.id'), nullable=False, index=True)
    file_name =  Column( String(200), nullable=False)
    file_ext =  Column( String(10), nullable=False)
    page_no =  Column( BigInteger)
    page_text =  Column( Text, nullable=False)
    image_width =  Column( Text)
    image_height =  Column( Text)
    file_create_date =  Column( DateTime)
    file_update_date =  Column( DateTime)
    file_last_opened_date =  Column( DateTime)
    upload_dt =  Column( DateTime)
    file_byte_count =  Column( Integer)
    file_hash =  Column( String(520), nullable=False)
    file_load_path =  Column( String(300), nullable=False)
    file_upload_date =  Column( DateTime)
    page_count =  Column( Integer)
    file_text =  Column( Text, nullable=False)
    is_image =  Column( Boolean)
    file_parse_status =  Column( Text, nullable=False)
    file_assessed =  Column( Boolean)
    file_accepted =  Column( Boolean)
    file_fee_amount =  Column( Numeric(12, 2))
    language =  Column( String(10), nullable=False)
    file_bin =  Column( Text, nullable=False)

    document1 =  relationship('Document', primaryjoin='Docpart.document == Document.id', backref='docparts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Doctemplate(Model):
    __versioned__ = {}
    __tablename__ = 'doctemplate'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    template =  Column( Text, nullable=False)
    docx =  Column( Text, nullable=False)
    name =  Column( Text, nullable=False)
    title =  Column( Text, nullable=False)
    summary =  Column( Text, nullable=False)
    template_type =  Column( ForeignKey('templatetype.id'), nullable=False, index=True)
    icon =  Column( Text, nullable=False)

    templatetype =  relationship('Templatetype', primaryjoin='Doctemplate.template_type == Templatetype.id', backref='doctemplates')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Document(Model):
    __versioned__ = {}
    __tablename__ = 'document'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( String(100), nullable=False)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)
    issue =  Column( ForeignKey('issue.id'), index=True)
    document_admissibility =  Column( Text, nullable=False)
    admisibility_notes =  Column( Text, nullable=False)
    admitted =  Column( Boolean)
    receiving_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)
    receive_date =  Column( DateTime, autoincrement=True)
    review_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)
    review_date =  Column( DateTime)
    filing_date =  Column( DateTime)
    docx =  Column( Text, nullable=False)
    document_text =  Column( Text, nullable=False)
    published =  Column( Boolean)
    publish_newspaper =  Column( Text, nullable=False)
    publish_date =  Column( Date, autoincrement=True)
    validated =  Column( Boolean)
    paid =  Column( Boolean)
    page_count =  Column( Integer)
    file_byte_count =  Column( Numeric(12, 2))
    file_hash =  Column( String(520), nullable=False)
    file_create_date =  Column( DateTime)
    file_update_date =  Column( DateTime)
    file_last_opened_date =  Column( DateTime)
    file_text =  Column( Text, nullable=False)
    file_name =  Column( String(300), nullable=False)
    file_ext =  Column( String(10), nullable=False)
    file_load_path =  Column( Text, nullable=False)
    file_upload_date =  Column( DateTime)
    file_parse_status =  Column( Text, nullable=False)
    doc_template =  Column( ForeignKey('doctemplate.id'), index=True)
    is_public =  Column( Boolean)
    is_image =  Column( Boolean)
    doc_shelf =  Column( Text, nullable=False)
    doc_row =  Column( Text, nullable=False)
    doc_room =  Column( Text, nullable=False)
    doc_placed_by =  Column( Text, nullable=False)
    citation =  Column( Text, nullable=False)
    language =  Column( String(10))
    request_urgent =  Column( Boolean)
    certify_urgent =  Column( Boolean)
    certifying_judicial_officer =  Column( ForeignKey('judicialofficer.id'), index=True)
    certify_date =  Column( DateTime)
    expiry_date =  Column( DateTime)
    locked =  Column( Boolean)
    lock_date =  Column( DateTime)

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Document.certifying_judicial_officer == Judicialofficer.id', backref='documents')
    courtcase =  relationship('Courtcase', primaryjoin='Document.court_case == Courtcase.id', backref='documents')
    doctemplate =  relationship('Doctemplate', primaryjoin='Document.doc_template == Doctemplate.id', backref='documents')
    issue1 =  relationship('Issue', primaryjoin='Document.issue == Issue.id', backref='documents')
    judicialofficer1 =  relationship('Judicialofficer', primaryjoin='Document.receiving_registrar == Judicialofficer.id', backref='documents_44')
    judicialofficer2 =  relationship('Judicialofficer', primaryjoin='Document.review_registrar == Judicialofficer.id', backref='documents_80')
    documenttype =  relationship('Documenttype', secondary='document_documenttype', backref='documents')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_document_documenttype =  Table(
    'document_documenttype', Model.metadata,
     Column('document',  ForeignKey('document.id'), primary_key=True, nullable=False),
     Column('documenttype',  ForeignKey('documenttype.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Documenttype(Model):
    __versioned__ = {}
    __tablename__ = 'documenttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Economicclass(Model):
    __versioned__ = {}
    __tablename__ = 'economicclass'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( String(50), nullable=False)
    description =  Column( String(100), nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Exhibit(Model):
    __versioned__ = {}
    __tablename__ = 'exhibit'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_entry =  Column( ForeignKey('investigationdiary.id'), nullable=False, index=True)
    exhibit_no =  Column( Text, nullable=False)
    docx =  Column( Text, nullable=False)
    seizure =  Column( ForeignKey('seizure.id'), nullable=False, index=True)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Exhibit.investigation_entry == Investigationdiary.id', backref='exhibits')
    seizure1 =  relationship('Seizure', primaryjoin='Exhibit.seizure == Seizure.id', backref='exhibits')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Expert(Model):
    __versioned__ = {}
    __tablename__ = 'expert'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    institution =  Column( Text, nullable=False)
    jobtitle =  Column( Text, nullable=False)
    credentials =  Column( Text, nullable=False)

    experttype =  relationship('Experttype', secondary='expert_experttype', backref='experts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_expert_experttype =  Table(
    'expert_experttype', Model.metadata,
     Column('expert',  ForeignKey('expert.id'), primary_key=True, nullable=False),
     Column('experttype',  ForeignKey('experttype.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Experttestimony(Model):
    __versioned__ = {}
    __tablename__ = 'experttestimony'

    investigation_entries =  Column( ForeignKey('investigationdiary.id'), primary_key=True, nullable=False)
    experts =  Column( ForeignKey('expert.id'), primary_key=True, nullable=False, index=True)
    task_given =  Column( Text, nullable=False)
    summary_of_facts =  Column( Text, nullable=False)
    statement =  Column( Text, nullable=False)
    task_request_date =  Column( Date)
    testimony_date =  Column( DateTime)
    validated =  Column( Boolean)
    requesting_police_officer =  Column( ForeignKey('policeofficer.id'), index=True)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)

    courtcase =  relationship('Courtcase', primaryjoin='Experttestimony.court_case == Courtcase.id', backref='experttestimonies')
    expert =  relationship('Expert', primaryjoin='Experttestimony.experts == Expert.id', backref='experttestimonies')
    investigationdiary =  relationship('Investigationdiary', primaryjoin='Experttestimony.investigation_entries == Investigationdiary.id', backref='experttestimonies')
    policeofficer =  relationship('Policeofficer', primaryjoin='Experttestimony.requesting_police_officer == Policeofficer.id', backref='experttestimonies')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Experttype(Model):
    __versioned__ = {}
    __tablename__ = 'experttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    expert_type =  Column( ForeignKey('experttype.id'), index=True)

    parent =  relationship('Experttype', remote_side=[id], primaryjoin='Experttype.expert_type == Experttype.id', backref='experttypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Feeclass(Model):
    __versioned__ = {}
    __tablename__ = 'feeclass'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    fee_type =  Column( ForeignKey('feeclass.id'), index=True)

    parent =  relationship('Feeclass', remote_side=[id], primaryjoin='Feeclass.fee_type == Feeclass.id', backref='feeclasses')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Feetype(Model):
    __versioned__ = {}
    __tablename__ = 'feetype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    filing_fee_type =  Column( ForeignKey('feeclass.id'), nullable=False, index=True)
    amount =  Column( Numeric(12, 2))
    unit =  Column( Text, nullable=False)
    min_fee =  Column( Numeric(12, 2))
    max_fee =  Column( Numeric(12, 2))
    description =  Column( Text)
    guide_sec =  Column( Text)
    guide_clause =  Column( Text)
    account_type =  Column( ForeignKey('accounttype.id'), nullable=False, index=True)

    accounttype =  relationship('Accounttype', primaryjoin='Feetype.account_type == Accounttype.id', backref='feetypes')
    feeclass =  relationship('Feeclass', primaryjoin='Feetype.filing_fee_type == Feeclass.id', backref='feetypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Healthevent(Model):
    __versioned__ = {}
    __tablename__ = 'healthevent'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=False, index=True)
    reporting_prison_officer =  Column( ForeignKey('prisonofficer.id'), index=True)
    health_event_type =  Column( ForeignKey('healtheventtype.id'), nullable=False, index=True)
    startdate =  Column( DateTime)
    enddate =  Column( DateTime)
    notes =  Column( Text, nullable=False)

    healtheventtype =  relationship('Healtheventtype', primaryjoin='Healthevent.health_event_type == Healtheventtype.id', backref='healthevents')
    party1 =  relationship('Party', primaryjoin='Healthevent.party == Party.id', backref='healthevents')
    prisonofficer =  relationship('Prisonofficer', primaryjoin='Healthevent.reporting_prison_officer == Prisonofficer.id', backref='healthevents')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Healtheventtype(Model):
    __versioned__ = {}
    __tablename__ = 'healtheventtype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Hearing(Model):
    __versioned__ = {}
    __tablename__ = 'hearing'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    court_cases =  Column( ForeignKey('courtcase.id'), index=True)
    hearing_type =  Column( ForeignKey('hearingtype.id'), nullable=False, index=True)
    schedule_status =  Column( ForeignKey('schedulestatustype.id'), nullable=False, index=True)
    hearing_date =  Column( Date)
    reason =  Column( Text, nullable=False)
    sequence =  Column( BigInteger)
    yearday =  Column( BigInteger)
    starttime =  Column( Time)
    endtime =  Column( Time)
    notes =  Column( Text, nullable=False)
    completed =  Column( Boolean)
    adjourned_to =  Column( Date)
    adjournment_reason =  Column( Text, nullable=False)
    transcript =  Column( Text, nullable=False)
    atendance =  Column( Text, nullable=False)
    next_hearing_date =  Column( Date)
    postponement_reason =  Column( Text, nullable=False)

    courtcase =  relationship('Courtcase', primaryjoin='Hearing.court_cases == Courtcase.id', backref='hearings')
    hearingtype =  relationship('Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref='hearings')
    schedulestatustype =  relationship('Schedulestatustype', primaryjoin='Hearing.schedule_status == Schedulestatustype.id', backref='hearings')
    issue =  relationship('Issue', secondary='hearing_issue', backref='hearings')
    judicialofficer =  relationship('Judicialofficer', secondary='hearing_judicialofficer', backref='hearings')
    lawfirm =  relationship('Lawfirm', secondary='hearing_lawfirm', backref='hearings')
    lawfirm1 =  relationship('Lawfirm', secondary='hearing_lawfirm_2', backref='hearings_48')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_hearing_issue =  Table(
    'hearing_issue', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=False),
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_hearing_judicialofficer =  Table(
    'hearing_judicialofficer', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=False),
     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_hearing_lawfirm =  Table(
    'hearing_lawfirm', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=False),
     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_hearing_lawfirm_2 =  Table(
    'hearing_lawfirm_2', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=False),
     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Hearingtype(Model):
    __versioned__ = {}
    __tablename__ = 'hearingtype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    hearing_type =  Column( ForeignKey('hearingtype.id'), index=True)

    parent =  relationship('Hearingtype', remote_side=[id], primaryjoin='Hearingtype.hearing_type == Hearingtype.id', backref='hearingtypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Instancecrime(Model):
    __versioned__ = {}
    __tablename__ = 'instancecrime'

    id =  Column( Integer, primary_key=True)
    parties =  Column( ForeignKey('party.id'), nullable=False, index=True)
    crimes =  Column( ForeignKey('crime.id'), nullable=False, index=True)
    crime_detail =  Column( Text, nullable=False)
    tffender_type =  Column( Text, nullable=False)
    crime_date =  Column( DateTime)
    date_note =  Column( Text, nullable=False)
    place_of_crime =  Column( Text, nullable=False)
    place_note =  Column( Text, nullable=False)

    crime =  relationship('Crime', primaryjoin='Instancecrime.crimes == Crime.id', backref='instancecrimes')
    party =  relationship('Party', primaryjoin='Instancecrime.parties == Party.id', backref='instancecrimes')
    issue =  relationship('Issue', secondary='instancecrime_issue', backref='instancecrimes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_instancecrime_issue =  Table(
    'instancecrime_issue', Model.metadata,
     Column('instancecrime',  ForeignKey('instancecrime.id'), primary_key=True, nullable=False),
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Interview(Model):
    __versioned__ = {}
    __tablename__ = 'interview'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_entry =  Column( ForeignKey('investigationdiary.id'), nullable=False, index=True)
    question =  Column( Text, nullable=False)
    answer =  Column( Text, nullable=False)
    validated =  Column( Boolean)
    language =  Column( Text, nullable=False)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Interview.investigation_entry == Investigationdiary.id', backref='interviews')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Investigationdiary(Model):
    __versioned__ = {}
    __tablename__ = 'investigationdiary'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    activity =  Column( Text, nullable=False)
    complaint =  Column( ForeignKey('complaint.id'), nullable=False, index=True)
    location =  Column( Text, nullable=False)
    outcome =  Column( Text, nullable=False)
    equipmentresults =  Column( Text, nullable=False)
    startdate =  Column( DateTime, nullable=False)
    enddate =  Column( DateTime)
    advocate_present =  Column( Text, nullable=False)
    summons_statement =  Column( Text, nullable=False)
    arrest_statement =  Column( Text, nullable=False)
    arrest_warrant =  Column( Text, nullable=False)
    search_seizure_statement =  Column( Text, nullable=False)
    docx =  Column( Text, nullable=False)
    detained =  Column( Text, nullable=False)
    detained_at =  Column( Text, nullable=False)
    provisional_release_statement =  Column( Text, nullable=False)
    warrant_type =  Column( ForeignKey('warranttype.id'), index=True)
    warrant_issued_by =  Column( Text, nullable=False)
    warrant_issue_date =  Column( Date)
    warrant_delivered_by =  Column( Text, nullable=False)
    warrant_received_by =  Column( Text, nullable=False)
    warrant_serve_date =  Column( Text, nullable=False)
    warrant_docx =  Column( Text, nullable=False)
    warrant_upload_date =  Column( Text, nullable=False)

    complaint1 =  relationship('Complaint', primaryjoin='Investigationdiary.complaint == Complaint.id', backref='investigationdiaries')
    warranttype =  relationship('Warranttype', primaryjoin='Investigationdiary.warrant_type == Warranttype.id', backref='investigationdiaries')
    party =  relationship('Party', secondary='investigationdiary_party', backref='investigationdiaries')
    policeofficer =  relationship('Policeofficer', secondary='investigationdiary_policeofficer', backref='investigationdiaries')
    vehicle =  relationship('Vehicle', secondary='investigationdiary_vehicle', backref='investigationdiaries')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_investigationdiary_party =  Table(
    'investigationdiary_party', Model.metadata,
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_investigationdiary_policeofficer =  Table(
    'investigationdiary_policeofficer', Model.metadata,
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_investigationdiary_vehicle =  Table(
    'investigationdiary_vehicle', Model.metadata,
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
     Column('vehicle',  ForeignKey('vehicle.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Issue(Model):
    __versioned__ = {}
    __tablename__ = 'issue'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    issue =  Column( Text, nullable=False)
    facts =  Column( Text)
    counter_claim =  Column( Boolean)
    argument =  Column( Text, nullable=False)
    argument_date =  Column( Date)
    argument_docx =  Column( Text)
    rebuttal =  Column( Text, nullable=False)
    rebuttal_date =  Column( Date)
    rebuttal_docx =  Column( Text)
    hearing_date =  Column( Date)
    determination =  Column( Text, nullable=False)
    dtermination_date =  Column( Date)
    determination_docx =  Column( Text, nullable=False)
    resolved =  Column( Boolean)
    defense_lawyer =  Column( ForeignKey('lawyer.id'), nullable=False, index=True)
    prosecutor =  Column( ForeignKey('prosecutor.id'), index=True)
    judicial_officer =  Column( ForeignKey('judicialofficer.id'), nullable=False, index=True)
    court_case =  Column( ForeignKey('courtcase.id'), nullable=False, index=True)
    tasks =  Column( Text, nullable=False)
    is_criminal =  Column( Boolean)
    moral_element =  Column( Text, nullable=False)
    material_element =  Column( Text, nullable=False)
    legal_element =  Column( Text, nullable=False)
    debt_amount =  Column( Numeric(12, 2))

    courtcase =  relationship('Courtcase', primaryjoin='Issue.court_case == Courtcase.id', backref='issues')
    lawyer =  relationship('Lawyer', primaryjoin='Issue.defense_lawyer == Lawyer.id', backref='issues')
    judicialofficer =  relationship('Judicialofficer', primaryjoin='Issue.judicial_officer == Judicialofficer.id', backref='issues')
    prosecutor1 =  relationship('Prosecutor', primaryjoin='Issue.prosecutor == Prosecutor.id', backref='issues')
    lawyer1 =  relationship('Lawyer', secondary='issue_lawyer', backref='issues_42')
    legalreference =  relationship('Legalreference', secondary='issue_legalreference', backref='issues')
    legalreference1 =  relationship('Legalreference', secondary='issue_legalreference_2', backref='issues_13')
    party =  relationship('Party', secondary='issue_party', backref='issues')
    party1 =  relationship('Party', secondary='issue_party_2', backref='issues_7')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_issue_lawyer =  Table(
    'issue_lawyer', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False),
     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_issue_legalreference =  Table(
    'issue_legalreference', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False),
     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_issue_legalreference_2 =  Table(
    'issue_legalreference_2', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False),
     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_issue_party =  Table(
    'issue_party', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
t_issue_party_2 =  Table(
    'issue_party_2', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=False),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Judicialofficer(Model):
    __versioned__ = {}
    __tablename__ = 'judicialofficer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    rank =  Column( ForeignKey('judicialrank.id'), nullable=False, index=True)
    judicial_role =  Column( ForeignKey('judicialrole.id'), nullable=False, index=True)
    court_station =  Column( ForeignKey('courtstation.id'), nullable=False, index=True)

    courtstation =  relationship('Courtstation', primaryjoin='Judicialofficer.court_station == Courtstation.id', backref='judicialofficers')
    judicialrole =  relationship('Judicialrole', primaryjoin='Judicialofficer.judicial_role == Judicialrole.id', backref='judicialofficers')
    judicialrank =  relationship('Judicialrank', primaryjoin='Judicialofficer.rank == Judicialrank.id', backref='judicialofficers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Judicialrank(Model):
    __versioned__ = {}
    __tablename__ = 'judicialrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Judicialrole(Model):
    __versioned__ = {}
    __tablename__ = 'judicialrole'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Law(Model):
    __versioned__ = {}
    __tablename__ = 'law'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=False)
    description =  Column( Text, nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Lawfirm(Model):
    __versioned__ = {}
    __tablename__ = 'lawfirm'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Lawyer(Model):
    __versioned__ = {}
    __tablename__ = 'lawyer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    law_firm =  Column( ForeignKey('lawfirm.id'), index=True)
    bar_no =  Column( Text, nullable=False)
    bar_date =  Column( Date)

    lawfirm =  relationship('Lawfirm', primaryjoin='Lawyer.law_firm == Lawfirm.id', backref='lawyers')
    party =  relationship('Party', secondary='lawyer_party', backref='lawyers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_lawyer_party =  Table(
    'lawyer_party', Model.metadata,
     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=False),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Legalreference(Model):
    __versioned__ = {}
    __tablename__ = 'legalreference'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    ref =  Column( Text, nullable=False)
    verbatim =  Column( Text, nullable=False)
    public =  Column( Boolean)
    commentary =  Column( Text, nullable=False)
    validated =  Column( Boolean)
    citation =  Column( Text, nullable=False)
    quote =  Column( Text, nullable=False)
    interpretation =  Column( Text, nullable=False)
    klr_url_full =  Column( String(300), nullable=False)
    klr_rul_short =  Column( Text, nullable=False)
    doc_id =  Column( String(300), nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Nextofkin(Model):
    __versioned__ = {}
    __tablename__ = 'nextofkin'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    biodata =  Column( ForeignKey('biodata.id'), nullable=False, index=True)
    childunder4 =  Column( Boolean)

    biodata1 =  relationship('Biodata', primaryjoin='Nextofkin.biodata == Biodata.id', backref='nextofkins')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Notification(Model):
    __versioned__ = {}
    __tablename__ = 'notification'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    contact =  Column( String(200), nullable=False)
    message =  Column( Text, nullable=False)
    confirmation =  Column( String(100), nullable=False)
    notification_register =  Column( ForeignKey('notificationregister.id'), index=True)
    send_date =  Column( DateTime, autoincrement=True)
    sent =  Column( Boolean)
    delivered =  Column( Boolean)
    retries =  Column( Integer)
    abandon =  Column( Boolean)
    retry_count =  Column( Integer)

    notificationregister =  relationship('Notificationregister', primaryjoin='Notification.notification_register == Notificationregister.id', backref='notifications')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Notificationregister(Model):
    __versioned__ = {}
    __tablename__ = 'notificationregister'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    notification_type =  Column( ForeignKey('notificationtype.id'), nullable=False, index=True)
    contact =  Column( Text, nullable=False)
    notify_event =  Column( ForeignKey('notifyevent.id'), index=True)
    retry_count =  Column( BigInteger)
    active =  Column( Boolean)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)
    hearing =  Column( ForeignKey('hearing.id'), index=True)
    document =  Column( ForeignKey('document.id'), index=True)
    complaint =  Column( ForeignKey('complaint.id'), index=True)
    complaint_category =  Column( ForeignKey('complaintcategory.id'), index=True)
    health_event =  Column( ForeignKey('healthevent.id'), index=True)
    party =  Column( ForeignKey('party.id'), index=True)
    user_to_notify =  Column( ForeignKey('sysuserextra.id'), nullable=False, index=True)

    complaint1 =  relationship('Complaint', primaryjoin='Notificationregister.complaint == Complaint.id', backref='notificationregisters')
    complaintcategory =  relationship('Complaintcategory', primaryjoin='Notificationregister.complaint_category == Complaintcategory.id', backref='notificationregisters')
    courtcase =  relationship('Courtcase', primaryjoin='Notificationregister.court_case == Courtcase.id', backref='notificationregisters')
    document1 =  relationship('Document', primaryjoin='Notificationregister.document == Document.id', backref='notificationregisters')
    healthevent =  relationship('Healthevent', primaryjoin='Notificationregister.health_event == Healthevent.id', backref='notificationregisters')
    hearing1 =  relationship('Hearing', primaryjoin='Notificationregister.hearing == Hearing.id', backref='notificationregisters')
    notificationtype =  relationship('Notificationtype', primaryjoin='Notificationregister.notification_type == Notificationtype.id', backref='notificationregisters')
    notifyevent =  relationship('Notifyevent', primaryjoin='Notificationregister.notify_event == Notifyevent.id', backref='notificationregisters')
    party1 =  relationship('Party', primaryjoin='Notificationregister.party == Party.id', backref='notificationregisters')
    sysuserextra =  relationship('Sysuserextra', primaryjoin='Notificationregister.user_to_notify == Sysuserextra.id', backref='notificationregisters')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Notificationtype(Model):
    __versioned__ = {}
    __tablename__ = 'notificationtype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=False)
    description =  Column( Text, nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Notifyevent(Model):
    __versioned__ = {}
    __tablename__ = 'notifyevent'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Party(Model):
    __versioned__ = {}
    __tablename__ = 'party'

    id =  Column( Integer, primary_key=True)
    complaints =  Column( ForeignKey('complaint.id'), nullable=False, index=True)
    statement =  Column( String(1000), nullable=False)
    statementdate =  Column( DateTime)
    complaint_role =  Column( ForeignKey('complaintrole.id'), nullable=False, index=True)
    notes =  Column( Text, nullable=False)
    dateofrepresentation =  Column( DateTime)
    party_type =  Column( ForeignKey('partytype.id'), nullable=False, index=True)
    relative =  Column( ForeignKey('party.id'), nullable=False, index=True)
    relationship_type =  Column( Text, nullable=False)
    is_infant =  Column( Boolean)
    is_minor =  Column( Boolean)
    miranda_read =  Column( Boolean)
    miranda_date =  Column( DateTime)
    miranda_witness =  Column( Text, nullable=False)

    complaintrole =  relationship('Complaintrole', primaryjoin='Party.complaint_role == Complaintrole.id', backref='parties')
    complaint =  relationship('Complaint', primaryjoin='Party.complaints == Complaint.id', backref='parties')
    partytype =  relationship('Partytype', primaryjoin='Party.party_type == Partytype.id', backref='parties')
    parent =  relationship('Party', remote_side=[id], primaryjoin='Party.relative == Party.id', backref='parties')
    settlement =  relationship('Settlement', secondary='party_settlement', backref='parties')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_party_settlement =  Table(
    'party_settlement', Model.metadata,
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=False),
     Column('settlement',  ForeignKey('settlement.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Partytype(Model):
    __versioned__ = {}
    __tablename__ = 'partytype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Payment(Model):
    __versioned__ = {}
    __tablename__ = 'payment'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    bill =  Column( ForeignKey('bill.id'), nullable=False, index=True)
    pay_amount =  Column( Numeric(12, 2))
    payment_ref =  Column( Text, unique=True)
    pay_date =  Column( DateTime)
    phone_number =  Column( String(20))
    validated =  Column( Boolean)
    validate_date =  Column( DateTime)
    payment_description =  Column( String(100))
    pay_trans_cost =  Column( Numeric(12, 2))
    receipt_no =  Column( String(100))

    bill1 =  relationship('Bill', primaryjoin='Payment.bill == Bill.id', backref='payments')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Personaleffect(Model):
    __versioned__ = {}
    __tablename__ = 'personaleffect'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=False, index=True)
    personal_effects_category =  Column( ForeignKey('personaleffectscategory.id'), nullable=False, index=True)

    party1 =  relationship('Party', primaryjoin='Personaleffect.party == Party.id', backref='personaleffects')
    personaleffectscategory =  relationship('Personaleffectscategory', primaryjoin='Personaleffect.personal_effects_category == Personaleffectscategory.id', backref='personaleffects')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Personaleffectscategory(Model):
    __versioned__ = {}
    __tablename__ = 'personaleffectscategory'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Policeofficer(Model):
    __versioned__ = {}
    __tablename__ = 'policeofficer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    police_rank =  Column( ForeignKey('policeofficerrank.id'), nullable=False, index=True)
    servicenumber =  Column( String(100), nullable=False, unique=True)

    policeofficerrank =  relationship('Policeofficerrank', primaryjoin='Policeofficer.police_rank == Policeofficerrank.id', backref='policeofficers')
    policestation =  relationship('Policestation', secondary='policeofficer_policestation', backref='policeofficers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_policeofficer_policestation =  Table(
    'policeofficer_policestation', Model.metadata,
     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=False),
     Column('policestation',  ForeignKey('policestation.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Policeofficerrank(Model):
    __versioned__ = {}
    __tablename__ = 'policeofficerrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=False)
    description =  Column( Text, nullable=False)
    sequence =  Column( Integer)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Policestation(Model):
    __versioned__ = {}
    __tablename__ = 'policestation'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    town =  Column( ForeignKey('town.id'), index=True)
    officer_commanding =  Column( ForeignKey('policeofficer.id'), nullable=False, index=True)
    police_station_rank =  Column( ForeignKey('policestationrank.id'), nullable=False, index=True)

    policeofficer =  relationship('Policeofficer', primaryjoin='Policestation.officer_commanding == Policeofficer.id', backref='policestations')
    policestationrank =  relationship('Policestationrank', primaryjoin='Policestation.police_station_rank == Policestationrank.id', backref='policestations')
    town1 =  relationship('Town', primaryjoin='Policestation.town == Town.id', backref='policestations')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Policestationrank(Model):
    __versioned__ = {}
    __tablename__ = 'policestationrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Prison(Model):
    __versioned__ = {}
    __tablename__ = 'prison'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    town =  Column( ForeignKey('town.id'), nullable=False, index=True)

    town1 =  relationship('Town', primaryjoin='Prison.town == Town.id', backref='prisons')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Prisonofficer(Model):
    __versioned__ = {}
    __tablename__ = 'prisonofficer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    prison =  Column( ForeignKey('prison.id'), nullable=False, index=True)
    prison_officer_rank =  Column( ForeignKey('prisonofficerrank.id'), nullable=False, index=True)

    prison1 =  relationship('Prison', primaryjoin='Prisonofficer.prison == Prison.id', backref='prisonofficers')
    prisonofficerrank =  relationship('Prisonofficerrank', primaryjoin='Prisonofficer.prison_officer_rank == Prisonofficerrank.id', backref='prisonofficers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Prisonofficerrank(Model):
    __versioned__ = {}
    __tablename__ = 'prisonofficerrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Prosecutor(Model):
    __versioned__ = {}
    __tablename__ = 'prosecutor'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    prosecutor_team =  Column( ForeignKey('prosecutorteam.id'), index=True)
    lawyer =  Column( ForeignKey('lawyer.id'), nullable=False, index=True)

    lawyer1 =  relationship('Lawyer', primaryjoin='Prosecutor.lawyer == Lawyer.id', backref='prosecutors')
    prosecutorteam =  relationship('Prosecutorteam', primaryjoin='Prosecutor.prosecutor_team == Prosecutorteam.id', backref='prosecutors')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Prosecutorteam(Model):
    __versioned__ = {}
    __tablename__ = 'prosecutorteam'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Releasetype(Model):
    __versioned__ = {}
    __tablename__ = 'releasetype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Religion(Model):
    __versioned__ = {}
    __tablename__ = 'religion'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Schedulestatustype(Model):
    __versioned__ = {}
    __tablename__ = 'schedulestatustype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Seizure(Model):
    __versioned__ = {}
    __tablename__ = 'seizure'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_diary =  Column( ForeignKey('investigationdiary.id'), nullable=False, index=True)
    owner =  Column( Text, nullable=False)
    item =  Column( Text, nullable=False)
    item_packaging =  Column( Text, nullable=False)
    item_pic =  Column( Text, nullable=False)
    premises =  Column( Text, nullable=False)
    reg_no =  Column( Text, nullable=False)
    witness =  Column( Text, nullable=False)
    notes =  Column( Text, nullable=False)
    docx =  Column( Text, nullable=False)
    item_description =  Column( Text, nullable=False)
    returned =  Column( Boolean)
    return_date =  Column( DateTime)
    return_notes =  Column( Text, nullable=False)
    return_signed_receipt =  Column( Text, nullable=False)
    destroyed =  Column( Boolean)
    destruction_date =  Column( Date)
    destruction_witnesses =  Column( Text, nullable=False)
    destruction_notes =  Column( Text, nullable=False)
    disposed =  Column( Boolean)
    sold_to =  Column( Text, nullable=False)
    disposal_date =  Column( Date)
    disposal_price =  Column( Numeric(12, 2))
    disposal_receipt =  Column( Text, nullable=False)
    recovery_town =  Column( ForeignKey('town.id'), index=True)
    destruction_pic =  Column( Text, nullable=False)
    is_evidence =  Column( Boolean)
    immovable =  Column( Boolean)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Seizure.investigation_diary == Investigationdiary.id', backref='seizures')
    town =  relationship('Town', primaryjoin='Seizure.recovery_town == Town.id', backref='seizures')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Settlement(Model):
    __versioned__ = {}
    __tablename__ = 'settlement'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    complaint =  Column( ForeignKey('complaint.id'), nullable=False, index=True)
    terms =  Column( Text, nullable=False)
    amount =  Column( Numeric(12, 2))
    paid =  Column( Boolean)
    docx =  Column( Text, nullable=False)
    settlor =  Column( ForeignKey('party.id'), nullable=False, index=True)

    complaint1 =  relationship('Complaint', primaryjoin='Settlement.complaint == Complaint.id', backref='settlements')
    party =  relationship('Party', primaryjoin='Settlement.settlor == Party.id', backref='settlements')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Subcounty(Model):
    __versioned__ = {}
    __tablename__ = 'subcounty'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    county =  Column( ForeignKey('county.id'), nullable=False, index=True)

    county1 =  relationship('County', primaryjoin='Subcounty.county == County.id', backref='subcounties')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Sysuserextra(Model):
    __versioned__ = {}
    __tablename__ = 'sysuserextra'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_birthday =  Column( Date)
    sys_job_grade =  Column( Text, nullable=False)
    sys_home_address =  Column( Text, nullable=False)
    mobile =  Column( String(20), nullable=False)
    off_phone =  Column( String(20), nullable=False)
    alt_email =  Column( String(120), nullable=False)
    office_address =  Column( Text, nullable=False)
    off_email =  Column( String(120), nullable=False)
    sys_notes =  Column( Text, nullable=False)
    syswkflowgrp =  Column( ForeignKey('syswkflowgrp.id'), nullable=False, index=True)

    syswkflowgrp1 =  relationship('Syswkflowgrp', primaryjoin='Sysuserextra.syswkflowgrp == Syswkflowgrp.id', backref='sysuserextras')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Sysviewfld(Model):
    __versioned__ = {}
    __tablename__ = 'sysviewfld'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys__view =  Column( ForeignKey('sysviewlist.id'), nullable=False, index=True)
    fld_name =  Column( String(100), nullable=False)
    fld_type =  Column( String(100), nullable=False)
    fld_unique =  Column( Boolean)
    fld_validator =  Column( String(200), nullable=False)
    fld_choices =  Column( String(300), nullable=False)
    fld_label =  Column( String(100), nullable=False)
    fld_default =  Column( String(100), nullable=False)
    fld_widget =  Column( String(200), nullable=False)
    fld_display_order =  Column( BigInteger)

    sysviewlist =  relationship('Sysviewlist', primaryjoin='Sysviewfld.sys__view == Sysviewlist.id', backref='sysviewflds')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Sysviewlist(Model):
    __versioned__ = {}
    __tablename__ = 'sysviewlist'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_name =  Column( String(100), nullable=False, unique=True)
    sys_route =  Column( String(200), nullable=False)
    sys_perms =  Column( String(300), nullable=False)
    sys_template =  Column( Text, nullable=False)
    sys_title =  Column( String(100), nullable=False)
    sys_wtf =  Column( Boolean)
    sys_table_name =  Column( String(100), nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Syswkflow(Model):
    __versioned__ = {}
    __tablename__ = 'syswkflow'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_name =  Column( String(200), unique=True)
    sys_description =  Column( String(200))
    sys_notes =  Column( Text)
    syswkflowgrp =  Column( ForeignKey('syswkflowgrp.id'), index=True)
    sys_wkflow_template =  Column( Text, nullable=False)
    sys_steps =  Column( Integer)

    syswkflowgrp1 =  relationship('Syswkflowgrp', primaryjoin='Syswkflow.syswkflowgrp == Syswkflowgrp.id', backref='syswkflows')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Syswkflowgrp(Model):
    __versioned__ = {}
    __tablename__ = 'syswkflowgrp'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_cat_name =  Column( String(200), nullable=False, unique=True)
    sys_cat_description =  Column( String(200))
    sys_cat_notes =  Column( Text, nullable=False)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Syswkflowviewseq(Model):
    __versioned__ = {}
    __tablename__ = 'syswkflowviewseq'

    sys__view__lists =  Column( ForeignKey('sysviewlist.id'), primary_key=True, nullable=False)
    sys_wkflows =  Column( ForeignKey('syswkflow.id'), primary_key=True, nullable=False, index=True)
    sys_order =  Column( BigInteger, nullable=False)
    sys_is_terminal =  Column( Boolean)

    sysviewlist =  relationship('Sysviewlist', primaryjoin='Syswkflowviewseq.sys__view__lists == Sysviewlist.id', backref='syswkflowviewseqs')
    syswkflow =  relationship('Syswkflow', primaryjoin='Syswkflowviewseq.sys_wkflows == Syswkflow.id', backref='syswkflowviewseqs')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Templatetype(Model):
    __versioned__ = {}
    __tablename__ = 'templatetype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    template_type =  Column( ForeignKey('templatetype.id'), index=True)

    parent =  relationship('Templatetype', remote_side=[id], primaryjoin='Templatetype.template_type == Templatetype.id', backref='templatetypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Town(Model):
    __versioned__ = {}
    __tablename__ = 'town'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    ward =  relationship('Ward', secondary='town_ward', backref='towns')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
t_town_ward =  Table(
    'town_ward', Model.metadata,
     Column('town',  ForeignKey('town.id'), primary_key=True, nullable=False),
     Column('ward',  ForeignKey('ward.id'), primary_key=True, nullable=False, index=True)
)

#ENDCLASS


#STARTCLASS
class Transcript(Model):
    __versioned__ = {}
    __tablename__ = 'transcript'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    video =  Column( Text, nullable=False)
    audio =  Column( Text, nullable=False)
    add_date =  Column( DateTime)
    asr_transcript =  Column( Text, nullable=False)
    asr_date =  Column( DateTime)
    edited_transcript =  Column( Text, nullable=False)
    edit_date =  Column( DateTime)
    certified_transcript =  Column( Text, nullable=False)
    certfiy_date =  Column( DateTime)
    locked =  Column( Boolean)
    hearing =  Column( ForeignKey('hearing.id'), nullable=False, index=True)

    hearing1 =  relationship('Hearing', primaryjoin='Transcript.hearing == Hearing.id', backref='transcripts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Vehicle(Model):
    __versioned__ = {}
    __tablename__ = 'vehicle'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    police_station =  Column( ForeignKey('policestation.id'), nullable=False, index=True)
    make =  Column( String(100), nullable=False)
    model =  Column( String(100), nullable=False)
    regno =  Column( String(100), nullable=False)

    policestation =  relationship('Policestation', primaryjoin='Vehicle.police_station == Policestation.id', backref='vehicles')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Ward(Model):
    __versioned__ = {}
    __tablename__ = 'ward'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    subcounty =  Column( ForeignKey('subcounty.id'), nullable=False, index=True)

    subcounty1 =  relationship('Subcounty', primaryjoin='Ward.subcounty == Subcounty.id', backref='wards')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS


#STARTCLASS
class Warranttype(Model):
    __versioned__ = {}
    __tablename__ = 'warranttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=False)

    # mindate = datetime.date(MINYEAR, 1, 1)

    def view_name(self):
        return self.__class__.__name__ +'View'

    def photo_img(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.view_name()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    def print_button(self):
        vn = self.view_name()
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
        vn = self.view_name()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )

    def download(self):
        vn = self.view_name()
        return Markup(
            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate

    def year(self):
        date = self.created_on #or self.mindate
        return datetime.datetime(date.year, 1, 1)
        
    # custom = Column(Integer(20))
    #
    # @renders('custom')
    # def my_custom(self):
    #     # will render this columns as bold on ListWidget
    #     return Markup('<b>' + custom + '</b>')#ENDMODEL

#ENDCLASS

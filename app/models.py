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
class Accounttype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'accounttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Bill( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'bill'
    __table_args__ = (
         ForeignKeyConstraint(['court_account_courts', 'court_account_account__types'], ['courtaccount.courts', 'courtaccount.account__types']),
         Index('idx_bill__court_account_courts_court_account_account__types', 'court_account_courts', 'court_account_account__types')
    )

    id =  Column( Integer, primary_key=True, autoincrement=True)
    assessing_registrar =  Column( ForeignKey('judicialofficer.id'), nullable=True, index=True)
    assess_date =  Column( DateTime)
    receiving_registrar =  Column( ForeignKey('judicialofficer.id'), nullable=True, index=True)
    receive_date =  Column( DateTime)
    lawyer_paying =  Column( ForeignKey('lawyer.id'), index=True)
    party_paying =  Column( ForeignKey('party.id'), index=True)
    documents =  Column( ForeignKey('document.id'), index=True)
    date_of_payment =  Column( DateTime)
    paid =  Column( Boolean)
    bill_code =  Column( String(20), unique=True)
    bill_total =  Column( Numeric(12, 2))
    court =  Column( ForeignKey('court.id'), nullable=True, index=True)
    court_account_courts =  Column( Integer, nullable=True)
    court_account_account__types =  Column( Integer, nullable=True)
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
    judicialofficer1 =  relationship('Judicialofficer', primaryjoin='Bill.receiving_registrar == Judicialofficer.id', backref='bills_66')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Billdetail( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'billdetail'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    receipt_id =  Column( ForeignKey('bill.id'), nullable=True, index=True)
    feetype =  Column( ForeignKey('feetype.id'), nullable=True, index=True)
    purpose =  Column( Text, nullable=True)
    unit =  Column( Text)
    qty =  Column( Integer)
    unit_cost =  Column( Numeric(12, 2))
    amount =  Column( Numeric(12, 2))
    bd_date =  Column( DateTime)

    feetype1 =  relationship('Feetype', primaryjoin='Billdetail.feetype == Feetype.id', backref='billdetails')
    receipt =  relationship('Bill', primaryjoin='Billdetail.receipt_id == Bill.id', backref='billdetails')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Biodata( PersonDocMixin, PersonMedicalMixin, BiometricMixin, ParentageMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'biodata'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=True, index=True)
    economic_class =  Column( ForeignKey('economicclass.id'), index=True)
    religion =  Column( ForeignKey('religion.id'), index=True)
    photo =  Column( LargeBinary)
    health_status =  Column( Text, nullable=True)

    economicclass =  relationship('Economicclass', primaryjoin='Biodata.economic_class == Economicclass.id', backref='biodatas')
    party1 =  relationship('Party', primaryjoin='Biodata.party == Party.id', backref='biodatas')
    religion1 =  relationship('Religion', primaryjoin='Biodata.religion == Religion.id', backref='biodatas')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Casecategory( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'casecategory'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    subcategory =  Column( ForeignKey('casecategory.id'), index=True)

    parent =  relationship('Casecategory', remote_side=[id], primaryjoin='Casecategory.subcategory == Casecategory.id', backref='casecategories')
    casechecklist =  relationship('Casechecklist', secondary='casecategory_casechecklist', backref='casecategories')
    courtcase =  relationship('Courtcase', secondary='casecategory_courtcase', backref='casecategories')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Casecategory_Casechecklist(Model):
	 __table__ =   Table(
    'casecategory_casechecklist', Model.metadata,
     Column('casechecklists',  ForeignKey('casechecklist.id'), primary_key=True, nullable=True),
     Column('casecategories',  ForeignKey('casecategory.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Casecategory_Courtcase(Model):
	 __table__ =   Table(
    'casecategory_courtcase', Model.metadata,
     Column('casecategory',  ForeignKey('casecategory.id'), primary_key=True, nullable=True),
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Casechecklist( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'casechecklist'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    check_list_item =  Column( String(100), nullable=True)
    description =  Column( String(100), nullable=True)
    notes =  Column( Text, nullable=True)
    is_mandatory =  Column( Boolean)
    priority =  Column( BigInteger)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Caselinktype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'caselinktype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Celltype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'celltype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Commital( ActivityMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'commital'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    prisons =  Column( ForeignKey('prison.id'), index=True)
    police_station =  Column( ForeignKey('policestation.id'), index=True)
    parties =  Column( ForeignKey('party.id'), nullable=True, index=True)
    casecomplete =  Column( Boolean)
    commit_date =  Column( Date, nullable=True)
    purpose =  Column( Text, nullable=True)
    warrant_type =  Column( ForeignKey('warranttype.id'), nullable=True, index=True)
    warrant_docx =  Column( Text, nullable=True)
    warrant_issue_date =  Column( Date)
    warrant_issued_by =  Column( Text, nullable=True)
    warrant_date_attached =  Column( DateTime)
    duration =  Column( Interval)
    commital =  Column( ForeignKey('commital.id'), index=True)
    commital_type =  Column( ForeignKey('commitaltype.id'), nullable=True, index=True)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)
    concurrent =  Column( Boolean)
    life_imprisonment =  Column( Boolean)
    arrival_date =  Column( DateTime)
    sentence_start_date =  Column( DateTime)
    arrest_date =  Column( DateTime)
    remaining_years =  Column( Integer)
    remaining_months =  Column( Integer)
    remaining_days =  Column( Integer)
    cell_number =  Column( Text, nullable=True)
    cell_type =  Column( ForeignKey('celltype.id'), index=True)
    release_date =  Column( DateTime)
    exit_date =  Column( DateTime)
    reason_for_release =  Column( Text, nullable=True)
    with_children =  Column( Boolean)
    release_type =  Column( ForeignKey('releasetype.id'), index=True)
    receiving_officer =  Column( ForeignKey('prisonofficer.id'), nullable=True, index=True)
    releasing_officer =  Column( ForeignKey('prisonofficer.id'), nullable=True, index=True)

    celltype =  relationship('Celltype', primaryjoin='Commital.cell_type == Celltype.id', backref='commitals')
    parent =  relationship('Commital', remote_side=[id], primaryjoin='Commital.commital == Commital.id', backref='commitals')
    commitaltype =  relationship('Commitaltype', primaryjoin='Commital.commital_type == Commitaltype.id', backref='commitals')
    courtcase =  relationship('Courtcase', primaryjoin='Commital.court_case == Courtcase.id', backref='commitals')
    party =  relationship('Party', primaryjoin='Commital.parties == Party.id', backref='commitals')
    policestation =  relationship('Policestation', primaryjoin='Commital.police_station == Policestation.id', backref='commitals')
    prison =  relationship('Prison', primaryjoin='Commital.prisons == Prison.id', backref='commitals')
    prisonofficer =  relationship('Prisonofficer', primaryjoin='Commital.receiving_officer == Prisonofficer.id', backref='commitals')
    releasetype =  relationship('Releasetype', primaryjoin='Commital.release_type == Releasetype.id', backref='commitals')
    prisonofficer1 =  relationship('Prisonofficer', primaryjoin='Commital.releasing_officer == Prisonofficer.id', backref='commitals_15')
    warranttype =  relationship('Warranttype', primaryjoin='Commital.warrant_type == Warranttype.id', backref='commitals')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Commitaltype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'commitaltype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    maxduration =  Column( Interval)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Complaint( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'complaint'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    active =  Column( Boolean)
    ob_number =  Column( String(20), nullable=True)
    police_station =  Column( ForeignKey('policestation.id'), nullable=True, index=True)
    daterecvd =  Column( DateTime, nullable=True)
    datefiled =  Column( DateTime)
    datecaseopened =  Column( DateTime)
    casesummary =  Column( String(2000), nullable=True)
    complaintstatement =  Column( Text, nullable=True)
    circumstances =  Column( Text, nullable=True)
    reportingofficer =  Column( ForeignKey('policeofficer.id'), nullable=True, index=True)
    casefileinformation =  Column( Text, nullable=True)
    p_request_help =  Column( Boolean)
    p_instruction =  Column( Text, nullable=True)
    p_submitted =  Column( Boolean)
    p_submission_date =  Column( DateTime)
    p_submission_notes =  Column( Text, nullable=True)
    p_closed =  Column( Text, nullable=True)
    p_evaluation =  Column( Text, nullable=True)
    p_recommend_charge =  Column( Boolean)
    charge_sheet =  Column( Text, nullable=True)
    charge_sheet_docx =  Column( Text, nullable=True)
    evaluating_prosecutor_team =  Column( ForeignKey('prosecutorteam.id'), index=True)
    magistrate_report_date =  Column( DateTime)
    reported_to_judicial_officer =  Column( ForeignKey('judicialofficer.id'), index=True)
    closed =  Column( Boolean)
    close_date =  Column( DateTime)
    close_reason =  Column( Text, nullable=True)

    prosecutorteam =  relationship('Prosecutorteam', primaryjoin='Complaint.evaluating_prosecutor_team == Prosecutorteam.id', backref='complaints')
    policestation =  relationship('Policestation', primaryjoin='Complaint.police_station == Policestation.id', backref='complaints')
    judicialofficer =  relationship('Judicialofficer', primaryjoin='Complaint.reported_to_judicial_officer == Judicialofficer.id', backref='complaints')
    policeofficer =  relationship('Policeofficer', primaryjoin='Complaint.reportingofficer == Policeofficer.id', backref='complaints')
    complaintcategory =  relationship('Complaintcategory', secondary='complaint_complaintcategory', backref='complaints')
    courtcase =  relationship('Courtcase', secondary='complaint_courtcase', backref='complaints')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Complaint_Complaintcategory(Model):
	 __table__ =   Table(
    'complaint_complaintcategory', Model.metadata,
     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=True),
     Column('complaintcategory',  ForeignKey('complaintcategory.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Complaint_Courtcase(Model):
	 __table__ =   Table(
    'complaint_courtcase', Model.metadata,
     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=True),
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Complaintcategory( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'complaintcategory'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    complaint_category_parent =  Column( ForeignKey('complaintcategory.id'), index=True)

    parent =  relationship('Complaintcategory', remote_side=[id], primaryjoin='Complaintcategory.complaint_category_parent == Complaintcategory.id', backref='complaintcategories')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Complaintrole( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'complaintrole'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Country( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'country'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class County( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'county'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    country =  Column( ForeignKey('country.id'), nullable=True, index=True)

    country1 =  relationship('Country', primaryjoin='County.country == Country.id', backref='counties')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Court( PlaceMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'court'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    court_rank =  Column( ForeignKey('courtrank.id'), nullable=True, index=True)
    court_station =  Column( ForeignKey('courtstation.id'), nullable=True, index=True)
    town =  Column( ForeignKey('town.id'), nullable=True, index=True)
    till_number =  Column( Text, nullable=True)

    courtrank =  relationship('Courtrank', primaryjoin='Court.court_rank == Courtrank.id', backref='courts')
    courtstation =  relationship('Courtstation', primaryjoin='Court.court_station == Courtstation.id', backref='courts')
    town1 =  relationship('Town', primaryjoin='Court.town == Town.id', backref='courts')
    judicialofficer =  relationship('Judicialofficer', secondary='court_judicialofficer', backref='courts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Court_Judicialofficer(Model):
	 __table__ =   Table(
    'court_judicialofficer', Model.metadata,
     Column('court',  ForeignKey('court.id'), primary_key=True, nullable=True),
     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Courtaccount( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'courtaccount'

    courts =  Column( ForeignKey('court.id'), primary_key=True, nullable=True)
    account__types =  Column( ForeignKey('accounttype.id'), primary_key=True, nullable=True, index=True)
    account_number =  Column( Text, nullable=True)
    account_name =  Column( Text, nullable=True)
    short_code =  Column( Text, nullable=True)
    bank_name =  Column( Text, nullable=True)

    accounttype =  relationship('Accounttype', primaryjoin='Courtaccount.account__types == Accounttype.id', backref='courtaccounts')
    court =  relationship('Court', primaryjoin='Courtaccount.courts == Court.id', backref='courtaccounts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Courtcase( ActivityMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'courtcase'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    docket_number =  Column( String(200), nullable=True)
    case_number =  Column( Text, nullable=True)
    adr =  Column( Boolean)
    mediation_proposal =  Column( Text, nullable=True)
    case_received_date =  Column( Date)
    case_filed_date =  Column( Date)
    case_summary =  Column( Text, nullable=True)
    filing_prosecutor =  Column( ForeignKey('prosecutor.id'), index=True)
    fast_track =  Column( Boolean)
    priority =  Column( Integer)
    object_of_litigation =  Column( Text, nullable=True)
    grounds =  Column( Text, nullable=True)
    prosecution_prayer =  Column( Text, nullable=True)
    pretrial_date =  Column( Date)
    pretrial_notes =  Column( Text, nullable=True)
    pretrial_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)
    case_admissible =  Column( Boolean)
    indictment_date =  Column( Text, nullable=True)
    judgement =  Column( Text, nullable=True)
    judgement_docx =  Column( Text, nullable=True)
    case_link_type =  Column( ForeignKey('caselinktype.id'), index=True)
    linked_cases =  Column( ForeignKey('courtcase.id'), index=True)
    appealed =  Column( Boolean)
    appeal_number =  Column( Text, nullable=True)
    inventory_of_docket =  Column( Text, nullable=True)
    next_hearing_date =  Column( Date)
    interlocutory_judgement =  Column( Text, nullable=True)
    reopen =  Column( Boolean)
    reopen_reason =  Column( Text, nullable=True)
    combined_case =  Column( Boolean)
    value_in_dispute =  Column( Numeric(12, 2))
    award =  Column( Numeric(12, 2))
    govt_liability =  Column( Text, nullable=True)
    active =  Column( Boolean)
    active_date =  Column( DateTime)

    caselinktype =  relationship('Caselinktype', primaryjoin='Courtcase.case_link_type == Caselinktype.id', backref='courtcases')
    prosecutor =  relationship('Prosecutor', primaryjoin='Courtcase.filing_prosecutor == Prosecutor.id', backref='courtcases')
    parent =  relationship('Courtcase', remote_side=[id], primaryjoin='Courtcase.linked_cases == Courtcase.id', backref='courtcases')
    judicialofficer =  relationship('Judicialofficer', primaryjoin='Courtcase.pretrial_registrar == Judicialofficer.id', backref='courtcases')
    judicialofficer1 =  relationship('Judicialofficer', secondary='courtcase_judicialofficer', backref='courtcases_32')
    lawfirm =  relationship('Lawfirm', secondary='courtcase_lawfirm', backref='courtcases')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Courtcase_Judicialofficer(Model):
	 __table__ =   Table(
    'courtcase_judicialofficer', Model.metadata,
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True),
     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Courtcase_Lawfirm(Model):
	 __table__ =   Table(
    'courtcase_lawfirm', Model.metadata,
     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True),
     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Courtrank( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'courtrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Courtstation( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'courtstation'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    till_number =  Column( Text, nullable=True)
    pay_bill =  Column( Text, nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Crime( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'crime'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    law =  Column( Text, nullable=True)
    description =  Column( Text, nullable=True)
    ref =  Column( Text, nullable=True)
    ref_law =  Column( ForeignKey('law.id'), index=True)
    min_sentence =  Column( Text, nullable=True)
    max_sentence =  Column( Text, nullable=True)
    max_fine =  Column( Numeric(12, 2))

    law1 =  relationship('Law', primaryjoin='Crime.ref_law == Law.id', backref='crimes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Csiequipment( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'csiequipment'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    investigationdiary =  relationship('Investigationdiary', secondary='csiequipment_investigationdiary', backref='csiequipments')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Csiequipment_Investigationdiary(Model):
	 __table__ =   Table(
    'csiequipment_investigationdiary', Model.metadata,
     Column('csiequipment',  ForeignKey('csiequipment.id'), primary_key=True, nullable=True),
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Diagram( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'diagram'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_diary =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)
    image =  Column( Text, nullable=True)
    description =  Column( Text, nullable=True)
    docx =  Column( Text, nullable=True)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Diagram.investigation_diary == Investigationdiary.id', backref='diagrams')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Discipline( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'discipline'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=True, index=True)
    prison_officer =  Column( ForeignKey('prisonofficer.id'), nullable=True, index=True)

    party1 =  relationship('Party', primaryjoin='Discipline.party == Party.id', backref='disciplines')
    prisonofficer =  relationship('Prisonofficer', primaryjoin='Discipline.prison_officer == Prisonofficer.id', backref='disciplines')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Docpart( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'docpart'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    document =  Column( ForeignKey('document.id'), nullable=True, index=True)
    file_name =  Column( String(200), nullable=True)
    file_ext =  Column( String(10), nullable=True)
    page_no =  Column( BigInteger)
    page_text =  Column( Text, nullable=True)
    image_width =  Column( Text)
    image_height =  Column( Text)
    file_create_date =  Column( DateTime)
    file_update_date =  Column( DateTime)
    file_last_opened_date =  Column( DateTime)
    upload_dt =  Column( DateTime)
    file_byte_count =  Column( Integer)
    file_hash =  Column( String(520), nullable=True)
    file_load_path =  Column( String(300), nullable=True)
    file_upload_date =  Column( DateTime)
    page_count =  Column( Integer)
    file_text =  Column( Text, nullable=True)
    is_image =  Column( Boolean)
    file_parse_status =  Column( Text, nullable=True)
    file_assessed =  Column( Boolean)
    file_accepted =  Column( Boolean)
    file_fee_amount =  Column( Numeric(12, 2))
    language =  Column( String(10), nullable=True)
    file_bin =  Column( Text, nullable=True)

    document1 =  relationship('Document', primaryjoin='Docpart.document == Document.id', backref='docparts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Doctemplate( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'doctemplate'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    template =  Column( Text, nullable=True)
    docx =  Column( Text, nullable=True)
    name =  Column( Text, nullable=True)
    title =  Column( Text, nullable=True)
    summary =  Column( Text, nullable=True)
    template_type =  Column( ForeignKey('templatetype.id'), nullable=True, index=True)
    icon =  Column( Text, nullable=True)

    templatetype =  relationship('Templatetype', primaryjoin='Doctemplate.template_type == Templatetype.id', backref='doctemplates')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Document( DocMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'document'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( String(100), nullable=True)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)
    issue =  Column( ForeignKey('issue.id'), index=True)
    document_admissibility =  Column( Text, nullable=True)
    admisibility_notes =  Column( Text, nullable=True)
    admitted =  Column( Boolean)
    receiving_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)
    receive_date =  Column( DateTime)
    review_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)
    review_date =  Column( DateTime)
    filing_date =  Column( DateTime)
    docx =  Column( Text, nullable=True)
    document_text =  Column( Text, nullable=True)
    published =  Column( Boolean)
    publish_newspaper =  Column( Text, nullable=True)
    publish_date =  Column( Date)
    validated =  Column( Boolean)
    paid =  Column( Boolean)
    page_count =  Column( Integer)
    file_byte_count =  Column( Numeric(12, 2))
    file_hash =  Column( String(520), nullable=True)
    file_create_date =  Column( DateTime)
    file_update_date =  Column( DateTime)
    file_last_opened_date =  Column( DateTime)
    file_text =  Column( Text, nullable=True)
    file_name =  Column( String(300), nullable=True)
    file_ext =  Column( String(10), nullable=True)
    file_load_path =  Column( Text, nullable=True)
    file_upload_date =  Column( DateTime)
    file_parse_status =  Column( Text, nullable=True)
    doc_template =  Column( ForeignKey('doctemplate.id'), index=True)
    is_public =  Column( Boolean)
    is_image =  Column( Boolean)
    doc_shelf =  Column( Text, nullable=True)
    doc_row =  Column( Text, nullable=True)
    doc_room =  Column( Text, nullable=True)
    doc_placed_by =  Column( Text, nullable=True)
    citation =  Column( Text, nullable=True)
    language =  Column( String(10))
    request_urgent =  Column( Boolean)
    certify_urgent =  Column( Boolean)
    certifying_judicial_officer =  Column( ForeignKey('judicialofficer.id'), index=True)
    certify_date =  Column( DateTime)
    expiry_date =  Column( DateTime)

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Document.certifying_judicial_officer == Judicialofficer.id', backref='documents')
    courtcase =  relationship('Courtcase', primaryjoin='Document.court_case == Courtcase.id', backref='documents')
    doctemplate =  relationship('Doctemplate', primaryjoin='Document.doc_template == Doctemplate.id', backref='documents')
    issue1 =  relationship('Issue', primaryjoin='Document.issue == Issue.id', backref='documents')
    judicialofficer1 =  relationship('Judicialofficer', primaryjoin='Document.receiving_registrar == Judicialofficer.id', backref='documents_83')
    judicialofficer2 =  relationship('Judicialofficer', primaryjoin='Document.review_registrar == Judicialofficer.id', backref='documents_21')
    documenttype =  relationship('Documenttype', secondary='document_documenttype', backref='documents')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Document_Documenttype(Model):
	 __table__ =   Table(
    'document_documenttype', Model.metadata,
     Column('document',  ForeignKey('document.id'), primary_key=True, nullable=True),
     Column('documenttype',  ForeignKey('documenttype.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Documenttype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'documenttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Economicclass( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'economicclass'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( String(50), nullable=True)
    description =  Column( String(100), nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Exhibit( DocMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'exhibit'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_entry =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)
    exhibit_no =  Column( Text, nullable=True)
    docx =  Column( Text, nullable=True)
    seizure =  Column( ForeignKey('seizure.id'), nullable=True, index=True)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Exhibit.investigation_entry == Investigationdiary.id', backref='exhibits')
    seizure1 =  relationship('Seizure', primaryjoin='Exhibit.seizure == Seizure.id', backref='exhibits')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Expert( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'expert'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    institution =  Column( Text, nullable=True)
    jobtitle =  Column( Text, nullable=True)
    credentials =  Column( Text, nullable=True)

    experttype =  relationship('Experttype', secondary='expert_experttype', backref='experts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Expert_Experttype(Model):
	 __table__ =   Table(
    'expert_experttype', Model.metadata,
     Column('expert',  ForeignKey('expert.id'), primary_key=True, nullable=True),
     Column('experttype',  ForeignKey('experttype.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Experttestimony( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'experttestimony'

    investigation_entries =  Column( ForeignKey('investigationdiary.id'), primary_key=True, nullable=True)
    experts =  Column( ForeignKey('expert.id'), primary_key=True, nullable=True, index=True)
    task_given =  Column( Text, nullable=True)
    summary_of_facts =  Column( Text, nullable=True)
    statement =  Column( Text, nullable=True)
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
    file = Column(FileColumn, nullable=True)

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
class Experttype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'experttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    expert_type =  Column( ForeignKey('experttype.id'), index=True)

    parent =  relationship('Experttype', remote_side=[id], primaryjoin='Experttype.expert_type == Experttype.id', backref='experttypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Feeclass( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'feeclass'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    fee_type =  Column( ForeignKey('feeclass.id'), index=True)

    parent =  relationship('Feeclass', remote_side=[id], primaryjoin='Feeclass.fee_type == Feeclass.id', backref='feeclasses')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Feetype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'feetype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    filing_fee_type =  Column( ForeignKey('feeclass.id'), nullable=True, index=True)
    amount =  Column( Numeric(12, 2))
    unit =  Column( Text, nullable=True)
    min_fee =  Column( Numeric(12, 2))
    max_fee =  Column( Numeric(12, 2))
    description =  Column( Text)
    guide_sec =  Column( Text)
    guide_clause =  Column( Text)
    account_type =  Column( ForeignKey('accounttype.id'), nullable=True, index=True)

    accounttype =  relationship('Accounttype', primaryjoin='Feetype.account_type == Accounttype.id', backref='feetypes')
    feeclass =  relationship('Feeclass', primaryjoin='Feetype.filing_fee_type == Feeclass.id', backref='feetypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Healthevent( ActivityMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'healthevent'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=True, index=True)
    reporting_prison_officer =  Column( ForeignKey('prisonofficer.id'), index=True)
    health_event_type =  Column( ForeignKey('healtheventtype.id'), nullable=True, index=True)
    startdate =  Column( DateTime)
    enddate =  Column( DateTime)
    notes =  Column( Text, nullable=True)

    healtheventtype =  relationship('Healtheventtype', primaryjoin='Healthevent.health_event_type == Healtheventtype.id', backref='healthevents')
    party1 =  relationship('Party', primaryjoin='Healthevent.party == Party.id', backref='healthevents')
    prisonofficer =  relationship('Prisonofficer', primaryjoin='Healthevent.reporting_prison_officer == Prisonofficer.id', backref='healthevents')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Healtheventtype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'healtheventtype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Hearing( ActivityMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'hearing'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    court_cases =  Column( ForeignKey('courtcase.id'), index=True)
    hearing_type =  Column( ForeignKey('hearingtype.id'), nullable=True, index=True)
    schedule_status =  Column( ForeignKey('schedulestatustype.id'), nullable=True, index=True)
    hearing_date =  Column( Date)
    reason =  Column( Text, nullable=True)
    sequence =  Column( BigInteger)
    yearday =  Column( BigInteger)
    starttime =  Column( Time)
    endtime =  Column( Time)
    notes =  Column( Text, nullable=True)
    completed =  Column( Boolean)
    adjourned_to =  Column( Date)
    adjournment_reason =  Column( Text, nullable=True)
    transcript =  Column( Text, nullable=True)
    atendance =  Column( Text, nullable=True)
    next_hearing_date =  Column( Date)
    postponement_reason =  Column( Text, nullable=True)

    courtcase =  relationship('Courtcase', primaryjoin='Hearing.court_cases == Courtcase.id', backref='hearings')
    hearingtype =  relationship('Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref='hearings')
    schedulestatustype =  relationship('Schedulestatustype', primaryjoin='Hearing.schedule_status == Schedulestatustype.id', backref='hearings')
    issue =  relationship('Issue', secondary='hearing_issue', backref='hearings')
    judicialofficer =  relationship('Judicialofficer', secondary='hearing_judicialofficer', backref='hearings')
    lawfirm =  relationship('Lawfirm', secondary='hearing_lawfirm', backref='hearings')
    lawfirm1 =  relationship('Lawfirm', secondary='hearing_lawfirm_2', backref='hearings_33')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Hearing_Issue(Model):
	 __table__ =   Table(
    'hearing_issue', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Hearing_Judicialofficer(Model):
	 __table__ =   Table(
    'hearing_judicialofficer', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),
     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Hearing_Lawfirm(Model):
	 __table__ =   Table(
    'hearing_lawfirm', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),
     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Hearing_Lawfirm_(Model):
	 __table__ =   Table(
    'hearing_lawfirm_2', Model.metadata,
     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),
     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Hearingtype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'hearingtype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    hearing_type =  Column( ForeignKey('hearingtype.id'), index=True)

    parent =  relationship('Hearingtype', remote_side=[id], primaryjoin='Hearingtype.hearing_type == Hearingtype.id', backref='hearingtypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Instancecrime( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'instancecrime'

    id =  Column( Integer, primary_key=True)
    parties =  Column( ForeignKey('party.id'), nullable=True, index=True)
    crimes =  Column( ForeignKey('crime.id'), nullable=True, index=True)
    crime_detail =  Column( Text, nullable=True)
    tffender_type =  Column( Text, nullable=True)
    crime_date =  Column( DateTime)
    date_note =  Column( Text, nullable=True)
    place_of_crime =  Column( Text, nullable=True)
    place_note =  Column( Text, nullable=True)

    crime =  relationship('Crime', primaryjoin='Instancecrime.crimes == Crime.id', backref='instancecrimes')
    party =  relationship('Party', primaryjoin='Instancecrime.parties == Party.id', backref='instancecrimes')
    issue =  relationship('Issue', secondary='instancecrime_issue', backref='instancecrimes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Instancecrime_Issue(Model):
	 __table__ =   Table(
    'instancecrime_issue', Model.metadata,
     Column('instancecrime',  ForeignKey('instancecrime.id'), primary_key=True, nullable=True),
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Interview( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'interview'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_entry =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)
    question =  Column( Text, nullable=True)
    answer =  Column( Text, nullable=True)
    validated =  Column( Boolean)
    language =  Column( Text, nullable=True)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Interview.investigation_entry == Investigationdiary.id', backref='interviews')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Investigationdiary( ActivityMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'investigationdiary'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    activity =  Column( Text, nullable=True)
    complaint =  Column( ForeignKey('complaint.id'), nullable=True, index=True)
    location =  Column( Text, nullable=True)
    outcome =  Column( Text, nullable=True)
    equipmentresults =  Column( Text, nullable=True)
    startdate =  Column( DateTime, nullable=True)
    enddate =  Column( DateTime)
    advocate_present =  Column( Text, nullable=True)
    summons_statement =  Column( Text, nullable=True)
    arrest_statement =  Column( Text, nullable=True)
    arrest_warrant =  Column( Text, nullable=True)
    search_seizure_statement =  Column( Text, nullable=True)
    docx =  Column( Text, nullable=True)
    detained =  Column( Text, nullable=True)
    detained_at =  Column( Text, nullable=True)
    provisional_release_statement =  Column( Text, nullable=True)
    warrant_type =  Column( ForeignKey('warranttype.id'), index=True)
    warrant_issued_by =  Column( Text, nullable=True)
    warrant_issue_date =  Column( Date)
    warrant_delivered_by =  Column( Text, nullable=True)
    warrant_received_by =  Column( Text, nullable=True)
    warrant_serve_date =  Column( Text, nullable=True)
    warrant_docx =  Column( Text, nullable=True)
    warrant_upload_date =  Column( Text, nullable=True)

    complaint1 =  relationship('Complaint', primaryjoin='Investigationdiary.complaint == Complaint.id', backref='investigationdiaries')
    warranttype =  relationship('Warranttype', primaryjoin='Investigationdiary.warrant_type == Warranttype.id', backref='investigationdiaries')
    party =  relationship('Party', secondary='investigationdiary_party', backref='investigationdiaries')
    policeofficer =  relationship('Policeofficer', secondary='investigationdiary_policeofficer', backref='investigationdiaries')
    vehicle =  relationship('Vehicle', secondary='investigationdiary_vehicle', backref='investigationdiaries')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Investigationdiary_Party(Model):
	 __table__ =   Table(
    'investigationdiary_party', Model.metadata,
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Investigationdiary_Policeofficer(Model):
	 __table__ =   Table(
    'investigationdiary_policeofficer', Model.metadata,
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),
     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Investigationdiary_Vehicle(Model):
	 __table__ =   Table(
    'investigationdiary_vehicle', Model.metadata,
     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),
     Column('vehicle',  ForeignKey('vehicle.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Issue( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'issue'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    issue =  Column( Text, nullable=True)
    facts =  Column( Text)
    counter_claim =  Column( Boolean)
    argument =  Column( Text, nullable=True)
    argument_date =  Column( Date)
    argument_docx =  Column( Text)
    rebuttal =  Column( Text, nullable=True)
    rebuttal_date =  Column( Date)
    rebuttal_docx =  Column( Text)
    hearing_date =  Column( Date)
    determination =  Column( Text, nullable=True)
    dtermination_date =  Column( Date)
    determination_docx =  Column( Text, nullable=True)
    resolved =  Column( Boolean)
    defense_lawyer =  Column( ForeignKey('lawyer.id'), nullable=True, index=True)
    prosecutor =  Column( ForeignKey('prosecutor.id'), index=True)
    judicial_officer =  Column( ForeignKey('judicialofficer.id'), nullable=True, index=True)
    court_case =  Column( ForeignKey('courtcase.id'), nullable=True, index=True)
    tasks =  Column( Text, nullable=True)
    is_criminal =  Column( Boolean)
    moral_element =  Column( Text, nullable=True)
    material_element =  Column( Text, nullable=True)
    legal_element =  Column( Text, nullable=True)
    debt_amount =  Column( Numeric(12, 2))

    courtcase =  relationship('Courtcase', primaryjoin='Issue.court_case == Courtcase.id', backref='issues')
    lawyer =  relationship('Lawyer', primaryjoin='Issue.defense_lawyer == Lawyer.id', backref='issues')
    judicialofficer =  relationship('Judicialofficer', primaryjoin='Issue.judicial_officer == Judicialofficer.id', backref='issues')
    prosecutor1 =  relationship('Prosecutor', primaryjoin='Issue.prosecutor == Prosecutor.id', backref='issues')
    lawyer1 =  relationship('Lawyer', secondary='issue_lawyer', backref='issues_19')
    legalreference =  relationship('Legalreference', secondary='issue_legalreference', backref='issues')
    legalreference1 =  relationship('Legalreference', secondary='issue_legalreference_2', backref='issues_53')
    party =  relationship('Party', secondary='issue_party', backref='issues')
    party1 =  relationship('Party', secondary='issue_party_2', backref='issues_80')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Issue_Lawyer(Model):
	 __table__ =   Table(
    'issue_lawyer', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),
     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Issue_Legalreference(Model):
	 __table__ =   Table(
    'issue_legalreference', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),
     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Issue_Legalreference_(Model):
	 __table__ =   Table(
    'issue_legalreference_2', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),
     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Issue_Party(Model):
	 __table__ =   Table(
    'issue_party', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class T_Issue_Party_(Model):
	 __table__ =   Table(
    'issue_party_2', Model.metadata,
     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Judicialofficer( PersonMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'judicialofficer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    rank =  Column( ForeignKey('judicialrank.id'), nullable=True, index=True)
    judicial_role =  Column( ForeignKey('judicialrole.id'), nullable=True, index=True)
    court_station =  Column( ForeignKey('courtstation.id'), nullable=True, index=True)

    courtstation =  relationship('Courtstation', primaryjoin='Judicialofficer.court_station == Courtstation.id', backref='judicialofficers')
    judicialrole =  relationship('Judicialrole', primaryjoin='Judicialofficer.judicial_role == Judicialrole.id', backref='judicialofficers')
    judicialrank =  relationship('Judicialrank', primaryjoin='Judicialofficer.rank == Judicialrank.id', backref='judicialofficers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Judicialrank( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'judicialrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Judicialrole( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'judicialrole'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Law( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'law'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=True)
    description =  Column( Text, nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Lawfirm( PlaceMixin,  RefTypeMixin, ContactMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'lawfirm'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Lawyer( PersonMixin, ContactMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'lawyer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    law_firm =  Column( ForeignKey('lawfirm.id'), index=True)
    bar_no =  Column( Text, nullable=True)
    bar_date =  Column( Date)

    lawfirm =  relationship('Lawfirm', primaryjoin='Lawyer.law_firm == Lawfirm.id', backref='lawyers')
    party =  relationship('Party', secondary='lawyer_party', backref='lawyers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Lawyer_Party(Model):
	 __table__ =   Table(
    'lawyer_party', Model.metadata,
     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=True),
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Legalreference( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'legalreference'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    ref =  Column( Text, nullable=True)
    verbatim =  Column( Text, nullable=True)
    public =  Column( Boolean)
    commentary =  Column( Text, nullable=True)
    validated =  Column( Boolean)
    citation =  Column( Text, nullable=True)
    quote =  Column( Text, nullable=True)
    interpretation =  Column( Text, nullable=True)
    klr_url_full =  Column( String(300), nullable=True)
    klr_rul_short =  Column( Text, nullable=True)
    doc_id =  Column( String(300), nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Nextofkin( PersonMixin, PersonDocMixin, ContactMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'nextofkin'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    biodata =  Column( ForeignKey('biodata.id'), nullable=True, index=True)
    childunder4 =  Column( Boolean)

    biodata1 =  relationship('Biodata', primaryjoin='Nextofkin.biodata == Biodata.id', backref='nextofkins')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Notification( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'notification'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    contact =  Column( Text, nullable=True)
    message =  Column( Text, nullable=True)
    confirmation =  Column( Text, nullable=True)
    notification_register =  Column( ForeignKey('notificationregister.id'), index=True)
    add_date =  Column( DateTime)
    send_date =  Column( DateTime)
    sent =  Column( Boolean)
    delivered =  Column( Boolean)
    retries =  Column( Integer)
    abandon =  Column( Boolean)
    retry_count =  Column( Integer)

    notificationregister =  relationship('Notificationregister', primaryjoin='Notification.notification_register == Notificationregister.id', backref='notifications')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Notificationregister( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'notificationregister'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    notification_type =  Column( ForeignKey('notificationtype.id'), nullable=True, index=True)
    contact =  Column( Text, nullable=True)
    notify_event =  Column( ForeignKey('notifyevent.id'), index=True)
    retry_count =  Column( BigInteger)
    active =  Column( Boolean)
    hearing =  Column( ForeignKey('hearing.id'), index=True)
    document =  Column( ForeignKey('document.id'), index=True)
    court_case =  Column( ForeignKey('courtcase.id'), index=True)
    complaint =  Column( ForeignKey('complaint.id'), index=True)
    complaint_category =  Column( ForeignKey('complaintcategory.id'), index=True)
    health_event =  Column( ForeignKey('healthevent.id'), index=True)
    party =  Column( ForeignKey('party.id'), index=True)

    complaint1 =  relationship('Complaint', primaryjoin='Notificationregister.complaint == Complaint.id', backref='notificationregisters')
    complaintcategory =  relationship('Complaintcategory', primaryjoin='Notificationregister.complaint_category == Complaintcategory.id', backref='notificationregisters')
    courtcase =  relationship('Courtcase', primaryjoin='Notificationregister.court_case == Courtcase.id', backref='notificationregisters')
    document1 =  relationship('Document', primaryjoin='Notificationregister.document == Document.id', backref='notificationregisters')
    healthevent =  relationship('Healthevent', primaryjoin='Notificationregister.health_event == Healthevent.id', backref='notificationregisters')
    hearing1 =  relationship('Hearing', primaryjoin='Notificationregister.hearing == Hearing.id', backref='notificationregisters')
    notificationtype =  relationship('Notificationtype', primaryjoin='Notificationregister.notification_type == Notificationtype.id', backref='notificationregisters')
    notifyevent =  relationship('Notifyevent', primaryjoin='Notificationregister.notify_event == Notifyevent.id', backref='notificationregisters')
    party1 =  relationship('Party', primaryjoin='Notificationregister.party == Party.id', backref='notificationregisters')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Notificationtype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'notificationtype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=True)
    description =  Column( Text, nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Notifyevent( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'notifyevent'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Party( PersonMixin, ContactMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'party'

    id =  Column( Integer, primary_key=True)
    complaints =  Column( ForeignKey('complaint.id'), nullable=True, index=True)
    statement =  Column( String(1000), nullable=True)
    statementdate =  Column( DateTime)
    complaint_role =  Column( ForeignKey('complaintrole.id'), nullable=True, index=True)
    notes =  Column( Text, nullable=True)
    dateofrepresentation =  Column( DateTime)
    party_type =  Column( ForeignKey('partytype.id'), nullable=True, index=True)
    relative =  Column( ForeignKey('party.id'), nullable=True, index=True)
    relationship_type =  Column( Text, nullable=True)
    is_infant =  Column( Boolean)
    is_minor =  Column( Boolean)
    miranda_read =  Column( Boolean)
    miranda_date =  Column( DateTime)
    miranda_witness =  Column( Text, nullable=True)

    complaintrole =  relationship('Complaintrole', primaryjoin='Party.complaint_role == Complaintrole.id', backref='parties')
    complaint =  relationship('Complaint', primaryjoin='Party.complaints == Complaint.id', backref='parties')
    partytype =  relationship('Partytype', primaryjoin='Party.party_type == Partytype.id', backref='parties')
    parent =  relationship('Party', remote_side=[id], primaryjoin='Party.relative == Party.id', backref='parties')
    settlement =  relationship('Settlement', secondary='party_settlement', backref='parties')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Party_Settlement(Model):
	 __table__ =   Table(
    'party_settlement', Model.metadata,
     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True),
     Column('settlement',  ForeignKey('settlement.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Partytype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'partytype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Payment( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'payment'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    bill =  Column( ForeignKey('bill.id'), nullable=True, index=True)
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
    file = Column(FileColumn, nullable=True)

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
class Personaleffect( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'personaleffect'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    party =  Column( ForeignKey('party.id'), nullable=True, index=True)
    personal_effects_category =  Column( ForeignKey('personaleffectscategory.id'), nullable=True, index=True)

    party1 =  relationship('Party', primaryjoin='Personaleffect.party == Party.id', backref='personaleffects')
    personaleffectscategory =  relationship('Personaleffectscategory', primaryjoin='Personaleffect.personal_effects_category == Personaleffectscategory.id', backref='personaleffects')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Personaleffectscategory( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'personaleffectscategory'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Policeofficer( PersonMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'policeofficer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    police_rank =  Column( ForeignKey('policeofficerrank.id'), nullable=True, index=True)
    servicenumber =  Column( String(100), nullable=True, unique=True)

    policeofficerrank =  relationship('Policeofficerrank', primaryjoin='Policeofficer.police_rank == Policeofficerrank.id', backref='policeofficers')
    policestation =  relationship('Policestation', secondary='policeofficer_policestation', backref='policeofficers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Policeofficer_Policestation(Model):
	 __table__ =   Table(
    'policeofficer_policestation', Model.metadata,
     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=True),
     Column('policestation',  ForeignKey('policestation.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Policeofficerrank( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'policeofficerrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    name =  Column( Text, nullable=True)
    description =  Column( Text, nullable=True)
    sequence =  Column( Integer)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Policestation( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'policestation'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    town =  Column( ForeignKey('town.id'), index=True)
    officer_commanding =  Column( ForeignKey('policeofficer.id'), nullable=True, index=True)
    police_station_rank =  Column( ForeignKey('policestationrank.id'), nullable=True, index=True)

    policeofficer =  relationship('Policeofficer', primaryjoin='Policestation.officer_commanding == Policeofficer.id', backref='policestations')
    policestationrank =  relationship('Policestationrank', primaryjoin='Policestation.police_station_rank == Policestationrank.id', backref='policestations')
    town1 =  relationship('Town', primaryjoin='Policestation.town == Town.id', backref='policestations')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Policestationrank( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'policestationrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Prison( PlaceMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'prison'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    town =  Column( ForeignKey('town.id'), nullable=True, index=True)

    town1 =  relationship('Town', primaryjoin='Prison.town == Town.id', backref='prisons')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Prisonofficer( PersonMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'prisonofficer'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    prison =  Column( ForeignKey('prison.id'), nullable=True, index=True)
    prison_officer_rank =  Column( ForeignKey('prisonofficerrank.id'), nullable=True, index=True)

    prison1 =  relationship('Prison', primaryjoin='Prisonofficer.prison == Prison.id', backref='prisonofficers')
    prisonofficerrank =  relationship('Prisonofficerrank', primaryjoin='Prisonofficer.prison_officer_rank == Prisonofficerrank.id', backref='prisonofficers')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Prisonofficerrank( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'prisonofficerrank'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Prosecutor( PersonMixin, ContactMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'prosecutor'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    prosecutor_team =  Column( ForeignKey('prosecutorteam.id'), index=True)
    lawyer =  Column( ForeignKey('lawyer.id'), nullable=True, index=True)

    lawyer1 =  relationship('Lawyer', primaryjoin='Prosecutor.lawyer == Lawyer.id', backref='prosecutors')
    prosecutorteam =  relationship('Prosecutorteam', primaryjoin='Prosecutor.prosecutor_team == Prosecutorteam.id', backref='prosecutors')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Prosecutorteam( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'prosecutorteam'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Releasetype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'releasetype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Religion( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'religion'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Schedulestatustype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'schedulestatustype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Seizure( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'seizure'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    investigation_diary =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)
    owner =  Column( Text, nullable=True)
    item =  Column( Text, nullable=True)
    item_packaging =  Column( Text, nullable=True)
    item_pic =  Column( Text, nullable=True)
    premises =  Column( Text, nullable=True)
    reg_no =  Column( Text, nullable=True)
    witness =  Column( Text, nullable=True)
    notes =  Column( Text, nullable=True)
    docx =  Column( Text, nullable=True)
    item_description =  Column( Text, nullable=True)
    returned =  Column( Boolean)
    return_date =  Column( DateTime)
    return_notes =  Column( Text, nullable=True)
    return_signed_receipt =  Column( Text, nullable=True)
    destroyed =  Column( Boolean)
    destruction_date =  Column( Date)
    destruction_witnesses =  Column( Text, nullable=True)
    destruction_notes =  Column( Text, nullable=True)
    disposed =  Column( Boolean)
    sold_to =  Column( Text, nullable=True)
    disposal_date =  Column( Date)
    disposal_price =  Column( Numeric(12, 2))
    disposal_receipt =  Column( Text, nullable=True)
    recovery_town =  Column( ForeignKey('town.id'), index=True)
    destruction_pic =  Column( Text, nullable=True)
    is_evidence =  Column( Boolean)
    immovable =  Column( Boolean)

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Seizure.investigation_diary == Investigationdiary.id', backref='seizures')
    town =  relationship('Town', primaryjoin='Seizure.recovery_town == Town.id', backref='seizures')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Settlement( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'settlement'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    complaint =  Column( ForeignKey('complaint.id'), nullable=True, index=True)
    terms =  Column( Text, nullable=True)
    amount =  Column( Numeric(12, 2))
    paid =  Column( Boolean)
    docx =  Column( Text, nullable=True)
    settlor =  Column( ForeignKey('party.id'), nullable=True, index=True)

    complaint1 =  relationship('Complaint', primaryjoin='Settlement.complaint == Complaint.id', backref='settlements')
    party =  relationship('Party', primaryjoin='Settlement.settlor == Party.id', backref='settlements')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Subcounty( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'subcounty'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    county =  Column( ForeignKey('county.id'), nullable=True, index=True)

    county1 =  relationship('County', primaryjoin='Subcounty.county == County.id', backref='subcounties')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Sysuserextra( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'sysuserextra'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_notes =  Column( Text, nullable=True)
    sys_birthday =  Column( Date)
    sys_job_grade =  Column( Text, nullable=True)
    sys_home_address =  Column( Text, nullable=True)
    alt_phone =  Column( String(20), nullable=True)
    alt_email =  Column( String(120), nullable=True)
    office_address =  Column( Text, nullable=True)
    off_email =  Column( String(120), nullable=True)
    syswkflowgrp =  Column( ForeignKey('syswkflowgrp.id'), nullable=True, index=True)
    off_phone =  Column( String(20), nullable=True)

    syswkflowgrp1 =  relationship('Syswkflowgrp', primaryjoin='Sysuserextra.syswkflowgrp == Syswkflowgrp.id', backref='sysuserextras')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Sysviewfld( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'sysviewfld'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys__view =  Column( ForeignKey('sysviewlist.id'), nullable=True, index=True)
    fld_name =  Column( String(100), nullable=True)
    fld_type =  Column( String(100), nullable=True)
    fld_unique =  Column( Boolean)
    fld_validator =  Column( String(200), nullable=True)
    fld_choices =  Column( String(300), nullable=True)
    fld_label =  Column( String(100), nullable=True)
    fld_default =  Column( String(100), nullable=True)
    fld_widget =  Column( String(200), nullable=True)

    sysviewlist =  relationship('Sysviewlist', primaryjoin='Sysviewfld.sys__view == Sysviewlist.id', backref='sysviewflds')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Sysviewlist( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'sysviewlist'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_name =  Column( String(100), nullable=True, unique=True)
    sys_route =  Column( String(200), nullable=True)
    sys_perms =  Column( String(300), nullable=True)
    sys_template =  Column( Text, nullable=True)
    sys_title =  Column( String(100), nullable=True)
    sys_wtf =  Column( Boolean)
    sys_table_name =  Column( String(100), nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Syswkflow( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'syswkflow'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_name =  Column( String(200), unique=True)
    sys_description =  Column( String(200))
    sys_notes =  Column( Text)
    syswkflowgrp =  Column( ForeignKey('syswkflowgrp.id'), index=True)
    sys_wkflow_template =  Column( Text, nullable=True)
    sys_steps =  Column( Integer)

    syswkflowgrp1 =  relationship('Syswkflowgrp', primaryjoin='Syswkflow.syswkflowgrp == Syswkflowgrp.id', backref='syswkflows')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Syswkflowgrp( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'syswkflowgrp'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    sys_cat_name =  Column( String(200), nullable=True, unique=True)
    sys_cat_description =  Column( String(200))
    sys_cat_notes =  Column( Text, nullable=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Syswkflowviewseq( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'syswkflowviewseq'

    sys__view__lists =  Column( ForeignKey('sysviewlist.id'), primary_key=True, nullable=True)
    sys_wkflows =  Column( ForeignKey('syswkflow.id'), primary_key=True, nullable=True, index=True)
    sys_order =  Column( BigInteger, nullable=True)
    sys_is_terminal =  Column( Boolean)

    sysviewlist =  relationship('Sysviewlist', primaryjoin='Syswkflowviewseq.sys__view__lists == Sysviewlist.id', backref='syswkflowviewseqs')
    syswkflow =  relationship('Syswkflow', primaryjoin='Syswkflowviewseq.sys_wkflows == Syswkflow.id', backref='syswkflowviewseqs')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Templatetype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'templatetype'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    template_type =  Column( ForeignKey('templatetype.id'), index=True)

    parent =  relationship('Templatetype', remote_side=[id], primaryjoin='Templatetype.template_type == Templatetype.id', backref='templatetypes')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Town( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'town'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    ward =  relationship('Ward', secondary='town_ward', backref='towns')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class T_Town_Ward(Model):
	 __table__ =   Table(
    'town_ward', Model.metadata,
     Column('town',  ForeignKey('town.id'), primary_key=True, nullable=True),
     Column('ward',  ForeignKey('ward.id'), primary_key=True, nullable=True, index=True)
)

#ENDCLASS


#STARTCLASS
class Transcript( DocMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'transcript'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    video =  Column( Text, nullable=True)
    audio =  Column( Text, nullable=True)
    add_date =  Column( DateTime)
    asr_transcript =  Column( Text, nullable=True)
    asr_date =  Column( DateTime)
    edited_transcript =  Column( Text, nullable=True)
    edit_date =  Column( DateTime)
    certified_transcript =  Column( Text, nullable=True)
    certfiy_date =  Column( DateTime)
    locked =  Column( Boolean)
    hearing =  Column( ForeignKey('hearing.id'), nullable=True, index=True)

    hearing1 =  relationship('Hearing', primaryjoin='Transcript.hearing == Hearing.id', backref='transcripts')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Vehicle( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'vehicle'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    police_station =  Column( ForeignKey('policestation.id'), nullable=True, index=True)
    make =  Column( String(100), nullable=True)
    model =  Column( String(100), nullable=True)
    regno =  Column( String(100), nullable=True)

    policestation =  relationship('Policestation', primaryjoin='Vehicle.police_station == Policestation.id', backref='vehicles')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Ward( AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'ward'

    id =  Column( Integer, primary_key=True, autoincrement=True)
    subcounty =  Column( ForeignKey('subcounty.id'), nullable=True, index=True)

    subcounty1 =  relationship('Subcounty', primaryjoin='Ward.subcounty == Subcounty.id', backref='wards')

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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
class Warranttype( RefTypeMixin,  AuditMixin, Model):
    __versioned__ = {}
    __tablename__ = 'warranttype'

    id =  Column( Integer, primary_key=True, autoincrement=True)

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    file = Column(FileColumn, nullable=True)

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

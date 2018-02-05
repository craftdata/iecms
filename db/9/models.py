# coding: utf-8

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time, text

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql.base import INTERVAL

from sqlalchemy.ext.declarative import declarative_base




from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy_utils import aggregated, force_auto_coercion, observes
from sqlalchemy.orm import column_property
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
from .mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')

# UTILITY CLASSES

import arrow, enum, datetime

# Initialize sqlalchemy_utils
#force_auto_coercion()

# Keep versions of all data
make_versioned()
make_searchable()




Base = declarative_base()

metadata = Base.metadata





class Accounttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'accounttype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('accounttype_id_seq'::regclass)"))





class Bill( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'bill'

    __table_args__ = (

        ForeignKeyConstraint(['court_account_courts', 'court_account_account__types'], ['courtaccount.courts', 'courtaccount.account__types']),

        Index('idx_bill__court_account_courts_court_account_account__types', 'court_account_courts', 'court_account_account__types')

    )



    id = Column(Integer, primary_key=True, server_default=text("nextval('bill_id_seq'::regclass)"))

    assessing_registrar = Column(ForeignKey('judicialofficer.id'), nullable=True, index=True)

    receiving_registrar = Column(ForeignKey('judicialofficer.id'), nullable=True, index=True)

    lawyer_paying = Column(ForeignKey('lawyer.id'), index=True)

    party_paying = Column(ForeignKey('party.complaints'), index=True)

    documents = Column(ForeignKey('document.id'), index=True)

    date_of_payment = Column(DateTime)

    paid = Column(Boolean)

    pay_code = Column(String(20), unique=True)

    bill_total = Column(Numeric(12, 2))

    court = Column(ForeignKey('court.id'), nullable=True, index=True)

    court_account_courts = Column(Integer, nullable=True)

    court_account_account__types = Column(Integer, nullable=True)

    validated = Column(Boolean)

    validation_date = Column(DateTime)



    judicialofficer = relationship('Judicialofficer', primaryjoin='Bill.assessing_registrar == Judicialofficer.id')

    court1 = relationship('Court')

    courtaccount = relationship('Courtaccount')

    document = relationship('Document')

    lawyer = relationship('Lawyer')

    party = relationship('Party')

    judicialofficer1 = relationship('Judicialofficer', primaryjoin='Bill.receiving_registrar == Judicialofficer.id')





class Billdetail( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'billdetail'



    id = Column(Integer, primary_key=True, server_default=text("nextval('billdetail_id_seq'::regclass)"))

    receipt_id = Column(ForeignKey('bill.id'), nullable=True, index=True)

    feetype = Column(ForeignKey('feetype.id'), nullable=True, index=True)

    purpose = Column(Text, nullable=True)

    unit = Column(Text)

    qty = Column(Integer)

    unit_cost = Column(Numeric(12, 2))

    amount = Column(Numeric(12, 2))



    feetype1 = relationship('Feetype')

    receipt = relationship('Bill')





class Biodatum( ParentageMixin,  BiometricMixin,  PersonMedicalMixin,  PersonDocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'biodata'



    id = Column(Integer, primary_key=True, server_default=text("nextval('biodata_id_seq'::regclass)"))

    party = Column(ForeignKey('party.complaints'), nullable=True, index=True)

    economic_class = Column(ForeignKey('economicclass.id'), index=True)

    religion = Column(ForeignKey('religion.id'), index=True)

    photo = Column(LargeBinary)

    health_status = Column(Text, nullable=True)



    economicclas = relationship('Economicclas')

    party1 = relationship('Party')

    religion1 = relationship('Religion')





class Casecategory( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'casecategory'



    id = Column(Integer, primary_key=True, server_default=text("nextval('casecategory_id_seq'::regclass)"))

    subcategory = Column(ForeignKey('casecategory.id'), index=True)



    parent = relationship('Casecategory', remote_side=[id])

    casechecklist = relationship('Casechecklist', secondary='t_casecategorychecklist')

    courtcase = relationship('Courtcase', secondary='t_casecategory_courtcase')





t_casecategory_courtcase = Table(

    'casecategory_courtcase', metadata,

    Column('casecategory', ForeignKey('casecategory.id'), primary_key=True, nullable=True),

    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)

)





t_casecategorychecklist = Table(

    'casecategorychecklist', metadata,

    Column('case_checklists', ForeignKey('casechecklist.id'), primary_key=True, nullable=True),

    Column('case_categories', ForeignKey('casecategory.id'), primary_key=True, nullable=True, index=True)

)





class Casechecklist( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'casechecklist'



    id = Column(Integer, primary_key=True, server_default=text("nextval('casechecklist_id_seq'::regclass)"))

    name = Column(String(100), nullable=True)

    description = Column(String(100), nullable=True)

    notes = Column(Text, nullable=True)





class Caselinktype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'caselinktype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('caselinktype_id_seq'::regclass)"))





class Celltype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'celltype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('celltype_id_seq'::regclass)"))





class Commital( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'commital'



    id = Column(Integer, primary_key=True, server_default=text("nextval('commital_id_seq'::regclass)"))

    prisons = Column(ForeignKey('prison.id'), index=True)

    police_station = Column(ForeignKey('policestation.id'), index=True)

    parties = Column(ForeignKey('party.complaints'), nullable=True, index=True)

    casecomplete = Column(Boolean)

    commit_date = Column(Date, nullable=True)

    purpose = Column(Text, nullable=True)

    warrant_type = Column(ForeignKey('warranttype.id'), nullable=True, index=True)

    warrant_docx = Column(Text, nullable=True)

    warrant_issue_date = Column(Date)

    warrant_issued_by = Column(Text, nullable=True)

    warrant_date_attached = Column(DateTime)

    duration = Column(INTERVAL(fields='day to second'))

    commital = Column(ForeignKey('commital.id'), index=True)

    commital_type = Column(ForeignKey('commitaltype.id'), nullable=True, index=True)

    court_case = Column(ForeignKey('courtcase.id'), index=True)

    concurrent = Column(Boolean)

    life_imprisonment = Column(Boolean)

    arrival_date = Column(DateTime)

    sentence_start_date = Column(DateTime)

    arrest_date = Column(DateTime)

    remaining_years = Column(Integer)

    remaining_months = Column(Integer)

    remaining_days = Column(Integer)

    cell_number = Column(Text, nullable=True)

    cell_type = Column(ForeignKey('celltype.id'), index=True)

    release_date = Column(DateTime)

    exit_date = Column(DateTime)

    reason_for_release = Column(Text, nullable=True)

    with_children = Column(Boolean)

    release_type = Column(ForeignKey('releasetype.id'), index=True)

    receiving_officer = Column(ForeignKey('prisonofficer.id'), nullable=True, index=True)

    releasing_officer = Column(ForeignKey('prisonofficer.id'), nullable=True, index=True)



    celltype = relationship('Celltype')

    parent = relationship('Commital', remote_side=[id])

    commitaltype = relationship('Commitaltype')

    courtcase = relationship('Courtcase')

    party = relationship('Party')

    policestation = relationship('Policestation')

    prison = relationship('Prison')

    prisonofficer = relationship('Prisonofficer', primaryjoin='Commital.receiving_officer == Prisonofficer.id')

    releasetype = relationship('Releasetype')

    prisonofficer1 = relationship('Prisonofficer', primaryjoin='Commital.releasing_officer == Prisonofficer.id')

    warranttype = relationship('Warranttype')





class Commitaltype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'commitaltype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('commitaltype_id_seq'::regclass)"))

    maxduration = Column(INTERVAL(fields='day to second'))





class Complaint( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'complaint'



    id = Column(Integer, primary_key=True, server_default=text("nextval('complaint_id_seq'::regclass)"))

    active = Column(Boolean)

    ob_number = Column(String(20), nullable=True)

    police_station = Column(ForeignKey('policestation.id'), nullable=True, index=True)

    daterecvd = Column(DateTime, nullable=True)

    datefiled = Column(DateTime)

    datecaseopened = Column(DateTime)

    casesummary = Column(String(2000), nullable=True)

    complaintstatement = Column(Text, nullable=True)

    circumstances = Column(Text, nullable=True)

    reportingofficer = Column(ForeignKey('policeofficer.id'), nullable=True, index=True)

    casefileinformation = Column(Text, nullable=True)

    p_request_help = Column(Boolean)

    p_instruction = Column(Text, nullable=True)

    p_submitted = Column(Boolean)

    p_submission_date = Column(DateTime)

    p_submission_notes = Column(Text, nullable=True)

    p_closed = Column(Text, nullable=True)

    p_evaluation = Column(Text, nullable=True)

    p_recommend_charge = Column(Boolean)

    charge_sheet = Column(Text, nullable=True)

    charge_sheet_docx = Column(Text, nullable=True)

    evaluating_prosecutor_team = Column(ForeignKey('prosecutorteam.id'), index=True)

    magistrate_report_date = Column(DateTime)

    reported_to_judicial_officer = Column(ForeignKey('judicialofficer.id'), index=True)

    closed = Column(Boolean)

    close_date = Column(DateTime)

    close_reason = Column(Text, nullable=True)



    prosecutorteam = relationship('Prosecutorteam')

    policestation = relationship('Policestation')

    judicialofficer = relationship('Judicialofficer')

    policeofficer = relationship('Policeofficer')

    complaintcategory = relationship('Complaintcategory', secondary='t_complaint_complaintcategory')

    courtcase = relationship('Courtcase', secondary='t_complaint_courtcase')





class Party( PersonMixin,  AuditMixin, AllFeaturesMixin, Complaint):

    __tablename__ = 'party'



    complaints = Column(ForeignKey('complaint.id'), primary_key=True)

    statement = Column(String(1000), nullable=True)

    statementdate = Column(DateTime)

    complaint_role = Column(ForeignKey('complaintrole.id'), nullable=True, index=True)

    notes = Column(Text, nullable=True)

    dateofrepresentation = Column(DateTime)

    party_type = Column(ForeignKey('partytype.id'), nullable=True, index=True)

    relative = Column(ForeignKey('party.complaints'), nullable=True, index=True)

    relationship_type = Column(Text, nullable=True)

    is_infant = Column(Boolean)

    is_minor = Column(Boolean)

    miranda_read = Column(Boolean)

    miranda_date = Column(DateTime)

    miranda_witness = Column(Text, nullable=True)



    complaintrole = relationship('Complaintrole')

    partytype = relationship('Partytype')

    parent = relationship('Party', remote_side=[complaints])

    settlement = relationship('Settlement', secondary='t_party_settlement')





t_complaint_complaintcategory = Table(

    'complaint_complaintcategory', metadata,

    Column('complaint', ForeignKey('complaint.id'), primary_key=True, nullable=True),

    Column('complaintcategory', ForeignKey('complaintcategory.id'), primary_key=True, nullable=True, index=True)

)





t_complaint_courtcase = Table(

    'complaint_courtcase', metadata,

    Column('complaint', ForeignKey('complaint.id'), primary_key=True, nullable=True),

    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)

)





class Complaintcategory( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'complaintcategory'



    id = Column(Integer, primary_key=True, server_default=text("nextval('complaintcategory_id_seq'::regclass)"))

    complaint_category_parent = Column(ForeignKey('complaintcategory.id'), index=True)



    parent = relationship('Complaintcategory', remote_side=[id])





class Complaintrole( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'complaintrole'



    id = Column(Integer, primary_key=True, server_default=text("nextval('complaintrole_id_seq'::regclass)"))





class Country( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'country'



    id = Column(Integer, primary_key=True, server_default=text("nextval('country_id_seq'::regclass)"))

    name = Column(Text, nullable=True)





class County( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'county'



    id = Column(Integer, primary_key=True, server_default=text("nextval('county_id_seq'::regclass)"))

    country = Column(ForeignKey('country.id'), nullable=True, index=True)



    country1 = relationship('Country')





class Court( PlaceMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'court'



    id = Column(Integer, primary_key=True, server_default=text("nextval('court_id_seq'::regclass)"))

    court_rank = Column(ForeignKey('courtrank.id'), nullable=True, index=True)

    court_station = Column(ForeignKey('courtstation.id'), nullable=True, index=True)

    town = Column(ForeignKey('town.id'), nullable=True, index=True)

    till_number = Column(Text, nullable=True)



    courtrank = relationship('Courtrank')

    courtstation = relationship('Courtstation')

    town1 = relationship('Town')

    judicialofficer = relationship('Judicialofficer', secondary='t_court_judicialofficer')





t_court_judicialofficer = Table(

    'court_judicialofficer', metadata,

    Column('court', ForeignKey('court.id'), primary_key=True, nullable=True),

    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)





class Courtaccount( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'courtaccount'



    courts = Column(ForeignKey('court.id'), primary_key=True, nullable=True)

    account__types = Column(ForeignKey('accounttype.id'), primary_key=True, nullable=True, index=True)

    account_number = Column(Text, nullable=True)

    account_name = Column(Text, nullable=True)

    short_code = Column(Text, nullable=True)

    bank_name = Column(Text, nullable=True)



    accounttype = relationship('Accounttype')

    court = relationship('Court')





class Courtcase( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'courtcase'



    id = Column(Integer, primary_key=True, server_default=text("nextval('courtcase_id_seq'::regclass)"))

    docket_number = Column(Text, nullable=True)

    case_number = Column(Text, nullable=True)

    adr = Column(Boolean)

    mediation_proposal = Column(Text, nullable=True)

    case_received_date = Column(Date)

    case_filed_date = Column(Date)

    case_summary = Column(Text, nullable=True)

    filing_prosecutor = Column(ForeignKey('prosecutor.id'), index=True)

    fast_track = Column(Boolean)

    priority = Column(Integer)

    object_of_litigation = Column(Text, nullable=True)

    grounds = Column(Text, nullable=True)

    prosecution_prayer = Column(Text, nullable=True)

    pretrial_date = Column(Date)

    pretrial_notes = Column(Text, nullable=True)

    pretrial_registrar = Column(ForeignKey('judicialofficer.id'), index=True)

    case_admissible = Column(Boolean)

    indictment_date = Column(Text, nullable=True)

    judgement = Column(Text, nullable=True)

    judgement_docx = Column(Text, nullable=True)

    case_link_type = Column(ForeignKey('caselinktype.id'), index=True)

    linked_cases = Column(ForeignKey('courtcase.id'), index=True)

    appealed = Column(Boolean)

    appeal_number = Column(Text, nullable=True)

    inventory_of_docket = Column(Text, nullable=True)

    next_hearing_date = Column(Date)

    interlocutory_judgement = Column(Text, nullable=True)

    reopen = Column(Boolean)

    reopen_reason = Column(Text, nullable=True)

    combined_case = Column(Boolean)

    value_in_dispute = Column(Numeric(12, 2))

    award = Column(Numeric(12, 2))

    govt_liability = Column(Text, nullable=True)

    active = Column(Boolean)

    active_date = Column(DateTime)



    caselinktype = relationship('Caselinktype')

    prosecutor = relationship('Prosecutor')

    parent = relationship('Courtcase', remote_side=[id])

    judicialofficer = relationship('Judicialofficer')

    judicialofficer1 = relationship('Judicialofficer', secondary='t_courtcase_judicialofficer')

    lawfirm = relationship('Lawfirm', secondary='t_courtcase_lawfirm')





t_courtcase_judicialofficer = Table(

    'courtcase_judicialofficer', metadata,

    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=True),

    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)





t_courtcase_lawfirm = Table(

    'courtcase_lawfirm', metadata,

    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=True),

    Column('lawfirm', ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)





class Courtrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'courtrank'



    id = Column(Integer, primary_key=True, server_default=text("nextval('courtrank_id_seq'::regclass)"))





class Courtstation( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'courtstation'



    id = Column(Integer, primary_key=True, server_default=text("nextval('courtstation_id_seq'::regclass)"))

    till_number = Column(Text, nullable=True)

    pay_bill = Column(Text, nullable=True)





class Crime( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'crime'



    id = Column(Integer, primary_key=True, server_default=text("nextval('crime_id_seq'::regclass)"))

    law = Column(Text, nullable=True)

    description = Column(Text, nullable=True)

    ref = Column(Text, nullable=True)

    ref_law = Column(ForeignKey('law.id'), index=True)



    law1 = relationship('Law')





class CsiEquipment( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'csi_equipment'



    id = Column(Integer, primary_key=True, server_default=text("nextval('csi_equipment_id_seq'::regclass)"))



    investigationdiary = relationship('Investigationdiary', secondary='t_csi_equipment_investigationdiary')





t_csi_equipment_investigationdiary = Table(

    'csi_equipment_investigationdiary', metadata,

    Column('csi_equipment', ForeignKey('csi_equipment.id'), primary_key=True, nullable=True),

    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=True, index=True)

)





class Diagram( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'diagram'



    id = Column(Integer, primary_key=True, server_default=text("nextval('diagram_id_seq'::regclass)"))

    investigation_diary = Column(ForeignKey('investigationdiary.id'), nullable=True, index=True)

    image = Column(Text, nullable=True)

    description = Column(Text, nullable=True)

    docx = Column(Text, nullable=True)



    investigationdiary = relationship('Investigationdiary')





class Discipline( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'discipline'



    id = Column(Integer, primary_key=True, server_default=text("nextval('discipline_id_seq'::regclass)"))

    party = Column(ForeignKey('party.complaints'), nullable=True, index=True)

    prison_officer = Column(ForeignKey('prisonofficer.id'), nullable=True, index=True)



    party1 = relationship('Party')

    prisonofficer = relationship('Prisonofficer')





class Doctemplate( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'doctemplate'



    id = Column(Integer, primary_key=True, server_default=text("nextval('doctemplate_id_seq'::regclass)"))

    template = Column(Text, nullable=True)

    docx = Column(Text, nullable=True)

    name = Column(Text, nullable=True)

    title = Column(Text, nullable=True)

    summary = Column(Text, nullable=True)

    template_type = Column(ForeignKey('templatetype.id'), nullable=True, index=True)

    icon = Column(Text, nullable=True)



    templatetype = relationship('Templatetype')





class Document( DocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'document'



    id = Column(Integer, primary_key=True, server_default=text("nextval('document_id_seq'::regclass)"))

    name = Column(Text, nullable=True)

    court_case = Column(ForeignKey('courtcase.id'), index=True)

    issue = Column(ForeignKey('issue.id'), index=True)

    document_admissibility = Column(Text, nullable=True)

    admitted = Column(Boolean)

    judicial_officer = Column(ForeignKey('judicialofficer.id'), index=True)

    filing_date = Column(DateTime)

    admisibility_notes = Column(Text, nullable=True)

    docx = Column(Text, nullable=True)

    document_text = Column(Text, nullable=True)

    published = Column(Boolean)

    publish_newspaper = Column(Text, nullable=True)

    publish_date = Column(Date)

    validated = Column(Boolean)

    paid = Column(Boolean)

    page_count = Column(Integer)

    file_byte_count = Column(Numeric(12, 2))

    file_hash = Column(Text, nullable=True)

    file_timestamp = Column(Text, nullable=True)

    file_create_date = Column(DateTime)

    file_update_date = Column(DateTime)

    file_text = Column(Text, nullable=True)

    file_name = Column(Text, nullable=True)

    file_ext = Column(Text, nullable=True)

    file_load_path = Column(Text, nullable=True)

    file_upload_date = Column(DateTime)

    file_parse_status = Column(Text, nullable=True)

    doc_template = Column(ForeignKey('doctemplate.id'), index=True)

    visible = Column(Boolean)

    is_scan = Column(Boolean)

    doc_shelf = Column(Text, nullable=True)

    doc_row = Column(Text, nullable=True)

    doc_room = Column(Text, nullable=True)

    doc_placed_by = Column(Text, nullable=True)

    citation = Column(Text, nullable=True)



    courtcase = relationship('Courtcase')

    doctemplate = relationship('Doctemplate')

    issue1 = relationship('Issue')

    judicialofficer = relationship('Judicialofficer')

    documenttype = relationship('Documenttype', secondary='t_document_documenttype')





t_document_documenttype = Table(

    'document_documenttype', metadata,

    Column('document', ForeignKey('document.id'), primary_key=True, nullable=True),

    Column('documenttype', ForeignKey('documenttype.id'), primary_key=True, nullable=True, index=True)

)





class Documenttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'documenttype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('documenttype_id_seq'::regclass)"))





class Economicclas( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'economicclass'



    id = Column(Integer, primary_key=True, server_default=text("nextval('economicclass_id_seq'::regclass)"))

    name = Column(String(50), nullable=True)

    description = Column(String(100), nullable=True)





class Exhibit( DocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'exhibit'



    id = Column(Integer, primary_key=True, server_default=text("nextval('exhibit_id_seq'::regclass)"))

    investigation_entry = Column(ForeignKey('investigationdiary.id'), nullable=True, index=True)

    photo = Column(Text, nullable=True)

    exhibit_no = Column(Text, nullable=True)

    docx = Column(Text, nullable=True)

    seizure = Column(ForeignKey('seizure.id'), nullable=True, index=True)



    investigationdiary = relationship('Investigationdiary')

    seizure1 = relationship('Seizure')





class Expert( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'expert'



    id = Column(Integer, primary_key=True, server_default=text("nextval('expert_id_seq'::regclass)"))

    institution = Column(Text, nullable=True)

    jobtitle = Column(Text, nullable=True)

    credentials = Column(Text, nullable=True)



    experttype = relationship('Experttype', secondary='t_expert_experttype')





t_expert_experttype = Table(

    'expert_experttype', metadata,

    Column('expert', ForeignKey('expert.id'), primary_key=True, nullable=True),

    Column('experttype', ForeignKey('experttype.id'), primary_key=True, nullable=True, index=True)

)





class Experttestimony( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'experttestimony'



    requesting_officer = Column(ForeignKey('investigating_officer.police_officers'), nullable=True, index=True)

    investigation_entries = Column(ForeignKey('investigationdiary.id'), primary_key=True, nullable=True)

    experts = Column(ForeignKey('expert.id'), primary_key=True, nullable=True, index=True)

    task_given = Column(Text, nullable=True)

    summary_of_facts = Column(Text, nullable=True)

    statement = Column(Text, nullable=True)

    testimony_date = Column(DateTime)

    task_request_date = Column(Date)

    docx = Column(Text, nullable=True)

    validated = Column(Boolean)



    expert = relationship('Expert')

    investigationdiary = relationship('Investigationdiary')

    investigating_officer = relationship('InvestigatingOfficer')





class Experttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'experttype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('experttype_id_seq'::regclass)"))





class Feeclas( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'feeclass'



    id = Column(Integer, primary_key=True, server_default=text("nextval('feeclass_id_seq'::regclass)"))

    fee_type = Column(ForeignKey('feeclass.id'), index=True)



    parent = relationship('Feeclas', remote_side=[id])





class Feetype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'feetype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('feetype_id_seq'::regclass)"))

    filing_fee_type = Column(ForeignKey('feeclass.id'), nullable=True, index=True)

    amount = Column(Numeric(12, 2))

    unit = Column(Text, nullable=True)

    min_fee = Column(Numeric(12, 2))

    max_fee = Column(Numeric(12, 2))

    description = Column(Text)

    guide_sec = Column(Text)

    guide_clause = Column(Text)

    account_type = Column(ForeignKey('accounttype.id'), nullable=True, index=True)



    accounttype = relationship('Accounttype')

    feeclas = relationship('Feeclas')





class Healthevent( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'healthevent'



    id = Column(Integer, primary_key=True, server_default=text("nextval('healthevent_id_seq'::regclass)"))

    party = Column(ForeignKey('party.complaints'), nullable=True, index=True)

    reporting_prison_officer = Column(ForeignKey('prisonofficer.id'), index=True)

    health_event_type = Column(ForeignKey('healtheventtype.id'), nullable=True, index=True)

    startdate = Column(DateTime)

    enddate = Column(DateTime)

    notes = Column(Text, nullable=True)



    healtheventtype = relationship('Healtheventtype')

    party1 = relationship('Party')

    prisonofficer = relationship('Prisonofficer')





class Healtheventtype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'healtheventtype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('healtheventtype_id_seq'::regclass)"))





class Hearing( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'hearing'



    id = Column(Integer, primary_key=True, server_default=text("nextval('hearing_id_seq'::regclass)"))

    court_cases = Column(ForeignKey('courtcase.id'), index=True)

    hearing_type = Column(ForeignKey('hearingtype.id'), nullable=True, index=True)

    schedule_status = Column(ForeignKey('schedulestatustype.id'), nullable=True, index=True)

    hearing_date = Column(Date)

    reason = Column(Text, nullable=True)

    sequence = Column(BigInteger)

    yearday = Column(BigInteger)

    starttime = Column(Time)

    endtime = Column(Time)

    notes = Column(Text, nullable=True)

    completed = Column(Boolean)

    adjourned_to = Column(Date)

    adjournment_reason = Column(Text, nullable=True)

    transcript = Column(Text, nullable=True)

    atendance = Column(Text, nullable=True)

    next_hearing_date = Column(Date)

    postponement_reason = Column(Text, nullable=True)



    courtcase = relationship('Courtcase')

    hearingtype = relationship('Hearingtype')

    schedulestatustype = relationship('Schedulestatustype')

    issue = relationship('Issue', secondary='t_hearing_issue')

    judicialofficer = relationship('Judicialofficer', secondary='t_hearing_judicialofficer')

    lawfirm = relationship('Lawfirm', secondary='t_hearing_lawfirm')

    lawfirm1 = relationship('Lawfirm', secondary='t_hearing_lawfirm_2')





t_hearing_issue = Table(

    'hearing_issue', metadata,

    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=True),

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True, index=True)

)





t_hearing_judicialofficer = Table(

    'hearing_judicialofficer', metadata,

    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=True),

    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)





t_hearing_lawfirm = Table(

    'hearing_lawfirm', metadata,

    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=True),

    Column('lawfirm', ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)





t_hearing_lawfirm_2 = Table(

    'hearing_lawfirm_2', metadata,

    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=True),

    Column('lawfirm', ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)





class Hearingtype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'hearingtype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('hearingtype_id_seq'::regclass)"))

    hearing_type = Column(ForeignKey('hearingtype.id'), index=True)



    parent = relationship('Hearingtype', remote_side=[id])





class Instancecrime( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'instancecrime'



    parties = Column(ForeignKey('party.complaints'), primary_key=True, nullable=True)

    crimes = Column(ForeignKey('crime.id'), primary_key=True, nullable=True, index=True)

    crime_detail = Column(Text, nullable=True)

    tffender_type = Column(Text, nullable=True)

    crime_date = Column(DateTime)

    date_note = Column(Text, nullable=True)

    place_of_crime = Column(Text, nullable=True)

    place_note = Column(Text, nullable=True)



    crime = relationship('Crime')

    party = relationship('Party')

    issue = relationship('Issue', secondary='t_instancecrime_issue')





t_instancecrime_issue = Table(

    'instancecrime_issue', metadata,

    Column('instancecrime_parties', Integer, primary_key=True, nullable=True),

    Column('instancecrime_crimes', Integer, primary_key=True, nullable=True),

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True, index=True),

    ForeignKeyConstraint(['instancecrime_parties', 'instancecrime_crimes'], ['instancecrime.parties', 'instancecrime.crimes'])

)





class Interview( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'interview'



    id = Column(Integer, primary_key=True, server_default=text("nextval('interview_id_seq'::regclass)"))

    investigation_entry = Column(ForeignKey('investigationdiary.id'), nullable=True, index=True)

    question = Column(Text, nullable=True)

    answer = Column(Text, nullable=True)

    validated = Column(Boolean)

    language = Column(Text, nullable=True)



    investigationdiary = relationship('Investigationdiary')





t_investigating_officer_investigationdiary = Table(

    'investigating_officer_investigationdiary', metadata,

    Column('investigating_officer', ForeignKey('investigating_officer.police_officers'), primary_key=True, nullable=True),

    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=True, index=True)

)





class Investigationdiary( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'investigationdiary'



    id = Column(Integer, primary_key=True, server_default=text("nextval('investigationdiary_id_seq'::regclass)"))

    complaint = Column(ForeignKey('complaint.id'), nullable=True, index=True)

    activity = Column(Text, nullable=True)

    location = Column(Text, nullable=True)

    outcome = Column(Text, nullable=True)

    equipmentresults = Column(Text, nullable=True)

    startdate = Column(DateTime, nullable=True)

    enddate = Column(DateTime)

    advocate_present = Column(Text, nullable=True)

    summons_statement = Column(Text, nullable=True)

    arrest_statement = Column(Text, nullable=True)

    arrest_warrant = Column(Text, nullable=True)

    search_seizure_statement = Column(Text, nullable=True)

    docx = Column(Text, nullable=True)

    detained = Column(Text, nullable=True)

    detained_at = Column(Text, nullable=True)

    provisional_release_statement = Column(Text, nullable=True)

    warrant_type = Column(ForeignKey('warranttype.id'), index=True)

    warrant_issued_by = Column(Text, nullable=True)

    warrant_issue_date = Column(Date)

    warrant_delivered_by = Column(Text, nullable=True)

    warrant_received_by = Column(Text, nullable=True)

    warrant_serve_date = Column(Text, nullable=True)

    warrant_docx = Column(Text, nullable=True)

    warrant_upload_date = Column(Text, nullable=True)



    complaint1 = relationship('Complaint')

    warranttype = relationship('Warranttype')

    party = relationship('Party', secondary='t_investigationdiary_party')

    vehicle = relationship('Vehicle', secondary='t_investigationdiary_vehicle')





t_investigationdiary_party = Table(

    'investigationdiary_party', metadata,

    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)





t_investigationdiary_vehicle = Table(

    'investigationdiary_vehicle', metadata,

    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

    Column('vehicle', ForeignKey('vehicle.id'), primary_key=True, nullable=True, index=True)

)





class Issue( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'issue'



    id = Column(Integer, primary_key=True, server_default=text("nextval('issue_id_seq'::regclass)"))

    issue = Column(Text, nullable=True)

    facts = Column(Text)

    counter_claim = Column(Boolean)

    argument = Column(Text, nullable=True)

    argument_date = Column(Date)

    argument_docx = Column(Text)

    rebuttal = Column(Text, nullable=True)

    rebuttal_date = Column(Date)

    rebuttal_docx = Column(Text)

    hearing_date = Column(Date)

    determination = Column(Text, nullable=True)

    dtermination_date = Column(Date)

    determination_docx = Column(Text, nullable=True)

    resolved = Column(Boolean)

    defense_lawyer = Column(ForeignKey('lawyer.id'), nullable=True, index=True)

    prosecutor = Column(ForeignKey('prosecutor.id'), index=True)

    judicial_officer = Column(ForeignKey('judicialofficer.id'), nullable=True, index=True)

    court_case = Column(ForeignKey('courtcase.id'), nullable=True, index=True)

    tasks = Column(Text, nullable=True)

    is_criminal = Column(Boolean)

    moral_element = Column(Text, nullable=True)

    material_element = Column(Text, nullable=True)

    legal_element = Column(Text, nullable=True)

    debt_amount = Column(Numeric(12, 2))



    courtcase = relationship('Courtcase')

    lawyer = relationship('Lawyer')

    judicialofficer = relationship('Judicialofficer')

    prosecutor1 = relationship('Prosecutor')

    lawyer1 = relationship('Lawyer', secondary='t_issue_lawyer')

    legalreference = relationship('Legalreference', secondary='t_issue_legalreference')

    legalreference1 = relationship('Legalreference', secondary='t_issue_legalreference_2')

    party = relationship('Party', secondary='t_issue_party')

    party1 = relationship('Party', secondary='t_issue_party_2')





t_issue_lawyer = Table(

    'issue_lawyer', metadata,

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True),

    Column('lawyer', ForeignKey('lawyer.id'), primary_key=True, nullable=True, index=True)

)





t_issue_legalreference = Table(

    'issue_legalreference', metadata,

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True),

    Column('legalreference', ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)

)





t_issue_legalreference_2 = Table(

    'issue_legalreference_2', metadata,

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True),

    Column('legalreference', ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)

)





t_issue_party = Table(

    'issue_party', metadata,

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True),

    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)





t_issue_party_2 = Table(

    'issue_party_2', metadata,

    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=True),

    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)





class Judicialofficer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'judicialofficer'



    id = Column(Integer, primary_key=True, server_default=text("nextval('judicialofficer_id_seq'::regclass)"))

    rank = Column(ForeignKey('judicialrank.id'), nullable=True, index=True)

    judicial_role = Column(ForeignKey('judicialrole.id'), nullable=True, index=True)

    court_station = Column(ForeignKey('courtstation.id'), nullable=True, index=True)



    courtstation = relationship('Courtstation')

    judicialrole = relationship('Judicialrole')

    judicialrank = relationship('Judicialrank')





class Judicialrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'judicialrank'



    id = Column(Integer, primary_key=True, server_default=text("nextval('judicialrank_id_seq'::regclass)"))





class Judicialrole( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'judicialrole'



    id = Column(Integer, primary_key=True, server_default=text("nextval('judicialrole_id_seq'::regclass)"))





class Law( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'law'



    id = Column(Integer, primary_key=True, server_default=text("nextval('law_id_seq'::regclass)"))

    name = Column(Text, nullable=True)

    description = Column(Text, nullable=True)





class Lawfirm( PlaceMixin,  RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'lawfirm'



    id = Column(Integer, primary_key=True, server_default=text("nextval('lawfirm_id_seq'::regclass)"))





class Lawyer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'lawyer'



    id = Column(Integer, primary_key=True, server_default=text("nextval('lawyer_id_seq'::regclass)"))

    law_firm = Column(ForeignKey('lawfirm.id'), index=True)

    bar_no = Column(Text, nullable=True)

    bar_date = Column(Date)



    lawfirm = relationship('Lawfirm')

    party = relationship('Party', secondary='t_lawyer_party')





t_lawyer_party = Table(

    'lawyer_party', metadata,

    Column('lawyer', ForeignKey('lawyer.id'), primary_key=True, nullable=True),

    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)





class Legalreference( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'legalreference'



    id = Column(Integer, primary_key=True, server_default=text("nextval('legalreference_id_seq'::regclass)"))

    ref = Column(Text, nullable=True)

    verbatim = Column(Text, nullable=True)

    public = Column(Boolean)

    commentary = Column(Text, nullable=True)

    validated = Column(Boolean)

    citation = Column(Text, nullable=True)

    quote = Column(Text, nullable=True)

    interpretation = Column(Text, nullable=True)





class Nextofkin( PersonMixin,  PersonDocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'nextofkin'



    id = Column(Integer, primary_key=True, server_default=text("nextval('nextofkin_id_seq'::regclass)"))

    biodata = Column(ForeignKey('biodata.id'), nullable=True, index=True)

    childunder4 = Column(Boolean)



    biodatum = relationship('Biodatum')





class Notification( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'notification'



    id = Column(Integer, primary_key=True, server_default=text("nextval('notification_id_seq'::regclass)"))

    contact = Column(Text, nullable=True)

    message = Column(Text, nullable=True)

    confirmation = Column(Text, nullable=True)

    notification_register = Column(ForeignKey('notificationregister.id'), index=True)

    add_date = Column(DateTime)

    send_date = Column(DateTime)

    sent = Column(Boolean)

    delivered = Column(Boolean)

    retries = Column(Integer)

    abandon = Column(Boolean)

    retry_count = Column(Integer)



    notificationregister = relationship('Notificationregister')





class Notificationregister( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'notificationregister'



    id = Column(Integer, primary_key=True, server_default=text("nextval('notificationregister_id_seq'::regclass)"))

    notification_type = Column(ForeignKey('notificationtype.id'), nullable=True, index=True)

    contact = Column(Text, nullable=True)

    notify_event = Column(ForeignKey('notifyevent.id'), index=True)

    retry_count = Column(BigInteger)

    active = Column(Boolean)

    hearing = Column(ForeignKey('hearing.id'), index=True)

    document = Column(ForeignKey('document.id'), index=True)

    court_case = Column(ForeignKey('courtcase.id'), index=True)

    complaint = Column(ForeignKey('complaint.id'), index=True)

    complaint_category = Column(ForeignKey('complaintcategory.id'), index=True)

    health_event = Column(ForeignKey('healthevent.id'), index=True)

    party = Column(ForeignKey('party.complaints'), index=True)



    complaint1 = relationship('Complaint')

    complaintcategory = relationship('Complaintcategory')

    courtcase = relationship('Courtcase')

    document1 = relationship('Document')

    healthevent = relationship('Healthevent')

    hearing1 = relationship('Hearing')

    notificationtype = relationship('Notificationtype')

    notifyevent = relationship('Notifyevent')

    party1 = relationship('Party')





class Notificationtype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'notificationtype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('notificationtype_id_seq'::regclass)"))

    name = Column(Text, nullable=True)

    description = Column(Text, nullable=True)





class Notifyevent( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'notifyevent'



    id = Column(Integer, primary_key=True, server_default=text("nextval('notifyevent_id_seq'::regclass)"))





class Page( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'page'



    id = Column(Integer, primary_key=True, server_default=text("nextval('page_id_seq'::regclass)"))

    document = Column(ForeignKey('document.id'), nullable=True, index=True)

    page_image = Column(LargeBinary)

    page_no = Column(BigInteger)

    page_text = Column(Text, nullable=True)

    image_ext = Column(Text)

    image_width = Column(Text)

    image_height = Column(Text)

    create_date = Column(DateTime)

    update_date = Column(DateTime)

    upload_dt = Column(DateTime)



    document1 = relationship('Document')





t_party_settlement = Table(

    'party_settlement', metadata,

    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=True),

    Column('settlement', ForeignKey('settlement.id'), primary_key=True, nullable=True, index=True)

)





class Partytype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'partytype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('partytype_id_seq'::regclass)"))





class Payment( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'payment'



    id = Column(Integer, primary_key=True, server_default=text("nextval('payment_id_seq'::regclass)"))

    bill = Column(ForeignKey('bill.id'), nullable=True, index=True)

    amount = Column(Numeric(12, 2))

    payment_ref = Column(Text, nullable=True)

    date_paid = Column(DateTime)

    phone_number = Column(String(20))

    validated = Column(Boolean)

    payment_description = Column(Text)



    bill1 = relationship('Bill')





class Personaleffect( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'personaleffect'



    id = Column(Integer, primary_key=True, server_default=text("nextval('personaleffect_id_seq'::regclass)"))

    party = Column(ForeignKey('party.complaints'), nullable=True, index=True)

    personal_effects_category = Column(ForeignKey('personaleffectscategory.id'), nullable=True, index=True)



    party1 = relationship('Party')

    personaleffectscategory = relationship('Personaleffectscategory')





class Personaleffectscategory( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'personaleffectscategory'



    id = Column(Integer, primary_key=True, server_default=text("nextval('personaleffectscategory_id_seq'::regclass)"))





class Policeofficer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'policeofficer'



    id = Column(Integer, primary_key=True, server_default=text("nextval('policeofficer_id_seq'::regclass)"))

    police_rank = Column(ForeignKey('policeofficerrank.id'), nullable=True, index=True)

    servicenumber = Column(String(100), nullable=True, unique=True)



    policeofficerrank = relationship('Policeofficerrank')

    policestation = relationship('Policestation', secondary='t_policeofficer_policestation')





class InvestigatingOfficer( AuditMixin, AllFeaturesMixin, Policeofficer):

    __tablename__ = 'investigating_officer'



    police_officers = Column(ForeignKey('policeofficer.id'), primary_key=True)

    date_assigned = Column(DateTime)

    lead_investigator = Column(Integer)



    investigationdiary = relationship('Investigationdiary', secondary='t_investigating_officer_investigationdiary')





t_policeofficer_policestation = Table(

    'policeofficer_policestation', metadata,

    Column('policeofficer', ForeignKey('policeofficer.id'), primary_key=True, nullable=True),

    Column('policestation', ForeignKey('policestation.id'), primary_key=True, nullable=True, index=True)

)





class Policeofficerrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'policeofficerrank'



    id = Column(Integer, primary_key=True, server_default=text("nextval('policeofficerrank_id_seq'::regclass)"))

    name = Column(Text, nullable=True)

    description = Column(Text, nullable=True)

    sequence = Column(Integer)





class Policestation( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'policestation'



    id = Column(Integer, primary_key=True, server_default=text("nextval('policestation_id_seq'::regclass)"))

    town = Column(ForeignKey('town.id'), index=True)

    officer_commanding = Column(ForeignKey('policeofficer.id'), nullable=True, index=True)

    police_station_rank = Column(ForeignKey('policestationrank.id'), nullable=True, index=True)



    policeofficer = relationship('Policeofficer')

    policestationrank = relationship('Policestationrank')

    town1 = relationship('Town')





class Policestationrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'policestationrank'



    id = Column(Integer, primary_key=True, server_default=text("nextval('policestationrank_id_seq'::regclass)"))





class Prison( PlaceMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'prison'



    id = Column(Integer, primary_key=True, server_default=text("nextval('prison_id_seq'::regclass)"))

    town = Column(ForeignKey('town.id'), nullable=True, index=True)



    town1 = relationship('Town')





class Prisonofficer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'prisonofficer'



    id = Column(Integer, primary_key=True, server_default=text("nextval('prisonofficer_id_seq'::regclass)"))

    prison = Column(ForeignKey('prison.id'), nullable=True, index=True)

    prison_officer_rank = Column(ForeignKey('prisonofficerrank.id'), nullable=True, index=True)



    prison1 = relationship('Prison')

    prisonofficerrank = relationship('Prisonofficerrank')





class Prisonofficerrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'prisonofficerrank'



    id = Column(Integer, primary_key=True, server_default=text("nextval('prisonofficerrank_id_seq'::regclass)"))





class Prosecutor( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'prosecutor'



    id = Column(Integer, primary_key=True, server_default=text("nextval('prosecutor_id_seq'::regclass)"))

    prosecutor_team = Column(ForeignKey('prosecutorteam.id'), index=True)

    lawyer = Column(ForeignKey('lawyer.id'), nullable=True, index=True)



    lawyer1 = relationship('Lawyer')

    prosecutorteam = relationship('Prosecutorteam')





class Prosecutorteam( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'prosecutorteam'



    id = Column(Integer, primary_key=True, server_default=text("nextval('prosecutorteam_id_seq'::regclass)"))





class Releasetype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'releasetype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('releasetype_id_seq'::regclass)"))





class Religion( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'religion'



    id = Column(Integer, primary_key=True, server_default=text("nextval('religion_id_seq'::regclass)"))





class Schedulestatustype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'schedulestatustype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('schedulestatustype_id_seq'::regclass)"))





class Seizure( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'seizure'



    id = Column(Integer, primary_key=True, server_default=text("nextval('seizure_id_seq'::regclass)"))

    investigation_diary = Column(ForeignKey('investigationdiary.id'), nullable=True, index=True)

    owner = Column(Text, nullable=True)

    item = Column(Text, nullable=True)

    item_packaging = Column(Text, nullable=True)

    item_pic = Column(Text, nullable=True)

    premises = Column(Text, nullable=True)

    reg_no = Column(Text, nullable=True)

    witness = Column(Text, nullable=True)

    notes = Column(Text, nullable=True)

    docx = Column(Text, nullable=True)

    item_description = Column(Text, nullable=True)

    returned = Column(Boolean)

    return_date = Column(DateTime)

    return_notes = Column(Text, nullable=True)

    return_signed_receipt = Column(Text, nullable=True)

    destroyed = Column(Boolean)

    destruction_date = Column(Date)

    destruction_witnesses = Column(Text, nullable=True)

    destruction_notes = Column(Text, nullable=True)

    disposed = Column(Boolean)

    sold_to = Column(Text, nullable=True)

    disposal_date = Column(Date)

    disposal_price = Column(Numeric(12, 2))

    disposal_receipt = Column(Text, nullable=True)

    recovery_town = Column(ForeignKey('town.id'), index=True)

    destruction_pic = Column(Text, nullable=True)

    is_evidence = Column(Boolean)

    immovable = Column(Boolean)



    investigationdiary = relationship('Investigationdiary')

    town = relationship('Town')





class Settlement( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'settlement'



    id = Column(Integer, primary_key=True, server_default=text("nextval('settlement_id_seq'::regclass)"))

    complaint = Column(ForeignKey('complaint.id'), nullable=True, index=True)

    terms = Column(Text, nullable=True)

    amount = Column(Numeric(12, 2))

    paid = Column(Boolean)

    docx = Column(Text, nullable=True)

    settlor = Column(ForeignKey('party.complaints'), nullable=True, index=True)



    complaint1 = relationship('Complaint')

    party = relationship('Party')





class Subcounty( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'subcounty'



    id = Column(Integer, primary_key=True, server_default=text("nextval('subcounty_id_seq'::regclass)"))

    county = Column(ForeignKey('county.id'), nullable=True, index=True)



    county1 = relationship('County')





class Templatetype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'templatetype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('templatetype_id_seq'::regclass)"))

    template_type = Column(ForeignKey('templatetype.id'), index=True)



    parent = relationship('Templatetype', remote_side=[id])





class Town( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'town'



    id = Column(Integer, primary_key=True, server_default=text("nextval('town_id_seq'::regclass)"))



    ward = relationship('Ward', secondary='t_town_ward')





t_town_ward = Table(

    'town_ward', metadata,

    Column('town', ForeignKey('town.id'), primary_key=True, nullable=True),

    Column('ward', ForeignKey('ward.id'), primary_key=True, nullable=True, index=True)

)





class Transcript( DocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'transcript'



    id = Column(Integer, primary_key=True, server_default=text("nextval('transcript_id_seq'::regclass)"))

    video = Column(Text, nullable=True)

    audio = Column(Text, nullable=True)

    add_date = Column(DateTime)

    asr_transcript = Column(Text, nullable=True)

    asr_date = Column(DateTime)

    edited_transcript = Column(Text, nullable=True)

    edit_date = Column(DateTime)

    certified_transcript = Column(Text, nullable=True)

    certfiy_date = Column(DateTime)

    locked = Column(Boolean)

    hearing = Column(ForeignKey('hearing.id'), nullable=True, index=True)



    hearing1 = relationship('Hearing')





class Vehicle( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'vehicle'



    id = Column(Integer, primary_key=True, server_default=text("nextval('vehicle_id_seq'::regclass)"))

    police_station = Column(ForeignKey('policestation.id'), nullable=True, index=True)

    make = Column(String(100), nullable=True)

    model = Column(String(100), nullable=True)

    regno = Column(String(100), nullable=True)



    policestation = relationship('Policestation')





class Ward( AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'ward'



    id = Column(Integer, primary_key=True, server_default=text("nextval('ward_id_seq'::regclass)"))

    subcounty = Column(ForeignKey('subcounty.id'), nullable=True, index=True)



    subcounty1 = relationship('Subcounty')





class Warranttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __tablename__ = 'warranttype'



    id = Column(Integer, primary_key=True, server_default=text("nextval('warranttype_id_seq'::regclass)"))


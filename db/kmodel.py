# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import INTERVAL
from flask_sqlalchemy import SQLAlchemy


#db = SQLAlchemy()


class Accounttype(db.Model):
    __tablename__ = 'accounttype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Bill(db.Model):
    __tablename__ = 'bill'
    __table_args__ = (
        db.ForeignKeyConstraint(['court_account_courts', 'court_account_account__types'], ['courtaccount.courts', 'courtaccount.account__types']),
        db.Index('idx_bill__court_account_courts_court_account_account__types', 'court_account_courts', 'court_account_account__types')
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    assessing_registrar = db.Column(db.ForeignKey('judicialofficer.id'), nullable=False, index=True)
    receiving_registrar = db.Column(db.ForeignKey('judicialofficer.id'), nullable=False, index=True)
    lawyer_paying = db.Column(db.ForeignKey('lawyer.id'), index=True)
    party_paying = db.Column(db.ForeignKey('party.complaints'), index=True)
    documents = db.Column(db.ForeignKey('document.id'), index=True)
    date_of_payment = db.Column(db.Text, nullable=False)
    paid = db.Column(db.Boolean)
    pay_code = db.Column(db.String(20), unique=True)
    bill_total = db.Column(db.Numeric(12, 2))
    court = db.Column(db.ForeignKey('court.id'), nullable=False, index=True)
    court_account_courts = db.Column(db.Integer, nullable=False)
    court_account_account__types = db.Column(db.Integer, nullable=False)
    validated = db.Column(db.Boolean)
    validation_date = db.Column(db.DateTime)

    judicialofficer = db.relationship('Judicialofficer', primaryjoin='Bill.assessing_registrar == Judicialofficer.id', backref='judicialofficer_bills')
    court1 = db.relationship('Court', primaryjoin='Bill.court == Court.id', backref='bills')
    courtaccount = db.relationship('Courtaccount', primaryjoin='and_(Bill.court_account_courts == Courtaccount.courts, Bill.court_account_account__types == Courtaccount.account__types)', backref='bills')
    document = db.relationship('Document', primaryjoin='Bill.documents == Document.id', backref='bills')
    lawyer = db.relationship('Lawyer', primaryjoin='Bill.lawyer_paying == Lawyer.id', backref='bills')
    party = db.relationship('Party', primaryjoin='Bill.party_paying == Party.complaints', backref='bills')
    judicialofficer1 = db.relationship('Judicialofficer', primaryjoin='Bill.receiving_registrar == Judicialofficer.id', backref='judicialofficer_bills_0')


class Billdetail(db.Model):
    __tablename__ = 'billdetail'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    receipt_id = db.Column(db.ForeignKey('bill.id'), nullable=False, index=True)
    feetype = db.Column(db.ForeignKey('feetype.id'), nullable=False, index=True)
    purpose = db.Column(db.Text, nullable=False)
    unit = db.Column(db.Text)
    qty = db.Column(db.Integer)
    unit_cost = db.Column(db.Numeric(12, 2))
    amount = db.Column(db.Numeric(12, 2))

    feetype1 = db.relationship('Feetype', primaryjoin='Billdetail.feetype == Feetype.id', backref='billdetails')
    receipt = db.relationship('Bill', primaryjoin='Billdetail.receipt_id == Bill.id', backref='billdetails')


class Biodatum(db.Model):
    __tablename__ = 'biodata'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    economic_class = db.Column(db.ForeignKey('economicclass.id'), index=True)
    religion = db.Column(db.ForeignKey('religion.id'), index=True)
    photo = db.Column(db.LargeBinary)
    health_status = db.Column(db.Text, nullable=False)

    economicclas = db.relationship('Economicclas', primaryjoin='Biodatum.economic_class == Economicclas.id', backref='biodata')
    religion1 = db.relationship('Religion', primaryjoin='Biodatum.religion == Religion.id', backref='biodata')


class Casecategory(db.Model):
    __tablename__ = 'casecategory'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subcategory = db.Column(db.ForeignKey('casecategory.id'), index=True)

    parent = db.relationship('Casecategory', remote_side=[id], primaryjoin='Casecategory.subcategory == Casecategory.id', backref='casecategories')
    casechecklist = db.relationship('Casechecklist', secondary='casecategorychecklist', backref='casecategories')
    courtcase = db.relationship('Courtcase', secondary='casecategory_courtcase', backref='casecategories')


casecategory_courtcase = db.Table(
    'casecategory_courtcase', Model.metadata, 
    db.Column('casecategory', db.ForeignKey('casecategory.id'), primary_key=True, nullable=False),
    db.Column('courtcase', db.ForeignKey('courtcase.id'), primary_key=True, nullable=False, index=True)
)


casecategorychecklist = db.Table(
    'casecategorychecklist', Model.metadata, 
    db.Column('case_checklists', db.ForeignKey('casechecklist.id'), primary_key=True, nullable=False),
    db.Column('case_categories', db.ForeignKey('casecategory.id'), primary_key=True, nullable=False, index=True)
)


class Casechecklist(db.Model):
    __tablename__ = 'casechecklist'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Caselinktype(db.Model):
    __tablename__ = 'caselinktype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Celltype(db.Model):
    __tablename__ = 'celltype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Commital(db.Model):
    __tablename__ = 'commital'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    prisons = db.Column(db.ForeignKey('prison.id'), index=True)
    police_station = db.Column(db.ForeignKey('policestation.id'), index=True)
    parties = db.Column(db.ForeignKey('party.complaints'), nullable=False, index=True)
    casecomplete = db.Column(db.Boolean)
    commit_date = db.Column(db.Date, nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    warrant_type = db.Column(db.ForeignKey('warranttype.id'), nullable=False, index=True)
    warrant_docx = db.Column(db.Text, nullable=False)
    warrant_issue_date = db.Column(db.Date)
    warrant_issued_by = db.Column(db.Text, nullable=False)
    warrant_date_attached = db.Column(db.DateTime)
    duration = db.Column(db.INTERVAL(fields='day to second'))
    commital = db.Column(db.ForeignKey('commital.id'), index=True)
    commital_type = db.Column(db.ForeignKey('commitaltype.id'), nullable=False, index=True)
    court_case = db.Column(db.ForeignKey('courtcase.id'), index=True)
    concurrent = db.Column(db.Boolean)
    life_imprisonment = db.Column(db.Boolean)
    arrival_date = db.Column(db.DateTime)
    sentence_start_date = db.Column(db.DateTime)
    arrest_date = db.Column(db.DateTime)
    remaining_years = db.Column(db.Integer)
    remaining_months = db.Column(db.Integer)
    remaining_days = db.Column(db.Integer)
    cell_number = db.Column(db.Text, nullable=False)
    cell_type = db.Column(db.ForeignKey('celltype.id'), index=True)
    release_date = db.Column(db.DateTime)
    exit_date = db.Column(db.DateTime)
    reason_for_release = db.Column(db.Text, nullable=False)
    with_children = db.Column(db.Boolean)
    release_type = db.Column(db.ForeignKey('releasetype.id'), index=True)
    receiving_officer = db.Column(db.ForeignKey('prisonofficer.id'), nullable=False, index=True)
    releasing_officer = db.Column(db.ForeignKey('prisonofficer.id'), nullable=False, index=True)

    celltype = db.relationship('Celltype', primaryjoin='Commital.cell_type == Celltype.id', backref='commitals')
    parent = db.relationship('Commital', remote_side=[id], primaryjoin='Commital.commital == Commital.id', backref='commitals')
    commitaltype = db.relationship('Commitaltype', primaryjoin='Commital.commital_type == Commitaltype.id', backref='commitals')
    courtcase = db.relationship('Courtcase', primaryjoin='Commital.court_case == Courtcase.id', backref='commitals')
    party = db.relationship('Party', primaryjoin='Commital.parties == Party.complaints', backref='commitals')
    policestation = db.relationship('Policestation', primaryjoin='Commital.police_station == Policestation.id', backref='commitals')
    prison = db.relationship('Prison', primaryjoin='Commital.prisons == Prison.id', backref='commitals')
    prisonofficer = db.relationship('Prisonofficer', primaryjoin='Commital.receiving_officer == Prisonofficer.id', backref='prisonofficer_commitals')
    releasetype = db.relationship('Releasetype', primaryjoin='Commital.release_type == Releasetype.id', backref='commitals')
    prisonofficer1 = db.relationship('Prisonofficer', primaryjoin='Commital.releasing_officer == Prisonofficer.id', backref='prisonofficer_commitals_0')
    warranttype = db.relationship('Warranttype', primaryjoin='Commital.warrant_type == Warranttype.id', backref='commitals')


class Commitaltype(db.Model):
    __tablename__ = 'commitaltype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    maxduration = db.Column(db.INTERVAL(fields='day to second'))


class Complaint(db.Model):
    __tablename__ = 'complaint'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    active = db.Column(db.Boolean)
    ob_number = db.Column(db.String(20), nullable=False)
    police_station = db.Column(db.ForeignKey('policestation.id'), nullable=False, index=True)
    daterecvd = db.Column(db.DateTime, nullable=False)
    datefiled = db.Column(db.DateTime)
    datecaseopened = db.Column(db.DateTime)
    casesummary = db.Column(db.String(2000), nullable=False)
    complaintstatement = db.Column(db.Text, nullable=False)
    circumstances = db.Column(db.Text, nullable=False)
    reportingofficer = db.Column(db.ForeignKey('policeofficer.id'), nullable=False, index=True)
    casefileinformation = db.Column(db.Text, nullable=False)
    p_request_help = db.Column(db.Boolean)
    p_instruction = db.Column(db.Text, nullable=False)
    p_submitted = db.Column(db.Boolean)
    p_submission_date = db.Column(db.DateTime)
    p_submission_notes = db.Column(db.Text, nullable=False)
    p_closed = db.Column(db.Text, nullable=False)
    p_evaluation = db.Column(db.Text, nullable=False)
    p_recommend_charge = db.Column(db.Boolean)
    charge_sheet = db.Column(db.Text, nullable=False)
    charge_sheet_docx = db.Column(db.Text, nullable=False)
    evaluating_prosecutor_team = db.Column(db.ForeignKey('prosecutorteam.id'), index=True)
    magistrate_report_date = db.Column(db.DateTime)
    reported_to_judicial_officer = db.Column(db.ForeignKey('judicialofficer.id'), index=True)
    closed = db.Column(db.Boolean)
    close_date = db.Column(db.DateTime)
    close_reason = db.Column(db.Text, nullable=False)

    prosecutorteam = db.relationship('Prosecutorteam', primaryjoin='Complaint.evaluating_prosecutor_team == Prosecutorteam.id', backref='complaints')
    policestation = db.relationship('Policestation', primaryjoin='Complaint.police_station == Policestation.id', backref='complaints')
    judicialofficer = db.relationship('Judicialofficer', primaryjoin='Complaint.reported_to_judicial_officer == Judicialofficer.id', backref='complaints')
    policeofficer = db.relationship('Policeofficer', primaryjoin='Complaint.reportingofficer == Policeofficer.id', backref='complaints')
    complaintcategory = db.relationship('Complaintcategory', secondary='complaint_complaintcategory', backref='complaints')
    courtcase = db.relationship('Courtcase', secondary='complaint_courtcase', backref='complaints')


class Party(Complaint):
    __tablename__ = 'party'

    complaints = db.Column(db.ForeignKey('complaint.id'), primary_key=True)
    statement = db.Column(db.String(1000), nullable=False)
    statementdate = db.Column(db.DateTime)
    complaint_role = db.Column(db.ForeignKey('complaintrole.id'), nullable=False, index=True)
    notes = db.Column(db.Text, nullable=False)
    dateofrepresentation = db.Column(db.DateTime)
    party_type = db.Column(db.ForeignKey('partytype.id'), nullable=False, index=True)
    relative = db.Column(db.ForeignKey('party.complaints'), nullable=False, index=True)
    relationship_type = db.Column(db.Text, nullable=False)
    biodata = db.Column(db.ForeignKey('biodata.id'), nullable=False, index=True)
    is_infant = db.Column(db.Boolean)
    is_minor = db.Column(db.Boolean)
    miranda_read = db.Column(db.Boolean)
    miranda_date = db.Column(db.DateTime)
    miranda_witness = db.Column(db.Text, nullable=False)

    biodatum = db.relationship('Biodatum', primaryjoin='Party.biodata == Biodatum.id', backref='parties')
    complaintrole = db.relationship('Complaintrole', primaryjoin='Party.complaint_role == Complaintrole.id', backref='parties')
    partytype = db.relationship('Partytype', primaryjoin='Party.party_type == Partytype.id', backref='parties')
    parent = db.relationship('Party', remote_side=[complaints], primaryjoin='Party.relative == Party.complaints', backref='parties')
    settlement = db.relationship('Settlement', secondary='party_settlement', backref='parties')


complaint_complaintcategory = db.Table(
    'complaint_complaintcategory', Model.metadata, 
    db.Column('complaint', db.ForeignKey('complaint.id'), primary_key=True, nullable=False),
    db.Column('complaintcategory', db.ForeignKey('complaintcategory.id'), primary_key=True, nullable=False, index=True)
)


complaint_courtcase = db.Table(
    'complaint_courtcase', Model.metadata, 
    db.Column('complaint', db.ForeignKey('complaint.id'), primary_key=True, nullable=False),
    db.Column('courtcase', db.ForeignKey('courtcase.id'), primary_key=True, nullable=False, index=True)
)


class Complaintcategory(db.Model):
    __tablename__ = 'complaintcategory'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complaint_category_parent = db.Column(db.ForeignKey('complaintcategory.id'), index=True)

    parent = db.relationship('Complaintcategory', remote_side=[id], primaryjoin='Complaintcategory.complaint_category_parent == Complaintcategory.id', backref='complaintcategories')


class Complaintrole(db.Model):
    __tablename__ = 'complaintrole'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Country(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)


class County(db.Model):
    __tablename__ = 'county'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    country = db.Column(db.ForeignKey('country.id'), nullable=False, index=True)

    country1 = db.relationship('Country', primaryjoin='County.country == Country.id', backref='counties')


class Court(db.Model):
    __tablename__ = 'court'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    court_rank = db.Column(db.ForeignKey('courtrank.id'), nullable=False, index=True)
    court_station = db.Column(db.ForeignKey('courtstation.id'), nullable=False, index=True)
    town = db.Column(db.ForeignKey('town.id'), nullable=False, index=True)

    courtrank = db.relationship('Courtrank', primaryjoin='Court.court_rank == Courtrank.id', backref='courts')
    courtstation = db.relationship('Courtstation', primaryjoin='Court.court_station == Courtstation.id', backref='courts')
    town1 = db.relationship('Town', primaryjoin='Court.town == Town.id', backref='courts')
    judicialofficer = db.relationship('Judicialofficer', secondary='court_judicialofficer', backref='courts')


court_judicialofficer = db.Table(
    'court_judicialofficer', Model.metadata, 
    db.Column('court', db.ForeignKey('court.id'), primary_key=True, nullable=False),
    db.Column('judicialofficer', db.ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)


class Courtaccount(db.Model):
    __tablename__ = 'courtaccount'

    courts = db.Column(db.ForeignKey('court.id'), primary_key=True, nullable=False)
    account__types = db.Column(db.ForeignKey('accounttype.id'), primary_key=True, nullable=False, index=True)
    account_number = db.Column(db.Text, nullable=False)
    account_name = db.Column(db.Text, nullable=False)
    short_code = db.Column(db.Text, nullable=False)
    bank_name = db.Column(db.Text, nullable=False)

    accounttype = db.relationship('Accounttype', primaryjoin='Courtaccount.account__types == Accounttype.id', backref='courtaccounts')
    court = db.relationship('Court', primaryjoin='Courtaccount.courts == Court.id', backref='courtaccounts')


class Courtcase(db.Model):
    __tablename__ = 'courtcase'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    docket_number = db.Column(db.Text, nullable=False)
    case_number = db.Column(db.Text, nullable=False)
    adr = db.Column(db.Boolean)
    mediation_proposal = db.Column(db.Text, nullable=False)
    case_received_date = db.Column(db.Date)
    case_filed_date = db.Column(db.Date)
    case_summary = db.Column(db.Text, nullable=False)
    filing_prosecutor = db.Column(db.ForeignKey('prosecutor.id'), index=True)
    fast_track = db.Column(db.Boolean)
    priority = db.Column(db.Integer)
    object_of_litigation = db.Column(db.Text, nullable=False)
    grounds = db.Column(db.Text, nullable=False)
    prosecution_prayer = db.Column(db.Text, nullable=False)
    pretrial_date = db.Column(db.Date)
    pretrial_notes = db.Column(db.Text, nullable=False)
    pretrial_registrar = db.Column(db.ForeignKey('judicialofficer.id'), index=True)
    case_admissible = db.Column(db.Boolean)
    indictment_date = db.Column(db.Text, nullable=False)
    judgement = db.Column(db.Text, nullable=False)
    judgement_docx = db.Column(db.Text, nullable=False)
    case_link_type = db.Column(db.ForeignKey('caselinktype.id'), index=True)
    linked_cases = db.Column(db.ForeignKey('courtcase.id'), index=True)
    appealed = db.Column(db.Boolean)
    appeal_number = db.Column(db.Text, nullable=False)
    inventory_of_docket = db.Column(db.Text, nullable=False)
    next_hearing_date = db.Column(db.Date)
    interlocutory_judgement = db.Column(db.Text, nullable=False)
    reopen = db.Column(db.Boolean)
    reopen_reason = db.Column(db.Text, nullable=False)
    combined_case = db.Column(db.Boolean)
    value_in_dispute = db.Column(db.Numeric(12, 2))
    award = db.Column(db.Numeric(12, 2))
    govt_liability = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean)
    active_date = db.Column(db.DateTime)

    caselinktype = db.relationship('Caselinktype', primaryjoin='Courtcase.case_link_type == Caselinktype.id', backref='courtcases')
    prosecutor = db.relationship('Prosecutor', primaryjoin='Courtcase.filing_prosecutor == Prosecutor.id', backref='courtcases')
    parent = db.relationship('Courtcase', remote_side=[id], primaryjoin='Courtcase.linked_cases == Courtcase.id', backref='courtcases')
    judicialofficer = db.relationship('Judicialofficer', primaryjoin='Courtcase.pretrial_registrar == Judicialofficer.id', backref='judicialofficer_courtcases')
    judicialofficer1 = db.relationship('Judicialofficer', secondary='courtcase_judicialofficer', backref='judicialofficer_courtcases_0')
    lawfirm = db.relationship('Lawfirm', secondary='courtcase_lawfirm', backref='courtcases')


courtcase_judicialofficer = db.Table(
    'courtcase_judicialofficer', Model.metadata, 
    db.Column('courtcase', db.ForeignKey('courtcase.id'), primary_key=True, nullable=False),
    db.Column('judicialofficer', db.ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)


courtcase_lawfirm = db.Table(
    'courtcase_lawfirm', Model.metadata, 
    db.Column('courtcase', db.ForeignKey('courtcase.id'), primary_key=True, nullable=False),
    db.Column('lawfirm', db.ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)


class Courtrank(db.Model):
    __tablename__ = 'courtrank'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Courtstation(db.Model):
    __tablename__ = 'courtstation'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Crime(db.Model):
    __tablename__ = 'crime'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    law = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    ref = db.Column(db.Text, nullable=False)


class CsiEquipment(db.Model):
    __tablename__ = 'csi_equipment'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    investigationdiary = db.relationship('Investigationdiary', secondary='csi_equipment_investigationdiary', backref='csi_equipments')


csi_equipment_investigationdiary = db.Table(
    'csi_equipment_investigationdiary', Model.metadata, 
    db.Column('csi_equipment', db.ForeignKey('csi_equipment.id'), primary_key=True, nullable=False),
    db.Column('investigationdiary', db.ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)


class Diagram(db.Model):
    __tablename__ = 'diagram'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    investigation_diary = db.Column(db.ForeignKey('investigationdiary.id'), nullable=False, index=True)
    image = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    docx = db.Column(db.Text, nullable=False)

    investigationdiary = db.relationship('Investigationdiary', primaryjoin='Diagram.investigation_diary == Investigationdiary.id', backref='diagrams')


class Discipline(db.Model):
    __tablename__ = 'discipline'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    party = db.Column(db.ForeignKey('party.complaints'), nullable=False, index=True)
    prison_officer = db.Column(db.ForeignKey('prisonofficer.id'), nullable=False, index=True)

    party1 = db.relationship('Party', primaryjoin='Discipline.party == Party.complaints', backref='disciplines')
    prisonofficer = db.relationship('Prisonofficer', primaryjoin='Discipline.prison_officer == Prisonofficer.id', backref='disciplines')


class Doctemplate(db.Model):
    __tablename__ = 'doctemplate'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    template = db.Column(db.Text, nullable=False)
    docx = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    template_type = db.Column(db.ForeignKey('templatetype.id'), nullable=False, index=True)
    icon = db.Column(db.Text, nullable=False)

    templatetype = db.relationship('Templatetype', primaryjoin='Doctemplate.template_type == Templatetype.id', backref='doctemplates')


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)
    court_case = db.Column(db.ForeignKey('courtcase.id'), index=True)
    issue = db.Column(db.ForeignKey('issue.id'), index=True)
    document_admissibility = db.Column(db.Text, nullable=False)
    admitted = db.Column(db.Boolean)
    judicial_officer = db.Column(db.ForeignKey('judicialofficer.id'), index=True)
    filing_date = db.Column(db.DateTime)
    admisibility_notes = db.Column(db.Text, nullable=False)
    docx = db.Column(db.Text, nullable=False)
    document_text = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean)
    publish_newspaper = db.Column(db.Text, nullable=False)
    publish_date = db.Column(db.Date)
    validated = db.Column(db.Boolean)
    paid = db.Column(db.Boolean)
    page_count = db.Column(db.Integer)
    file_byte_count = db.Column(db.Numeric(12, 2))
    file_hash = db.Column(db.Text, nullable=False)
    file_timestamp = db.Column(db.Text, nullable=False)
    file_create_date = db.Column(db.DateTime)
    file_update_date = db.Column(db.DateTime)
    file_text = db.Column(db.Text, nullable=False)
    file_name = db.Column(db.Text, nullable=False)
    file_ext = db.Column(db.Text, nullable=False)
    file_load_path = db.Column(db.Text, nullable=False)
    file_upload_date = db.Column(db.DateTime)
    file_parse_status = db.Column(db.Text, nullable=False)
    doc_template = db.Column(db.ForeignKey('doctemplate.id'), index=True)
    visible = db.Column(db.Boolean)
    is_scan = db.Column(db.Boolean)
    doc_shelf = db.Column(db.Text, nullable=False)
    doc_row = db.Column(db.Text, nullable=False)
    doc_room = db.Column(db.Text, nullable=False)
    doc_placed_by = db.Column(db.Text, nullable=False)
    citation = db.Column(db.Text, nullable=False)

    courtcase = db.relationship('Courtcase', primaryjoin='Document.court_case == Courtcase.id', backref='documents')
    doctemplate = db.relationship('Doctemplate', primaryjoin='Document.doc_template == Doctemplate.id', backref='documents')
    issue1 = db.relationship('Issue', primaryjoin='Document.issue == Issue.id', backref='documents')
    judicialofficer = db.relationship('Judicialofficer', primaryjoin='Document.judicial_officer == Judicialofficer.id', backref='documents')
    documenttype = db.relationship('Documenttype', secondary='document_documenttype', backref='documents')


document_documenttype = db.Table(
    'document_documenttype', Model.metadata, 
    db.Column('document', db.ForeignKey('document.id'), primary_key=True, nullable=False),
    db.Column('documenttype', db.ForeignKey('documenttype.id'), primary_key=True, nullable=False, index=True)
)


class Documenttype(db.Model):
    __tablename__ = 'documenttype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Economicclas(db.Model):
    __tablename__ = 'economicclass'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Exhibit(db.Model):
    __tablename__ = 'exhibit'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    investigation_entry = db.Column(db.ForeignKey('investigationdiary.id'), nullable=False, index=True)
    photo = db.Column(db.Text, nullable=False)
    exhibit_no = db.Column(db.Text, nullable=False)
    docx = db.Column(db.Text, nullable=False)
    seizure = db.Column(db.ForeignKey('seizure.id'), nullable=False, index=True)

    investigationdiary = db.relationship('Investigationdiary', primaryjoin='Exhibit.investigation_entry == Investigationdiary.id', backref='exhibits')
    seizure1 = db.relationship('Seizure', primaryjoin='Exhibit.seizure == Seizure.id', backref='exhibits')


class Expert(db.Model):
    __tablename__ = 'expert'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    institution = db.Column(db.Text, nullable=False)
    jobtitle = db.Column(db.Text, nullable=False)
    credentials = db.Column(db.Text, nullable=False)

    experttype = db.relationship('Experttype', secondary='expert_experttype', backref='experts')


expert_experttype = db.Table(
    'expert_experttype', Model.metadata, 
    db.Column('expert', db.ForeignKey('expert.id'), primary_key=True, nullable=False),
    db.Column('experttype', db.ForeignKey('experttype.id'), primary_key=True, nullable=False, index=True)
)


class Experttestimony(db.Model):
    __tablename__ = 'experttestimony'

    requesting_officer = db.Column(db.ForeignKey('investigating_officer.police_officers'), nullable=False, index=True)
    investigation_entries = db.Column(db.ForeignKey('investigationdiary.id'), primary_key=True, nullable=False)
    experts = db.Column(db.ForeignKey('expert.id'), primary_key=True, nullable=False, index=True)
    task_given = db.Column(db.Text, nullable=False)
    summary_of_facts = db.Column(db.Text, nullable=False)
    statement = db.Column(db.Text, nullable=False)
    testimony_date = db.Column(db.DateTime)
    task_request_date = db.Column(db.Date)
    docx = db.Column(db.Text, nullable=False)
    validated = db.Column(db.Boolean)

    expert = db.relationship('Expert', primaryjoin='Experttestimony.experts == Expert.id', backref='experttestimonies')
    investigationdiary = db.relationship('Investigationdiary', primaryjoin='Experttestimony.investigation_entries == Investigationdiary.id', backref='experttestimonies')
    investigating_officer = db.relationship('InvestigatingOfficer', primaryjoin='Experttestimony.requesting_officer == InvestigatingOfficer.police_officers', backref='experttestimonies')


class Experttype(db.Model):
    __tablename__ = 'experttype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Feeclas(db.Model):
    __tablename__ = 'feeclass'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    fee_type = db.Column(db.ForeignKey('feeclass.id'), index=True)

    parent = db.relationship('Feeclas', remote_side=[id], primaryjoin='Feeclas.fee_type == Feeclas.id', backref='feeclass')


class Feetype(db.Model):
    __tablename__ = 'feetype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    filing_fee_type = db.Column(db.ForeignKey('feeclass.id'), nullable=False, index=True)
    amount = db.Column(db.Numeric(12, 2))
    unit = db.Column(db.Text, nullable=False)
    min_fee = db.Column(db.Numeric(12, 2))
    max_fee = db.Column(db.Numeric(12, 2))
    description = db.Column(db.Text)
    guide_sec = db.Column(db.Text)
    guide_clause = db.Column(db.Text)
    account_type = db.Column(db.ForeignKey('accounttype.id'), nullable=False, index=True)

    accounttype = db.relationship('Accounttype', primaryjoin='Feetype.account_type == Accounttype.id', backref='feetypes')
    feeclas = db.relationship('Feeclas', primaryjoin='Feetype.filing_fee_type == Feeclas.id', backref='feetypes')


class Healthevent(db.Model):
    __tablename__ = 'healthevent'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    party = db.Column(db.ForeignKey('party.complaints'), nullable=False, index=True)
    reporting_prison_officer = db.Column(db.ForeignKey('prisonofficer.id'), index=True)
    health_event_type = db.Column(db.ForeignKey('healtheventtype.id'), nullable=False, index=True)
    startdate = db.Column(db.DateTime)
    enddate = db.Column(db.DateTime)
    notes = db.Column(db.Text, nullable=False)

    healtheventtype = db.relationship('Healtheventtype', primaryjoin='Healthevent.health_event_type == Healtheventtype.id', backref='healthevents')
    party1 = db.relationship('Party', primaryjoin='Healthevent.party == Party.complaints', backref='healthevents')
    prisonofficer = db.relationship('Prisonofficer', primaryjoin='Healthevent.reporting_prison_officer == Prisonofficer.id', backref='healthevents')


class Healtheventtype(db.Model):
    __tablename__ = 'healtheventtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Hearing(db.Model):
    __tablename__ = 'hearing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    court_cases = db.Column(db.ForeignKey('courtcase.id'), index=True)
    hearing_type = db.Column(db.ForeignKey('hearingtype.id'), nullable=False, index=True)
    schedule_status = db.Column(db.ForeignKey('schedulestatustype.id'), nullable=False, index=True)
    hearing_date = db.Column(db.Date)
    reason = db.Column(db.Text, nullable=False)
    sequence = db.Column(db.BigInteger)
    yearday = db.Column(db.BigInteger)
    starttime = db.Column(db.Time)
    endtime = db.Column(db.Time)
    notes = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean)
    adjourned_to = db.Column(db.Date)
    adjournment_reason = db.Column(db.Text, nullable=False)
    transcript = db.Column(db.Text, nullable=False)
    atendance = db.Column(db.Text, nullable=False)
    next_hearing_date = db.Column(db.Date)
    postponement_reason = db.Column(db.Text, nullable=False)

    courtcase = db.relationship('Courtcase', primaryjoin='Hearing.court_cases == Courtcase.id', backref='hearings')
    hearingtype = db.relationship('Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref='hearings')
    schedulestatustype = db.relationship('Schedulestatustype', primaryjoin='Hearing.schedule_status == Schedulestatustype.id', backref='hearings')
    issue = db.relationship('Issue', secondary='hearing_issue', backref='hearings')
    judicialofficer = db.relationship('Judicialofficer', secondary='hearing_judicialofficer', backref='hearings')
    lawfirm = db.relationship('Lawfirm', secondary='hearing_lawfirm', backref='lawfirm_hearings')
    lawfirm1 = db.relationship('Lawfirm', secondary='hearing_lawfirm_2', backref='lawfirm_hearings_0')


hearing_issue = db.Table(
    'hearing_issue', Model.metadata, 
    db.Column('hearing', db.ForeignKey('hearing.id'), primary_key=True, nullable=False),
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False, index=True)
)


hearing_judicialofficer = db.Table(
    'hearing_judicialofficer', Model.metadata, 
    db.Column('hearing', db.ForeignKey('hearing.id'), primary_key=True, nullable=False),
    db.Column('judicialofficer', db.ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)


hearing_lawfirm = db.Table(
    'hearing_lawfirm', Model.metadata, 
    db.Column('hearing', db.ForeignKey('hearing.id'), primary_key=True, nullable=False),
    db.Column('lawfirm', db.ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)


hearing_lawfirm_2 = db.Table(
    'hearing_lawfirm_2', Model.metadata, 
    db.Column('hearing', db.ForeignKey('hearing.id'), primary_key=True, nullable=False),
    db.Column('lawfirm', db.ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)


class Hearingtype(db.Model):
    __tablename__ = 'hearingtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    hearing_type = db.Column(db.ForeignKey('hearingtype.id'), index=True)

    parent = db.relationship('Hearingtype', remote_side=[id], primaryjoin='Hearingtype.hearing_type == Hearingtype.id', backref='hearingtypes')


class Instancecrime(db.Model):
    __tablename__ = 'instancecrime'

    parties = db.Column(db.ForeignKey('party.complaints'), primary_key=True, nullable=False)
    crimes = db.Column(db.ForeignKey('crime.id'), primary_key=True, nullable=False, index=True)
    crime_detail = db.Column(db.Text, nullable=False)
    tffender_type = db.Column(db.Text, nullable=False)
    crime_date = db.Column(db.DateTime)
    date_note = db.Column(db.Text, nullable=False)
    place_of_crime = db.Column(db.Text, nullable=False)
    place_note = db.Column(db.Text, nullable=False)

    crime = db.relationship('Crime', primaryjoin='Instancecrime.crimes == Crime.id', backref='instancecrimes')
    party = db.relationship('Party', primaryjoin='Instancecrime.parties == Party.complaints', backref='instancecrimes')
    issue = db.relationship('Issue', secondary='instancecrime_issue', backref='instancecrimes')


instancecrime_issue = db.Table(
    'instancecrime_issue', Model.metadata, 
    db.Column('instancecrime_parties', db.Integer, primary_key=True, nullable=False),
    db.Column('instancecrime_crimes', db.Integer, primary_key=True, nullable=False),
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['instancecrime_parties', 'instancecrime_crimes'], ['instancecrime.parties', 'instancecrime.crimes'])
)


class Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    investigation_entry = db.Column(db.ForeignKey('investigationdiary.id'), nullable=False, index=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    validated = db.Column(db.Boolean)
    language = db.Column(db.Text, nullable=False)

    investigationdiary = db.relationship('Investigationdiary', primaryjoin='Interview.investigation_entry == Investigationdiary.id', backref='interviews')


investigating_officer_investigationdiary = db.Table(
    'investigating_officer_investigationdiary', Model.metadata, 
    db.Column('investigating_officer', db.ForeignKey('investigating_officer.police_officers'), primary_key=True, nullable=False),
    db.Column('investigationdiary', db.ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)


class Investigationdiary(db.Model):
    __tablename__ = 'investigationdiary'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complaint = db.Column(db.ForeignKey('complaint.id'), nullable=False, index=True)
    activity = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    outcome = db.Column(db.Text, nullable=False)
    equipmentresults = db.Column(db.Text, nullable=False)
    startdate = db.Column(db.DateTime, nullable=False)
    enddate = db.Column(db.DateTime)
    advocate_present = db.Column(db.Text, nullable=False)
    summons_statement = db.Column(db.Text, nullable=False)
    arrest_statement = db.Column(db.Text, nullable=False)
    arrest_warrant = db.Column(db.Text, nullable=False)
    search_seizure_statement = db.Column(db.Text, nullable=False)
    docx = db.Column(db.Text, nullable=False)
    detained = db.Column(db.Text, nullable=False)
    detained_at = db.Column(db.Text, nullable=False)
    provisional_release_statement = db.Column(db.Text, nullable=False)
    warrant_type = db.Column(db.ForeignKey('warranttype.id'), index=True)
    warrant_issued_by = db.Column(db.Text, nullable=False)
    warrant_issue_date = db.Column(db.Date)
    warrant_delivered_by = db.Column(db.Text, nullable=False)
    warrant_received_by = db.Column(db.Text, nullable=False)
    warrant_serve_date = db.Column(db.Text, nullable=False)
    warrant_docx = db.Column(db.Text, nullable=False)
    warrant_upload_date = db.Column(db.Text, nullable=False)

    complaint1 = db.relationship('Complaint', primaryjoin='Investigationdiary.complaint == Complaint.id', backref='investigationdiaries')
    warranttype = db.relationship('Warranttype', primaryjoin='Investigationdiary.warrant_type == Warranttype.id', backref='investigationdiaries')
    party = db.relationship('Party', secondary='investigationdiary_party', backref='party_investigationdiaries')
    vehicle = db.relationship('Vehicle', secondary='investigationdiary_vehicle', backref='investigationdiaries')


investigationdiary_party = db.Table(
    'investigationdiary_party', Model.metadata, 
    db.Column('investigationdiary', db.ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
    db.Column('party', db.ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


investigationdiary_vehicle = db.Table(
    'investigationdiary_vehicle', Model.metadata, 
    db.Column('investigationdiary', db.ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
    db.Column('vehicle', db.ForeignKey('vehicle.id'), primary_key=True, nullable=False, index=True)
)


class Issue(db.Model):
    __tablename__ = 'issue'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    issue = db.Column(db.Text, nullable=False)
    facts = db.Column(db.Text)
    counter_claim = db.Column(db.Boolean)
    argument = db.Column(db.Text, nullable=False)
    argument_date = db.Column(db.Date)
    argument_docx = db.Column(db.Text)
    rebuttal = db.Column(db.Text, nullable=False)
    rebuttal_date = db.Column(db.Date)
    rebuttal_docx = db.Column(db.Text)
    hearing_date = db.Column(db.Date)
    determination = db.Column(db.Text, nullable=False)
    dtermination_date = db.Column(db.Date)
    determination_docx = db.Column(db.Text, nullable=False)
    resolved = db.Column(db.Boolean)
    defense_lawyer = db.Column(db.ForeignKey('lawyer.id'), nullable=False, index=True)
    prosecutor = db.Column(db.ForeignKey('prosecutor.id'), index=True)
    judicial_officer = db.Column(db.ForeignKey('judicialofficer.id'), nullable=False, index=True)
    court_case = db.Column(db.ForeignKey('courtcase.id'), nullable=False, index=True)
    tasks = db.Column(db.Text, nullable=False)
    is_criminal = db.Column(db.Boolean)
    moral_element = db.Column(db.Text, nullable=False)
    material_element = db.Column(db.Text, nullable=False)
    legal_element = db.Column(db.Text, nullable=False)
    debt_amount = db.Column(db.Numeric(12, 2))

    courtcase = db.relationship('Courtcase', primaryjoin='Issue.court_case == Courtcase.id', backref='issues')
    lawyer = db.relationship('Lawyer', primaryjoin='Issue.defense_lawyer == Lawyer.id', backref='lawyer_issues')
    judicialofficer = db.relationship('Judicialofficer', primaryjoin='Issue.judicial_officer == Judicialofficer.id', backref='issues')
    prosecutor1 = db.relationship('Prosecutor', primaryjoin='Issue.prosecutor == Prosecutor.id', backref='issues')
    lawyer1 = db.relationship('Lawyer', secondary='issue_lawyer', backref='lawyer_issues_0')
    legalreference = db.relationship('Legalreference', secondary='issue_legalreference', backref='legalreference_issues')
    legalreference1 = db.relationship('Legalreference', secondary='issue_legalreference_2', backref='legalreference_issues_0')
    party = db.relationship('Party', secondary='issue_party', backref='party_issues')
    party1 = db.relationship('Party', secondary='issue_party_2', backref='party_issues_0')


issue_lawyer = db.Table(
    'issue_lawyer', Model.metadata, 
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False),
    db.Column('lawyer', db.ForeignKey('lawyer.id'), primary_key=True, nullable=False, index=True)
)


issue_legalreference = db.Table(
    'issue_legalreference', Model.metadata, 
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False),
    db.Column('legalreference', db.ForeignKey('legalreference.id'), primary_key=True, nullable=False, index=True)
)


issue_legalreference_2 = db.Table(
    'issue_legalreference_2', Model.metadata, 
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False),
    db.Column('legalreference', db.ForeignKey('legalreference.id'), primary_key=True, nullable=False, index=True)
)


issue_party = db.Table(
    'issue_party', Model.metadata, 
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False),
    db.Column('party', db.ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


issue_party_2 = db.Table(
    'issue_party_2', Model.metadata, 
    db.Column('issue', db.ForeignKey('issue.id'), primary_key=True, nullable=False),
    db.Column('party', db.ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


class Judicialofficer(db.Model):
    __tablename__ = 'judicialofficer'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    rank = db.Column(db.ForeignKey('judicialrank.id'), nullable=False, index=True)
    judicial_role = db.Column(db.ForeignKey('judicialrole.id'), nullable=False, index=True)
    court_station = db.Column(db.ForeignKey('courtstation.id'), nullable=False, index=True)

    courtstation = db.relationship('Courtstation', primaryjoin='Judicialofficer.court_station == Courtstation.id', backref='judicialofficers')
    judicialrole = db.relationship('Judicialrole', primaryjoin='Judicialofficer.judicial_role == Judicialrole.id', backref='judicialofficers')
    judicialrank = db.relationship('Judicialrank', primaryjoin='Judicialofficer.rank == Judicialrank.id', backref='judicialofficers')


class Judicialrank(db.Model):
    __tablename__ = 'judicialrank'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Judicialrole(db.Model):
    __tablename__ = 'judicialrole'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Lawfirm(db.Model):
    __tablename__ = 'lawfirm'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Lawyer(db.Model):
    __tablename__ = 'lawyer'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    law_firm = db.Column(db.ForeignKey('lawfirm.id'), index=True)
    bar_no = db.Column(db.Text, nullable=False)
    bar_date = db.Column(db.Date)

    lawfirm = db.relationship('Lawfirm', primaryjoin='Lawyer.law_firm == Lawfirm.id', backref='lawyers')
    party = db.relationship('Party', secondary='lawyer_party', backref='lawyers')


lawyer_party = db.Table(
    'lawyer_party', Model.metadata, 
    db.Column('lawyer', db.ForeignKey('lawyer.id'), primary_key=True, nullable=False),
    db.Column('party', db.ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


class Legalreference(db.Model):
    __tablename__ = 'legalreference'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    ref = db.Column(db.Text, nullable=False)
    verbatim = db.Column(db.Text, nullable=False)
    public = db.Column(db.Boolean)
    commentary = db.Column(db.Text, nullable=False)
    validated = db.Column(db.Boolean)
    citation = db.Column(db.Text, nullable=False)
    quote = db.Column(db.Text, nullable=False)
    interpretation = db.Column(db.Text, nullable=False)


class Nextofkin(db.Model):
    __tablename__ = 'nextofkin'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    biodata = db.Column(db.ForeignKey('biodata.id'), nullable=False, index=True)
    childunder4 = db.Column(db.Boolean)

    biodatum = db.relationship('Biodatum', primaryjoin='Nextofkin.biodata == Biodatum.id', backref='nextofkins')


class Notification(db.Model):
    __tablename__ = 'notification'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    contact = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    confirmation = db.Column(db.Text, nullable=False)
    notification_register = db.Column(db.ForeignKey('notificationregister.id'), index=True)
    add_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    sent = db.Column(db.Boolean)
    delivered = db.Column(db.Boolean)
    retries = db.Column(db.Integer)
    abandon = db.Column(db.Boolean)
    retry_count = db.Column(db.Integer)

    notificationregister = db.relationship('Notificationregister', primaryjoin='Notification.notification_register == Notificationregister.id', backref='notifications')


class Notificationregister(db.Model):
    __tablename__ = 'notificationregister'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    notification_type = db.Column(db.ForeignKey('notificationtype.id'), nullable=False, index=True)
    contact = db.Column(db.Text, nullable=False)
    notify_event = db.Column(db.ForeignKey('notifyevent.id'), index=True)
    retry_count = db.Column(db.BigInteger)
    active = db.Column(db.Boolean)
    hearing = db.Column(db.ForeignKey('hearing.id'), index=True)
    document = db.Column(db.ForeignKey('document.id'), index=True)
    court_case = db.Column(db.ForeignKey('courtcase.id'), index=True)
    complaint = db.Column(db.ForeignKey('complaint.id'), index=True)
    complaint_category = db.Column(db.ForeignKey('complaintcategory.id'), index=True)
    health_event = db.Column(db.ForeignKey('healthevent.id'), index=True)
    party = db.Column(db.ForeignKey('party.complaints'), index=True)

    complaint1 = db.relationship('Complaint', primaryjoin='Notificationregister.complaint == Complaint.id', backref='notificationregisters')
    complaintcategory = db.relationship('Complaintcategory', primaryjoin='Notificationregister.complaint_category == Complaintcategory.id', backref='notificationregisters')
    courtcase = db.relationship('Courtcase', primaryjoin='Notificationregister.court_case == Courtcase.id', backref='notificationregisters')
    document1 = db.relationship('Document', primaryjoin='Notificationregister.document == Document.id', backref='notificationregisters')
    healthevent = db.relationship('Healthevent', primaryjoin='Notificationregister.health_event == Healthevent.id', backref='notificationregisters')
    hearing1 = db.relationship('Hearing', primaryjoin='Notificationregister.hearing == Hearing.id', backref='notificationregisters')
    notificationtype = db.relationship('Notificationtype', primaryjoin='Notificationregister.notification_type == Notificationtype.id', backref='notificationregisters')
    notifyevent = db.relationship('Notifyevent', primaryjoin='Notificationregister.notify_event == Notifyevent.id', backref='notificationregisters')
    party1 = db.relationship('Party', primaryjoin='Notificationregister.party == Party.complaints', backref='party_notificationregisters')


class Notificationtype(db.Model):
    __tablename__ = 'notificationtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)


class Notifyevent(db.Model):
    __tablename__ = 'notifyevent'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Page(db.Model):
    __tablename__ = 'page'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    document = db.Column(db.ForeignKey('document.id'), nullable=False, index=True)
    page_image = db.Column(db.LargeBinary)
    page_no = db.Column(db.BigInteger)
    page_text = db.Column(db.Text, nullable=False)
    image_ext = db.Column(db.Text)
    image_width = db.Column(db.Text)
    image_height = db.Column(db.Text)
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    upload_dt = db.Column(db.DateTime)

    document1 = db.relationship('Document', primaryjoin='Page.document == Document.id', backref='pages')


party_settlement = db.Table(
    'party_settlement', Model.metadata, 
    db.Column('party', db.ForeignKey('party.complaints'), primary_key=True, nullable=False),
    db.Column('settlement', db.ForeignKey('settlement.id'), primary_key=True, nullable=False, index=True)
)


class Partytype(db.Model):
    __tablename__ = 'partytype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    bill = db.Column(db.ForeignKey('bill.id'), nullable=False, index=True)
    amount = db.Column(db.Text, nullable=False)
    payment_ref = db.Column(db.Text, nullable=False)
    date_paid = db.Column(db.DateTime)
    phone_number = db.Column(db.String(20))
    validated = db.Column(db.Boolean)
    payment_description = db.Column(db.Text)

    bill1 = db.relationship('Bill', primaryjoin='Payment.bill == Bill.id', backref='payments')


class Personaleffect(db.Model):
    __tablename__ = 'personaleffect'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    party = db.Column(db.ForeignKey('party.complaints'), nullable=False, index=True)
    personal_effects_category = db.Column(db.ForeignKey('personaleffectscategory.id'), nullable=False, index=True)

    party1 = db.relationship('Party', primaryjoin='Personaleffect.party == Party.complaints', backref='personaleffects')
    personaleffectscategory = db.relationship('Personaleffectscategory', primaryjoin='Personaleffect.personal_effects_category == Personaleffectscategory.id', backref='personaleffects')


class Personaleffectscategory(db.Model):
    __tablename__ = 'personaleffectscategory'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Policeofficer(db.Model):
    __tablename__ = 'policeofficer'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    police_rank = db.Column(db.ForeignKey('policeofficerrank.id'), nullable=False, index=True)
    servicenumber = db.Column(db.String(100), nullable=False, unique=True)

    policeofficerrank = db.relationship('Policeofficerrank', primaryjoin='Policeofficer.police_rank == Policeofficerrank.id', backref='policeofficers')
    policestation = db.relationship('Policestation', secondary='policeofficer_policestation', backref='policeofficers')


class InvestigatingOfficer(Policeofficer):
    __tablename__ = 'investigating_officer'

    police_officers = db.Column(db.ForeignKey('policeofficer.id'), primary_key=True)
    date_assigned = db.Column(db.DateTime)
    lead_investigator = db.Column(db.Integer)

    investigationdiary = db.relationship('Investigationdiary', secondary='investigating_officer_investigationdiary', backref='investigating_officers')


policeofficer_policestation = db.Table(
    'policeofficer_policestation', Model.metadata, 
    db.Column('policeofficer', db.ForeignKey('policeofficer.id'), primary_key=True, nullable=False),
    db.Column('policestation', db.ForeignKey('policestation.id'), primary_key=True, nullable=False, index=True)
)


class Policeofficerrank(db.Model):
    __tablename__ = 'policeofficerrank'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    sequence = db.Column(db.Integer)


class Policestation(db.Model):
    __tablename__ = 'policestation'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey('town.id'), index=True)
    officer_commanding = db.Column(db.ForeignKey('policeofficer.id'), nullable=False, index=True)
    police_station_rank = db.Column(db.ForeignKey('policestationrank.id'), nullable=False, index=True)

    policeofficer = db.relationship('Policeofficer', primaryjoin='Policestation.officer_commanding == Policeofficer.id', backref='policestations')
    policestationrank = db.relationship('Policestationrank', primaryjoin='Policestation.police_station_rank == Policestationrank.id', backref='policestations')
    town1 = db.relationship('Town', primaryjoin='Policestation.town == Town.id', backref='policestations')


class Policestationrank(db.Model):
    __tablename__ = 'policestationrank'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Prison(db.Model):
    __tablename__ = 'prison'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey('town.id'), nullable=False, index=True)

    town1 = db.relationship('Town', primaryjoin='Prison.town == Town.id', backref='prisons')


class Prisonofficer(db.Model):
    __tablename__ = 'prisonofficer'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    prison = db.Column(db.ForeignKey('prison.id'), nullable=False, index=True)
    prison_officer_rank = db.Column(db.ForeignKey('prisonofficerrank.id'), nullable=False, index=True)

    prison1 = db.relationship('Prison', primaryjoin='Prisonofficer.prison == Prison.id', backref='prisonofficers')
    prisonofficerrank = db.relationship('Prisonofficerrank', primaryjoin='Prisonofficer.prison_officer_rank == Prisonofficerrank.id', backref='prisonofficers')


class Prisonofficerrank(db.Model):
    __tablename__ = 'prisonofficerrank'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Prosecutor(db.Model):
    __tablename__ = 'prosecutor'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    prosecutor_team = db.Column(db.ForeignKey('prosecutorteam.id'), index=True)
    lawyer = db.Column(db.ForeignKey('lawyer.id'), nullable=False, index=True)

    lawyer1 = db.relationship('Lawyer', primaryjoin='Prosecutor.lawyer == Lawyer.id', backref='prosecutors')
    prosecutorteam = db.relationship('Prosecutorteam', primaryjoin='Prosecutor.prosecutor_team == Prosecutorteam.id', backref='prosecutors')


class Prosecutorteam(db.Model):
    __tablename__ = 'prosecutorteam'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Releasetype(db.Model):
    __tablename__ = 'releasetype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Religion(db.Model):
    __tablename__ = 'religion'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Schedulestatustype(db.Model):
    __tablename__ = 'schedulestatustype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Seizure(db.Model):
    __tablename__ = 'seizure'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    investigation_diary = db.Column(db.ForeignKey('investigationdiary.id'), nullable=False, index=True)
    owner = db.Column(db.Text, nullable=False)
    item = db.Column(db.Text, nullable=False)
    item_packaging = db.Column(db.Text, nullable=False)
    item_pic = db.Column(db.Text, nullable=False)
    premises = db.Column(db.Text, nullable=False)
    reg_no = db.Column(db.Text, nullable=False)
    witness = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    docx = db.Column(db.Text, nullable=False)
    item_description = db.Column(db.Text, nullable=False)
    returned = db.Column(db.Boolean)
    return_date = db.Column(db.DateTime)
    return_notes = db.Column(db.Text, nullable=False)
    return_signed_receipt = db.Column(db.Text, nullable=False)
    destroyed = db.Column(db.Boolean)
    destruction_date = db.Column(db.Date)
    destruction_witnesses = db.Column(db.Text, nullable=False)
    destruction_notes = db.Column(db.Text, nullable=False)
    disposed = db.Column(db.Boolean)
    sold_to = db.Column(db.Text, nullable=False)
    disposal_date = db.Column(db.Date)
    disposal_price = db.Column(db.Numeric(12, 2))
    disposal_receipt = db.Column(db.Text, nullable=False)
    recovery_town = db.Column(db.ForeignKey('town.id'), index=True)
    destruction_pic = db.Column(db.Text, nullable=False)
    is_evidence = db.Column(db.Boolean)
    immovable = db.Column(db.Boolean)

    investigationdiary = db.relationship('Investigationdiary', primaryjoin='Seizure.investigation_diary == Investigationdiary.id', backref='seizures')
    town = db.relationship('Town', primaryjoin='Seizure.recovery_town == Town.id', backref='seizures')


class Settlement(db.Model):
    __tablename__ = 'settlement'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complaint = db.Column(db.ForeignKey('complaint.id'), nullable=False, index=True)
    terms = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Numeric(12, 2))
    paid = db.Column(db.Boolean)
    docx = db.Column(db.Text, nullable=False)
    settlor = db.Column(db.ForeignKey('party.complaints'), nullable=False, index=True)

    complaint1 = db.relationship('Complaint', primaryjoin='Settlement.complaint == Complaint.id', backref='settlements')
    party = db.relationship('Party', primaryjoin='Settlement.settlor == Party.complaints', backref='party_settlements')


class Subcounty(db.Model):
    __tablename__ = 'subcounty'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    county = db.Column(db.ForeignKey('county.id'), nullable=False, index=True)

    county1 = db.relationship('County', primaryjoin='Subcounty.county == County.id', backref='subcounties')


class Templatetype(db.Model):
    __tablename__ = 'templatetype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    template_type = db.Column(db.ForeignKey('templatetype.id'), index=True)

    parent = db.relationship('Templatetype', remote_side=[id], primaryjoin='Templatetype.template_type == Templatetype.id', backref='templatetypes')


class Town(db.Model):
    __tablename__ = 'town'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    ward = db.relationship('Ward', secondary='town_ward', backref='towns')


town_ward = db.Table(
    'town_ward', Model.metadata, 
    db.Column('town', db.ForeignKey('town.id'), primary_key=True, nullable=False),
    db.Column('ward', db.ForeignKey('ward.id'), primary_key=True, nullable=False, index=True)
)


class Transcript(db.Model):
    __tablename__ = 'transcript'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    video = db.Column(db.Text, nullable=False)
    audio = db.Column(db.Text, nullable=False)
    add_date = db.Column(db.DateTime)
    asr_transcript = db.Column(db.Text, nullable=False)
    asr_date = db.Column(db.DateTime)
    edited_transcript = db.Column(db.Text, nullable=False)
    edit_date = db.Column(db.DateTime)
    certified_transcript = db.Column(db.Text, nullable=False)
    certfiy_date = db.Column(db.DateTime)
    locked = db.Column(db.Boolean)
    hearing = db.Column(db.ForeignKey('hearing.id'), nullable=False, index=True)

    hearing1 = db.relationship('Hearing', primaryjoin='Transcript.hearing == Hearing.id', backref='transcripts')


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    police_station = db.Column(db.ForeignKey('policestation.id'), nullable=False, index=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    regno = db.Column(db.String(100), nullable=False)

    policestation = db.relationship('Policestation', primaryjoin='Vehicle.police_station == Policestation.id', backref='vehicles')


class Ward(db.Model):
    __tablename__ = 'ward'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subcounty = db.Column(db.ForeignKey('subcounty.id'), nullable=False, index=True)

    subcounty1 = db.relationship('Subcounty', primaryjoin='Ward.subcounty == Subcounty.id', backref='wards')


class Warranttype(db.Model):
    __tablename__ = 'warranttype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

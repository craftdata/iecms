# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import INTERVAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Accounttype(Base):
    __tablename__ = 'accounttype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('accounttype_id_seq'::regclass)"))


class Bill(Base):
    __tablename__ = 'bill'
    __table_args__ = (
        ForeignKeyConstraint(['court_account_courts', 'court_account_account__types'], ['courtaccount.courts', 'courtaccount.account__types']),
        Index('idx_bill__court_account_courts_court_account_account__types', 'court_account_courts', 'court_account_account__types')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('bill_id_seq'::regclass)"))
    assessing_registrar = Column(ForeignKey('judicialofficer.id'), nullable=False, index=True)
    receiving_registrar = Column(ForeignKey('judicialofficer.id'), nullable=False, index=True)
    lawyer_paying = Column(ForeignKey('lawyer.id'), index=True)
    party_paying = Column(ForeignKey('party.complaints'), index=True)
    documents = Column(ForeignKey('document.id'), index=True)
    date_of_payment = Column(Text, nullable=False)
    paid = Column(Boolean)
    pay_code = Column(String(20), unique=True)
    bill_total = Column(Numeric(12, 2))
    court = Column(ForeignKey('court.id'), nullable=False, index=True)
    court_account_courts = Column(Integer, nullable=False)
    court_account_account__types = Column(Integer, nullable=False)
    validated = Column(Boolean)
    validation_date = Column(DateTime)

    judicialofficer = relationship('Judicialofficer', primaryjoin='Bill.assessing_registrar == Judicialofficer.id')
    court1 = relationship('Court')
    courtaccount = relationship('Courtaccount')
    document = relationship('Document')
    lawyer = relationship('Lawyer')
    party = relationship('Party')
    judicialofficer1 = relationship('Judicialofficer', primaryjoin='Bill.receiving_registrar == Judicialofficer.id')


class Billdetail(Base):
    __tablename__ = 'billdetail'

    id = Column(Integer, primary_key=True, server_default=text("nextval('billdetail_id_seq'::regclass)"))
    receipt_id = Column(ForeignKey('bill.id'), nullable=False, index=True)
    feetype = Column(ForeignKey('feetype.id'), nullable=False, index=True)
    purpose = Column(Text, nullable=False)
    unit = Column(Text)
    qty = Column(Integer)
    unit_cost = Column(Numeric(12, 2))
    amount = Column(Numeric(12, 2))

    feetype1 = relationship('Feetype')
    receipt = relationship('Bill')


class Biodatum(Base):
    __tablename__ = 'biodata'

    id = Column(Integer, primary_key=True, server_default=text("nextval('biodata_id_seq'::regclass)"))
    economic_class = Column(ForeignKey('economicclass.id'), index=True)
    religion = Column(ForeignKey('religion.id'), index=True)
    photo = Column(LargeBinary)
    health_status = Column(Text, nullable=False)

    economicclas = relationship('Economicclas')
    religion1 = relationship('Religion')


class Casecategory(Base):
    __tablename__ = 'casecategory'

    id = Column(Integer, primary_key=True, server_default=text("nextval('casecategory_id_seq'::regclass)"))
    subcategory = Column(ForeignKey('casecategory.id'), index=True)

    parent = relationship('Casecategory', remote_side=[id])
    casechecklist = relationship('Casechecklist', secondary='casecategorychecklist')
    courtcase = relationship('Courtcase', secondary='casecategory_courtcase')


t_casecategory_courtcase = Table(
    'casecategory_courtcase', metadata,
    Column('casecategory', ForeignKey('casecategory.id'), primary_key=True, nullable=False),
    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=False, index=True)
)


t_casecategorychecklist = Table(
    'casecategorychecklist', metadata,
    Column('case_checklists', ForeignKey('casechecklist.id'), primary_key=True, nullable=False),
    Column('case_categories', ForeignKey('casecategory.id'), primary_key=True, nullable=False, index=True)
)


class Casechecklist(Base):
    __tablename__ = 'casechecklist'

    id = Column(Integer, primary_key=True, server_default=text("nextval('casechecklist_id_seq'::regclass)"))


class Caselinktype(Base):
    __tablename__ = 'caselinktype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('caselinktype_id_seq'::regclass)"))


class Celltype(Base):
    __tablename__ = 'celltype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('celltype_id_seq'::regclass)"))


class Commital(Base):
    __tablename__ = 'commital'

    id = Column(Integer, primary_key=True, server_default=text("nextval('commital_id_seq'::regclass)"))
    prisons = Column(ForeignKey('prison.id'), index=True)
    police_station = Column(ForeignKey('policestation.id'), index=True)
    parties = Column(ForeignKey('party.complaints'), nullable=False, index=True)
    casecomplete = Column(Boolean)
    commit_date = Column(Date, nullable=False)
    purpose = Column(Text, nullable=False)
    warrant_type = Column(ForeignKey('warranttype.id'), nullable=False, index=True)
    warrant_docx = Column(Text, nullable=False)
    warrant_issue_date = Column(Date)
    warrant_issued_by = Column(Text, nullable=False)
    warrant_date_attached = Column(DateTime)
    duration = Column(INTERVAL(fields='day to second'))
    commital = Column(ForeignKey('commital.id'), index=True)
    commital_type = Column(ForeignKey('commitaltype.id'), nullable=False, index=True)
    court_case = Column(ForeignKey('courtcase.id'), index=True)
    concurrent = Column(Boolean)
    life_imprisonment = Column(Boolean)
    arrival_date = Column(DateTime)
    sentence_start_date = Column(DateTime)
    arrest_date = Column(DateTime)
    remaining_years = Column(Integer)
    remaining_months = Column(Integer)
    remaining_days = Column(Integer)
    cell_number = Column(Text, nullable=False)
    cell_type = Column(ForeignKey('celltype.id'), index=True)
    release_date = Column(DateTime)
    exit_date = Column(DateTime)
    reason_for_release = Column(Text, nullable=False)
    with_children = Column(Boolean)
    release_type = Column(ForeignKey('releasetype.id'), index=True)
    receiving_officer = Column(ForeignKey('prisonofficer.id'), nullable=False, index=True)
    releasing_officer = Column(ForeignKey('prisonofficer.id'), nullable=False, index=True)

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


class Commitaltype(Base):
    __tablename__ = 'commitaltype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('commitaltype_id_seq'::regclass)"))
    maxduration = Column(INTERVAL(fields='day to second'))


class Complaint(Base):
    __tablename__ = 'complaint'

    id = Column(Integer, primary_key=True, server_default=text("nextval('complaint_id_seq'::regclass)"))
    active = Column(Boolean)
    ob_number = Column(String(20), nullable=False)
    police_station = Column(ForeignKey('policestation.id'), nullable=False, index=True)
    daterecvd = Column(DateTime, nullable=False)
    datefiled = Column(DateTime)
    datecaseopened = Column(DateTime)
    casesummary = Column(String(2000), nullable=False)
    complaintstatement = Column(Text, nullable=False)
    circumstances = Column(Text, nullable=False)
    reportingofficer = Column(ForeignKey('policeofficer.id'), nullable=False, index=True)
    casefileinformation = Column(Text, nullable=False)
    p_request_help = Column(Boolean)
    p_instruction = Column(Text, nullable=False)
    p_submitted = Column(Boolean)
    p_submission_date = Column(DateTime)
    p_submission_notes = Column(Text, nullable=False)
    p_closed = Column(Text, nullable=False)
    p_evaluation = Column(Text, nullable=False)
    p_recommend_charge = Column(Boolean)
    charge_sheet = Column(Text, nullable=False)
    charge_sheet_docx = Column(Text, nullable=False)
    evaluating_prosecutor_team = Column(ForeignKey('prosecutorteam.id'), index=True)
    magistrate_report_date = Column(DateTime)
    reported_to_judicial_officer = Column(ForeignKey('judicialofficer.id'), index=True)
    closed = Column(Boolean)
    close_date = Column(DateTime)
    close_reason = Column(Text, nullable=False)

    prosecutorteam = relationship('Prosecutorteam')
    policestation = relationship('Policestation')
    judicialofficer = relationship('Judicialofficer')
    policeofficer = relationship('Policeofficer')
    complaintcategory = relationship('Complaintcategory', secondary='complaint_complaintcategory')
    courtcase = relationship('Courtcase', secondary='complaint_courtcase')


class Party(Complaint):
    __tablename__ = 'party'

    complaints = Column(ForeignKey('complaint.id'), primary_key=True)
    statement = Column(String(1000), nullable=False)
    statementdate = Column(DateTime)
    complaint_role = Column(ForeignKey('complaintrole.id'), nullable=False, index=True)
    notes = Column(Text, nullable=False)
    dateofrepresentation = Column(DateTime)
    party_type = Column(ForeignKey('partytype.id'), nullable=False, index=True)
    relative = Column(ForeignKey('party.complaints'), nullable=False, index=True)
    relationship_type = Column(Text, nullable=False)
    biodata = Column(ForeignKey('biodata.id'), nullable=False, index=True)
    is_infant = Column(Boolean)
    is_minor = Column(Boolean)
    miranda_read = Column(Boolean)
    miranda_date = Column(DateTime)
    miranda_witness = Column(Text, nullable=False)

    biodatum = relationship('Biodatum')
    complaintrole = relationship('Complaintrole')
    partytype = relationship('Partytype')
    parent = relationship('Party', remote_side=[complaints])
    settlement = relationship('Settlement', secondary='party_settlement')


t_complaint_complaintcategory = Table(
    'complaint_complaintcategory', metadata,
    Column('complaint', ForeignKey('complaint.id'), primary_key=True, nullable=False),
    Column('complaintcategory', ForeignKey('complaintcategory.id'), primary_key=True, nullable=False, index=True)
)


t_complaint_courtcase = Table(
    'complaint_courtcase', metadata,
    Column('complaint', ForeignKey('complaint.id'), primary_key=True, nullable=False),
    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=False, index=True)
)


class Complaintcategory(Base):
    __tablename__ = 'complaintcategory'

    id = Column(Integer, primary_key=True, server_default=text("nextval('complaintcategory_id_seq'::regclass)"))
    complaint_category_parent = Column(ForeignKey('complaintcategory.id'), index=True)

    parent = relationship('Complaintcategory', remote_side=[id])


class Complaintrole(Base):
    __tablename__ = 'complaintrole'

    id = Column(Integer, primary_key=True, server_default=text("nextval('complaintrole_id_seq'::regclass)"))


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, server_default=text("nextval('country_id_seq'::regclass)"))
    name = Column(Text, nullable=False)


class County(Base):
    __tablename__ = 'county'

    id = Column(Integer, primary_key=True, server_default=text("nextval('county_id_seq'::regclass)"))
    country = Column(ForeignKey('country.id'), nullable=False, index=True)

    country1 = relationship('Country')


class Court(Base):
    __tablename__ = 'court'

    id = Column(Integer, primary_key=True, server_default=text("nextval('court_id_seq'::regclass)"))
    court_rank = Column(ForeignKey('courtrank.id'), nullable=False, index=True)
    court_station = Column(ForeignKey('courtstation.id'), nullable=False, index=True)
    town = Column(ForeignKey('town.id'), nullable=False, index=True)

    courtrank = relationship('Courtrank')
    courtstation = relationship('Courtstation')
    town1 = relationship('Town')
    judicialofficer = relationship('Judicialofficer', secondary='court_judicialofficer')


t_court_judicialofficer = Table(
    'court_judicialofficer', metadata,
    Column('court', ForeignKey('court.id'), primary_key=True, nullable=False),
    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)


class Courtaccount(Base):
    __tablename__ = 'courtaccount'

    courts = Column(ForeignKey('court.id'), primary_key=True, nullable=False)
    account__types = Column(ForeignKey('accounttype.id'), primary_key=True, nullable=False, index=True)
    account_number = Column(Text, nullable=False)
    account_name = Column(Text, nullable=False)
    short_code = Column(Text, nullable=False)
    bank_name = Column(Text, nullable=False)

    accounttype = relationship('Accounttype')
    court = relationship('Court')


class Courtcase(Base):
    __tablename__ = 'courtcase'

    id = Column(Integer, primary_key=True, server_default=text("nextval('courtcase_id_seq'::regclass)"))
    docket_number = Column(Text, nullable=False)
    case_number = Column(Text, nullable=False)
    adr = Column(Boolean)
    mediation_proposal = Column(Text, nullable=False)
    case_received_date = Column(Date)
    case_filed_date = Column(Date)
    case_summary = Column(Text, nullable=False)
    filing_prosecutor = Column(ForeignKey('prosecutor.id'), index=True)
    fast_track = Column(Boolean)
    priority = Column(Integer)
    object_of_litigation = Column(Text, nullable=False)
    grounds = Column(Text, nullable=False)
    prosecution_prayer = Column(Text, nullable=False)
    pretrial_date = Column(Date)
    pretrial_notes = Column(Text, nullable=False)
    pretrial_registrar = Column(ForeignKey('judicialofficer.id'), index=True)
    case_admissible = Column(Boolean)
    indictment_date = Column(Text, nullable=False)
    judgement = Column(Text, nullable=False)
    judgement_docx = Column(Text, nullable=False)
    case_link_type = Column(ForeignKey('caselinktype.id'), index=True)
    linked_cases = Column(ForeignKey('courtcase.id'), index=True)
    appealed = Column(Boolean)
    appeal_number = Column(Text, nullable=False)
    inventory_of_docket = Column(Text, nullable=False)
    next_hearing_date = Column(Date)
    interlocutory_judgement = Column(Text, nullable=False)
    reopen = Column(Boolean)
    reopen_reason = Column(Text, nullable=False)
    combined_case = Column(Boolean)
    value_in_dispute = Column(Numeric(12, 2))
    award = Column(Numeric(12, 2))
    govt_liability = Column(Text, nullable=False)
    active = Column(Boolean)
    active_date = Column(DateTime)

    caselinktype = relationship('Caselinktype')
    prosecutor = relationship('Prosecutor')
    parent = relationship('Courtcase', remote_side=[id])
    judicialofficer = relationship('Judicialofficer')
    judicialofficer1 = relationship('Judicialofficer', secondary='courtcase_judicialofficer')
    lawfirm = relationship('Lawfirm', secondary='courtcase_lawfirm')


t_courtcase_judicialofficer = Table(
    'courtcase_judicialofficer', metadata,
    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=False),
    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)


t_courtcase_lawfirm = Table(
    'courtcase_lawfirm', metadata,
    Column('courtcase', ForeignKey('courtcase.id'), primary_key=True, nullable=False),
    Column('lawfirm', ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)


class Courtrank(Base):
    __tablename__ = 'courtrank'

    id = Column(Integer, primary_key=True, server_default=text("nextval('courtrank_id_seq'::regclass)"))


class Courtstation(Base):
    __tablename__ = 'courtstation'

    id = Column(Integer, primary_key=True, server_default=text("nextval('courtstation_id_seq'::regclass)"))


class Crime(Base):
    __tablename__ = 'crime'

    id = Column(Integer, primary_key=True, server_default=text("nextval('crime_id_seq'::regclass)"))
    law = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    ref = Column(Text, nullable=False)


class CsiEquipment(Base):
    __tablename__ = 'csi_equipment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('csi_equipment_id_seq'::regclass)"))

    investigationdiary = relationship('Investigationdiary', secondary='csi_equipment_investigationdiary')


t_csi_equipment_investigationdiary = Table(
    'csi_equipment_investigationdiary', metadata,
    Column('csi_equipment', ForeignKey('csi_equipment.id'), primary_key=True, nullable=False),
    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)


class Diagram(Base):
    __tablename__ = 'diagram'

    id = Column(Integer, primary_key=True, server_default=text("nextval('diagram_id_seq'::regclass)"))
    investigation_diary = Column(ForeignKey('investigationdiary.id'), nullable=False, index=True)
    image = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    docx = Column(Text, nullable=False)

    investigationdiary = relationship('Investigationdiary')


class Discipline(Base):
    __tablename__ = 'discipline'

    id = Column(Integer, primary_key=True, server_default=text("nextval('discipline_id_seq'::regclass)"))
    party = Column(ForeignKey('party.complaints'), nullable=False, index=True)
    prison_officer = Column(ForeignKey('prisonofficer.id'), nullable=False, index=True)

    party1 = relationship('Party')
    prisonofficer = relationship('Prisonofficer')


class Doctemplate(Base):
    __tablename__ = 'doctemplate'

    id = Column(Integer, primary_key=True, server_default=text("nextval('doctemplate_id_seq'::regclass)"))
    template = Column(Text, nullable=False)
    docx = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    template_type = Column(ForeignKey('templatetype.id'), nullable=False, index=True)
    icon = Column(Text, nullable=False)

    templatetype = relationship('Templatetype')


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, server_default=text("nextval('document_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    court_case = Column(ForeignKey('courtcase.id'), index=True)
    issue = Column(ForeignKey('issue.id'), index=True)
    document_admissibility = Column(Text, nullable=False)
    admitted = Column(Boolean)
    judicial_officer = Column(ForeignKey('judicialofficer.id'), index=True)
    filing_date = Column(DateTime)
    admisibility_notes = Column(Text, nullable=False)
    docx = Column(Text, nullable=False)
    document_text = Column(Text, nullable=False)
    published = Column(Boolean)
    publish_newspaper = Column(Text, nullable=False)
    publish_date = Column(Date)
    validated = Column(Boolean)
    paid = Column(Boolean)
    page_count = Column(Integer)
    file_byte_count = Column(Numeric(12, 2))
    file_hash = Column(Text, nullable=False)
    file_timestamp = Column(Text, nullable=False)
    file_create_date = Column(DateTime)
    file_update_date = Column(DateTime)
    file_text = Column(Text, nullable=False)
    file_name = Column(Text, nullable=False)
    file_ext = Column(Text, nullable=False)
    file_load_path = Column(Text, nullable=False)
    file_upload_date = Column(DateTime)
    file_parse_status = Column(Text, nullable=False)
    doc_template = Column(ForeignKey('doctemplate.id'), index=True)
    visible = Column(Boolean)
    is_scan = Column(Boolean)
    doc_shelf = Column(Text, nullable=False)
    doc_row = Column(Text, nullable=False)
    doc_room = Column(Text, nullable=False)
    doc_placed_by = Column(Text, nullable=False)
    citation = Column(Text, nullable=False)

    courtcase = relationship('Courtcase')
    doctemplate = relationship('Doctemplate')
    issue1 = relationship('Issue')
    judicialofficer = relationship('Judicialofficer')
    documenttype = relationship('Documenttype', secondary='document_documenttype')


t_document_documenttype = Table(
    'document_documenttype', metadata,
    Column('document', ForeignKey('document.id'), primary_key=True, nullable=False),
    Column('documenttype', ForeignKey('documenttype.id'), primary_key=True, nullable=False, index=True)
)


class Documenttype(Base):
    __tablename__ = 'documenttype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('documenttype_id_seq'::regclass)"))


class Economicclas(Base):
    __tablename__ = 'economicclass'

    id = Column(Integer, primary_key=True, server_default=text("nextval('economicclass_id_seq'::regclass)"))


class Exhibit(Base):
    __tablename__ = 'exhibit'

    id = Column(Integer, primary_key=True, server_default=text("nextval('exhibit_id_seq'::regclass)"))
    investigation_entry = Column(ForeignKey('investigationdiary.id'), nullable=False, index=True)
    photo = Column(Text, nullable=False)
    exhibit_no = Column(Text, nullable=False)
    docx = Column(Text, nullable=False)
    seizure = Column(ForeignKey('seizure.id'), nullable=False, index=True)

    investigationdiary = relationship('Investigationdiary')
    seizure1 = relationship('Seizure')


class Expert(Base):
    __tablename__ = 'expert'

    id = Column(Integer, primary_key=True, server_default=text("nextval('expert_id_seq'::regclass)"))
    institution = Column(Text, nullable=False)
    jobtitle = Column(Text, nullable=False)
    credentials = Column(Text, nullable=False)

    experttype = relationship('Experttype', secondary='expert_experttype')


t_expert_experttype = Table(
    'expert_experttype', metadata,
    Column('expert', ForeignKey('expert.id'), primary_key=True, nullable=False),
    Column('experttype', ForeignKey('experttype.id'), primary_key=True, nullable=False, index=True)
)


class Experttestimony(Base):
    __tablename__ = 'experttestimony'

    requesting_officer = Column(ForeignKey('investigating_officer.police_officers'), nullable=False, index=True)
    investigation_entries = Column(ForeignKey('investigationdiary.id'), primary_key=True, nullable=False)
    experts = Column(ForeignKey('expert.id'), primary_key=True, nullable=False, index=True)
    task_given = Column(Text, nullable=False)
    summary_of_facts = Column(Text, nullable=False)
    statement = Column(Text, nullable=False)
    testimony_date = Column(DateTime)
    task_request_date = Column(Date)
    docx = Column(Text, nullable=False)
    validated = Column(Boolean)

    expert = relationship('Expert')
    investigationdiary = relationship('Investigationdiary')
    investigating_officer = relationship('InvestigatingOfficer')


class Experttype(Base):
    __tablename__ = 'experttype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('experttype_id_seq'::regclass)"))


class Feeclas(Base):
    __tablename__ = 'feeclass'

    id = Column(Integer, primary_key=True, server_default=text("nextval('feeclass_id_seq'::regclass)"))
    fee_type = Column(ForeignKey('feeclass.id'), index=True)

    parent = relationship('Feeclas', remote_side=[id])


class Feetype(Base):
    __tablename__ = 'feetype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('feetype_id_seq'::regclass)"))
    filing_fee_type = Column(ForeignKey('feeclass.id'), nullable=False, index=True)
    amount = Column(Numeric(12, 2))
    unit = Column(Text, nullable=False)
    min_fee = Column(Numeric(12, 2))
    max_fee = Column(Numeric(12, 2))
    description = Column(Text)
    guide_sec = Column(Text)
    guide_clause = Column(Text)
    account_type = Column(ForeignKey('accounttype.id'), nullable=False, index=True)

    accounttype = relationship('Accounttype')
    feeclas = relationship('Feeclas')


class Healthevent(Base):
    __tablename__ = 'healthevent'

    id = Column(Integer, primary_key=True, server_default=text("nextval('healthevent_id_seq'::regclass)"))
    party = Column(ForeignKey('party.complaints'), nullable=False, index=True)
    reporting_prison_officer = Column(ForeignKey('prisonofficer.id'), index=True)
    health_event_type = Column(ForeignKey('healtheventtype.id'), nullable=False, index=True)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    notes = Column(Text, nullable=False)

    healtheventtype = relationship('Healtheventtype')
    party1 = relationship('Party')
    prisonofficer = relationship('Prisonofficer')


class Healtheventtype(Base):
    __tablename__ = 'healtheventtype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('healtheventtype_id_seq'::regclass)"))


class Hearing(Base):
    __tablename__ = 'hearing'

    id = Column(Integer, primary_key=True, server_default=text("nextval('hearing_id_seq'::regclass)"))
    court_cases = Column(ForeignKey('courtcase.id'), index=True)
    hearing_type = Column(ForeignKey('hearingtype.id'), nullable=False, index=True)
    schedule_status = Column(ForeignKey('schedulestatustype.id'), nullable=False, index=True)
    hearing_date = Column(Date)
    reason = Column(Text, nullable=False)
    sequence = Column(BigInteger)
    yearday = Column(BigInteger)
    starttime = Column(Time)
    endtime = Column(Time)
    notes = Column(Text, nullable=False)
    completed = Column(Boolean)
    adjourned_to = Column(Date)
    adjournment_reason = Column(Text, nullable=False)
    transcript = Column(Text, nullable=False)
    atendance = Column(Text, nullable=False)
    next_hearing_date = Column(Date)
    postponement_reason = Column(Text, nullable=False)

    courtcase = relationship('Courtcase')
    hearingtype = relationship('Hearingtype')
    schedulestatustype = relationship('Schedulestatustype')
    issue = relationship('Issue', secondary='hearing_issue')
    judicialofficer = relationship('Judicialofficer', secondary='hearing_judicialofficer')
    lawfirm = relationship('Lawfirm', secondary='hearing_lawfirm')
    lawfirm1 = relationship('Lawfirm', secondary='hearing_lawfirm_2')


t_hearing_issue = Table(
    'hearing_issue', metadata,
    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=False),
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_judicialofficer = Table(
    'hearing_judicialofficer', metadata,
    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=False),
    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_lawfirm = Table(
    'hearing_lawfirm', metadata,
    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=False),
    Column('lawfirm', ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_lawfirm_2 = Table(
    'hearing_lawfirm_2', metadata,
    Column('hearing', ForeignKey('hearing.id'), primary_key=True, nullable=False),
    Column('lawfirm', ForeignKey('lawfirm.id'), primary_key=True, nullable=False, index=True)
)


class Hearingtype(Base):
    __tablename__ = 'hearingtype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('hearingtype_id_seq'::regclass)"))
    hearing_type = Column(ForeignKey('hearingtype.id'), index=True)

    parent = relationship('Hearingtype', remote_side=[id])


class Instancecrime(Base):
    __tablename__ = 'instancecrime'

    parties = Column(ForeignKey('party.complaints'), primary_key=True, nullable=False)
    crimes = Column(ForeignKey('crime.id'), primary_key=True, nullable=False, index=True)
    crime_detail = Column(Text, nullable=False)
    tffender_type = Column(Text, nullable=False)
    crime_date = Column(DateTime)
    date_note = Column(Text, nullable=False)
    place_of_crime = Column(Text, nullable=False)
    place_note = Column(Text, nullable=False)

    crime = relationship('Crime')
    party = relationship('Party')
    issue = relationship('Issue', secondary='instancecrime_issue')


t_instancecrime_issue = Table(
    'instancecrime_issue', metadata,
    Column('instancecrime_parties', Integer, primary_key=True, nullable=False),
    Column('instancecrime_crimes', Integer, primary_key=True, nullable=False),
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['instancecrime_parties', 'instancecrime_crimes'], ['instancecrime.parties', 'instancecrime.crimes'])
)


class Interview(Base):
    __tablename__ = 'interview'

    id = Column(Integer, primary_key=True, server_default=text("nextval('interview_id_seq'::regclass)"))
    investigation_entry = Column(ForeignKey('investigationdiary.id'), nullable=False, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    validated = Column(Boolean)
    language = Column(Text, nullable=False)

    investigationdiary = relationship('Investigationdiary')


t_investigating_officer_investigationdiary = Table(
    'investigating_officer_investigationdiary', metadata,
    Column('investigating_officer', ForeignKey('investigating_officer.police_officers'), primary_key=True, nullable=False),
    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)


class Investigationdiary(Base):
    __tablename__ = 'investigationdiary'

    id = Column(Integer, primary_key=True, server_default=text("nextval('investigationdiary_id_seq'::regclass)"))
    complaint = Column(ForeignKey('complaint.id'), nullable=False, index=True)
    activity = Column(Text, nullable=False)
    location = Column(Text, nullable=False)
    outcome = Column(Text, nullable=False)
    equipmentresults = Column(Text, nullable=False)
    startdate = Column(DateTime, nullable=False)
    enddate = Column(DateTime)
    advocate_present = Column(Text, nullable=False)
    summons_statement = Column(Text, nullable=False)
    arrest_statement = Column(Text, nullable=False)
    arrest_warrant = Column(Text, nullable=False)
    search_seizure_statement = Column(Text, nullable=False)
    docx = Column(Text, nullable=False)
    detained = Column(Text, nullable=False)
    detained_at = Column(Text, nullable=False)
    provisional_release_statement = Column(Text, nullable=False)
    warrant_type = Column(ForeignKey('warranttype.id'), index=True)
    warrant_issued_by = Column(Text, nullable=False)
    warrant_issue_date = Column(Date)
    warrant_delivered_by = Column(Text, nullable=False)
    warrant_received_by = Column(Text, nullable=False)
    warrant_serve_date = Column(Text, nullable=False)
    warrant_docx = Column(Text, nullable=False)
    warrant_upload_date = Column(Text, nullable=False)

    complaint1 = relationship('Complaint')
    warranttype = relationship('Warranttype')
    party = relationship('Party', secondary='investigationdiary_party')
    vehicle = relationship('Vehicle', secondary='investigationdiary_vehicle')


t_investigationdiary_party = Table(
    'investigationdiary_party', metadata,
    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


t_investigationdiary_vehicle = Table(
    'investigationdiary_vehicle', metadata,
    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=False),
    Column('vehicle', ForeignKey('vehicle.id'), primary_key=True, nullable=False, index=True)
)


class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True, server_default=text("nextval('issue_id_seq'::regclass)"))
    issue = Column(Text, nullable=False)
    facts = Column(Text)
    counter_claim = Column(Boolean)
    argument = Column(Text, nullable=False)
    argument_date = Column(Date)
    argument_docx = Column(Text)
    rebuttal = Column(Text, nullable=False)
    rebuttal_date = Column(Date)
    rebuttal_docx = Column(Text)
    hearing_date = Column(Date)
    determination = Column(Text, nullable=False)
    dtermination_date = Column(Date)
    determination_docx = Column(Text, nullable=False)
    resolved = Column(Boolean)
    defense_lawyer = Column(ForeignKey('lawyer.id'), nullable=False, index=True)
    prosecutor = Column(ForeignKey('prosecutor.id'), index=True)
    judicial_officer = Column(ForeignKey('judicialofficer.id'), nullable=False, index=True)
    court_case = Column(ForeignKey('courtcase.id'), nullable=False, index=True)
    tasks = Column(Text, nullable=False)
    is_criminal = Column(Boolean)
    moral_element = Column(Text, nullable=False)
    material_element = Column(Text, nullable=False)
    legal_element = Column(Text, nullable=False)
    debt_amount = Column(Numeric(12, 2))

    courtcase = relationship('Courtcase')
    lawyer = relationship('Lawyer')
    judicialofficer = relationship('Judicialofficer')
    prosecutor1 = relationship('Prosecutor')
    lawyer1 = relationship('Lawyer', secondary='issue_lawyer')
    legalreference = relationship('Legalreference', secondary='issue_legalreference')
    legalreference1 = relationship('Legalreference', secondary='issue_legalreference_2')
    party = relationship('Party', secondary='issue_party')
    party1 = relationship('Party', secondary='issue_party_2')


t_issue_lawyer = Table(
    'issue_lawyer', metadata,
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False),
    Column('lawyer', ForeignKey('lawyer.id'), primary_key=True, nullable=False, index=True)
)


t_issue_legalreference = Table(
    'issue_legalreference', metadata,
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False),
    Column('legalreference', ForeignKey('legalreference.id'), primary_key=True, nullable=False, index=True)
)


t_issue_legalreference_2 = Table(
    'issue_legalreference_2', metadata,
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False),
    Column('legalreference', ForeignKey('legalreference.id'), primary_key=True, nullable=False, index=True)
)


t_issue_party = Table(
    'issue_party', metadata,
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False),
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


t_issue_party_2 = Table(
    'issue_party_2', metadata,
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False),
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


class Judicialofficer(Base):
    __tablename__ = 'judicialofficer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('judicialofficer_id_seq'::regclass)"))
    rank = Column(ForeignKey('judicialrank.id'), nullable=False, index=True)
    judicial_role = Column(ForeignKey('judicialrole.id'), nullable=False, index=True)
    court_station = Column(ForeignKey('courtstation.id'), nullable=False, index=True)

    courtstation = relationship('Courtstation')
    judicialrole = relationship('Judicialrole')
    judicialrank = relationship('Judicialrank')


class Judicialrank(Base):
    __tablename__ = 'judicialrank'

    id = Column(Integer, primary_key=True, server_default=text("nextval('judicialrank_id_seq'::regclass)"))


class Judicialrole(Base):
    __tablename__ = 'judicialrole'

    id = Column(Integer, primary_key=True, server_default=text("nextval('judicialrole_id_seq'::regclass)"))


class Lawfirm(Base):
    __tablename__ = 'lawfirm'

    id = Column(Integer, primary_key=True, server_default=text("nextval('lawfirm_id_seq'::regclass)"))


class Lawyer(Base):
    __tablename__ = 'lawyer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('lawyer_id_seq'::regclass)"))
    law_firm = Column(ForeignKey('lawfirm.id'), index=True)
    bar_no = Column(Text, nullable=False)
    bar_date = Column(Date)

    lawfirm = relationship('Lawfirm')
    party = relationship('Party', secondary='lawyer_party')


t_lawyer_party = Table(
    'lawyer_party', metadata,
    Column('lawyer', ForeignKey('lawyer.id'), primary_key=True, nullable=False),
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)


class Legalreference(Base):
    __tablename__ = 'legalreference'

    id = Column(Integer, primary_key=True, server_default=text("nextval('legalreference_id_seq'::regclass)"))
    ref = Column(Text, nullable=False)
    verbatim = Column(Text, nullable=False)
    public = Column(Boolean)
    commentary = Column(Text, nullable=False)
    validated = Column(Boolean)
    citation = Column(Text, nullable=False)
    quote = Column(Text, nullable=False)
    interpretation = Column(Text, nullable=False)


class Nextofkin(Base):
    __tablename__ = 'nextofkin'

    id = Column(Integer, primary_key=True, server_default=text("nextval('nextofkin_id_seq'::regclass)"))
    biodata = Column(ForeignKey('biodata.id'), nullable=False, index=True)
    childunder4 = Column(Boolean)

    biodatum = relationship('Biodatum')


class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True, server_default=text("nextval('notification_id_seq'::regclass)"))
    contact = Column(Text, nullable=False)
    message = Column(Text, nullable=False)
    confirmation = Column(Text, nullable=False)
    notification_register = Column(ForeignKey('notificationregister.id'), index=True)
    add_date = Column(DateTime)
    send_date = Column(DateTime)
    sent = Column(Boolean)
    delivered = Column(Boolean)
    retries = Column(Integer)
    abandon = Column(Boolean)
    retry_count = Column(Integer)

    notificationregister = relationship('Notificationregister')


class Notificationregister(Base):
    __tablename__ = 'notificationregister'

    id = Column(Integer, primary_key=True, server_default=text("nextval('notificationregister_id_seq'::regclass)"))
    notification_type = Column(ForeignKey('notificationtype.id'), nullable=False, index=True)
    contact = Column(Text, nullable=False)
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


class Notificationtype(Base):
    __tablename__ = 'notificationtype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('notificationtype_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class Notifyevent(Base):
    __tablename__ = 'notifyevent'

    id = Column(Integer, primary_key=True, server_default=text("nextval('notifyevent_id_seq'::regclass)"))


class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True, server_default=text("nextval('page_id_seq'::regclass)"))
    document = Column(ForeignKey('document.id'), nullable=False, index=True)
    page_image = Column(LargeBinary)
    page_no = Column(BigInteger)
    page_text = Column(Text, nullable=False)
    image_ext = Column(Text)
    image_width = Column(Text)
    image_height = Column(Text)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
    upload_dt = Column(DateTime)

    document1 = relationship('Document')


t_party_settlement = Table(
    'party_settlement', metadata,
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False),
    Column('settlement', ForeignKey('settlement.id'), primary_key=True, nullable=False, index=True)
)


class Partytype(Base):
    __tablename__ = 'partytype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('partytype_id_seq'::regclass)"))


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('payment_id_seq'::regclass)"))
    bill = Column(ForeignKey('bill.id'), nullable=False, index=True)
    amount = Column(Text, nullable=False)
    payment_ref = Column(Text, nullable=False)
    date_paid = Column(DateTime)
    phone_number = Column(String(20))
    validated = Column(Boolean)
    payment_description = Column(Text)

    bill1 = relationship('Bill')


class Personaleffect(Base):
    __tablename__ = 'personaleffect'

    id = Column(Integer, primary_key=True, server_default=text("nextval('personaleffect_id_seq'::regclass)"))
    party = Column(ForeignKey('party.complaints'), nullable=False, index=True)
    personal_effects_category = Column(ForeignKey('personaleffectscategory.id'), nullable=False, index=True)

    party1 = relationship('Party')
    personaleffectscategory = relationship('Personaleffectscategory')


class Personaleffectscategory(Base):
    __tablename__ = 'personaleffectscategory'

    id = Column(Integer, primary_key=True, server_default=text("nextval('personaleffectscategory_id_seq'::regclass)"))


class Policeofficer(Base):
    __tablename__ = 'policeofficer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('policeofficer_id_seq'::regclass)"))
    police_rank = Column(ForeignKey('policeofficerrank.id'), nullable=False, index=True)
    servicenumber = Column(String(100), nullable=False, unique=True)

    policeofficerrank = relationship('Policeofficerrank')
    policestation = relationship('Policestation', secondary='policeofficer_policestation')


class InvestigatingOfficer(Policeofficer):
    __tablename__ = 'investigating_officer'

    police_officers = Column(ForeignKey('policeofficer.id'), primary_key=True)
    date_assigned = Column(DateTime)
    lead_investigator = Column(Integer)

    investigationdiary = relationship('Investigationdiary', secondary='investigating_officer_investigationdiary')


t_policeofficer_policestation = Table(
    'policeofficer_policestation', metadata,
    Column('policeofficer', ForeignKey('policeofficer.id'), primary_key=True, nullable=False),
    Column('policestation', ForeignKey('policestation.id'), primary_key=True, nullable=False, index=True)
)


class Policeofficerrank(Base):
    __tablename__ = 'policeofficerrank'

    id = Column(Integer, primary_key=True, server_default=text("nextval('policeofficerrank_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    sequence = Column(Integer)


class Policestation(Base):
    __tablename__ = 'policestation'

    id = Column(Integer, primary_key=True, server_default=text("nextval('policestation_id_seq'::regclass)"))
    town = Column(ForeignKey('town.id'), index=True)
    officer_commanding = Column(ForeignKey('policeofficer.id'), nullable=False, index=True)
    police_station_rank = Column(ForeignKey('policestationrank.id'), nullable=False, index=True)

    policeofficer = relationship('Policeofficer')
    policestationrank = relationship('Policestationrank')
    town1 = relationship('Town')


class Policestationrank(Base):
    __tablename__ = 'policestationrank'

    id = Column(Integer, primary_key=True, server_default=text("nextval('policestationrank_id_seq'::regclass)"))


class Prison(Base):
    __tablename__ = 'prison'

    id = Column(Integer, primary_key=True, server_default=text("nextval('prison_id_seq'::regclass)"))
    town = Column(ForeignKey('town.id'), nullable=False, index=True)

    town1 = relationship('Town')


class Prisonofficer(Base):
    __tablename__ = 'prisonofficer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('prisonofficer_id_seq'::regclass)"))
    prison = Column(ForeignKey('prison.id'), nullable=False, index=True)
    prison_officer_rank = Column(ForeignKey('prisonofficerrank.id'), nullable=False, index=True)

    prison1 = relationship('Prison')
    prisonofficerrank = relationship('Prisonofficerrank')


class Prisonofficerrank(Base):
    __tablename__ = 'prisonofficerrank'

    id = Column(Integer, primary_key=True, server_default=text("nextval('prisonofficerrank_id_seq'::regclass)"))


class Prosecutor(Base):
    __tablename__ = 'prosecutor'

    id = Column(Integer, primary_key=True, server_default=text("nextval('prosecutor_id_seq'::regclass)"))
    prosecutor_team = Column(ForeignKey('prosecutorteam.id'), index=True)
    lawyer = Column(ForeignKey('lawyer.id'), nullable=False, index=True)

    lawyer1 = relationship('Lawyer')
    prosecutorteam = relationship('Prosecutorteam')


class Prosecutorteam(Base):
    __tablename__ = 'prosecutorteam'

    id = Column(Integer, primary_key=True, server_default=text("nextval('prosecutorteam_id_seq'::regclass)"))


class Releasetype(Base):
    __tablename__ = 'releasetype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('releasetype_id_seq'::regclass)"))


class Religion(Base):
    __tablename__ = 'religion'

    id = Column(Integer, primary_key=True, server_default=text("nextval('religion_id_seq'::regclass)"))


class Schedulestatustype(Base):
    __tablename__ = 'schedulestatustype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('schedulestatustype_id_seq'::regclass)"))


class Seizure(Base):
    __tablename__ = 'seizure'

    id = Column(Integer, primary_key=True, server_default=text("nextval('seizure_id_seq'::regclass)"))
    investigation_diary = Column(ForeignKey('investigationdiary.id'), nullable=False, index=True)
    owner = Column(Text, nullable=False)
    item = Column(Text, nullable=False)
    item_packaging = Column(Text, nullable=False)
    item_pic = Column(Text, nullable=False)
    premises = Column(Text, nullable=False)
    reg_no = Column(Text, nullable=False)
    witness = Column(Text, nullable=False)
    notes = Column(Text, nullable=False)
    docx = Column(Text, nullable=False)
    item_description = Column(Text, nullable=False)
    returned = Column(Boolean)
    return_date = Column(DateTime)
    return_notes = Column(Text, nullable=False)
    return_signed_receipt = Column(Text, nullable=False)
    destroyed = Column(Boolean)
    destruction_date = Column(Date)
    destruction_witnesses = Column(Text, nullable=False)
    destruction_notes = Column(Text, nullable=False)
    disposed = Column(Boolean)
    sold_to = Column(Text, nullable=False)
    disposal_date = Column(Date)
    disposal_price = Column(Numeric(12, 2))
    disposal_receipt = Column(Text, nullable=False)
    recovery_town = Column(ForeignKey('town.id'), index=True)
    destruction_pic = Column(Text, nullable=False)
    is_evidence = Column(Boolean)
    immovable = Column(Boolean)

    investigationdiary = relationship('Investigationdiary')
    town = relationship('Town')


class Settlement(Base):
    __tablename__ = 'settlement'

    id = Column(Integer, primary_key=True, server_default=text("nextval('settlement_id_seq'::regclass)"))
    complaint = Column(ForeignKey('complaint.id'), nullable=False, index=True)
    terms = Column(Text, nullable=False)
    amount = Column(Numeric(12, 2))
    paid = Column(Boolean)
    docx = Column(Text, nullable=False)
    settlor = Column(ForeignKey('party.complaints'), nullable=False, index=True)

    complaint1 = relationship('Complaint')
    party = relationship('Party')


class Subcounty(Base):
    __tablename__ = 'subcounty'

    id = Column(Integer, primary_key=True, server_default=text("nextval('subcounty_id_seq'::regclass)"))
    county = Column(ForeignKey('county.id'), nullable=False, index=True)

    county1 = relationship('County')


class Templatetype(Base):
    __tablename__ = 'templatetype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('templatetype_id_seq'::regclass)"))
    template_type = Column(ForeignKey('templatetype.id'), index=True)

    parent = relationship('Templatetype', remote_side=[id])


class Town(Base):
    __tablename__ = 'town'

    id = Column(Integer, primary_key=True, server_default=text("nextval('town_id_seq'::regclass)"))

    ward = relationship('Ward', secondary='town_ward')


t_town_ward = Table(
    'town_ward', metadata,
    Column('town', ForeignKey('town.id'), primary_key=True, nullable=False),
    Column('ward', ForeignKey('ward.id'), primary_key=True, nullable=False, index=True)
)


class Transcript(Base):
    __tablename__ = 'transcript'

    id = Column(Integer, primary_key=True, server_default=text("nextval('transcript_id_seq'::regclass)"))
    video = Column(Text, nullable=False)
    audio = Column(Text, nullable=False)
    add_date = Column(DateTime)
    asr_transcript = Column(Text, nullable=False)
    asr_date = Column(DateTime)
    edited_transcript = Column(Text, nullable=False)
    edit_date = Column(DateTime)
    certified_transcript = Column(Text, nullable=False)
    certfiy_date = Column(DateTime)
    locked = Column(Boolean)
    hearing = Column(ForeignKey('hearing.id'), nullable=False, index=True)

    hearing1 = relationship('Hearing')


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True, server_default=text("nextval('vehicle_id_seq'::regclass)"))
    police_station = Column(ForeignKey('policestation.id'), nullable=False, index=True)
    make = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    regno = Column(String(100), nullable=False)

    policestation = relationship('Policestation')


class Ward(Base):
    __tablename__ = 'ward'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ward_id_seq'::regclass)"))
    subcounty = Column(ForeignKey('subcounty.id'), nullable=False, index=True)

    subcounty1 = relationship('Subcounty')


class Warranttype(Base):
    __tablename__ = 'warranttype'

    id = Column(Integer, primary_key=True, server_default=text("nextval('warranttype_id_seq'::regclass)"))

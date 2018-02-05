from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from decimal import Decimal
from pony.orm import *


db = Database()


class County(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    subcounties = Set('Subcounty')
    country = Required('Country')


class Subcounty(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    county = Required(County)
    wards = Set('Ward')


class Ward(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    subcounty = Required(Subcounty)
    towns = Set('Town')


class Town(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    wards = Set(Ward)
    police_stations = Set('PoliceStation')
    courts = Set('Court')
    seizures = Set('Seizure')
    prisons = Set('Prison')


class Country(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    counties = Set(County)
    Name = Optional(str)


class PoliceStation(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    town = Optional(Town)
    police_officers = Set('PoliceOfficer', reverse='Assigned_Station')
    complaints = Set('Complaint')
    vehicles = Set('Vehicle')
    officer_commanding = Required('PoliceOfficer', reverse='station_command')
    police_station_rank = Required('PoliceStationRank')
    commitals = Set('Commital')


class PoliceOfficer(db.Entity):
    """PersonMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    Assigned_Station = Set(PoliceStation, reverse='police_officers')
    police_rank = Required('PoliceOfficerRank')
    ServiceNumber = Required(str, 100, unique=True)
    complaint_recorded = Set('Complaint')
    investigating_cases = Set('Investigating_officer')
    station_command = Set(PoliceStation, reverse='officer_commanding')


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    Active = Optional(str)
    OB_Number = Optional(str)
    police_station = Required(PoliceStation)
    DateRecvd = Required(datetime, default=lambda: datetime.now())
    DateFiled = Optional(datetime, default=lambda: datetime.now())
    DateCaseOpened = Optional(datetime, default=lambda: datetime.now())
    CaseSummary = Optional(str, 2000)
    complaint_categories = Set('ComplaintCategory')
    parties = Set('Party')
    ComplaintStatement = Optional(str)
    Circumstances = Optional(str)
    ReportingOfficer = Required(PoliceOfficer)
    investigation_entries = Set('InvestigationDiary')
    CaseFileInformation = Optional(str)
    p_request_help = Optional(bool)
    p_instruction = Optional(LongStr)
    p_submitted = Optional(bool)
    p_submission_date = Optional(datetime)
    p_submission_notes = Optional(str)
    p_closed = Optional(str)
    closed = Optional(bool)
    p_evaluation = Optional(LongStr)
    p_recommend_charge = Optional(bool)
    settlements = Set('Settlement')
    charge_sheet = Optional(LongStr)
    charge_sheet_docx = Optional(LongStr)
    evaluating_prosecutor_team = Optional('ProsecutorTeam')
    court_cases = Set('CourtCase')


class Investigating_officer(db.Entity):
    police_officers = PrimaryKey(PoliceOfficer)
    DateAssigned = Optional(datetime, default=lambda: datetime.now())
    LeadInvestigator = Optional(int)
    investigation_entries = Set('InvestigationDiary')
    expert_Request = Set('ExpertTestimony')


class ComplaintCategory(db.Entity):
    """Human Trafficking, Gender Based Violence, Committed by a Minor, """
    id = PrimaryKey(int, auto=True)
    complaints = Set(Complaint)
    complaint_categories = Set('ComplaintCategory', reverse='complaint_category_Parent')
    complaint_category_Parent = Optional('ComplaintCategory', reverse='complaint_categories')


class Party(db.Entity):
    """PersonMixin, ContactMixin"""
    complaints = PrimaryKey(Complaint)
    Statement = Optional(str, 1000)
    StatementDate = Optional(datetime, default=lambda: datetime.now())
    complaint_role = Required('ComplaintRole')
    Notes = Optional(str)  # Notes by recording officer
    represented_by = Set('Lawyer')
    DateOfRepresentation = Optional(datetime)
    investigation_diaries = Set('InvestigationDiary')
    instance_crimes = Set('InstanceCrime')
    settlements = Set('Settlement', reverse='settlor')
    settlees = Set('Settlement', reverse='setlee')
    plaintiff_issues = Set('Issue', reverse='InjuredParties')
    DefenseIssues = Set('Issue', reverse='DefendingParties')
    party_type = Required('PartyType')
    parties = Set('Party', reverse='relative')
    relative = Required('Party', reverse='parties')
    Relationship_type = Optional(str)
    commitals = Set('Commital')
    biodata = Required('Biodata')
    disciplines = Set('Discipline')
    personal_effects = Set('PersonalEffect')


class ComplaintRole(db.Entity):
    """witness, accused, complainant"""
    id = PrimaryKey(int, auto=True)
    parties = Set(Party)


class Lawyer(db.Entity):
    """PersonMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    law_firm = Optional('LawFirm')
    Representing = Set(Party)
    ArgumentIssues = Set('Issue', reverse='Defenselawyer')
    issues = Set('Issue', reverse='plaintiff_lawyers')
    prosecutor = Optional('Prosecutor')
    bar_no = Optional(str)
    bar_date = Optional(date)


class LawFirm(db.Entity):
    """PlaceMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    court_cases = Set('CourtCase')
    lawyers = Set(Lawyer)
    lawyers_defense = Set('Hearing', reverse='lawyers_defense')
    lawyer_plaintiff = Set('Hearing', reverse='lawyer_plaintiff')


class Crime(db.Entity):
    id = PrimaryKey(int, auto=True)
    Law = Optional(str)
    Description = Optional(str)
    Ref = Optional(str)
    instance_crimes = Set('InstanceCrime')


class InstanceCrime(db.Entity):
    parties = Required(Party)
    crimes = Required(Crime)
    CrimeDetail = Optional(str)
    OffenderType = Optional(str)  # Accessory, Perpetrator
    CrimeDate = Optional(datetime, default=lambda: datetime.now())
    DateNote = Optional(str)
    CrimePlace = Optional(str)
    PlaceNote = Optional(str)
    issues = Set('Issue')
    PrimaryKey(parties, crimes)


class InvestigationDiary(db.Entity):
    id = PrimaryKey(int, auto=True)
    complaint = Required(Complaint)
    investigating_officers = Set(Investigating_officer)
    CSI_equipment = Set('CSI_Equipment')
    Activity = Optional(str)
    Location = Optional(str)
    Outcome = Optional(str)
    EquipmentResults = Optional(str)
    vehicles = Set('Vehicle')
    StartDate = Required(datetime, default=lambda: datetime.now())
    EndDate = Optional(datetime, default=lambda: datetime.now())
    expert_testimonies = Set('ExpertTestimony')
    advocate_present = Optional(str)
    interviews = Set('Interview')
    Summons_Statement = Optional(LongStr)
    Arrest_Statement = Optional(LongStr)
    exhibits = Set('Exhibit')
    Arrest_warrant = Optional(LongStr)
    Search_Seizure_Statement = Optional(str)
    docx = Optional(str)
    Detained = Optional(str)
    Detained_at = Optional(str)
    provisional_release_statement = Optional(str)
    parties = Set(Party)
    items_seized = Set('Seizure')
    warrant_type = Optional('WarrantType')
    Warrant_issued_by = Optional(str)
    warrant_issue_date = Optional(date)
    warrant_delivered_by = Optional(str)
    warrant_received_by = Optional(str)
    warrant_serve_date = Optional(str)
    warrant_docx = Optional(str)
    warrant_upload_date = Optional(str)
    diagrams = Set('Diagram')


class CSI_Equipment(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    investigation_entries = Set(InvestigationDiary)


class Exhibit(db.Entity):
    id = PrimaryKey(int, auto=True)
    investigation_entry = Required(InvestigationDiary)
    Photo = Optional(str)
    ExhibitNo = Optional(str)
    docx = Optional(str)
    seizure = Required('Seizure')


class Vehicle(db.Entity):
    id = PrimaryKey(int, auto=True)
    police_station = Required(PoliceStation)
    investigation_entries = Set(InvestigationDiary)
    make = Optional(str)
    model = Optional(str)
    regNo = Optional(str)


class Expert(db.Entity):
    """personMixin, ContactMixin
"""
    id = PrimaryKey(int, auto=True)
    expert_testimonies = Set('ExpertTestimony')
    Institution = Optional(str)
    JobTitle = Optional(str)
    Credentials = Optional(str)
    expert_types = Set('ExpertType')


class ExpertTestimony(db.Entity):
    Requesting_officer = Required(Investigating_officer)
    investigation_entries = Required(InvestigationDiary)
    experts = Required(Expert)
    TaskGiven = Optional(LongStr)
    SummaryofFacts = Optional(LongStr)
    Statement = Optional(str)
    TestimonyDate = Optional(datetime)
    TaskRequestDate = Optional(date)
    docx = Optional(str)
    validated = Optional(bool)
    PrimaryKey(investigation_entries, experts)


class Interview(db.Entity):
    id = PrimaryKey(int, auto=True)
    investigation_entry = Required(InvestigationDiary)
    Question = Optional(LongStr)
    Answer = Optional(LongStr)
    Validated = Optional(bool)
    Language = Optional(str)


class Seizure(db.Entity):
    id = PrimaryKey(int, auto=True)
    investigation_diary = Required(InvestigationDiary)
    Owner = Optional(str)
    item = Optional(str)
    ItemPackaging = Optional(str)
    Item_pic = Optional(str)
    Premises = Optional(str)
    RegNo = Optional(str)
    Witness = Optional(str)
    Notes = Optional(str)
    docx = Optional(str)
    item_description = Optional(str)
    returned = Optional(bool)
    return_date = Optional(datetime)
    Return_notes = Optional(str)
    return_signed_receipt = Optional(str)
    Destroyed = Optional(bool)
    Destruction_date = Optional(date)
    destruction_witnesses = Optional(str)
    destruction_notes = Optional(LongStr)
    disposed = Optional(bool)
    sold_to = Optional(LongStr)
    disposal_date = Optional(date)
    disposal_price = Optional(Decimal)
    disposal_receipt = Optional(LongStr)
    recovery_town = Optional(Town)
    destruction_pic = Optional(LongStr)
    exhibits = Set(Exhibit)
    is_evidence = Optional(bool)
    immovable = Optional(bool)


class WarrantType(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    warrant_issued = Set(InvestigationDiary)
    commitals = Set('Commital')


class Settlement(db.Entity):
    id = PrimaryKey(int, auto=True)
    complaint = Required(Complaint)
    terms = Optional(LongStr)
    amount = Optional(Decimal, default="0.00")
    paid = Optional(bool)
    docx = Optional(str)
    settlor = Required(Party, reverse='settlements')
    setlee = Set(Party, reverse='settlees')


class Issue(db.Entity):
    """Claims and Issues for determination"""
    id = PrimaryKey(int, auto=True)
    Issue = Optional(LongStr)
    Facts = Optional(str)
    counter_claim = Optional(bool)
    Argument = Optional(LongStr)
    ArgumentDate = Optional(date, default=lambda: date.today())
    Argument_docx = Optional(str)
    Rebuttal = Optional(LongStr)
    RebuttalDate = Optional(date, default=lambda: date.today())
    Rebuttal_docx = Optional(str)
    HearingDate = Optional(date)
    Determination = Optional(LongStr)
    DterminationDate = Optional(date)
    Determination_docx = Optional(str)
    Resolved = Optional(bool)
    InjuredParties = Set(Party, reverse='plaintiff_issues')
    DefendingParties = Set(Party, reverse='DefenseIssues')
    Defenselawyer = Required(Lawyer, reverse='ArgumentIssues')
    prosecutor = Optional('Prosecutor')
    judicial_officer = Required('JudicialOfficer')
    court_case = Required('CourtCase')
    plaintiff_lawyers = Set(Lawyer, reverse='issues')
    argument_legal_references = Set('LegalReference', reverse='argument_issues')
    rebuttal_legal_references = Set('LegalReference', reverse='rebuttaL_issues')
    Tasks = Optional(str)
    instance_crimes = Set(InstanceCrime)
    is_criminal = Optional(bool)
    Moral_Element = Optional(str)
    Material_element = Optional(str)
    Legal_element = Optional(str)
    documents = Set('Document')
    hearing = Set('Hearing')
    Debt_amount = Optional(Decimal)


class Prosecutor(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutor_team = Optional('ProsecutorTeam')
    issues = Set(Issue)
    court_cases = Set('CourtCase')
    lawyer = Required(Lawyer)


class ProsecutorTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutors = Set(Prosecutor)
    complaints = Set(Complaint)


class Court(db.Entity):
    """ContactMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    court_rank = Required('CourtRank')
    judicial_officers = Set('JudicialOfficer')
    town = Required(Town)


class CourtRank(db.Entity):
    """supreme, appeal, high court, magistrates court, kadhi court"""
    id = PrimaryKey(int, auto=True)
    courts = Set(Court)


class JudicialOfficer(db.Entity):
    """PersonMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    j_o_rank = Required('JORank')
    court = Required(Court)
    issues = Set(Issue)
    registrar = Set('CourtCase', reverse='pretrial_registrar')
    court_cases = Set('CourtCase', reverse='bench')
    judicial_role = Required('JudicialRole')
    documents = Set('Document')
    hearing = Set('Hearing')


class JORank(db.Entity):
    """Supreme Court, Judge, Magistrate"""
    id = PrimaryKey(int, auto=True)
    judicial_officers = Set(JudicialOfficer)


class CourtCase(db.Entity):
    id = PrimaryKey(int, auto=True)
    docket_number = Optional(str)
    complaints = Set(Complaint)
    issues = Set(Issue)
    ADR = Optional(bool)
    mediation_proposal = Optional(LongStr)
    FileDate = Optional(date, default=lambda: date.today())
    case_summary = Optional(LongStr)
    filing_prosecutor = Optional(Prosecutor)
    FastTrack = Optional(bool)
    Priority = Optional(str)
    law_firm = Set(LawFirm)
    ObjectofLitigation = Optional(LongStr)
    Prosecution_motivation = Optional(LongStr)
    Prosecution_prayer = Optional(str)
    pretrial_date = Optional(date, default=lambda: date.today())
    pretrial_notes = Optional(LongStr)
    pretrial_registrar = Optional(JudicialOfficer, reverse='registrar')
    case_admissible = Optional(bool)
    indictment_date = Optional(str)
    bench = Set(JudicialOfficer, reverse='court_cases')
    hearings = Set('Hearing')
    Judgement = Optional(str)
    Judgement_docx = Optional(str)
    case_link_type = Optional('CaseLinkType')
    court_case = Set('CourtCase', reverse='linked_cases')
    linked_cases = Optional('CourtCase', reverse='court_case')
    appealed = Optional(bool)
    appeal_number = Optional(str)
    Inventory_of_docket = Optional(str)
    documents = Set('Document')
    case_categories = Set('CaseCategory')
    commitals = Set('Commital')
    next_hearing_date = Optional(date)
    interlocutory_judgement = Optional(LongStr)
    reopen = Optional(bool)
    reopen_reason = Optional(LongStr)
    combined_case = Optional(bool)


class Hearing(db.Entity):
    """Cause List"""
    id = PrimaryKey(int, auto=True)
    court_cases = Optional(CourtCase)
    hearing_type = Required('HearingType')
    schedule_status = Required('ScheduleStatusType')
    hearing_date = Optional(date)
    reason = Optional(LongStr)  # reason for setting date
    sequence = Optional(int, unsigned=True)
    yearDay = Optional(int, unsigned=True)
    startTime = Optional(time)
    endTime = Optional(time)
    Notes = Optional(LongStr)
    completed = Optional(bool)
    adjourned_to = Optional(date)
    Transcript = Optional(LongStr)
    issues = Set(Issue)
    atendance = Optional(str)
    next_hearing_date = Optional(date)
    postponement_reason = Optional(str)
    lawyers_defense = Set(LawFirm, reverse='lawyers_defense')
    lawyer_plaintiff = Set(LawFirm, reverse='lawyer_plaintiff')
    adjudicating_officer = Set(JudicialOfficer)
    transcripts = Set('Transcript')


class LegalReference(db.Entity):
    """Statutes, Precedent, Court Position"""
    id = PrimaryKey(int, auto=True)
    ref = Required(str)
    verbatim = Optional(LongStr)
    argument_issues = Set(Issue, reverse='argument_legal_references')
    rebuttaL_issues = Set(Issue, reverse='rebuttal_legal_references')
    Public = Optional(bool)
    Commentary = Optional(LongStr)
    validated = Optional(bool)


class PartyType(db.Entity):
    id = PrimaryKey(int, auto=True)
    parties = Set(Party)


class Diagram(db.Entity):
    id = PrimaryKey(int, auto=True)
    investigation_diary = Required(InvestigationDiary)
    Image = Optional(str)
    Description = Optional(str)
    docx = Optional(str)


class Document(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Optional(str)
    court_case = Optional(CourtCase)
    issue = Optional(Issue)
    document_admissibility = Optional(str)
    admitted = Optional(bool)
    judicial_officer = Optional(JudicialOfficer)  # probably a registrar
    filing_date = Optional(datetime)
    admisibility_notes = Optional(LongStr)
    is_judgement = Optional(bool)
    is_court_order = Optional(bool)
    document_types = Set('DocumentType')
    document = Optional(LongStr)
    Published = Optional(bool)
    publish_newspaper = Optional(str)
    publish_date = Optional(date)
    validated = Optional(bool)
    filesize = Optional(Decimal)
    page_count = Optional(int)
    filing_costs = Set('FilingCost')


class FilingFee(db.Entity):
    id = PrimaryKey(int, auto=True)
    filing_fee_type = Required('FilingFeeType')
    filing_costs = Set('FilingCost')
    Amount = Optional(Decimal)
    Unit = Optional(str)


class FilingFeeType(db.Entity):
    id = PrimaryKey(int, auto=True)
    filing_fees = Set(FilingFee)


class CaseCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    court_cases = Set(CourtCase)
    case_categories = Set('CaseCategory', reverse='subcategory')
    subcategory = Required('CaseCategory', reverse='case_categories')


class JudicialRole(db.Entity):
    """Judge, Magistrate, Registrar"""
    id = PrimaryKey(int, auto=True)
    judicial_officers = Set(JudicialOfficer)


class ScheduleStatusType(db.Entity):
    """Completed, Adjourned, Judgement"""
    id = PrimaryKey(int, auto=True)  # Adjourned
    hearing = Set(Hearing)


class Transcript(db.Entity):
    id = PrimaryKey(int, auto=True)
    video = Optional(str)
    audio = Optional(str)
    add_date = Optional(datetime, default=lambda: datetime.now())
    asr_transcript = Optional(LongStr)
    asr_date = Optional(datetime, default=lambda: datetime.now())
    edited_transcript = Optional(LongStr)
    edit_date = Optional(datetime, default=lambda: datetime.now())
    certified_transcript = Optional(LongStr)
    certfiy_date = Optional(datetime, default=lambda: datetime.now())
    locked = Optional(bool)
    hearing = Required(Hearing)


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearing = Set(Hearing)


class Prison(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    commitals = Set('Commital')
    prison_officers = Set('PrisonOfficer')


class Commital(db.Entity):
    id = PrimaryKey(int, auto=True)
    prisons = Optional(Prison)
    police_station = Optional(PoliceStation)
    parties = Required(Party)
    CaseComplete = Optional(bool)
    commit_date = Required(date)
    purpose = Optional(str)
    warrant_type = Required(WarrantType)
    warrant_docx = Optional(str)
    warrant_issue_date = Optional(date)
    warrant_issued_by = Optional(str)
    warrant_date_attached = Optional(datetime)
    duration = Optional(timedelta)
    commital = Required('Commital', reverse='commital_transfer')
    commital_transfer = Optional('Commital', reverse='commital')
    commital_type = Required('CommitalType')
    court_case = Required(CourtCase)
    concurrent = Optional(bool)
    LifeImprisonment = Optional(bool)
    arrival_date = Optional(datetime, default=lambda: datetime.now())
    sentence_start_date = Optional(datetime, default=lambda: datetime.now())
    arrest_date = Optional(datetime, default=lambda: datetime.now())
    Remaining_years = Optional(int)
    remaining_months = Optional(int)
    Remaining_days = Optional(int)
    cell_number = Optional(str)
    cell_type = Optional('CellType')
    release_date = Optional(datetime)
    exit_date = Optional(datetime, default=lambda: datetime.now())
    Reason_for_release = Optional(LongStr)
    WithChildren = Optional(bool)
    release_type = Optional('ReleaseType')
    receiving_officer = Required('PrisonOfficer', reverse='commitals')
    releasing_officer = Required('PrisonOfficer', reverse='release_commitals')


class CommitalType(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    commitals = Set(Commital)
    maxDuration = Optional(timedelta)


class Biodata(db.Entity):
    id = PrimaryKey(int, auto=True)
    parties = Set(Party)
    economic_class = Optional('EconomicClass')
    religion = Optional('Religion')
    nextof_kins = Set('NextOfKin')
    Photo = Optional(buffer)


class EconomicClass(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    biodata = Set(Biodata)


class Religion(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    biodata = Set(Biodata)


class CellType(db.Entity):
    id = PrimaryKey(int, auto=True)
    commitals = Set(Commital)


class NextOfKin(db.Entity):
    """PersonMixin"""
    id = PrimaryKey(int, auto=True)
    biodata = Required(Biodata)
    ChildUnder4 = Optional(bool)


class Discipline(db.Entity):
    id = PrimaryKey(int, auto=True)
    party = Required(Party)
    prison_officer = Required('PrisonOfficer')


class PersonalEffect(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    party = Required(Party)
    personal_effects_category = Required('PersonalEffectsCategory')


class PersonalEffectsCategory(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    personal_effects = Set(PersonalEffect)


class DocumentType(db.Entity):
    """RefTypeMixin, Summons, Orders, Warrants"""
    id = PrimaryKey(int, auto=True)
    documents = Set(Document)


class ExpertType(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    experts = Set(Expert)


class CaseLinkType(db.Entity):
    """Appeal, Combination, Reintroduction"""
    id = PrimaryKey(int, auto=True)
    court_cases = Set(CourtCase)


class PoliceOfficerRank(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    Name = Required(str)
    Description = Optional(str)
    police_officers = Set(PoliceOfficer)
    sequence = Optional(int)


class PoliceStationRank(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    police_stations = Set(PoliceStation)


class FilingCost(db.Entity):
    documents = Required(Document)
    filing_fees = Required(FilingFee)
    Unit = Optional(str)
    Qty = Optional(int)
    unit_cost = Optional(Decimal)
    Amount = Optional(Decimal)
    paid = Optional(bool)
    payment_ref = Optional(str)
    PrimaryKey(documents, filing_fees)


class ReleaseType(db.Entity):
    id = PrimaryKey(int, auto=True)
    commitals = Set(Commital)


class PrisonOfficer(db.Entity):
    """PersonMixin"""
    id = PrimaryKey(int, auto=True)
    prison = Required(Prison)
    prison_officer_rank = Required('PrisonOfficerRank')
    disciplines = Set(Discipline)
    commitals = Set(Commital, reverse='receiving_officer')
    release_commitals = Set(Commital, reverse='releasing_officer')


class PrisonOfficerRank(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison_officers = Set(PrisonOfficer)



db.generate_mapping()

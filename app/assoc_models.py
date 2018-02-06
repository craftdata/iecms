from sqlalchemy import Table, Column, ForeignKey, Integer, ForeignKeyConstraint

from app.models import metadata

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
t_court_judicialofficer = Table(
    'court_judicialofficer', metadata,
    Column('court', ForeignKey('court.id'), primary_key=True, nullable=False),
    Column('judicialofficer', ForeignKey('judicialofficer.id'), primary_key=True, nullable=False, index=True)
)
t_csi_equipment_investigationdiary = Table(
    'csi_equipment_investigationdiary', metadata,
    Column('csi_equipment', ForeignKey('csi_equipment.id'), primary_key=True, nullable=False),
    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)
t_document_documenttype = Table(
    'document_documenttype', metadata,
    Column('document', ForeignKey('document.id'), primary_key=True, nullable=False),
    Column('documenttype', ForeignKey('documenttype.id'), primary_key=True, nullable=False, index=True)
)
t_expert_experttype = Table(
    'expert_experttype', metadata,
    Column('expert', ForeignKey('expert.id'), primary_key=True, nullable=False),
    Column('experttype', ForeignKey('experttype.id'), primary_key=True, nullable=False, index=True)
)
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
t_instancecrime_issue = Table(
    'instancecrime_issue', metadata,
    Column('instancecrime_parties', Integer, primary_key=True, nullable=False),
    Column('instancecrime_crimes', Integer, primary_key=True, nullable=False),
    Column('issue', ForeignKey('issue.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['instancecrime_parties', 'instancecrime_crimes'], ['instancecrime.parties', 'instancecrime.crimes'])
)
t_investigating_officer_investigationdiary = Table(
    'investigating_officer_investigationdiary', metadata,
    Column('investigating_officer', ForeignKey('investigating_officer.police_officers'), primary_key=True, nullable=False),
    Column('investigationdiary', ForeignKey('investigationdiary.id'), primary_key=True, nullable=False, index=True)
)
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
t_lawyer_party = Table(
    'lawyer_party', metadata,
    Column('lawyer', ForeignKey('lawyer.id'), primary_key=True, nullable=False),
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False, index=True)
)
t_party_settlement = Table(
    'party_settlement', metadata,
    Column('party', ForeignKey('party.complaints'), primary_key=True, nullable=False),
    Column('settlement', ForeignKey('settlement.id'), primary_key=True, nullable=False, index=True)
)
t_policeofficer_policestation = Table(
    'policeofficer_policestation', metadata,
    Column('policeofficer', ForeignKey('policeofficer.id'), primary_key=True, nullable=False),
    Column('policestation', ForeignKey('policestation.id'), primary_key=True, nullable=False, index=True)
)
t_town_ward = Table(
    'town_ward', metadata,
    Column('town', ForeignKey('town.id'), primary_key=True, nullable=False),
    Column('ward', ForeignKey('ward.id'), primary_key=True, nullable=False, index=True)
)
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
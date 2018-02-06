from flask_appbuilder import Model
from sqlalchemy import Table, Column, ForeignKey

t_casecategorychecklist =  Table(

    'casecategorychecklist', Model.metadata,

     Column('case_checklists',  ForeignKey('casechecklist.id'), primary_key=True, nullable=True),

     Column('case_categories',  ForeignKey('casecategory.id'), primary_key=True, nullable=True, index=True)

)
t_complaint_complaintcategory =  Table(

    'complaint_complaintcategory', Model.metadata,

     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=True),

     Column('complaintcategory',  ForeignKey('complaintcategory.id'), primary_key=True, nullable=True, index=True)

)
t_complaint_courtcase =  Table(

    'complaint_courtcase', Model.metadata,

     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=True),

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)

)
t_court_judicialofficer =  Table(

    'court_judicialofficer', Model.metadata,

     Column('court',  ForeignKey('court.id'), primary_key=True, nullable=True),

     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)
t_casecategory_courtcase =  Table(

    'casecategory_courtcase', Model.metadata,

     Column('casecategory',  ForeignKey('casecategory.id'), primary_key=True, nullable=True),

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)

)
t_courtcase_judicialofficer =  Table(

    'courtcase_judicialofficer', Model.metadata,

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True),

     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)
t_courtcase_lawfirm =  Table(

    'courtcase_lawfirm', Model.metadata,

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True),

     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)
t_csi_equipment_investigationdiary =  Table(

    'csi_equipment_investigationdiary', Model.metadata,

     Column('csi_equipment',  ForeignKey('csi_equipment.id'), primary_key=True, nullable=True),

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True, index=True)

)
t_document_documenttype =  Table(

    'document_documenttype',Model.metadata,

     Column('document',  ForeignKey('document.id'), primary_key=True, nullable=True),

     Column('documenttype',  ForeignKey('documenttype.id'), primary_key=True, nullable=True, index=True)

)
t_expert_experttype =  Table(

    'expert_experttype',Model.metadata,

     Column('expert',  ForeignKey('expert.id'), primary_key=True, nullable=True),

     Column('experttype',  ForeignKey('experttype.id'), primary_key=True, nullable=True, index=True)

)
t_hearing_issue =  Table(

    'hearing_issue', Model.metadata,

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True, index=True)

)
t_hearing_judicialofficer =  Table(

    'hearing_judicialofficer', Model.metadata,

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)
t_hearing_lawfirm =  Table(

    'hearing_lawfirm', Model.metadata,

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)
t_hearing_lawfirm_2 =  Table(

    'hearing_lawfirm_2', Model.metadata,

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)
t_instancecrime_issue =  Table(

    'instancecrime_issue',Model.metadata,

     Column('instancecrime',  ForeignKey('instancecrime.id'), primary_key=True, nullable=True),

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True, index=True)

)
t_investigationdiary_party =  Table(

    'investigationdiary_party', Model.metadata,

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)

)
t_investigationdiary_policeofficer =  Table(

    'investigationdiary_policeofficer',Model.metadata,

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=True, index=True)

)
t_investigationdiary_vehicle =  Table(

    'investigationdiary_vehicle',Model.metadata,

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

     Column('vehicle',  ForeignKey('vehicle.id'), primary_key=True, nullable=True, index=True)

)
t_issue_lawyer =  Table(

    'issue_lawyer', Model.metadata,

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=True, index=True)

)
t_issue_legalreference =  Table(

    'issue_legalreference', Model.metadata,

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)

)
t_issue_legalreference_2 =  Table(

    'issue_legalreference_2', Model.metadata,

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)

)
t_issue_party =  Table(

    'issue_party', Model.metadata,

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)

)
t_issue_party_2 =  Table(

    'issue_party_2', Model.metadata,

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)

)
t_lawyer_party =  Table(

    'lawyer_party', Model.metadata,

     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True, index=True)

)
t_party_settlement =  Table(

    'party_settlement', Model.metadata,

     Column('party',  ForeignKey('party.id'), primary_key=True, nullable=True),

     Column('settlement',  ForeignKey('settlement.id'), primary_key=True, nullable=True, index=True)

)
t_policeofficer_policestation =  Table(

    'policeofficer_policestation', Model.metadata,

     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=True),

     Column('policestation',  ForeignKey('policestation.id'), primary_key=True, nullable=True, index=True)

)
t_town_ward =  Table(

    'town_ward', Model.metadata,

     Column('town',  ForeignKey('town.id'), primary_key=True, nullable=True),

     Column('ward',  ForeignKey('ward.id'), primary_key=True, nullable=True, index=True)

)
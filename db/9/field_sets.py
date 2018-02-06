
Accounttype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Accounttype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Accounttype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Accounttype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Accounttype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Accounttype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



AuditMixin_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']


AuditMixin_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']


AuditMixin_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']


AuditMixin_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



AuditMixin_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



AuditMixin_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_add_columns = ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']


Bill_edit_columns = ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']


Bill_list_columns = ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']


Bill_add_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_edit_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_show_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_add_columns = ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_edit_columns = ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_list_columns = ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_add_field_set = [
    ('Data', {'fields': ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_edit_field_set = [
    ('Data', {'fields': ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_show_field_set = [
    ('Data', {'fields': ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodatum_add_columns = ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']


Biodatum_edit_columns = ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']


Biodatum_list_columns = ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']


Biodatum_add_field_set = [
    ('Data', {'fields': ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodatum_edit_field_set = [
    ('Data', {'fields': ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodatum_show_field_set = [
    ('Data', {'fields': ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_add_columns = ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']


Casecategory_edit_columns = ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']


Casecategory_list_columns = ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']


Casecategory_add_field_set = [
    ('Data', {'fields': ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_edit_field_set = [
    ('Data', {'fields': ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_show_field_set = [
    ('Data', {'fields': ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_add_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo']


Casechecklist_edit_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo']


Casechecklist_list_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo']


Casechecklist_add_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_edit_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_show_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Caselinktype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Caselinktype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Caselinktype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Celltype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Celltype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Celltype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_add_columns = ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_edit_columns = ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_list_columns = ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_add_field_set = [
    ('Data', {'fields': ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_edit_field_set = [
    ('Data', {'fields': ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_show_field_set = [
    ('Data', {'fields': ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_add_columns = ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo']


Commitaltype_edit_columns = ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo']


Commitaltype_list_columns = ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo']


Commitaltype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_add_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_edit_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_list_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_add_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_edit_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_show_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_add_columns = ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']


Complaintcategory_edit_columns = ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']


Complaintcategory_list_columns = ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']


Complaintcategory_add_field_set = [
    ('Data', {'fields': ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_edit_field_set = [
    ('Data', {'fields': ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_show_field_set = [
    ('Data', {'fields': ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Complaintrole_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Complaintrole_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Complaintrole_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_add_columns = ['file', 'id', 'metadata', 'mindate', 'name', 'photo']


Country_edit_columns = ['file', 'id', 'metadata', 'mindate', 'name', 'photo']


Country_list_columns = ['file', 'id', 'metadata', 'mindate', 'name', 'photo']


Country_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_add_columns = ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo']


County_edit_columns = ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo']


County_list_columns = ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo']


County_add_field_set = [
    ('Data', {'fields': ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_edit_field_set = [
    ('Data', {'fields': ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_show_field_set = [
    ('Data', {'fields': ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_add_columns = ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']


Court_edit_columns = ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']


Court_list_columns = ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']


Court_add_field_set = [
    ('Data', {'fields': ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_edit_field_set = [
    ('Data', {'fields': ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_show_field_set = [
    ('Data', {'fields': ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_add_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code']


Courtaccount_edit_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code']


Courtaccount_list_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code']


Courtaccount_add_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_edit_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_show_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_add_columns = ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']


Courtcase_edit_columns = ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']


Courtcase_list_columns = ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']


Courtcase_add_field_set = [
    ('Data', {'fields': ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_edit_field_set = [
    ('Data', {'fields': ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_show_field_set = [
    ('Data', {'fields': ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Courtrank_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Courtrank_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Courtrank_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_add_columns = ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number']


Courtstation_edit_columns = ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number']


Courtstation_list_columns = ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number']


Courtstation_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_add_columns = ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']


Crime_edit_columns = ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']


Crime_list_columns = ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']


Crime_add_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_edit_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_show_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_add_columns = ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo']


CsiEquipment_edit_columns = ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo']


CsiEquipment_list_columns = ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo']


CsiEquipment_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_add_columns = ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']


Diagram_edit_columns = ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']


Diagram_list_columns = ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']


Diagram_add_field_set = [
    ('Data', {'fields': ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_edit_field_set = [
    ('Data', {'fields': ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_show_field_set = [
    ('Data', {'fields': ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_add_columns = ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']


Discipline_edit_columns = ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']


Discipline_list_columns = ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']


Discipline_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_add_columns = ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_edit_columns = ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_list_columns = ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_add_field_set = [
    ('Data', {'fields': ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_edit_field_set = [
    ('Data', {'fields': ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_show_field_set = [
    ('Data', {'fields': ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_add_columns = ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']


Document_edit_columns = ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']


Document_list_columns = ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']


Document_add_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_edit_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_show_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Documenttype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Documenttype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Documenttype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclas_add_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Economicclas_edit_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Economicclas_list_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Economicclas_add_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclas_edit_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclas_show_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_add_columns = ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']


Exhibit_edit_columns = ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']


Exhibit_list_columns = ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']


Exhibit_add_field_set = [
    ('Data', {'fields': ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_edit_field_set = [
    ('Data', {'fields': ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_show_field_set = [
    ('Data', {'fields': ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_add_columns = ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']


Expert_edit_columns = ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']


Expert_list_columns = ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']


Expert_add_field_set = [
    ('Data', {'fields': ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_edit_field_set = [
    ('Data', {'fields': ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_show_field_set = [
    ('Data', {'fields': ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_add_columns = ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_edit_columns = ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_list_columns = ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_add_field_set = [
    ('Data', {'fields': ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_edit_field_set = [
    ('Data', {'fields': ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_show_field_set = [
    ('Data', {'fields': ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Experttype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Experttype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Experttype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclas_add_columns = ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']


Feeclas_edit_columns = ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']


Feeclas_list_columns = ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']


Feeclas_add_field_set = [
    ('Data', {'fields': ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclas_edit_field_set = [
    ('Data', {'fields': ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclas_show_field_set = [
    ('Data', {'fields': ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_add_columns = ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']


Feetype_edit_columns = ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']


Feetype_list_columns = ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']


Feetype_add_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_edit_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_show_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FetchedValue_add_columns = ['dispatch', 'has_argument', 'is_server_default', 'reflected']


FetchedValue_edit_columns = ['dispatch', 'has_argument', 'is_server_default', 'reflected']


FetchedValue_list_columns = ['dispatch', 'has_argument', 'is_server_default', 'reflected']


FetchedValue_add_field_set = [
    ('Data', {'fields': ['dispatch', 'has_argument', 'is_server_default', 'reflected'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FetchedValue_edit_field_set = [
    ('Data', {'fields': ['dispatch', 'has_argument', 'is_server_default', 'reflected'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FetchedValue_show_field_set = [
    ('Data', {'fields': ['dispatch', 'has_argument', 'is_server_default', 'reflected'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FileColumn_add_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


FileColumn_edit_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


FileColumn_list_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


FileColumn_add_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FileColumn_edit_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FileColumn_show_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_add_columns = ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']


Healthevent_edit_columns = ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']


Healthevent_list_columns = ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']


Healthevent_add_field_set = [
    ('Data', {'fields': ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_edit_field_set = [
    ('Data', {'fields': ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_show_field_set = [
    ('Data', {'fields': ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Healtheventtype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Healtheventtype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Healtheventtype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_add_columns = ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']


Hearing_edit_columns = ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']


Hearing_list_columns = ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']


Hearing_add_field_set = [
    ('Data', {'fields': ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_edit_field_set = [
    ('Data', {'fields': ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_show_field_set = [
    ('Data', {'fields': ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_add_columns = ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo']


Hearingtype_edit_columns = ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo']


Hearingtype_list_columns = ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo']


Hearingtype_add_field_set = [
    ('Data', {'fields': ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_edit_field_set = [
    ('Data', {'fields': ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_show_field_set = [
    ('Data', {'fields': ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageColumn_add_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


ImageColumn_edit_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


ImageColumn_list_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


ImageColumn_add_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageColumn_edit_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageColumn_show_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageManager_add_columns = ['keep_image_formats']


ImageManager_edit_columns = ['keep_image_formats']


ImageManager_list_columns = ['keep_image_formats']


ImageManager_add_field_set = [
    ('Data', {'fields': ['keep_image_formats'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageManager_edit_field_set = [
    ('Data', {'fields': ['keep_image_formats'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageManager_show_field_set = [
    ('Data', {'fields': ['keep_image_formats'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_add_columns = ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_edit_columns = ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_list_columns = ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_add_field_set = [
    ('Data', {'fields': ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_edit_field_set = [
    ('Data', {'fields': ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_show_field_set = [
    ('Data', {'fields': ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_add_columns = ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']


Interview_edit_columns = ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']


Interview_list_columns = ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']


Interview_add_field_set = [
    ('Data', {'fields': ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_edit_field_set = [
    ('Data', {'fields': ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_show_field_set = [
    ('Data', {'fields': ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



InvestigatingOfficer_add_columns = ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


InvestigatingOfficer_edit_columns = ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


InvestigatingOfficer_list_columns = ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


InvestigatingOfficer_add_field_set = [
    ('Data', {'fields': ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



InvestigatingOfficer_edit_field_set = [
    ('Data', {'fields': ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



InvestigatingOfficer_show_field_set = [
    ('Data', {'fields': ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_add_columns = ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_edit_columns = ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_list_columns = ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_add_field_set = [
    ('Data', {'fields': ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_edit_field_set = [
    ('Data', {'fields': ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_show_field_set = [
    ('Data', {'fields': ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_add_columns = ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_edit_columns = ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_list_columns = ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_add_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_edit_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_show_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_add_columns = ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']


Judicialofficer_edit_columns = ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']


Judicialofficer_list_columns = ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']


Judicialofficer_add_field_set = [
    ('Data', {'fields': ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_edit_field_set = [
    ('Data', {'fields': ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_show_field_set = [
    ('Data', {'fields': ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Judicialrank_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Judicialrank_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Judicialrank_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Judicialrole_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Judicialrole_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Judicialrole_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_add_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Law_edit_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Law_list_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Law_add_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_edit_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_show_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Lawfirm_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Lawfirm_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Lawfirm_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_add_columns = ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']


Lawyer_edit_columns = ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']


Lawyer_list_columns = ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']


Lawyer_add_field_set = [
    ('Data', {'fields': ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_edit_field_set = [
    ('Data', {'fields': ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_show_field_set = [
    ('Data', {'fields': ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_add_columns = ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_edit_columns = ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_list_columns = ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_add_field_set = [
    ('Data', {'fields': ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_edit_field_set = [
    ('Data', {'fields': ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_show_field_set = [
    ('Data', {'fields': ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Markup_add_columns = []


Markup_edit_columns = []


Markup_list_columns = []


Markup_add_field_set = [
    ('Data', {'fields': [], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Markup_edit_field_set = [
    ('Data', {'fields': [], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Markup_show_field_set = [
    ('Data', {'fields': [], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



MetaData_add_columns = ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']


MetaData_edit_columns = ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']


MetaData_list_columns = ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']


MetaData_add_field_set = [
    ('Data', {'fields': ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



MetaData_edit_field_set = [
    ('Data', {'fields': ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



MetaData_show_field_set = [
    ('Data', {'fields': ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Model_add_columns = ['metadata']


Model_edit_columns = ['metadata']


Model_list_columns = ['metadata']


Model_add_field_set = [
    ('Data', {'fields': ['metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Model_edit_field_set = [
    ('Data', {'fields': ['metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Model_show_field_set = [
    ('Data', {'fields': ['metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_add_columns = ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo']


Nextofkin_edit_columns = ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo']


Nextofkin_list_columns = ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo']


Nextofkin_add_field_set = [
    ('Data', {'fields': ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_edit_field_set = [
    ('Data', {'fields': ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_show_field_set = [
    ('Data', {'fields': ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_add_columns = ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']


Notification_edit_columns = ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']


Notification_list_columns = ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']


Notification_add_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_edit_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_show_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_add_columns = ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']


Notificationregister_edit_columns = ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']


Notificationregister_list_columns = ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']


Notificationregister_add_field_set = [
    ('Data', {'fields': ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_edit_field_set = [
    ('Data', {'fields': ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_show_field_set = [
    ('Data', {'fields': ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_add_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Notificationtype_edit_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Notificationtype_list_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']


Notificationtype_add_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_edit_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_show_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Notifyevent_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Notifyevent_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Notifyevent_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_add_columns = ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']


Page_edit_columns = ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']


Page_list_columns = ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']


Page_add_field_set = [
    ('Data', {'fields': ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_edit_field_set = [
    ('Data', {'fields': ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_show_field_set = [
    ('Data', {'fields': ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_add_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']


Party_edit_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']


Party_list_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']


Party_add_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_edit_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_show_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Partytype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Partytype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Partytype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_add_columns = ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']


Payment_edit_columns = ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']


Payment_list_columns = ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']


Payment_add_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_edit_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_show_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_add_columns = ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']


Personaleffect_edit_columns = ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']


Personaleffect_list_columns = ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']


Personaleffect_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Personaleffectscategory_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Personaleffectscategory_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Personaleffectscategory_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_add_columns = ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


Policeofficer_edit_columns = ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


Policeofficer_list_columns = ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


Policeofficer_add_field_set = [
    ('Data', {'fields': ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_edit_field_set = [
    ('Data', {'fields': ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_show_field_set = [
    ('Data', {'fields': ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_add_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence']


Policeofficerrank_edit_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence']


Policeofficerrank_list_columns = ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence']


Policeofficerrank_add_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_edit_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_show_field_set = [
    ('Data', {'fields': ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_add_columns = ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_edit_columns = ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_list_columns = ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Policestationrank_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Policestationrank_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Policestationrank_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1']


Prison_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1']


Prison_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1']


Prison_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']


Prisonofficer_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']


Prisonofficer_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']


Prisonofficer_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Prisonofficerrank_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Prisonofficerrank_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Prisonofficerrank_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_add_columns = ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']


Prosecutor_edit_columns = ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']


Prosecutor_list_columns = ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']


Prosecutor_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Prosecutorteam_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Prosecutorteam_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Prosecutorteam_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Releasetype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Releasetype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Releasetype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Religion_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Religion_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Religion_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Schedulestatustype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Schedulestatustype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Schedulestatustype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_add_columns = ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_edit_columns = ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_list_columns = ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_add_field_set = [
    ('Data', {'fields': ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_edit_field_set = [
    ('Data', {'fields': ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_show_field_set = [
    ('Data', {'fields': ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_add_columns = ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']


Settlement_edit_columns = ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']


Settlement_list_columns = ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']


Settlement_add_field_set = [
    ('Data', {'fields': ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_edit_field_set = [
    ('Data', {'fields': ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_show_field_set = [
    ('Data', {'fields': ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_add_columns = ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo']


Subcounty_edit_columns = ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo']


Subcounty_list_columns = ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo']


Subcounty_add_field_set = [
    ('Data', {'fields': ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_edit_field_set = [
    ('Data', {'fields': ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_show_field_set = [
    ('Data', {'fields': ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_add_columns = ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type']


Templatetype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type']


Templatetype_list_columns = ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type']


Templatetype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'ward']


Town_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'ward']


Town_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'ward']


Town_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_add_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video']


Transcript_edit_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video']


Transcript_list_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video']


Transcript_add_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_edit_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_show_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_add_columns = ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']


Vehicle_edit_columns = ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']


Vehicle_list_columns = ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']


Vehicle_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']


Ward_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']


Ward_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']


Ward_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_add_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Warranttype_edit_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Warranttype_list_columns = ['file', 'id', 'metadata', 'mindate', 'photo']


Warranttype_add_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_edit_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_show_field_set = [
    ('Data', {'fields': ['file', 'id', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



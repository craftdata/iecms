
Accounttype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Accounttype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Accounttype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Accounttype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Accounttype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Accounttype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_add_columns = ['assessing_registrar', 'bill_total', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'created_by', 'created_by_fk', 'created_on', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date']


Bill_edit_columns = ['assessing_registrar', 'bill_total', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'created_by', 'created_by_fk', 'created_on', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date']


Bill_list_columns = ['assessing_registrar', 'bill_total', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'created_by', 'created_by_fk', 'created_on', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date']


Bill_add_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'created_by', 'created_by_fk', 'created_on', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_edit_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'created_by', 'created_by_fk', 'created_on', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_show_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'created_by', 'created_by_fk', 'created_on', 'date_of_payment', 'document', 'documents', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'paid', 'party', 'party_paying', 'pay_code', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_add_columns = ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_edit_columns = ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_list_columns = ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_add_field_set = [
    ('Data', {'fields': ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_edit_field_set = [
    ('Data', {'fields': ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_show_field_set = [
    ('Data', {'fields': ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'feetype', 'feetype1', 'id', 'metadata', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodata_add_columns = ['allergies', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'blood_group', 'changed_by', 'changed_by_fk', 'changed_on', 'chronic_conditions', 'chronic_medications', 'citizenship', 'complexion', 'created_by', 'created_by_fk', 'created_on', 'current_health_status', 'diabetes', 'economic_class', 'economicclass', 'ethnicity', 'eye_colour', 'eye_left', 'eye_right', 'f_education', 'f_firstname', 'f_income', 'f_nat_id_num', 'f_occupation', 'f_othernames', 'f_prn', 'f_surname', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_lthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5', 'fp_rthumb', 'hair_colour', 'hbp', 'health_status', 'height_m', 'hiv', 'id', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'm_education', 'm_firstname', 'm_income', 'm_nat_id_num', 'm_occupation', 'm_othernames', 'm_prn', 'm_surname', 'metadata', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'palm_left', 'palm_right', 'party', 'party1', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'religion', 'religion1', 'striking_features', 'weight_kg']


Biodata_edit_columns = ['allergies', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'blood_group', 'changed_by', 'changed_by_fk', 'changed_on', 'chronic_conditions', 'chronic_medications', 'citizenship', 'complexion', 'created_by', 'created_by_fk', 'created_on', 'current_health_status', 'diabetes', 'economic_class', 'economicclass', 'ethnicity', 'eye_colour', 'eye_left', 'eye_right', 'f_education', 'f_firstname', 'f_income', 'f_nat_id_num', 'f_occupation', 'f_othernames', 'f_prn', 'f_surname', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_lthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5', 'fp_rthumb', 'hair_colour', 'hbp', 'health_status', 'height_m', 'hiv', 'id', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'm_education', 'm_firstname', 'm_income', 'm_nat_id_num', 'm_occupation', 'm_othernames', 'm_prn', 'm_surname', 'metadata', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'palm_left', 'palm_right', 'party', 'party1', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'religion', 'religion1', 'striking_features', 'weight_kg']


Biodata_list_columns = ['allergies', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'blood_group', 'changed_by', 'changed_by_fk', 'changed_on', 'chronic_conditions', 'chronic_medications', 'citizenship', 'complexion', 'created_by', 'created_by_fk', 'created_on', 'current_health_status', 'diabetes', 'economic_class', 'economicclass', 'ethnicity', 'eye_colour', 'eye_left', 'eye_right', 'f_education', 'f_firstname', 'f_income', 'f_nat_id_num', 'f_occupation', 'f_othernames', 'f_prn', 'f_surname', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_lthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5', 'fp_rthumb', 'hair_colour', 'hbp', 'health_status', 'height_m', 'hiv', 'id', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'm_education', 'm_firstname', 'm_income', 'm_nat_id_num', 'm_occupation', 'm_othernames', 'm_prn', 'm_surname', 'metadata', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'palm_left', 'palm_right', 'party', 'party1', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'religion', 'religion1', 'striking_features', 'weight_kg']


Biodata_add_field_set = [
    ('Data', {'fields': ['allergies', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'blood_group', 'changed_by', 'changed_by_fk', 'changed_on', 'chronic_conditions', 'chronic_medications', 'citizenship', 'complexion', 'created_by', 'created_by_fk', 'created_on', 'current_health_status', 'diabetes', 'economic_class', 'economicclass', 'ethnicity', 'eye_colour', 'eye_left', 'eye_right', 'f_education', 'f_firstname', 'f_income', 'f_nat_id_num', 'f_occupation', 'f_othernames', 'f_prn', 'f_surname', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_lthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5', 'fp_rthumb', 'hair_colour', 'hbp', 'health_status', 'height_m', 'hiv', 'id', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'm_education', 'm_firstname', 'm_income', 'm_nat_id_num', 'm_occupation', 'm_othernames', 'm_prn', 'm_surname', 'metadata', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'palm_left', 'palm_right', 'party', 'party1', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'religion', 'religion1', 'striking_features', 'weight_kg'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodata_edit_field_set = [
    ('Data', {'fields': ['allergies', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'blood_group', 'changed_by', 'changed_by_fk', 'changed_on', 'chronic_conditions', 'chronic_medications', 'citizenship', 'complexion', 'created_by', 'created_by_fk', 'created_on', 'current_health_status', 'diabetes', 'economic_class', 'economicclass', 'ethnicity', 'eye_colour', 'eye_left', 'eye_right', 'f_education', 'f_firstname', 'f_income', 'f_nat_id_num', 'f_occupation', 'f_othernames', 'f_prn', 'f_surname', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_lthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5', 'fp_rthumb', 'hair_colour', 'hbp', 'health_status', 'height_m', 'hiv', 'id', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'm_education', 'm_firstname', 'm_income', 'm_nat_id_num', 'm_occupation', 'm_othernames', 'm_prn', 'm_surname', 'metadata', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'palm_left', 'palm_right', 'party', 'party1', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'religion', 'religion1', 'striking_features', 'weight_kg'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodata_show_field_set = [
    ('Data', {'fields': ['allergies', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'blood_group', 'changed_by', 'changed_by_fk', 'changed_on', 'chronic_conditions', 'chronic_medications', 'citizenship', 'complexion', 'created_by', 'created_by_fk', 'created_on', 'current_health_status', 'diabetes', 'economic_class', 'economicclass', 'ethnicity', 'eye_colour', 'eye_left', 'eye_right', 'f_education', 'f_firstname', 'f_income', 'f_nat_id_num', 'f_occupation', 'f_othernames', 'f_prn', 'f_surname', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_lthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5', 'fp_rthumb', 'hair_colour', 'hbp', 'health_status', 'height_m', 'hiv', 'id', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'm_education', 'm_firstname', 'm_income', 'm_nat_id_num', 'm_occupation', 'm_othernames', 'm_prn', 'm_surname', 'metadata', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'palm_left', 'palm_right', 'party', 'party1', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'religion', 'religion1', 'striking_features', 'weight_kg'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_add_columns = ['casechecklist', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'subcategory']


Casecategory_edit_columns = ['casechecklist', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'subcategory']


Casecategory_list_columns = ['casechecklist', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'subcategory']


Casecategory_add_field_set = [
    ('Data', {'fields': ['casechecklist', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_edit_field_set = [
    ('Data', {'fields': ['casechecklist', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_show_field_set = [
    ('Data', {'fields': ['casechecklist', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Casechecklist_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Casechecklist_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Casechecklist_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Caselinktype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Caselinktype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Caselinktype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Celltype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Celltype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Celltype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_add_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'arrest_date', 'arrival_date', 'balance_avail', 'budget', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'changed_by', 'changed_by_fk', 'changed_on', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'completed', 'concurrent', 'contingency_plan', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'duration', 'early_end', 'early_start', 'end_delay', 'end_notes', 'exit_date', 'goal', 'id', 'late_end', 'late_start', 'life_imprisonment', 'metadata', 'not_started', 'over_budget', 'parent', 'parties', 'party', 'planned_end', 'planned_start', 'police_station', 'policestation', 'priority', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'segment', 'sentence_start_date', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_edit_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'arrest_date', 'arrival_date', 'balance_avail', 'budget', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'changed_by', 'changed_by_fk', 'changed_on', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'completed', 'concurrent', 'contingency_plan', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'duration', 'early_end', 'early_start', 'end_delay', 'end_notes', 'exit_date', 'goal', 'id', 'late_end', 'late_start', 'life_imprisonment', 'metadata', 'not_started', 'over_budget', 'parent', 'parties', 'party', 'planned_end', 'planned_start', 'police_station', 'policestation', 'priority', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'segment', 'sentence_start_date', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_list_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'arrest_date', 'arrival_date', 'balance_avail', 'budget', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'changed_by', 'changed_by_fk', 'changed_on', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'completed', 'concurrent', 'contingency_plan', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'duration', 'early_end', 'early_start', 'end_delay', 'end_notes', 'exit_date', 'goal', 'id', 'late_end', 'late_start', 'life_imprisonment', 'metadata', 'not_started', 'over_budget', 'parent', 'parties', 'party', 'planned_end', 'planned_start', 'police_station', 'policestation', 'priority', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'segment', 'sentence_start_date', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_add_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'arrest_date', 'arrival_date', 'balance_avail', 'budget', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'changed_by', 'changed_by_fk', 'changed_on', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'completed', 'concurrent', 'contingency_plan', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'duration', 'early_end', 'early_start', 'end_delay', 'end_notes', 'exit_date', 'goal', 'id', 'late_end', 'late_start', 'life_imprisonment', 'metadata', 'not_started', 'over_budget', 'parent', 'parties', 'party', 'planned_end', 'planned_start', 'police_station', 'policestation', 'priority', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'segment', 'sentence_start_date', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_edit_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'arrest_date', 'arrival_date', 'balance_avail', 'budget', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'changed_by', 'changed_by_fk', 'changed_on', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'completed', 'concurrent', 'contingency_plan', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'duration', 'early_end', 'early_start', 'end_delay', 'end_notes', 'exit_date', 'goal', 'id', 'late_end', 'late_start', 'life_imprisonment', 'metadata', 'not_started', 'over_budget', 'parent', 'parties', 'party', 'planned_end', 'planned_start', 'police_station', 'policestation', 'priority', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'segment', 'sentence_start_date', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_show_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'arrest_date', 'arrival_date', 'balance_avail', 'budget', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'changed_by', 'changed_by_fk', 'changed_on', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'completed', 'concurrent', 'contingency_plan', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'duration', 'early_end', 'early_start', 'end_delay', 'end_notes', 'exit_date', 'goal', 'id', 'late_end', 'late_start', 'life_imprisonment', 'metadata', 'not_started', 'over_budget', 'parent', 'parties', 'party', 'planned_end', 'planned_start', 'police_station', 'policestation', 'priority', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'segment', 'sentence_start_date', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'maxduration', 'metadata', 'name', 'notes']


Commitaltype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'maxduration', 'metadata', 'name', 'notes']


Commitaltype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'maxduration', 'metadata', 'name', 'notes']


Commitaltype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'maxduration', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'maxduration', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'maxduration', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_add_columns = ['active', 'casefileinformation', 'casesummary', 'changed_by', 'changed_by_fk', 'changed_on', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_edit_columns = ['active', 'casefileinformation', 'casesummary', 'changed_by', 'changed_by_fk', 'changed_on', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_list_columns = ['active', 'casefileinformation', 'casesummary', 'changed_by', 'changed_by_fk', 'changed_on', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_add_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'changed_by', 'changed_by_fk', 'changed_on', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_edit_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'changed_by', 'changed_by_fk', 'changed_on', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_show_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'changed_by', 'changed_by_fk', 'changed_on', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'complaint_category_parent', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent']


Complaintcategory_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'complaint_category_parent', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent']


Complaintcategory_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'complaint_category_parent', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent']


Complaintcategory_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'complaint_category_parent', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'complaint_category_parent', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'complaint_category_parent', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Complaintrole_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Complaintrole_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Complaintrole_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'name']


Country_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'name']


Country_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'name']


Country_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'country', 'country1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


County_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'country', 'country1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


County_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'country', 'country1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


County_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'country', 'country1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'country', 'country1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'country', 'country1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_add_columns = ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'court_rank', 'court_station', 'courtrank', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'judicialofficer', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'till_number', 'town', 'town1']


Court_edit_columns = ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'court_rank', 'court_station', 'courtrank', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'judicialofficer', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'till_number', 'town', 'town1']


Court_list_columns = ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'court_rank', 'court_station', 'courtrank', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'judicialofficer', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'till_number', 'town', 'town1']


Court_add_field_set = [
    ('Data', {'fields': ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'court_rank', 'court_station', 'courtrank', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'judicialofficer', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_edit_field_set = [
    ('Data', {'fields': ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'court_rank', 'court_station', 'courtrank', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'judicialofficer', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_show_field_set = [
    ('Data', {'fields': ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'court_rank', 'court_station', 'courtrank', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'judicialofficer', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_add_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'courts', 'created_by', 'created_by_fk', 'created_on', 'metadata', 'short_code']


Courtaccount_edit_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'courts', 'created_by', 'created_by_fk', 'created_on', 'metadata', 'short_code']


Courtaccount_list_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'courts', 'created_by', 'created_by_fk', 'created_on', 'metadata', 'short_code']


Courtaccount_add_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'courts', 'created_by', 'created_by_fk', 'created_on', 'metadata', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_edit_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'courts', 'created_by', 'created_by_fk', 'created_on', 'metadata', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_show_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'changed_by', 'changed_by_fk', 'changed_on', 'court', 'courts', 'created_by', 'created_by_fk', 'created_on', 'metadata', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_add_columns = ['action', 'active', 'active_date', 'activity_description', 'actual_end', 'actual_start', 'adr', 'appeal_number', 'appealed', 'award', 'balance_avail', 'budget', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'changed_by', 'changed_by_fk', 'changed_on', 'combined_case', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'docket_number', 'early_end', 'early_start', 'end_delay', 'end_notes', 'fast_track', 'filing_prosecutor', 'goal', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'late_end', 'late_start', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'not_started', 'object_of_litigation', 'over_budget', 'parent', 'planned_end', 'planned_start', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'value_in_dispute']


Courtcase_edit_columns = ['action', 'active', 'active_date', 'activity_description', 'actual_end', 'actual_start', 'adr', 'appeal_number', 'appealed', 'award', 'balance_avail', 'budget', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'changed_by', 'changed_by_fk', 'changed_on', 'combined_case', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'docket_number', 'early_end', 'early_start', 'end_delay', 'end_notes', 'fast_track', 'filing_prosecutor', 'goal', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'late_end', 'late_start', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'not_started', 'object_of_litigation', 'over_budget', 'parent', 'planned_end', 'planned_start', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'value_in_dispute']


Courtcase_list_columns = ['action', 'active', 'active_date', 'activity_description', 'actual_end', 'actual_start', 'adr', 'appeal_number', 'appealed', 'award', 'balance_avail', 'budget', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'changed_by', 'changed_by_fk', 'changed_on', 'combined_case', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'docket_number', 'early_end', 'early_start', 'end_delay', 'end_notes', 'fast_track', 'filing_prosecutor', 'goal', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'late_end', 'late_start', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'not_started', 'object_of_litigation', 'over_budget', 'parent', 'planned_end', 'planned_start', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'value_in_dispute']


Courtcase_add_field_set = [
    ('Data', {'fields': ['action', 'active', 'active_date', 'activity_description', 'actual_end', 'actual_start', 'adr', 'appeal_number', 'appealed', 'award', 'balance_avail', 'budget', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'changed_by', 'changed_by_fk', 'changed_on', 'combined_case', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'docket_number', 'early_end', 'early_start', 'end_delay', 'end_notes', 'fast_track', 'filing_prosecutor', 'goal', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'late_end', 'late_start', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'not_started', 'object_of_litigation', 'over_budget', 'parent', 'planned_end', 'planned_start', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_edit_field_set = [
    ('Data', {'fields': ['action', 'active', 'active_date', 'activity_description', 'actual_end', 'actual_start', 'adr', 'appeal_number', 'appealed', 'award', 'balance_avail', 'budget', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'changed_by', 'changed_by_fk', 'changed_on', 'combined_case', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'docket_number', 'early_end', 'early_start', 'end_delay', 'end_notes', 'fast_track', 'filing_prosecutor', 'goal', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'late_end', 'late_start', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'not_started', 'object_of_litigation', 'over_budget', 'parent', 'planned_end', 'planned_start', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_show_field_set = [
    ('Data', {'fields': ['action', 'active', 'active_date', 'activity_description', 'actual_end', 'actual_start', 'adr', 'appeal_number', 'appealed', 'award', 'balance_avail', 'budget', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'changed_by', 'changed_by_fk', 'changed_on', 'combined_case', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'docket_number', 'early_end', 'early_start', 'end_delay', 'end_notes', 'fast_track', 'filing_prosecutor', 'goal', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'late_end', 'late_start', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'next_hearing_date', 'not_started', 'object_of_litigation', 'over_budget', 'parent', 'planned_end', 'planned_start', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'status', 'task_group', 'under_budget', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Courtrank_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Courtrank_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Courtrank_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'pay_bill', 'till_number']


Courtstation_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'pay_bill', 'till_number']


Courtstation_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'pay_bill', 'till_number']


Courtstation_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'pay_bill', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'pay_bill', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'pay_bill', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'law', 'law1', 'metadata', 'ref', 'ref_law']


Crime_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'law', 'law1', 'metadata', 'ref', 'ref_law']


Crime_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'law', 'law1', 'metadata', 'ref', 'ref_law']


Crime_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'law', 'law1', 'metadata', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'law', 'law1', 'metadata', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'law', 'law1', 'metadata', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigationdiary', 'metadata']


CsiEquipment_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigationdiary', 'metadata']


CsiEquipment_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigationdiary', 'metadata']


CsiEquipment_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigationdiary', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigationdiary', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigationdiary', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata']


Diagram_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata']


Diagram_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata']


Diagram_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'docx', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'party', 'party1', 'prison_officer', 'prisonofficer']


Discipline_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'party', 'party1', 'prison_officer', 'prisonofficer']


Discipline_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'party', 'party1', 'prison_officer', 'prisonofficer']


Discipline_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'party', 'party1', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'party', 'party1', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'party', 'party1', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'docx', 'icon', 'id', 'metadata', 'name', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_add_columns = ['admisibility_notes', 'admitted', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'citation', 'comments', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doc_text', 'doc_title', 'doc_type', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_size_bytes', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'hashx', 'id', 'immutable', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'keywords', 'lines', 'metadata', 'mime_type', 'name', 'page_count', 'page_size', 'paid', 'paragraphs', 'producer_prog', 'publish_date', 'publish_newspaper', 'published', 'search_vector', 'subject', 'validated', 'visible', 'word_count']


Document_edit_columns = ['admisibility_notes', 'admitted', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'citation', 'comments', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doc_text', 'doc_title', 'doc_type', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_size_bytes', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'hashx', 'id', 'immutable', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'keywords', 'lines', 'metadata', 'mime_type', 'name', 'page_count', 'page_size', 'paid', 'paragraphs', 'producer_prog', 'publish_date', 'publish_newspaper', 'published', 'search_vector', 'subject', 'validated', 'visible', 'word_count']


Document_list_columns = ['admisibility_notes', 'admitted', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'citation', 'comments', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doc_text', 'doc_title', 'doc_type', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_size_bytes', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'hashx', 'id', 'immutable', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'keywords', 'lines', 'metadata', 'mime_type', 'name', 'page_count', 'page_size', 'paid', 'paragraphs', 'producer_prog', 'publish_date', 'publish_newspaper', 'published', 'search_vector', 'subject', 'validated', 'visible', 'word_count']


Document_add_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'citation', 'comments', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doc_text', 'doc_title', 'doc_type', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_size_bytes', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'hashx', 'id', 'immutable', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'keywords', 'lines', 'metadata', 'mime_type', 'name', 'page_count', 'page_size', 'paid', 'paragraphs', 'producer_prog', 'publish_date', 'publish_newspaper', 'published', 'search_vector', 'subject', 'validated', 'visible', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_edit_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'citation', 'comments', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doc_text', 'doc_title', 'doc_type', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_size_bytes', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'hashx', 'id', 'immutable', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'keywords', 'lines', 'metadata', 'mime_type', 'name', 'page_count', 'page_size', 'paid', 'paragraphs', 'producer_prog', 'publish_date', 'publish_newspaper', 'published', 'search_vector', 'subject', 'validated', 'visible', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_show_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'citation', 'comments', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doc_text', 'doc_title', 'doc_type', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_size_bytes', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'hashx', 'id', 'immutable', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'keywords', 'lines', 'metadata', 'mime_type', 'name', 'page_count', 'page_size', 'paid', 'paragraphs', 'producer_prog', 'publish_date', 'publish_newspaper', 'published', 'search_vector', 'subject', 'validated', 'visible', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Documenttype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Documenttype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Documenttype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclass_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name']


Economicclass_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name']


Economicclass_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name']


Economicclass_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclass_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclass_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_add_columns = ['audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'docx', 'exhibit_no', 'file_size_bytes', 'hashx', 'id', 'immutable', 'investigation_entry', 'investigationdiary', 'keywords', 'lines', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'seizure', 'seizure1', 'subject', 'word_count']


Exhibit_edit_columns = ['audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'docx', 'exhibit_no', 'file_size_bytes', 'hashx', 'id', 'immutable', 'investigation_entry', 'investigationdiary', 'keywords', 'lines', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'seizure', 'seizure1', 'subject', 'word_count']


Exhibit_list_columns = ['audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'docx', 'exhibit_no', 'file_size_bytes', 'hashx', 'id', 'immutable', 'investigation_entry', 'investigationdiary', 'keywords', 'lines', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'seizure', 'seizure1', 'subject', 'word_count']


Exhibit_add_field_set = [
    ('Data', {'fields': ['audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'docx', 'exhibit_no', 'file_size_bytes', 'hashx', 'id', 'immutable', 'investigation_entry', 'investigationdiary', 'keywords', 'lines', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'seizure', 'seizure1', 'subject', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_edit_field_set = [
    ('Data', {'fields': ['audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'docx', 'exhibit_no', 'file_size_bytes', 'hashx', 'id', 'immutable', 'investigation_entry', 'investigationdiary', 'keywords', 'lines', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'seizure', 'seizure1', 'subject', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_show_field_set = [
    ('Data', {'fields': ['audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'docx', 'exhibit_no', 'file_size_bytes', 'hashx', 'id', 'immutable', 'investigation_entry', 'investigationdiary', 'keywords', 'lines', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'seizure', 'seizure1', 'subject', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata']


Expert_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata']


Expert_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata']


Expert_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'credentials', 'experttype', 'id', 'institution', 'jobtitle', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'expert', 'experts', 'investigation_entries', 'investigationdiary', 'metadata', 'policeofficer', 'requesting_police_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'expert', 'experts', 'investigation_entries', 'investigationdiary', 'metadata', 'policeofficer', 'requesting_police_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'expert', 'experts', 'investigation_entries', 'investigationdiary', 'metadata', 'policeofficer', 'requesting_police_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'expert', 'experts', 'investigation_entries', 'investigationdiary', 'metadata', 'policeofficer', 'requesting_police_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'expert', 'experts', 'investigation_entries', 'investigationdiary', 'metadata', 'policeofficer', 'requesting_police_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'expert', 'experts', 'investigation_entries', 'investigationdiary', 'metadata', 'policeofficer', 'requesting_police_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'expert_type', 'id', 'metadata', 'name', 'notes', 'parent']


Experttype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'expert_type', 'id', 'metadata', 'name', 'notes', 'parent']


Experttype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'expert_type', 'id', 'metadata', 'name', 'notes', 'parent']


Experttype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'expert_type', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'expert_type', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'expert_type', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclass_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'fee_type', 'id', 'metadata', 'parent']


Feeclass_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'fee_type', 'id', 'metadata', 'parent']


Feeclass_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'fee_type', 'id', 'metadata', 'parent']


Feeclass_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'fee_type', 'id', 'metadata', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclass_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'fee_type', 'id', 'metadata', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclass_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'fee_type', 'id', 'metadata', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_add_columns = ['account_type', 'accounttype', 'amount', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'feeclass', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'name', 'notes', 'unit']


Feetype_edit_columns = ['account_type', 'accounttype', 'amount', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'feeclass', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'name', 'notes', 'unit']


Feetype_list_columns = ['account_type', 'accounttype', 'amount', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'feeclass', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'name', 'notes', 'unit']


Feetype_add_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'feeclass', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'name', 'notes', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_edit_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'feeclass', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'name', 'notes', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_show_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'feeclass', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'name', 'notes', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_add_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'goal', 'health_event_type', 'healtheventtype', 'id', 'late_end', 'late_start', 'metadata', 'not_started', 'notes', 'over_budget', 'party', 'party1', 'planned_end', 'planned_start', 'priority', 'prisonofficer', 'reporting_prison_officer', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'task_group', 'under_budget']


Healthevent_edit_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'goal', 'health_event_type', 'healtheventtype', 'id', 'late_end', 'late_start', 'metadata', 'not_started', 'notes', 'over_budget', 'party', 'party1', 'planned_end', 'planned_start', 'priority', 'prisonofficer', 'reporting_prison_officer', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'task_group', 'under_budget']


Healthevent_list_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'goal', 'health_event_type', 'healtheventtype', 'id', 'late_end', 'late_start', 'metadata', 'not_started', 'notes', 'over_budget', 'party', 'party1', 'planned_end', 'planned_start', 'priority', 'prisonofficer', 'reporting_prison_officer', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'task_group', 'under_budget']


Healthevent_add_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'goal', 'health_event_type', 'healtheventtype', 'id', 'late_end', 'late_start', 'metadata', 'not_started', 'notes', 'over_budget', 'party', 'party1', 'planned_end', 'planned_start', 'priority', 'prisonofficer', 'reporting_prison_officer', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'task_group', 'under_budget'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_edit_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'goal', 'health_event_type', 'healtheventtype', 'id', 'late_end', 'late_start', 'metadata', 'not_started', 'notes', 'over_budget', 'party', 'party1', 'planned_end', 'planned_start', 'priority', 'prisonofficer', 'reporting_prison_officer', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'task_group', 'under_budget'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_show_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'goal', 'health_event_type', 'healtheventtype', 'id', 'late_end', 'late_start', 'metadata', 'not_started', 'notes', 'over_budget', 'party', 'party1', 'planned_end', 'planned_start', 'priority', 'prisonofficer', 'reporting_prison_officer', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'task_group', 'under_budget'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Healtheventtype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Healtheventtype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Healtheventtype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_add_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'adjourned_to', 'adjournment_reason', 'atendance', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'court_cases', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'endtime', 'goal', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'late_end', 'late_start', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'not_started', 'notes', 'over_budget', 'planned_end', 'planned_start', 'postponement_reason', 'priority', 'reason', 'schedule_status', 'schedulestatustype', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'starttime', 'status', 'task_group', 'transcript', 'under_budget', 'yearday']


Hearing_edit_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'adjourned_to', 'adjournment_reason', 'atendance', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'court_cases', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'endtime', 'goal', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'late_end', 'late_start', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'not_started', 'notes', 'over_budget', 'planned_end', 'planned_start', 'postponement_reason', 'priority', 'reason', 'schedule_status', 'schedulestatustype', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'starttime', 'status', 'task_group', 'transcript', 'under_budget', 'yearday']


Hearing_list_columns = ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'adjourned_to', 'adjournment_reason', 'atendance', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'court_cases', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'endtime', 'goal', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'late_end', 'late_start', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'not_started', 'notes', 'over_budget', 'planned_end', 'planned_start', 'postponement_reason', 'priority', 'reason', 'schedule_status', 'schedulestatustype', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'starttime', 'status', 'task_group', 'transcript', 'under_budget', 'yearday']


Hearing_add_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'adjourned_to', 'adjournment_reason', 'atendance', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'court_cases', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'endtime', 'goal', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'late_end', 'late_start', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'not_started', 'notes', 'over_budget', 'planned_end', 'planned_start', 'postponement_reason', 'priority', 'reason', 'schedule_status', 'schedulestatustype', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'starttime', 'status', 'task_group', 'transcript', 'under_budget', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_edit_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'adjourned_to', 'adjournment_reason', 'atendance', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'court_cases', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'endtime', 'goal', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'late_end', 'late_start', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'not_started', 'notes', 'over_budget', 'planned_end', 'planned_start', 'postponement_reason', 'priority', 'reason', 'schedule_status', 'schedulestatustype', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'starttime', 'status', 'task_group', 'transcript', 'under_budget', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_show_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity_description', 'actual_end', 'actual_start', 'adjourned_to', 'adjournment_reason', 'atendance', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'completed', 'contingency_plan', 'court_cases', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'deviation_expected', 'early_end', 'early_start', 'end_delay', 'end_notes', 'endtime', 'goal', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'late_end', 'late_start', 'lawfirm', 'lawfirm1', 'metadata', 'next_hearing_date', 'not_started', 'notes', 'over_budget', 'planned_end', 'planned_start', 'postponement_reason', 'priority', 'reason', 'schedule_status', 'schedulestatustype', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'starttime', 'status', 'task_group', 'transcript', 'under_budget', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'hearing_type', 'id', 'metadata', 'name', 'notes', 'parent']


Hearingtype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'hearing_type', 'id', 'metadata', 'name', 'notes', 'parent']


Hearingtype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'hearing_type', 'id', 'metadata', 'name', 'notes', 'parent']


Hearingtype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'hearing_type', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'hearing_type', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'hearing_type', 'id', 'metadata', 'name', 'notes', 'parent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'id', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'id', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'id', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'id', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'id', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'id', 'issue', 'metadata', 'parties', 'party', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_add_columns = ['answer', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated']


Interview_edit_columns = ['answer', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated']


Interview_list_columns = ['answer', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated']


Interview_add_field_set = [
    ('Data', {'fields': ['answer', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_edit_field_set = [
    ('Data', {'fields': ['answer', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_show_field_set = [
    ('Data', {'fields': ['answer', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_add_columns = ['action', 'active', 'activity', 'activity_description', 'actual_end', 'actual_start', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'detained', 'detained_at', 'deviation_expected', 'docx', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'equipmentresults', 'goal', 'id', 'late_end', 'late_start', 'location', 'metadata', 'not_started', 'outcome', 'over_budget', 'party', 'planned_end', 'planned_start', 'policeofficer', 'priority', 'provisional_release_statement', 'search_seizure_statement', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'summons_statement', 'task_group', 'under_budget', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_edit_columns = ['action', 'active', 'activity', 'activity_description', 'actual_end', 'actual_start', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'detained', 'detained_at', 'deviation_expected', 'docx', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'equipmentresults', 'goal', 'id', 'late_end', 'late_start', 'location', 'metadata', 'not_started', 'outcome', 'over_budget', 'party', 'planned_end', 'planned_start', 'policeofficer', 'priority', 'provisional_release_statement', 'search_seizure_statement', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'summons_statement', 'task_group', 'under_budget', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_list_columns = ['action', 'active', 'activity', 'activity_description', 'actual_end', 'actual_start', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'detained', 'detained_at', 'deviation_expected', 'docx', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'equipmentresults', 'goal', 'id', 'late_end', 'late_start', 'location', 'metadata', 'not_started', 'outcome', 'over_budget', 'party', 'planned_end', 'planned_start', 'policeofficer', 'priority', 'provisional_release_statement', 'search_seizure_statement', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'summons_statement', 'task_group', 'under_budget', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_add_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity', 'activity_description', 'actual_end', 'actual_start', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'detained', 'detained_at', 'deviation_expected', 'docx', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'equipmentresults', 'goal', 'id', 'late_end', 'late_start', 'location', 'metadata', 'not_started', 'outcome', 'over_budget', 'party', 'planned_end', 'planned_start', 'policeofficer', 'priority', 'provisional_release_statement', 'search_seizure_statement', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'summons_statement', 'task_group', 'under_budget', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_edit_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity', 'activity_description', 'actual_end', 'actual_start', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'detained', 'detained_at', 'deviation_expected', 'docx', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'equipmentresults', 'goal', 'id', 'late_end', 'late_start', 'location', 'metadata', 'not_started', 'outcome', 'over_budget', 'party', 'planned_end', 'planned_start', 'policeofficer', 'priority', 'provisional_release_statement', 'search_seizure_statement', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'summons_statement', 'task_group', 'under_budget', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_show_field_set = [
    ('Data', {'fields': ['action', 'active', 'activity', 'activity_description', 'actual_end', 'actual_start', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'balance_avail', 'budget', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'completed', 'contingency_plan', 'created_by', 'created_by_fk', 'created_on', 'deadline', 'detained', 'detained_at', 'deviation_expected', 'docx', 'early_end', 'early_start', 'end_delay', 'end_notes', 'enddate', 'equipmentresults', 'goal', 'id', 'late_end', 'late_start', 'location', 'metadata', 'not_started', 'outcome', 'over_budget', 'party', 'planned_end', 'planned_start', 'policeofficer', 'priority', 'provisional_release_statement', 'search_seizure_statement', 'segment', 'sequence', 'spend_td', 'start_delay', 'start_notes', 'startdate', 'status', 'summons_statement', 'task_group', 'under_budget', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_add_columns = ['argument', 'argument_date', 'argument_docx', 'changed_by', 'changed_by_fk', 'changed_on', 'counter_claim', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_edit_columns = ['argument', 'argument_date', 'argument_docx', 'changed_by', 'changed_by_fk', 'changed_on', 'counter_claim', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_list_columns = ['argument', 'argument_date', 'argument_docx', 'changed_by', 'changed_by_fk', 'changed_on', 'counter_claim', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_add_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'changed_by', 'changed_by_fk', 'changed_on', 'counter_claim', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_edit_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'changed_by', 'changed_by_fk', 'changed_on', 'counter_claim', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_show_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'changed_by', 'changed_by_fk', 'changed_on', 'counter_claim', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'moral_element', 'party', 'party1', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'court_station', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'marital_status', 'metadata', 'othernames', 'rank', 'surname']


Judicialofficer_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'court_station', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'marital_status', 'metadata', 'othernames', 'rank', 'surname']


Judicialofficer_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'court_station', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'marital_status', 'metadata', 'othernames', 'rank', 'surname']


Judicialofficer_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'court_station', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'marital_status', 'metadata', 'othernames', 'rank', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'court_station', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'marital_status', 'metadata', 'othernames', 'rank', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'court_station', 'courtstation', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'marital_status', 'metadata', 'othernames', 'rank', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Judicialrank_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Judicialrank_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Judicialrank_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Judicialrole_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Judicialrole_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Judicialrole_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name']


Law_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name']


Law_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name']


Law_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_add_columns = ['address_line_1', 'address_line_2', 'alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'country', 'created_by', 'created_by_fk', 'created_on', 'description', 'email', 'facebook', 'fax', 'fixed_line', 'gcode', 'id', 'info', 'instagram', 'lat', 'lng', 'map', 'metadata', 'mobile', 'name', 'nearest_feature', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'twitter', 'whatsapp', 'zipcode']


Lawfirm_edit_columns = ['address_line_1', 'address_line_2', 'alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'country', 'created_by', 'created_by_fk', 'created_on', 'description', 'email', 'facebook', 'fax', 'fixed_line', 'gcode', 'id', 'info', 'instagram', 'lat', 'lng', 'map', 'metadata', 'mobile', 'name', 'nearest_feature', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'twitter', 'whatsapp', 'zipcode']


Lawfirm_list_columns = ['address_line_1', 'address_line_2', 'alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'country', 'created_by', 'created_by_fk', 'created_on', 'description', 'email', 'facebook', 'fax', 'fixed_line', 'gcode', 'id', 'info', 'instagram', 'lat', 'lng', 'map', 'metadata', 'mobile', 'name', 'nearest_feature', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'twitter', 'whatsapp', 'zipcode']


Lawfirm_add_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'country', 'created_by', 'created_by_fk', 'created_on', 'description', 'email', 'facebook', 'fax', 'fixed_line', 'gcode', 'id', 'info', 'instagram', 'lat', 'lng', 'map', 'metadata', 'mobile', 'name', 'nearest_feature', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_edit_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'country', 'created_by', 'created_by_fk', 'created_on', 'description', 'email', 'facebook', 'fax', 'fixed_line', 'gcode', 'id', 'info', 'instagram', 'lat', 'lng', 'map', 'metadata', 'mobile', 'name', 'nearest_feature', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_show_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'code', 'country', 'created_by', 'created_by_fk', 'created_on', 'description', 'email', 'facebook', 'fax', 'fixed_line', 'gcode', 'id', 'info', 'instagram', 'lat', 'lng', 'map', 'metadata', 'mobile', 'name', 'nearest_feature', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_add_columns = ['address_line_1', 'address_line_2', 'bar_date', 'bar_no', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'law_firm', 'lawfirm', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'party', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Lawyer_edit_columns = ['address_line_1', 'address_line_2', 'bar_date', 'bar_no', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'law_firm', 'lawfirm', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'party', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Lawyer_list_columns = ['address_line_1', 'address_line_2', 'bar_date', 'bar_no', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'law_firm', 'lawfirm', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'party', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Lawyer_add_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'bar_date', 'bar_no', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'law_firm', 'lawfirm', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'party', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_edit_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'bar_date', 'bar_no', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'law_firm', 'lawfirm', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'party', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_show_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'bar_date', 'bar_no', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'law_firm', 'lawfirm', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'party', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'citation', 'commentary', 'created_by', 'created_by_fk', 'created_on', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'citation', 'commentary', 'created_by', 'created_by_fk', 'created_on', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'citation', 'commentary', 'created_by', 'created_by_fk', 'created_on', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'citation', 'commentary', 'created_by', 'created_by_fk', 'created_on', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'citation', 'commentary', 'created_by', 'created_by_fk', 'created_on', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'citation', 'commentary', 'created_by', 'created_by_fk', 'created_on', 'id', 'interpretation', 'metadata', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_add_columns = ['address_line_1', 'address_line_2', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'biodata', 'biodata1', 'changed_by', 'changed_by_fk', 'changed_on', 'childunder4', 'citizenship', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'marital_status', 'metadata', 'mobile', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Nextofkin_edit_columns = ['address_line_1', 'address_line_2', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'biodata', 'biodata1', 'changed_by', 'changed_by_fk', 'changed_on', 'childunder4', 'citizenship', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'marital_status', 'metadata', 'mobile', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Nextofkin_list_columns = ['address_line_1', 'address_line_2', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'biodata', 'biodata1', 'changed_by', 'changed_by_fk', 'changed_on', 'childunder4', 'citizenship', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'marital_status', 'metadata', 'mobile', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Nextofkin_add_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'biodata', 'biodata1', 'changed_by', 'changed_by_fk', 'changed_on', 'childunder4', 'citizenship', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'marital_status', 'metadata', 'mobile', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_edit_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'biodata', 'biodata1', 'changed_by', 'changed_by_fk', 'changed_on', 'childunder4', 'citizenship', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'marital_status', 'metadata', 'mobile', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_show_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'bc_id', 'bc_number', 'bc_place', 'bc_scan', 'bc_serial', 'biodata', 'biodata1', 'changed_by', 'changed_by_fk', 'changed_on', 'childunder4', 'citizenship', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'kin1_addr', 'kin1_email', 'kin1_name', 'kin1_phone', 'kin1_relation', 'kin2_addr', 'kin2_email', 'kin2_name', 'kin2_phone', 'marital_status', 'metadata', 'mobile', 'nat_id_num', 'nat_id_scan', 'nat_id_serial', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'pp_expiry_date', 'pp_issue_date', 'pp_issue_place', 'pp_no', 'pp_scan', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_add_columns = ['abandon', 'add_date', 'changed_by', 'changed_by_fk', 'changed_on', 'confirmation', 'contact', 'created_by', 'created_by_fk', 'created_on', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent']


Notification_edit_columns = ['abandon', 'add_date', 'changed_by', 'changed_by_fk', 'changed_on', 'confirmation', 'contact', 'created_by', 'created_by_fk', 'created_on', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent']


Notification_list_columns = ['abandon', 'add_date', 'changed_by', 'changed_by_fk', 'changed_on', 'confirmation', 'contact', 'created_by', 'created_by_fk', 'created_on', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent']


Notification_add_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'changed_by', 'changed_by_fk', 'changed_on', 'confirmation', 'contact', 'created_by', 'created_by_fk', 'created_on', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_edit_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'changed_by', 'changed_by_fk', 'changed_on', 'confirmation', 'contact', 'created_by', 'created_by_fk', 'created_on', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_show_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'changed_by', 'changed_by_fk', 'changed_on', 'confirmation', 'contact', 'created_by', 'created_by_fk', 'created_on', 'delivered', 'id', 'message', 'metadata', 'notification_register', 'notificationregister', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_add_columns = ['active', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count']


Notificationregister_edit_columns = ['active', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count']


Notificationregister_list_columns = ['active', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count']


Notificationregister_add_field_set = [
    ('Data', {'fields': ['active', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_edit_field_set = [
    ('Data', {'fields': ['active', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_show_field_set = [
    ('Data', {'fields': ['active', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Notificationtype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Notificationtype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Notificationtype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Notifyevent_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Notifyevent_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Notifyevent_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'create_date', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt']


Page_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'create_date', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt']


Page_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'create_date', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt']


Page_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'create_date', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'create_date', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'create_date', 'created_by', 'created_by_fk', 'created_on', 'document', 'document1', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'page_image', 'page_no', 'page_text', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_add_columns = ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint_role', 'complaintrole', 'complaints', 'country', 'created_by', 'created_by_fk', 'created_on', 'dateofrepresentation', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'is_infant', 'is_minor', 'marital_status', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'mobile', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'parent', 'party_type', 'partytype', 'relationship_type', 'relative', 'settlement', 'statement', 'statementdate', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Party_edit_columns = ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint_role', 'complaintrole', 'complaints', 'country', 'created_by', 'created_by_fk', 'created_on', 'dateofrepresentation', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'is_infant', 'is_minor', 'marital_status', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'mobile', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'parent', 'party_type', 'partytype', 'relationship_type', 'relative', 'settlement', 'statement', 'statementdate', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Party_list_columns = ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint_role', 'complaintrole', 'complaints', 'country', 'created_by', 'created_by_fk', 'created_on', 'dateofrepresentation', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'is_infant', 'is_minor', 'marital_status', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'mobile', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'parent', 'party_type', 'partytype', 'relationship_type', 'relative', 'settlement', 'statement', 'statementdate', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Party_add_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint_role', 'complaintrole', 'complaints', 'country', 'created_by', 'created_by_fk', 'created_on', 'dateofrepresentation', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'is_infant', 'is_minor', 'marital_status', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'mobile', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'parent', 'party_type', 'partytype', 'relationship_type', 'relative', 'settlement', 'statement', 'statementdate', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_edit_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint_role', 'complaintrole', 'complaints', 'country', 'created_by', 'created_by_fk', 'created_on', 'dateofrepresentation', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'is_infant', 'is_minor', 'marital_status', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'mobile', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'parent', 'party_type', 'partytype', 'relationship_type', 'relative', 'settlement', 'statement', 'statementdate', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_show_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint_role', 'complaintrole', 'complaints', 'country', 'created_by', 'created_by_fk', 'created_on', 'dateofrepresentation', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'is_infant', 'is_minor', 'marital_status', 'metadata', 'miranda_date', 'miranda_read', 'miranda_witness', 'mobile', 'notes', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'parent', 'party_type', 'partytype', 'relationship_type', 'relative', 'settlement', 'statement', 'statementdate', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Partytype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Partytype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Partytype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_add_columns = ['amount', 'bill', 'bill1', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated']


Payment_edit_columns = ['amount', 'bill', 'bill1', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated']


Payment_list_columns = ['amount', 'bill', 'bill1', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated']


Payment_add_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_edit_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_show_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'date_paid', 'id', 'metadata', 'payment_description', 'payment_ref', 'phone_number', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory']


Personaleffect_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory']


Personaleffect_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory']


Personaleffect_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Personaleffectscategory_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Personaleffectscategory_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Personaleffectscategory_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber', 'surname']


Policeofficer_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber', 'surname']


Policeofficer_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber', 'surname']


Policeofficer_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'sequence']


Policeofficerrank_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'sequence']


Policeofficerrank_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'sequence']


Policeofficerrank_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'officer_commanding', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Policestationrank_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Policestationrank_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Policestationrank_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_add_columns = ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'town1']


Prison_edit_columns = ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'town1']


Prison_list_columns = ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'town1']


Prison_add_field_set = [
    ('Data', {'fields': ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_edit_field_set = [
    ('Data', {'fields': ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_show_field_set = [
    ('Data', {'fields': ['alt', 'centered', 'changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'info', 'lat', 'lng', 'map', 'metadata', 'nearest_feature', 'pin', 'pin_color', 'pin_icon', 'place_name', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank', 'surname']


Prisonofficer_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank', 'surname']


Prisonofficer_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank', 'surname']


Prisonofficer_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'dob', 'firstname', 'gender', 'id', 'marital_status', 'metadata', 'othernames', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank', 'surname'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Prisonofficerrank_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Prisonofficerrank_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Prisonofficerrank_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_add_columns = ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'lawyer', 'lawyer1', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'prosecutor_team', 'prosecutorteam', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Prosecutor_edit_columns = ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'lawyer', 'lawyer1', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'prosecutor_team', 'prosecutorteam', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Prosecutor_list_columns = ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'lawyer', 'lawyer1', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'prosecutor_team', 'prosecutorteam', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode']


Prosecutor_add_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'lawyer', 'lawyer1', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'prosecutor_team', 'prosecutorteam', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_edit_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'lawyer', 'lawyer1', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'prosecutor_team', 'prosecutorteam', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_show_field_set = [
    ('Data', {'fields': ['address_line_1', 'address_line_2', 'changed_by', 'changed_by_fk', 'changed_on', 'country', 'created_by', 'created_by_fk', 'created_on', 'dob', 'email', 'facebook', 'fax', 'firstname', 'fixed_line', 'gcode', 'gender', 'id', 'instagram', 'lawyer', 'lawyer1', 'marital_status', 'metadata', 'mobile', 'okhi', 'other_email', 'other_fixed_line', 'other_mobile', 'other_whatsapp', 'othernames', 'prosecutor_team', 'prosecutorteam', 'surname', 'town', 'twitter', 'whatsapp', 'zipcode'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Prosecutorteam_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Prosecutorteam_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Prosecutorteam_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Releasetype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Releasetype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Releasetype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Religion_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Religion_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Religion_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Schedulestatustype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Schedulestatustype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Schedulestatustype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'notes', 'owner', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_add_columns = ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'created_by', 'created_by_fk', 'created_on', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms']


Settlement_edit_columns = ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'created_by', 'created_by_fk', 'created_on', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms']


Settlement_list_columns = ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'created_by', 'created_by_fk', 'created_on', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms']


Settlement_add_field_set = [
    ('Data', {'fields': ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'created_by', 'created_by_fk', 'created_on', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_edit_field_set = [
    ('Data', {'fields': ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'created_by', 'created_by_fk', 'created_on', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_show_field_set = [
    ('Data', {'fields': ['amount', 'changed_by', 'changed_by_fk', 'changed_on', 'complaint', 'complaint1', 'created_by', 'created_by_fk', 'created_on', 'docx', 'id', 'metadata', 'paid', 'party', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'county', 'county1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Subcounty_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'county', 'county1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Subcounty_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'county', 'county1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata']


Subcounty_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'county', 'county1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'county', 'county1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'county', 'county1', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'template_type']


Templatetype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'template_type']


Templatetype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'template_type']


Templatetype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes', 'parent', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'ward']


Town_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'ward']


Town_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'ward']


Town_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_add_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'certfiy_date', 'certified_transcript', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'edit_date', 'edited_transcript', 'file_size_bytes', 'hashx', 'hearing', 'hearing1', 'id', 'immutable', 'keywords', 'lines', 'locked', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'subject', 'video', 'word_count']


Transcript_edit_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'certfiy_date', 'certified_transcript', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'edit_date', 'edited_transcript', 'file_size_bytes', 'hashx', 'hearing', 'hearing1', 'id', 'immutable', 'keywords', 'lines', 'locked', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'subject', 'video', 'word_count']


Transcript_list_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'certfiy_date', 'certified_transcript', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'edit_date', 'edited_transcript', 'file_size_bytes', 'hashx', 'hearing', 'hearing1', 'id', 'immutable', 'keywords', 'lines', 'locked', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'subject', 'video', 'word_count']


Transcript_add_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'certfiy_date', 'certified_transcript', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'edit_date', 'edited_transcript', 'file_size_bytes', 'hashx', 'hearing', 'hearing1', 'id', 'immutable', 'keywords', 'lines', 'locked', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'subject', 'video', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_edit_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'certfiy_date', 'certified_transcript', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'edit_date', 'edited_transcript', 'file_size_bytes', 'hashx', 'hearing', 'hearing1', 'id', 'immutable', 'keywords', 'lines', 'locked', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'subject', 'video', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_show_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'audio_channels', 'audio_duration_secs', 'audio_frame_rate', 'author', 'certfiy_date', 'certified_transcript', 'changed_by', 'changed_by_fk', 'changed_on', 'char_count', 'comments', 'created_by', 'created_by_fk', 'created_on', 'doc', 'doc_binary', 'doc_text', 'doc_title', 'doc_type', 'edit_date', 'edited_transcript', 'file_size_bytes', 'hashx', 'hearing', 'hearing1', 'id', 'immutable', 'keywords', 'lines', 'locked', 'metadata', 'mime_type', 'page_count', 'page_size', 'paragraphs', 'producer_prog', 'search_vector', 'subject', 'video', 'word_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno']


Vehicle_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno']


Vehicle_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno']


Vehicle_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'make', 'metadata', 'model', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'subcounty', 'subcounty1']


Ward_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'subcounty', 'subcounty1']


Ward_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'subcounty', 'subcounty1']


Ward_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on', 'id', 'metadata', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Warranttype_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Warranttype_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes']


Warranttype_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'code', 'created_by', 'created_by_fk', 'created_on', 'description', 'id', 'metadata', 'name', 'notes'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



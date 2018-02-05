CREATE TABLE "accounttype" (
  "id" INTEGER CONSTRAINT "pk_accounttype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "casecategory" (
  "id" INTEGER CONSTRAINT "pk_casecategory" PRIMARY KEY AUTOINCREMENT,
  "subcategory" INTEGER REFERENCES "casecategory" ("id")
);

CREATE INDEX "idx_casecategory__subcategory" ON "casecategory" ("subcategory");

CREATE TABLE "casechecklist" (
  "id" INTEGER CONSTRAINT "pk_casechecklist" PRIMARY KEY AUTOINCREMENT,
  "name" VARCHAR(100) NOT NULL,
  "description" VARCHAR(100) NOT NULL,
  "notes" TEXT NOT NULL
);

CREATE TABLE "casecategorychecklist" (
  "case_checklists" INTEGER NOT NULL REFERENCES "casechecklist" ("id"),
  "case_categories" INTEGER NOT NULL REFERENCES "casecategory" ("id"),
  CONSTRAINT "pk_casecategorychecklist" PRIMARY KEY ("case_checklists", "case_categories")
);

CREATE INDEX "idx_casecategorychecklist__case_categories" ON "casecategorychecklist" ("case_categories");

CREATE TABLE "caselinktype" (
  "id" INTEGER CONSTRAINT "pk_caselinktype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "celltype" (
  "id" INTEGER CONSTRAINT "pk_celltype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "commitaltype" (
  "id" INTEGER CONSTRAINT "pk_commitaltype" PRIMARY KEY AUTOINCREMENT,
  "maxduration" INTERVAL
);

CREATE TABLE "complaintcategory" (
  "id" INTEGER CONSTRAINT "pk_complaintcategory" PRIMARY KEY AUTOINCREMENT,
  "complaint_category_parent" INTEGER REFERENCES "complaintcategory" ("id")
);

CREATE INDEX "idx_complaintcategory__complaint_category_parent" ON "complaintcategory" ("complaint_category_parent");

CREATE TABLE "complaintrole" (
  "id" INTEGER CONSTRAINT "pk_complaintrole" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "country" (
  "id" INTEGER CONSTRAINT "pk_country" PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL
);

CREATE TABLE "county" (
  "id" INTEGER CONSTRAINT "pk_county" PRIMARY KEY AUTOINCREMENT,
  "country" INTEGER NOT NULL REFERENCES "country" ("id")
);

CREATE INDEX "idx_county__country" ON "county" ("country");

CREATE TABLE "courtrank" (
  "id" INTEGER CONSTRAINT "pk_courtrank" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "courtstation" (
  "id" INTEGER CONSTRAINT "pk_courtstation" PRIMARY KEY AUTOINCREMENT,
  "till_number" TEXT NOT NULL,
  "pay_bill" TEXT NOT NULL
);

CREATE TABLE "csi_equipment" (
  "id" INTEGER CONSTRAINT "pk_csi_equipment" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "documenttype" (
  "id" INTEGER CONSTRAINT "pk_documenttype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "economicclass" (
  "id" INTEGER CONSTRAINT "pk_economicclass" PRIMARY KEY AUTOINCREMENT,
  "name" VARCHAR(50) NOT NULL,
  "description" VARCHAR(100) NOT NULL
);

CREATE TABLE "expert" (
  "id" INTEGER CONSTRAINT "pk_expert" PRIMARY KEY AUTOINCREMENT,
  "institution" TEXT NOT NULL,
  "jobtitle" TEXT NOT NULL,
  "credentials" TEXT NOT NULL
);

CREATE TABLE "experttype" (
  "id" INTEGER CONSTRAINT "pk_experttype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "expert_expert_types" (
  "expert" INTEGER NOT NULL REFERENCES "expert" ("id"),
  "experttype" INTEGER NOT NULL REFERENCES "experttype" ("id"),
  CONSTRAINT "pk_expert_expert_types" PRIMARY KEY ("expert", "experttype")
);

CREATE INDEX "idx_expert_expert_types" ON "expert_expert_types" ("experttype");

CREATE TABLE "feeclass" (
  "id" INTEGER CONSTRAINT "pk_feeclass" PRIMARY KEY AUTOINCREMENT,
  "fee_type" INTEGER REFERENCES "feeclass" ("id")
);

CREATE INDEX "idx_feeclass__fee_type" ON "feeclass" ("fee_type");

CREATE TABLE "feetype" (
  "id" INTEGER CONSTRAINT "pk_feetype" PRIMARY KEY AUTOINCREMENT,
  "filing_fee_type" INTEGER NOT NULL REFERENCES "feeclass" ("id"),
  "amount" DECIMAL(12, 2),
  "unit" TEXT NOT NULL,
  "min_fee" DECIMAL(12, 2),
  "max_fee" DECIMAL(12, 2),
  "description" TEXT,
  "guide_sec" TEXT,
  "guide_clause" TEXT,
  "account_type" INTEGER NOT NULL REFERENCES "accounttype" ("id")
);

CREATE INDEX "idx_feetype__account_type" ON "feetype" ("account_type");

CREATE INDEX "idx_feetype__filing_fee_type" ON "feetype" ("filing_fee_type");

CREATE TABLE "healtheventtype" (
  "id" INTEGER CONSTRAINT "pk_healtheventtype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "hearingtype" (
  "id" INTEGER CONSTRAINT "pk_hearingtype" PRIMARY KEY AUTOINCREMENT,
  "hearing_type" INTEGER REFERENCES "hearingtype" ("id")
);

CREATE INDEX "idx_hearingtype__hearing_type" ON "hearingtype" ("hearing_type");

CREATE TABLE "judicialrank" (
  "id" INTEGER CONSTRAINT "pk_judicialrank" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "judicialrole" (
  "id" INTEGER CONSTRAINT "pk_judicialrole" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "judicialofficer" (
  "id" INTEGER CONSTRAINT "pk_judicialofficer" PRIMARY KEY AUTOINCREMENT,
  "rank" INTEGER NOT NULL REFERENCES "judicialrank" ("id"),
  "judicial_role" INTEGER NOT NULL REFERENCES "judicialrole" ("id"),
  "court_station" INTEGER NOT NULL REFERENCES "courtstation" ("id")
);

CREATE INDEX "idx_judicialofficer__court_station" ON "judicialofficer" ("court_station");

CREATE INDEX "idx_judicialofficer__judicial_role" ON "judicialofficer" ("judicial_role");

CREATE INDEX "idx_judicialofficer__rank" ON "judicialofficer" ("rank");

CREATE TABLE "law" (
  "id" INTEGER CONSTRAINT "pk_law" PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "description" TEXT NOT NULL
);

CREATE TABLE "crime" (
  "id" INTEGER CONSTRAINT "pk_crime" PRIMARY KEY AUTOINCREMENT,
  "law" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "ref" TEXT NOT NULL,
  "ref_law" INTEGER REFERENCES "law" ("id")
);

CREATE INDEX "idx_crime__ref_law" ON "crime" ("ref_law");

CREATE TABLE "lawfirm" (
  "id" INTEGER CONSTRAINT "pk_lawfirm" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "lawyer" (
  "id" INTEGER CONSTRAINT "pk_lawyer" PRIMARY KEY AUTOINCREMENT,
  "law_firm" INTEGER REFERENCES "lawfirm" ("id"),
  "bar_no" TEXT NOT NULL,
  "bar_date" DATE
);

CREATE INDEX "idx_lawyer__law_firm" ON "lawyer" ("law_firm");

CREATE TABLE "legalreference" (
  "id" INTEGER CONSTRAINT "pk_legalreference" PRIMARY KEY AUTOINCREMENT,
  "ref" TEXT NOT NULL,
  "verbatim" TEXT NOT NULL,
  "public" BOOLEAN,
  "commentary" TEXT NOT NULL,
  "validated" BOOLEAN,
  "citation" TEXT NOT NULL,
  "quote" TEXT NOT NULL,
  "interpretation" TEXT NOT NULL
);

CREATE TABLE "notificationtype" (
  "id" INTEGER CONSTRAINT "pk_notificationtype" PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "description" TEXT NOT NULL
);

CREATE TABLE "notifyevent" (
  "id" INTEGER CONSTRAINT "pk_notifyevent" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "partytype" (
  "id" INTEGER CONSTRAINT "pk_partytype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "personaleffectscategory" (
  "id" INTEGER CONSTRAINT "pk_personaleffectscategory" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "policeofficerrank" (
  "id" INTEGER CONSTRAINT "pk_policeofficerrank" PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "sequence" INTEGER
);

CREATE TABLE "policeofficer" (
  "id" INTEGER CONSTRAINT "pk_policeofficer" PRIMARY KEY AUTOINCREMENT,
  "police_rank" INTEGER NOT NULL REFERENCES "policeofficerrank" ("id"),
  "servicenumber" VARCHAR(100) UNIQUE NOT NULL
);

CREATE INDEX "idx_policeofficer__police_rank" ON "policeofficer" ("police_rank");

CREATE TABLE "investigating_officer" (
  "police_officers" INTEGER NOT NULL CONSTRAINT "pk_investigating_officer" PRIMARY KEY REFERENCES "policeofficer" ("id"),
  "date_assigned" DATETIME,
  "lead_investigator" INTEGER
);

CREATE TABLE "policestationrank" (
  "id" INTEGER CONSTRAINT "pk_policestationrank" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "prisonofficerrank" (
  "id" INTEGER CONSTRAINT "pk_prisonofficerrank" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "prosecutorteam" (
  "id" INTEGER CONSTRAINT "pk_prosecutorteam" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "prosecutor" (
  "id" INTEGER CONSTRAINT "pk_prosecutor" PRIMARY KEY AUTOINCREMENT,
  "prosecutor_team" INTEGER REFERENCES "prosecutorteam" ("id"),
  "lawyer" INTEGER NOT NULL REFERENCES "lawyer" ("id")
);

CREATE INDEX "idx_prosecutor__lawyer" ON "prosecutor" ("lawyer");

CREATE INDEX "idx_prosecutor__prosecutor_team" ON "prosecutor" ("prosecutor_team");

CREATE TABLE "courtcase" (
  "id" INTEGER CONSTRAINT "pk_courtcase" PRIMARY KEY AUTOINCREMENT,
  "docket_number" TEXT NOT NULL,
  "case_number" TEXT NOT NULL,
  "adr" BOOLEAN,
  "mediation_proposal" TEXT NOT NULL,
  "case_received_date" DATE,
  "case_filed_date" DATE,
  "case_summary" TEXT NOT NULL,
  "filing_prosecutor" INTEGER REFERENCES "prosecutor" ("id"),
  "fast_track" BOOLEAN,
  "priority" INTEGER,
  "object_of_litigation" TEXT NOT NULL,
  "grounds" TEXT NOT NULL,
  "prosecution_prayer" TEXT NOT NULL,
  "pretrial_date" DATE,
  "pretrial_notes" TEXT NOT NULL,
  "pretrial_registrar" INTEGER REFERENCES "judicialofficer" ("id"),
  "case_admissible" BOOLEAN,
  "indictment_date" TEXT NOT NULL,
  "judgement" TEXT NOT NULL,
  "judgement_docx" TEXT NOT NULL,
  "case_link_type" INTEGER REFERENCES "caselinktype" ("id"),
  "linked_cases" INTEGER REFERENCES "courtcase" ("id"),
  "appealed" BOOLEAN,
  "appeal_number" TEXT NOT NULL,
  "inventory_of_docket" TEXT NOT NULL,
  "next_hearing_date" DATE,
  "interlocutory_judgement" TEXT NOT NULL,
  "reopen" BOOLEAN,
  "reopen_reason" TEXT NOT NULL,
  "combined_case" BOOLEAN,
  "value_in_dispute" DECIMAL(12, 2),
  "award" DECIMAL(12, 2),
  "govt_liability" TEXT NOT NULL,
  "active" BOOLEAN,
  "active_date" DATETIME
);

CREATE INDEX "idx_courtcase__case_link_type" ON "courtcase" ("case_link_type");

CREATE INDEX "idx_courtcase__filing_prosecutor" ON "courtcase" ("filing_prosecutor");

CREATE INDEX "idx_courtcase__linked_cases" ON "courtcase" ("linked_cases");

CREATE INDEX "idx_courtcase__pretrial_registrar" ON "courtcase" ("pretrial_registrar");

CREATE TABLE "casecategory_court_cases" (
  "courtcase" INTEGER NOT NULL REFERENCES "courtcase" ("id"),
  "casecategory" INTEGER NOT NULL REFERENCES "casecategory" ("id"),
  CONSTRAINT "pk_casecategory_court_cases" PRIMARY KEY ("courtcase", "casecategory")
);

CREATE INDEX "idx_casecategory_court_cases" ON "casecategory_court_cases" ("casecategory");

CREATE TABLE "courtcase_bench" (
  "judicialofficer" INTEGER NOT NULL REFERENCES "judicialofficer" ("id"),
  "courtcase" INTEGER NOT NULL REFERENCES "courtcase" ("id"),
  CONSTRAINT "pk_courtcase_bench" PRIMARY KEY ("judicialofficer", "courtcase")
);

CREATE INDEX "idx_courtcase_bench" ON "courtcase_bench" ("courtcase");

CREATE TABLE "courtcase_law_firm" (
  "lawfirm" INTEGER NOT NULL REFERENCES "lawfirm" ("id"),
  "courtcase" INTEGER NOT NULL REFERENCES "courtcase" ("id"),
  CONSTRAINT "pk_courtcase_law_firm" PRIMARY KEY ("lawfirm", "courtcase")
);

CREATE INDEX "idx_courtcase_law_firm" ON "courtcase_law_firm" ("courtcase");

CREATE TABLE "issue" (
  "id" INTEGER CONSTRAINT "pk_issue" PRIMARY KEY AUTOINCREMENT,
  "issue" TEXT NOT NULL,
  "facts" TEXT,
  "counter_claim" BOOLEAN,
  "argument" TEXT NOT NULL,
  "argument_date" DATE,
  "argument_docx" TEXT,
  "rebuttal" TEXT NOT NULL,
  "rebuttal_date" DATE,
  "rebuttal_docx" TEXT,
  "hearing_date" DATE,
  "determination" TEXT NOT NULL,
  "dtermination_date" DATE,
  "determination_docx" TEXT NOT NULL,
  "resolved" BOOLEAN,
  "defense_lawyer" INTEGER NOT NULL REFERENCES "lawyer" ("id"),
  "prosecutor" INTEGER REFERENCES "prosecutor" ("id"),
  "judicial_officer" INTEGER NOT NULL REFERENCES "judicialofficer" ("id"),
  "court_case" INTEGER NOT NULL REFERENCES "courtcase" ("id"),
  "tasks" TEXT NOT NULL,
  "is_criminal" BOOLEAN,
  "moral_element" TEXT NOT NULL,
  "material_element" TEXT NOT NULL,
  "legal_element" TEXT NOT NULL,
  "debt_amount" DECIMAL(12, 2)
);

CREATE INDEX "idx_issue__court_case" ON "issue" ("court_case");

CREATE INDEX "idx_issue__defense_lawyer" ON "issue" ("defense_lawyer");

CREATE INDEX "idx_issue__judicial_officer" ON "issue" ("judicial_officer");

CREATE INDEX "idx_issue__prosecutor" ON "issue" ("prosecutor");

CREATE TABLE "issue_argument_legal_references" (
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  "legalreference" INTEGER NOT NULL REFERENCES "legalreference" ("id"),
  CONSTRAINT "pk_issue_argument_legal_references" PRIMARY KEY ("issue", "legalreference")
);

CREATE INDEX "idx_issue_argument_legal_references" ON "issue_argument_legal_references" ("legalreference");

CREATE TABLE "issue_plaintiff_lawyers" (
  "lawyer" INTEGER NOT NULL REFERENCES "lawyer" ("id"),
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  CONSTRAINT "pk_issue_plaintiff_lawyers" PRIMARY KEY ("lawyer", "issue")
);

CREATE INDEX "idx_issue_plaintiff_lawyers" ON "issue_plaintiff_lawyers" ("issue");

CREATE TABLE "issue_rebuttal_legal_references" (
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  "legalreference" INTEGER NOT NULL REFERENCES "legalreference" ("id"),
  CONSTRAINT "pk_issue_rebuttal_legal_references" PRIMARY KEY ("issue", "legalreference")
);

CREATE INDEX "idx_issue_rebuttal_legal_references" ON "issue_rebuttal_legal_references" ("legalreference");

CREATE TABLE "releasetype" (
  "id" INTEGER CONSTRAINT "pk_releasetype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "religion" (
  "id" INTEGER CONSTRAINT "pk_religion" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "schedulestatustype" (
  "id" INTEGER CONSTRAINT "pk_schedulestatustype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "hearing" (
  "id" INTEGER CONSTRAINT "pk_hearing" PRIMARY KEY AUTOINCREMENT,
  "court_cases" INTEGER REFERENCES "courtcase" ("id"),
  "hearing_type" INTEGER NOT NULL REFERENCES "hearingtype" ("id"),
  "schedule_status" INTEGER NOT NULL REFERENCES "schedulestatustype" ("id"),
  "hearing_date" DATE,
  "reason" TEXT NOT NULL,
  "sequence" INTEGER UNSIGNED,
  "yearday" INTEGER UNSIGNED,
  "starttime" TIME,
  "endtime" TIME,
  "notes" TEXT NOT NULL,
  "completed" BOOLEAN,
  "adjourned_to" DATE,
  "adjournment_reason" TEXT NOT NULL,
  "transcript" TEXT NOT NULL,
  "atendance" TEXT NOT NULL,
  "next_hearing_date" DATE,
  "postponement_reason" TEXT NOT NULL
);

CREATE INDEX "idx_hearing__court_cases" ON "hearing" ("court_cases");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

CREATE INDEX "idx_hearing__schedule_status" ON "hearing" ("schedule_status");

CREATE TABLE "hearing_adjudicating_officer" (
  "judicialofficer" INTEGER NOT NULL REFERENCES "judicialofficer" ("id"),
  "hearing" INTEGER NOT NULL REFERENCES "hearing" ("id"),
  CONSTRAINT "pk_hearing_adjudicating_officer" PRIMARY KEY ("judicialofficer", "hearing")
);

CREATE INDEX "idx_hearing_adjudicating_officer" ON "hearing_adjudicating_officer" ("hearing");

CREATE TABLE "hearing_issues" (
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  "hearing" INTEGER NOT NULL REFERENCES "hearing" ("id"),
  CONSTRAINT "pk_hearing_issues" PRIMARY KEY ("issue", "hearing")
);

CREATE INDEX "idx_hearing_issues" ON "hearing_issues" ("hearing");

CREATE TABLE "hearing_lawyer_plaintiff" (
  "lawfirm" INTEGER NOT NULL REFERENCES "lawfirm" ("id"),
  "hearing" INTEGER NOT NULL REFERENCES "hearing" ("id"),
  CONSTRAINT "pk_hearing_lawyer_plaintiff" PRIMARY KEY ("lawfirm", "hearing")
);

CREATE INDEX "idx_hearing_lawyer_plaintiff" ON "hearing_lawyer_plaintiff" ("hearing");

CREATE TABLE "hearing_lawyers_defense" (
  "lawfirm" INTEGER NOT NULL REFERENCES "lawfirm" ("id"),
  "hearing" INTEGER NOT NULL REFERENCES "hearing" ("id"),
  CONSTRAINT "pk_hearing_lawyers_defense" PRIMARY KEY ("lawfirm", "hearing")
);

CREATE INDEX "idx_hearing_lawyers_defense" ON "hearing_lawyers_defense" ("hearing");

CREATE TABLE "subcounty" (
  "id" INTEGER CONSTRAINT "pk_subcounty" PRIMARY KEY AUTOINCREMENT,
  "county" INTEGER NOT NULL REFERENCES "county" ("id")
);

CREATE INDEX "idx_subcounty__county" ON "subcounty" ("county");

CREATE TABLE "templatetype" (
  "id" INTEGER CONSTRAINT "pk_templatetype" PRIMARY KEY AUTOINCREMENT,
  "template_type" INTEGER REFERENCES "templatetype" ("id")
);

CREATE INDEX "idx_templatetype__template_type" ON "templatetype" ("template_type");

CREATE TABLE "doctemplate" (
  "id" INTEGER CONSTRAINT "pk_doctemplate" PRIMARY KEY AUTOINCREMENT,
  "template" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "name" TEXT NOT NULL,
  "title" TEXT NOT NULL,
  "summary" TEXT NOT NULL,
  "template_type" INTEGER NOT NULL REFERENCES "templatetype" ("id"),
  "icon" TEXT NOT NULL
);

CREATE INDEX "idx_doctemplate__template_type" ON "doctemplate" ("template_type");

CREATE TABLE "document" (
  "id" INTEGER CONSTRAINT "pk_document" PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "court_case" INTEGER REFERENCES "courtcase" ("id"),
  "issue" INTEGER REFERENCES "issue" ("id"),
  "document_admissibility" TEXT NOT NULL,
  "admitted" BOOLEAN,
  "judicial_officer" INTEGER REFERENCES "judicialofficer" ("id"),
  "filing_date" DATETIME,
  "admisibility_notes" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "document_text" TEXT NOT NULL,
  "published" BOOLEAN,
  "publish_newspaper" TEXT NOT NULL,
  "publish_date" DATE,
  "validated" BOOLEAN,
  "paid" BOOLEAN,
  "page_count" INTEGER,
  "file_byte_count" DECIMAL(12, 2),
  "file_hash" TEXT NOT NULL,
  "file_timestamp" TEXT NOT NULL,
  "file_create_date" DATETIME,
  "file_update_date" DATETIME,
  "file_text" TEXT NOT NULL,
  "file_name" TEXT NOT NULL,
  "file_ext" TEXT NOT NULL,
  "file_load_path" TEXT NOT NULL,
  "file_upload_date" DATETIME,
  "file_parse_status" TEXT NOT NULL,
  "doc_template" INTEGER REFERENCES "doctemplate" ("id"),
  "visible" BOOLEAN,
  "is_scan" BOOLEAN,
  "doc_shelf" TEXT NOT NULL,
  "doc_row" TEXT NOT NULL,
  "doc_room" TEXT NOT NULL,
  "doc_placed_by" TEXT NOT NULL,
  "citation" TEXT NOT NULL
);

CREATE INDEX "idx_document__court_case" ON "document" ("court_case");

CREATE INDEX "idx_document__doc_template" ON "document" ("doc_template");

CREATE INDEX "idx_document__issue" ON "document" ("issue");

CREATE INDEX "idx_document__judicial_officer" ON "document" ("judicial_officer");

CREATE TABLE "document_document_types" (
  "document" INTEGER NOT NULL REFERENCES "document" ("id"),
  "documenttype" INTEGER NOT NULL REFERENCES "documenttype" ("id"),
  CONSTRAINT "pk_document_document_types" PRIMARY KEY ("document", "documenttype")
);

CREATE INDEX "idx_document_document_types" ON "document_document_types" ("documenttype");

CREATE TABLE "page" (
  "id" INTEGER CONSTRAINT "pk_page" PRIMARY KEY AUTOINCREMENT,
  "document" INTEGER NOT NULL REFERENCES "document" ("id"),
  "page_image" BLOB,
  "page_no" INTEGER UNSIGNED,
  "page_text" TEXT NOT NULL,
  "image_ext" TEXT,
  "image_width" TEXT,
  "image_height" TEXT,
  "create_date" DATETIME,
  "update_date" DATETIME,
  "upload_dt" DATETIME
);

CREATE INDEX "idx_page__document" ON "page" ("document");

CREATE TABLE "town" (
  "id" INTEGER CONSTRAINT "pk_town" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "court" (
  "id" INTEGER CONSTRAINT "pk_court" PRIMARY KEY AUTOINCREMENT,
  "court_rank" INTEGER NOT NULL REFERENCES "courtrank" ("id"),
  "court_station" INTEGER NOT NULL REFERENCES "courtstation" ("id"),
  "town" INTEGER NOT NULL REFERENCES "town" ("id"),
  "till_number" TEXT NOT NULL
);

CREATE INDEX "idx_court__court_rank" ON "court" ("court_rank");

CREATE INDEX "idx_court__court_station" ON "court" ("court_station");

CREATE INDEX "idx_court__town" ON "court" ("town");

CREATE TABLE "court_judicial_officers" (
  "court" INTEGER NOT NULL REFERENCES "court" ("id"),
  "judicialofficer" INTEGER NOT NULL REFERENCES "judicialofficer" ("id"),
  CONSTRAINT "pk_court_judicial_officers" PRIMARY KEY ("court", "judicialofficer")
);

CREATE INDEX "idx_court_judicial_officers" ON "court_judicial_officers" ("judicialofficer");

CREATE TABLE "courtaccount" (
  "courts" INTEGER NOT NULL REFERENCES "court" ("id"),
  "account__types" INTEGER NOT NULL REFERENCES "accounttype" ("id"),
  "account_number" TEXT NOT NULL,
  "account_name" TEXT NOT NULL,
  "short_code" TEXT NOT NULL,
  "bank_name" TEXT NOT NULL,
  CONSTRAINT "pk_courtaccount" PRIMARY KEY ("courts", "account__types")
);

CREATE INDEX "idx_courtaccount__account__types" ON "courtaccount" ("account__types");

CREATE TABLE "policestation" (
  "id" INTEGER CONSTRAINT "pk_policestation" PRIMARY KEY AUTOINCREMENT,
  "town" INTEGER REFERENCES "town" ("id"),
  "officer_commanding" INTEGER NOT NULL REFERENCES "policeofficer" ("id"),
  "police_station_rank" INTEGER NOT NULL REFERENCES "policestationrank" ("id")
);

CREATE INDEX "idx_policestation__officer_commanding" ON "policestation" ("officer_commanding");

CREATE INDEX "idx_policestation__police_station_rank" ON "policestation" ("police_station_rank");

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

CREATE TABLE "complaint" (
  "id" INTEGER CONSTRAINT "pk_complaint" PRIMARY KEY AUTOINCREMENT,
  "active" BOOLEAN,
  "ob_number" VARCHAR(20) NOT NULL,
  "police_station" INTEGER NOT NULL REFERENCES "policestation" ("id"),
  "daterecvd" DATETIME NOT NULL,
  "datefiled" DATETIME,
  "datecaseopened" DATETIME,
  "casesummary" VARCHAR(2000) NOT NULL,
  "complaintstatement" TEXT NOT NULL,
  "circumstances" TEXT NOT NULL,
  "reportingofficer" INTEGER NOT NULL REFERENCES "policeofficer" ("id"),
  "casefileinformation" TEXT NOT NULL,
  "p_request_help" BOOLEAN,
  "p_instruction" TEXT NOT NULL,
  "p_submitted" BOOLEAN,
  "p_submission_date" DATETIME,
  "p_submission_notes" TEXT NOT NULL,
  "p_closed" TEXT NOT NULL,
  "p_evaluation" TEXT NOT NULL,
  "p_recommend_charge" BOOLEAN,
  "charge_sheet" TEXT NOT NULL,
  "charge_sheet_docx" TEXT NOT NULL,
  "evaluating_prosecutor_team" INTEGER REFERENCES "prosecutorteam" ("id"),
  "magistrate_report_date" DATETIME,
  "reported_to_judicial_officer" INTEGER REFERENCES "judicialofficer" ("id"),
  "closed" BOOLEAN,
  "close_date" DATETIME,
  "close_reason" TEXT NOT NULL
);

CREATE INDEX "idx_complaint__evaluating_prosecutor_team" ON "complaint" ("evaluating_prosecutor_team");

CREATE INDEX "idx_complaint__police_station" ON "complaint" ("police_station");

CREATE INDEX "idx_complaint__reported_to_judicial_officer" ON "complaint" ("reported_to_judicial_officer");

CREATE INDEX "idx_complaint__reportingofficer" ON "complaint" ("reportingofficer");

CREATE TABLE "complaint_complaint_categories" (
  "complaint" INTEGER NOT NULL REFERENCES "complaint" ("id"),
  "complaintcategory" INTEGER NOT NULL REFERENCES "complaintcategory" ("id"),
  CONSTRAINT "pk_complaint_complaint_categories" PRIMARY KEY ("complaint", "complaintcategory")
);

CREATE INDEX "idx_complaint_complaint_categories" ON "complaint_complaint_categories" ("complaintcategory");

CREATE TABLE "complaint_court_cases" (
  "complaint" INTEGER NOT NULL REFERENCES "complaint" ("id"),
  "courtcase" INTEGER NOT NULL REFERENCES "courtcase" ("id"),
  CONSTRAINT "pk_complaint_court_cases" PRIMARY KEY ("complaint", "courtcase")
);

CREATE INDEX "idx_complaint_court_cases" ON "complaint_court_cases" ("courtcase");

CREATE TABLE "party" (
  "complaints" INTEGER NOT NULL CONSTRAINT "pk_party" PRIMARY KEY REFERENCES "complaint" ("id"),
  "statement" VARCHAR(1000) NOT NULL,
  "statementdate" DATETIME,
  "complaint_role" INTEGER NOT NULL REFERENCES "complaintrole" ("id"),
  "notes" TEXT NOT NULL,
  "dateofrepresentation" DATETIME,
  "party_type" INTEGER NOT NULL REFERENCES "partytype" ("id"),
  "relative" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "relationship_type" TEXT NOT NULL,
  "is_infant" BOOLEAN,
  "is_minor" BOOLEAN,
  "miranda_read" BOOLEAN,
  "miranda_date" DATETIME,
  "miranda_witness" TEXT NOT NULL
);

CREATE INDEX "idx_party__complaint_role" ON "party" ("complaint_role");

CREATE INDEX "idx_party__party_type" ON "party" ("party_type");

CREATE INDEX "idx_party__relative" ON "party" ("relative");

CREATE TABLE "bill" (
  "id" INTEGER CONSTRAINT "pk_bill" PRIMARY KEY AUTOINCREMENT,
  "assessing_registrar" INTEGER NOT NULL REFERENCES "judicialofficer" ("id"),
  "receiving_registrar" INTEGER NOT NULL REFERENCES "judicialofficer" ("id"),
  "lawyer_paying" INTEGER REFERENCES "lawyer" ("id"),
  "party_paying" INTEGER REFERENCES "party" ("complaints"),
  "documents" INTEGER REFERENCES "document" ("id"),
  "date_of_payment" DATETIME,
  "paid" BOOLEAN,
  "pay_code" VARCHAR(20) UNIQUE,
  "bill_total" DECIMAL(12, 2),
  "court" INTEGER NOT NULL REFERENCES "court" ("id"),
  "court_account_courts" INTEGER NOT NULL,
  "court_account_account__types" INTEGER NOT NULL,
  "validated" BOOLEAN,
  "validation_date" DATETIME,
  FOREIGN KEY ("court_account_courts", "court_account_account__types") REFERENCES "courtaccount" ("courts", "account__types")
);

CREATE INDEX "idx_bill__assessing_registrar" ON "bill" ("assessing_registrar");

CREATE INDEX "idx_bill__court" ON "bill" ("court");

CREATE INDEX "idx_bill__court_account_courts_court_account_account__types" ON "bill" ("court_account_courts", "court_account_account__types");

CREATE INDEX "idx_bill__documents" ON "bill" ("documents");

CREATE INDEX "idx_bill__lawyer_paying" ON "bill" ("lawyer_paying");

CREATE INDEX "idx_bill__party_paying" ON "bill" ("party_paying");

CREATE INDEX "idx_bill__receiving_registrar" ON "bill" ("receiving_registrar");

CREATE TABLE "billdetail" (
  "id" INTEGER CONSTRAINT "pk_billdetail" PRIMARY KEY AUTOINCREMENT,
  "receipt_id" INTEGER NOT NULL REFERENCES "bill" ("id"),
  "feetype" INTEGER NOT NULL REFERENCES "feetype" ("id"),
  "purpose" TEXT NOT NULL,
  "unit" TEXT,
  "qty" INTEGER DEFAULT 1,
  "unit_cost" DECIMAL(12, 2),
  "amount" DECIMAL(12, 2)
);

CREATE INDEX "idx_billdetail__feetype" ON "billdetail" ("feetype");

CREATE INDEX "idx_billdetail__receipt_id" ON "billdetail" ("receipt_id");

CREATE TABLE "biodata" (
  "id" INTEGER CONSTRAINT "pk_biodata" PRIMARY KEY AUTOINCREMENT,
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "economic_class" INTEGER REFERENCES "economicclass" ("id"),
  "religion" INTEGER REFERENCES "religion" ("id"),
  "photo" BLOB,
  "health_status" TEXT NOT NULL
);

CREATE INDEX "idx_biodata__economic_class" ON "biodata" ("economic_class");

CREATE INDEX "idx_biodata__party" ON "biodata" ("party");

CREATE INDEX "idx_biodata__religion" ON "biodata" ("religion");

CREATE TABLE "instancecrime" (
  "parties" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "crimes" INTEGER NOT NULL REFERENCES "crime" ("id"),
  "crime_detail" TEXT NOT NULL,
  "tffender_type" TEXT NOT NULL,
  "crime_date" DATETIME,
  "date_note" TEXT NOT NULL,
  "place_of_crime" TEXT NOT NULL,
  "place_note" TEXT NOT NULL,
  CONSTRAINT "pk_instancecrime" PRIMARY KEY ("parties", "crimes")
);

CREATE INDEX "idx_instancecrime__crimes" ON "instancecrime" ("crimes");

CREATE TABLE "instancecrime_issues" (
  "instancecrime_parties" INTEGER NOT NULL,
  "instancecrime_crimes" INTEGER NOT NULL,
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  CONSTRAINT "pk_instancecrime_issues" PRIMARY KEY ("instancecrime_parties", "instancecrime_crimes", "issue"),
  FOREIGN KEY ("instancecrime_parties", "instancecrime_crimes") REFERENCES "instancecrime" ("parties", "crimes")
);

CREATE INDEX "idx_instancecrime_issues" ON "instancecrime_issues" ("issue");

CREATE TABLE "issue_defending_parties" (
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  CONSTRAINT "pk_issue_defending_parties" PRIMARY KEY ("party", "issue")
);

CREATE INDEX "idx_issue_defending_parties" ON "issue_defending_parties" ("issue");

CREATE TABLE "issue_injured_parties" (
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "issue" INTEGER NOT NULL REFERENCES "issue" ("id"),
  CONSTRAINT "pk_issue_injured_parties" PRIMARY KEY ("party", "issue")
);

CREATE INDEX "idx_issue_injured_parties" ON "issue_injured_parties" ("issue");

CREATE TABLE "lawyer_representing" (
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "lawyer" INTEGER NOT NULL REFERENCES "lawyer" ("id"),
  CONSTRAINT "pk_lawyer_representing" PRIMARY KEY ("party", "lawyer")
);

CREATE INDEX "idx_lawyer_representing" ON "lawyer_representing" ("lawyer");

CREATE TABLE "nextofkin" (
  "id" INTEGER CONSTRAINT "pk_nextofkin" PRIMARY KEY AUTOINCREMENT,
  "biodata" INTEGER NOT NULL REFERENCES "biodata" ("id"),
  "childunder4" BOOLEAN
);

CREATE INDEX "idx_nextofkin__biodata" ON "nextofkin" ("biodata");

CREATE TABLE "payment" (
  "id" INTEGER CONSTRAINT "pk_payment" PRIMARY KEY AUTOINCREMENT,
  "bill" INTEGER NOT NULL REFERENCES "bill" ("id"),
  "amount" DECIMAL(12, 2),
  "payment_ref" TEXT NOT NULL,
  "date_paid" DATETIME,
  "phone_number" VARCHAR(20),
  "validated" BOOLEAN,
  "payment_description" TEXT
);

CREATE INDEX "idx_payment__bill" ON "payment" ("bill");

CREATE TABLE "personaleffect" (
  "id" INTEGER CONSTRAINT "pk_personaleffect" PRIMARY KEY AUTOINCREMENT,
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "personal_effects_category" INTEGER NOT NULL REFERENCES "personaleffectscategory" ("id")
);

CREATE INDEX "idx_personaleffect__party" ON "personaleffect" ("party");

CREATE INDEX "idx_personaleffect__personal_effects_category" ON "personaleffect" ("personal_effects_category");

CREATE TABLE "policeofficer_assigned_station" (
  "policestation" INTEGER NOT NULL REFERENCES "policestation" ("id"),
  "policeofficer" INTEGER NOT NULL REFERENCES "policeofficer" ("id"),
  CONSTRAINT "pk_policeofficer_assigned_station" PRIMARY KEY ("policestation", "policeofficer")
);

CREATE INDEX "idx_policeofficer_assigned_station" ON "policeofficer_assigned_station" ("policeofficer");

CREATE TABLE "prison" (
  "id" INTEGER CONSTRAINT "pk_prison" PRIMARY KEY AUTOINCREMENT,
  "town" INTEGER NOT NULL REFERENCES "town" ("id")
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

CREATE TABLE "prisonofficer" (
  "id" INTEGER CONSTRAINT "pk_prisonofficer" PRIMARY KEY AUTOINCREMENT,
  "prison" INTEGER NOT NULL REFERENCES "prison" ("id"),
  "prison_officer_rank" INTEGER NOT NULL REFERENCES "prisonofficerrank" ("id")
);

CREATE INDEX "idx_prisonofficer__prison" ON "prisonofficer" ("prison");

CREATE INDEX "idx_prisonofficer__prison_officer_rank" ON "prisonofficer" ("prison_officer_rank");

CREATE TABLE "discipline" (
  "id" INTEGER CONSTRAINT "pk_discipline" PRIMARY KEY AUTOINCREMENT,
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "prison_officer" INTEGER NOT NULL REFERENCES "prisonofficer" ("id")
);

CREATE INDEX "idx_discipline__party" ON "discipline" ("party");

CREATE INDEX "idx_discipline__prison_officer" ON "discipline" ("prison_officer");

CREATE TABLE "healthevent" (
  "id" INTEGER CONSTRAINT "pk_healthevent" PRIMARY KEY AUTOINCREMENT,
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "reporting_prison_officer" INTEGER REFERENCES "prisonofficer" ("id"),
  "health_event_type" INTEGER NOT NULL REFERENCES "healtheventtype" ("id"),
  "startdate" DATETIME,
  "enddate" DATETIME,
  "notes" TEXT NOT NULL
);

CREATE INDEX "idx_healthevent__health_event_type" ON "healthevent" ("health_event_type");

CREATE INDEX "idx_healthevent__party" ON "healthevent" ("party");

CREATE INDEX "idx_healthevent__reporting_prison_officer" ON "healthevent" ("reporting_prison_officer");

CREATE TABLE "notificationregister" (
  "id" INTEGER CONSTRAINT "pk_notificationregister" PRIMARY KEY AUTOINCREMENT,
  "notification_type" INTEGER NOT NULL REFERENCES "notificationtype" ("id"),
  "contact" TEXT NOT NULL,
  "notify_event" INTEGER REFERENCES "notifyevent" ("id"),
  "retry_count" INTEGER UNSIGNED DEFAULT 3,
  "active" BOOLEAN,
  "hearing" INTEGER REFERENCES "hearing" ("id"),
  "document" INTEGER REFERENCES "document" ("id"),
  "court_case" INTEGER REFERENCES "courtcase" ("id"),
  "complaint" INTEGER REFERENCES "complaint" ("id"),
  "complaint_category" INTEGER REFERENCES "complaintcategory" ("id"),
  "health_event" INTEGER REFERENCES "healthevent" ("id"),
  "party" INTEGER REFERENCES "party" ("complaints")
);

CREATE INDEX "idx_notificationregister__complaint" ON "notificationregister" ("complaint");

CREATE INDEX "idx_notificationregister__complaint_category" ON "notificationregister" ("complaint_category");

CREATE INDEX "idx_notificationregister__court_case" ON "notificationregister" ("court_case");

CREATE INDEX "idx_notificationregister__document" ON "notificationregister" ("document");

CREATE INDEX "idx_notificationregister__health_event" ON "notificationregister" ("health_event");

CREATE INDEX "idx_notificationregister__hearing" ON "notificationregister" ("hearing");

CREATE INDEX "idx_notificationregister__notification_type" ON "notificationregister" ("notification_type");

CREATE INDEX "idx_notificationregister__notify_event" ON "notificationregister" ("notify_event");

CREATE INDEX "idx_notificationregister__party" ON "notificationregister" ("party");

CREATE TABLE "notification" (
  "id" INTEGER CONSTRAINT "pk_notification" PRIMARY KEY AUTOINCREMENT,
  "contact" TEXT NOT NULL,
  "message" TEXT NOT NULL,
  "confirmation" TEXT NOT NULL,
  "notification_register" INTEGER REFERENCES "notificationregister" ("id"),
  "add_date" DATETIME,
  "send_date" DATETIME,
  "sent" BOOLEAN,
  "delivered" BOOLEAN,
  "retries" INTEGER,
  "abandon" BOOLEAN,
  "retry_count" INTEGER DEFAULT 3
);

CREATE INDEX "idx_notification__notification_register" ON "notification" ("notification_register");

CREATE TABLE "settlement" (
  "id" INTEGER CONSTRAINT "pk_settlement" PRIMARY KEY AUTOINCREMENT,
  "complaint" INTEGER NOT NULL REFERENCES "complaint" ("id"),
  "terms" TEXT NOT NULL,
  "amount" DECIMAL(12, 2),
  "paid" BOOLEAN,
  "docx" TEXT NOT NULL,
  "settlor" INTEGER NOT NULL REFERENCES "party" ("complaints")
);

CREATE INDEX "idx_settlement__complaint" ON "settlement" ("complaint");

CREATE INDEX "idx_settlement__settlor" ON "settlement" ("settlor");

CREATE TABLE "party_settlees" (
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "settlement" INTEGER NOT NULL REFERENCES "settlement" ("id"),
  CONSTRAINT "pk_party_settlees" PRIMARY KEY ("party", "settlement")
);

CREATE INDEX "idx_party_settlees" ON "party_settlees" ("settlement");

CREATE TABLE "transcript" (
  "id" INTEGER CONSTRAINT "pk_transcript" PRIMARY KEY AUTOINCREMENT,
  "video" TEXT NOT NULL,
  "audio" TEXT NOT NULL,
  "add_date" DATETIME,
  "asr_transcript" TEXT NOT NULL,
  "asr_date" DATETIME,
  "edited_transcript" TEXT NOT NULL,
  "edit_date" DATETIME,
  "certified_transcript" TEXT NOT NULL,
  "certfiy_date" DATETIME,
  "locked" BOOLEAN,
  "hearing" INTEGER NOT NULL REFERENCES "hearing" ("id")
);

CREATE INDEX "idx_transcript__hearing" ON "transcript" ("hearing");

CREATE TABLE "vehicle" (
  "id" INTEGER CONSTRAINT "pk_vehicle" PRIMARY KEY AUTOINCREMENT,
  "police_station" INTEGER NOT NULL REFERENCES "policestation" ("id"),
  "make" VARCHAR(100) NOT NULL,
  "model" VARCHAR(100) NOT NULL,
  "regno" VARCHAR(100) NOT NULL
);

CREATE INDEX "idx_vehicle__police_station" ON "vehicle" ("police_station");

CREATE TABLE "ward" (
  "id" INTEGER CONSTRAINT "pk_ward" PRIMARY KEY AUTOINCREMENT,
  "subcounty" INTEGER NOT NULL REFERENCES "subcounty" ("id")
);

CREATE INDEX "idx_ward__subcounty" ON "ward" ("subcounty");

CREATE TABLE "town_wards" (
  "ward" INTEGER NOT NULL REFERENCES "ward" ("id"),
  "town" INTEGER NOT NULL REFERENCES "town" ("id"),
  CONSTRAINT "pk_town_wards" PRIMARY KEY ("ward", "town")
);

CREATE INDEX "idx_town_wards" ON "town_wards" ("town");

CREATE TABLE "warranttype" (
  "id" INTEGER CONSTRAINT "pk_warranttype" PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "commital" (
  "id" INTEGER CONSTRAINT "pk_commital" PRIMARY KEY AUTOINCREMENT,
  "prisons" INTEGER REFERENCES "prison" ("id"),
  "police_station" INTEGER REFERENCES "policestation" ("id"),
  "parties" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "casecomplete" BOOLEAN,
  "commit_date" DATE NOT NULL,
  "purpose" TEXT NOT NULL,
  "warrant_type" INTEGER NOT NULL REFERENCES "warranttype" ("id"),
  "warrant_docx" TEXT NOT NULL,
  "warrant_issue_date" DATE,
  "warrant_issued_by" TEXT NOT NULL,
  "warrant_date_attached" DATETIME,
  "duration" INTERVAL,
  "commital" INTEGER REFERENCES "commital" ("id"),
  "commital_type" INTEGER NOT NULL REFERENCES "commitaltype" ("id"),
  "court_case" INTEGER REFERENCES "courtcase" ("id"),
  "concurrent" BOOLEAN,
  "life_imprisonment" BOOLEAN,
  "arrival_date" DATETIME,
  "sentence_start_date" DATETIME,
  "arrest_date" DATETIME,
  "remaining_years" INTEGER,
  "remaining_months" INTEGER,
  "remaining_days" INTEGER,
  "cell_number" TEXT NOT NULL,
  "cell_type" INTEGER REFERENCES "celltype" ("id"),
  "release_date" DATETIME,
  "exit_date" DATETIME,
  "reason_for_release" TEXT NOT NULL,
  "with_children" BOOLEAN,
  "release_type" INTEGER REFERENCES "releasetype" ("id"),
  "receiving_officer" INTEGER NOT NULL REFERENCES "prisonofficer" ("id"),
  "releasing_officer" INTEGER NOT NULL REFERENCES "prisonofficer" ("id")
);

CREATE INDEX "idx_commital__cell_type" ON "commital" ("cell_type");

CREATE INDEX "idx_commital__commital" ON "commital" ("commital");

CREATE INDEX "idx_commital__commital_type" ON "commital" ("commital_type");

CREATE INDEX "idx_commital__court_case" ON "commital" ("court_case");

CREATE INDEX "idx_commital__parties" ON "commital" ("parties");

CREATE INDEX "idx_commital__police_station" ON "commital" ("police_station");

CREATE INDEX "idx_commital__prisons" ON "commital" ("prisons");

CREATE INDEX "idx_commital__receiving_officer" ON "commital" ("receiving_officer");

CREATE INDEX "idx_commital__release_type" ON "commital" ("release_type");

CREATE INDEX "idx_commital__releasing_officer" ON "commital" ("releasing_officer");

CREATE INDEX "idx_commital__warrant_type" ON "commital" ("warrant_type");

CREATE TABLE "investigationdiary" (
  "id" INTEGER CONSTRAINT "pk_investigationdiary" PRIMARY KEY AUTOINCREMENT,
  "complaint" INTEGER NOT NULL REFERENCES "complaint" ("id"),
  "activity" TEXT NOT NULL,
  "location" TEXT NOT NULL,
  "outcome" TEXT NOT NULL,
  "equipmentresults" TEXT NOT NULL,
  "startdate" DATETIME NOT NULL,
  "enddate" DATETIME,
  "advocate_present" TEXT NOT NULL,
  "summons_statement" TEXT NOT NULL,
  "arrest_statement" TEXT NOT NULL,
  "arrest_warrant" TEXT NOT NULL,
  "search_seizure_statement" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "detained" TEXT NOT NULL,
  "detained_at" TEXT NOT NULL,
  "provisional_release_statement" TEXT NOT NULL,
  "warrant_type" INTEGER REFERENCES "warranttype" ("id"),
  "warrant_issued_by" TEXT NOT NULL,
  "warrant_issue_date" DATE,
  "warrant_delivered_by" TEXT NOT NULL,
  "warrant_received_by" TEXT NOT NULL,
  "warrant_serve_date" TEXT NOT NULL,
  "warrant_docx" TEXT NOT NULL,
  "warrant_upload_date" TEXT NOT NULL
);

CREATE INDEX "idx_investigationdiary__complaint" ON "investigationdiary" ("complaint");

CREATE INDEX "idx_investigationdiary__warrant_type" ON "investigationdiary" ("warrant_type");

CREATE TABLE "csi_equipment_investigation_entries" (
  "investigationdiary" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "csi_equipment" INTEGER NOT NULL REFERENCES "csi_equipment" ("id"),
  CONSTRAINT "pk_csi_equipment_investigation_entries" PRIMARY KEY ("investigationdiary", "csi_equipment")
);

CREATE INDEX "idx_csi_equipment_investigation_entries" ON "csi_equipment_investigation_entries" ("csi_equipment");

CREATE TABLE "diagram" (
  "id" INTEGER CONSTRAINT "pk_diagram" PRIMARY KEY AUTOINCREMENT,
  "investigation_diary" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "image" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "docx" TEXT NOT NULL
);

CREATE INDEX "idx_diagram__investigation_diary" ON "diagram" ("investigation_diary");

CREATE TABLE "experttestimony" (
  "requesting_officer" INTEGER NOT NULL REFERENCES "investigating_officer" ("police_officers"),
  "investigation_entries" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "experts" INTEGER NOT NULL REFERENCES "expert" ("id"),
  "task_given" TEXT NOT NULL,
  "summary_of_facts" TEXT NOT NULL,
  "statement" TEXT NOT NULL,
  "testimony_date" DATETIME,
  "task_request_date" DATE,
  "docx" TEXT NOT NULL,
  "validated" BOOLEAN,
  CONSTRAINT "pk_experttestimony" PRIMARY KEY ("investigation_entries", "experts")
);

CREATE INDEX "idx_experttestimony__experts" ON "experttestimony" ("experts");

CREATE INDEX "idx_experttestimony__requesting_officer" ON "experttestimony" ("requesting_officer");

CREATE TABLE "interview" (
  "id" INTEGER CONSTRAINT "pk_interview" PRIMARY KEY AUTOINCREMENT,
  "investigation_entry" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "question" TEXT NOT NULL,
  "answer" TEXT NOT NULL,
  "validated" BOOLEAN,
  "language" TEXT NOT NULL
);

CREATE INDEX "idx_interview__investigation_entry" ON "interview" ("investigation_entry");

CREATE TABLE "investigating_officer_investigation_entries" (
  "investigating_officer" INTEGER NOT NULL REFERENCES "investigating_officer" ("police_officers"),
  "investigationdiary" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  CONSTRAINT "pk_investigating_officer_investigation_entries" PRIMARY KEY ("investigating_officer", "investigationdiary")
);

CREATE INDEX "idx_investigating_officer_investigation_entries" ON "investigating_officer_investigation_entries" ("investigationdiary");

CREATE TABLE "investigationdiary_parties" (
  "party" INTEGER NOT NULL REFERENCES "party" ("complaints"),
  "investigationdiary" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  CONSTRAINT "pk_investigationdiary_parties" PRIMARY KEY ("party", "investigationdiary")
);

CREATE INDEX "idx_investigationdiary_parties" ON "investigationdiary_parties" ("investigationdiary");

CREATE TABLE "investigationdiary_vehicles" (
  "investigationdiary" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "vehicle" INTEGER NOT NULL REFERENCES "vehicle" ("id"),
  CONSTRAINT "pk_investigationdiary_vehicles" PRIMARY KEY ("investigationdiary", "vehicle")
);

CREATE INDEX "idx_investigationdiary_vehicles" ON "investigationdiary_vehicles" ("vehicle");

CREATE TABLE "seizure" (
  "id" INTEGER CONSTRAINT "pk_seizure" PRIMARY KEY AUTOINCREMENT,
  "investigation_diary" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "owner" TEXT NOT NULL,
  "item" TEXT NOT NULL,
  "item_packaging" TEXT NOT NULL,
  "item_pic" TEXT NOT NULL,
  "premises" TEXT NOT NULL,
  "reg_no" TEXT NOT NULL,
  "witness" TEXT NOT NULL,
  "notes" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "item_description" TEXT NOT NULL,
  "returned" BOOLEAN,
  "return_date" DATETIME,
  "return_notes" TEXT NOT NULL,
  "return_signed_receipt" TEXT NOT NULL,
  "destroyed" BOOLEAN,
  "destruction_date" DATE,
  "destruction_witnesses" TEXT NOT NULL,
  "destruction_notes" TEXT NOT NULL,
  "disposed" BOOLEAN,
  "sold_to" TEXT NOT NULL,
  "disposal_date" DATE,
  "disposal_price" DECIMAL(12, 2),
  "disposal_receipt" TEXT NOT NULL,
  "recovery_town" INTEGER REFERENCES "town" ("id"),
  "destruction_pic" TEXT NOT NULL,
  "is_evidence" BOOLEAN,
  "immovable" BOOLEAN
);

CREATE INDEX "idx_seizure__investigation_diary" ON "seizure" ("investigation_diary");

CREATE INDEX "idx_seizure__recovery_town" ON "seizure" ("recovery_town");

CREATE TABLE "exhibit" (
  "id" INTEGER CONSTRAINT "pk_exhibit" PRIMARY KEY AUTOINCREMENT,
  "investigation_entry" INTEGER NOT NULL REFERENCES "investigationdiary" ("id"),
  "photo" TEXT NOT NULL,
  "exhibit_no" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "seizure" INTEGER NOT NULL REFERENCES "seizure" ("id")
);

CREATE INDEX "idx_exhibit__investigation_entry" ON "exhibit" ("investigation_entry");

CREATE INDEX "idx_exhibit__seizure" ON "exhibit" ("seizure")


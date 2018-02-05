CREATE TABLE "casecategory" (
  "id" SERIAL CONSTRAINT "pk_casecategory" PRIMARY KEY,
  "subcategory" INTEGER
);

CREATE INDEX "idx_casecategory__subcategory" ON "casecategory" ("subcategory");

ALTER TABLE "casecategory" ADD CONSTRAINT "fk_casecategory__subcategory" FOREIGN KEY ("subcategory") REFERENCES "casecategory" ("id");

CREATE TABLE "caselinktype" (
  "id" SERIAL CONSTRAINT "pk_caselinktype" PRIMARY KEY
);

CREATE TABLE "celltype" (
  "id" SERIAL CONSTRAINT "pk_celltype" PRIMARY KEY
);

CREATE TABLE "commitaltype" (
  "id" SERIAL CONSTRAINT "pk_commitaltype" PRIMARY KEY,
  "maxduration" INTERVAL DAY TO SECOND
);

CREATE TABLE "complaintcategory" (
  "id" SERIAL CONSTRAINT "pk_complaintcategory" PRIMARY KEY,
  "complaint_category_parent" INTEGER
);

CREATE INDEX "idx_complaintcategory__complaint_category_parent" ON "complaintcategory" ("complaint_category_parent");

ALTER TABLE "complaintcategory" ADD CONSTRAINT "fk_complaintcategory__complaint_category_parent" FOREIGN KEY ("complaint_category_parent") REFERENCES "complaintcategory" ("id");

CREATE TABLE "complaintrole" (
  "id" SERIAL CONSTRAINT "pk_complaintrole" PRIMARY KEY
);

CREATE TABLE "country" (
  "id" SERIAL CONSTRAINT "pk_country" PRIMARY KEY,
  "name" TEXT NOT NULL
);

CREATE TABLE "county" (
  "id" SERIAL CONSTRAINT "pk_county" PRIMARY KEY,
  "country" INTEGER NOT NULL
);

CREATE INDEX "idx_county__country" ON "county" ("country");

ALTER TABLE "county" ADD CONSTRAINT "fk_county__country" FOREIGN KEY ("country") REFERENCES "country" ("id");

CREATE TABLE "courtrank" (
  "id" SERIAL CONSTRAINT "pk_courtrank" PRIMARY KEY
);

CREATE TABLE "courtstation" (
  "id" SERIAL CONSTRAINT "pk_courtstation" PRIMARY KEY
);

CREATE TABLE "crime" (
  "id" SERIAL CONSTRAINT "pk_crime" PRIMARY KEY,
  "law" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "ref" TEXT NOT NULL
);

CREATE TABLE "csi_equipment" (
  "id" SERIAL CONSTRAINT "pk_csi_equipment" PRIMARY KEY
);

CREATE TABLE "documenttype" (
  "id" SERIAL CONSTRAINT "pk_documenttype" PRIMARY KEY
);

CREATE TABLE "economicclass" (
  "id" SERIAL CONSTRAINT "pk_economicclass" PRIMARY KEY
);

CREATE TABLE "expert" (
  "id" SERIAL CONSTRAINT "pk_expert" PRIMARY KEY,
  "institution" TEXT NOT NULL,
  "jobtitle" TEXT NOT NULL,
  "credentials" TEXT NOT NULL
);

CREATE TABLE "experttype" (
  "id" SERIAL CONSTRAINT "pk_experttype" PRIMARY KEY
);

CREATE TABLE "expert_expert_types" (
  "expert" INTEGER NOT NULL,
  "experttype" INTEGER NOT NULL,
  CONSTRAINT "pk_expert_expert_types" PRIMARY KEY ("expert", "experttype")
);

CREATE INDEX "idx_expert_expert_types" ON "expert_expert_types" ("experttype");

ALTER TABLE "expert_expert_types" ADD CONSTRAINT "fk_expert_expert_types__expert" FOREIGN KEY ("expert") REFERENCES "expert" ("id");

ALTER TABLE "expert_expert_types" ADD CONSTRAINT "fk_expert_expert_types__experttype" FOREIGN KEY ("experttype") REFERENCES "experttype" ("id");

CREATE TABLE "feetype" (
  "id" SERIAL CONSTRAINT "pk_feetype" PRIMARY KEY,
  "fee_type" INTEGER
);

CREATE INDEX "idx_feetype__fee_type" ON "feetype" ("fee_type");

ALTER TABLE "feetype" ADD CONSTRAINT "fk_feetype__fee_type" FOREIGN KEY ("fee_type") REFERENCES "feetype" ("id");

CREATE TABLE "fee" (
  "id" SERIAL CONSTRAINT "pk_fee" PRIMARY KEY,
  "filing_fee_type" INTEGER NOT NULL,
  "amount" DECIMAL(12, 2),
  "unit" TEXT NOT NULL,
  "min_fee" DECIMAL(12, 2),
  "max_fee" DECIMAL(12, 2),
  "description" TEXT NOT NULL,
  "guide_sec" TEXT NOT NULL,
  "guide_clause" TEXT NOT NULL
);

CREATE INDEX "idx_fee__filing_fee_type" ON "fee" ("filing_fee_type");

ALTER TABLE "fee" ADD CONSTRAINT "fk_fee__filing_fee_type" FOREIGN KEY ("filing_fee_type") REFERENCES "feetype" ("id");

CREATE TABLE "healtheventtype" (
  "id" SERIAL CONSTRAINT "pk_healtheventtype" PRIMARY KEY
);

CREATE TABLE "hearingtype" (
  "id" SERIAL CONSTRAINT "pk_hearingtype" PRIMARY KEY
);

CREATE TABLE "judicialrank" (
  "id" SERIAL CONSTRAINT "pk_judicialrank" PRIMARY KEY
);

CREATE TABLE "judicialrole" (
  "id" SERIAL CONSTRAINT "pk_judicialrole" PRIMARY KEY
);

CREATE TABLE "judicialofficer" (
  "id" SERIAL CONSTRAINT "pk_judicialofficer" PRIMARY KEY,
  "rank" INTEGER NOT NULL,
  "judicial_role" INTEGER NOT NULL,
  "court_station" INTEGER NOT NULL
);

CREATE INDEX "idx_judicialofficer__court_station" ON "judicialofficer" ("court_station");

CREATE INDEX "idx_judicialofficer__judicial_role" ON "judicialofficer" ("judicial_role");

CREATE INDEX "idx_judicialofficer__rank" ON "judicialofficer" ("rank");

ALTER TABLE "judicialofficer" ADD CONSTRAINT "fk_judicialofficer__court_station" FOREIGN KEY ("court_station") REFERENCES "courtstation" ("id");

ALTER TABLE "judicialofficer" ADD CONSTRAINT "fk_judicialofficer__judicial_role" FOREIGN KEY ("judicial_role") REFERENCES "judicialrole" ("id");

ALTER TABLE "judicialofficer" ADD CONSTRAINT "fk_judicialofficer__rank" FOREIGN KEY ("rank") REFERENCES "judicialrank" ("id");

CREATE TABLE "lawfirm" (
  "id" SERIAL CONSTRAINT "pk_lawfirm" PRIMARY KEY
);

CREATE TABLE "lawyer" (
  "id" SERIAL CONSTRAINT "pk_lawyer" PRIMARY KEY,
  "law_firm" INTEGER,
  "bar_no" TEXT NOT NULL,
  "bar_date" DATE
);

CREATE INDEX "idx_lawyer__law_firm" ON "lawyer" ("law_firm");

ALTER TABLE "lawyer" ADD CONSTRAINT "fk_lawyer__law_firm" FOREIGN KEY ("law_firm") REFERENCES "lawfirm" ("id");

CREATE TABLE "legalreference" (
  "id" SERIAL CONSTRAINT "pk_legalreference" PRIMARY KEY,
  "ref" TEXT NOT NULL,
  "verbatim" TEXT NOT NULL,
  "public" BOOLEAN,
  "commentary" TEXT NOT NULL,
  "validated" BOOLEAN
);

CREATE TABLE "partytype" (
  "id" SERIAL CONSTRAINT "pk_partytype" PRIMARY KEY
);

CREATE TABLE "personaleffectscategory" (
  "id" SERIAL CONSTRAINT "pk_personaleffectscategory" PRIMARY KEY
);

CREATE TABLE "policeofficerrank" (
  "id" SERIAL CONSTRAINT "pk_policeofficerrank" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "sequence" INTEGER
);

CREATE TABLE "policeofficer" (
  "id" SERIAL CONSTRAINT "pk_policeofficer" PRIMARY KEY,
  "police_rank" INTEGER NOT NULL,
  "servicenumber" VARCHAR(100) UNIQUE NOT NULL
);

CREATE INDEX "idx_policeofficer__police_rank" ON "policeofficer" ("police_rank");

ALTER TABLE "policeofficer" ADD CONSTRAINT "fk_policeofficer__police_rank" FOREIGN KEY ("police_rank") REFERENCES "policeofficerrank" ("id");

CREATE TABLE "investigating_officer" (
  "police_officers" INTEGER CONSTRAINT "pk_investigating_officer" PRIMARY KEY,
  "date_assigned" TIMESTAMP,
  "lead_investigator" INTEGER
);

ALTER TABLE "investigating_officer" ADD CONSTRAINT "fk_investigating_officer__police_officers" FOREIGN KEY ("police_officers") REFERENCES "policeofficer" ("id");

CREATE TABLE "policestationrank" (
  "id" SERIAL CONSTRAINT "pk_policestationrank" PRIMARY KEY
);

CREATE TABLE "prisonofficerrank" (
  "id" SERIAL CONSTRAINT "pk_prisonofficerrank" PRIMARY KEY
);

CREATE TABLE "prosecutorteam" (
  "id" SERIAL CONSTRAINT "pk_prosecutorteam" PRIMARY KEY
);

CREATE TABLE "prosecutor" (
  "id" SERIAL CONSTRAINT "pk_prosecutor" PRIMARY KEY,
  "prosecutor_team" INTEGER,
  "lawyer" INTEGER NOT NULL
);

CREATE INDEX "idx_prosecutor__lawyer" ON "prosecutor" ("lawyer");

CREATE INDEX "idx_prosecutor__prosecutor_team" ON "prosecutor" ("prosecutor_team");

ALTER TABLE "prosecutor" ADD CONSTRAINT "fk_prosecutor__lawyer" FOREIGN KEY ("lawyer") REFERENCES "lawyer" ("id");

ALTER TABLE "prosecutor" ADD CONSTRAINT "fk_prosecutor__prosecutor_team" FOREIGN KEY ("prosecutor_team") REFERENCES "prosecutorteam" ("id");

CREATE TABLE "courtcase" (
  "id" SERIAL CONSTRAINT "pk_courtcase" PRIMARY KEY,
  "docket_number" TEXT NOT NULL,
  "adr" BOOLEAN,
  "mediation_proposal" TEXT NOT NULL,
  "case_received_date" DATE,
  "case_filed_date" DATE,
  "case_summary" TEXT NOT NULL,
  "filing_prosecutor" INTEGER,
  "fast_track" BOOLEAN,
  "priority" INTEGER,
  "object_of_litigation" TEXT NOT NULL,
  "grounds" TEXT NOT NULL,
  "prosecution_prayer" TEXT NOT NULL,
  "pretrial_date" DATE,
  "pretrial_notes" TEXT NOT NULL,
  "pretrial_registrar" INTEGER,
  "case_admissible" BOOLEAN,
  "indictment_date" TEXT NOT NULL,
  "judgement" TEXT NOT NULL,
  "judgement_docx" TEXT NOT NULL,
  "case_link_type" INTEGER,
  "linked_cases" INTEGER,
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
  "govt_liability" TEXT NOT NULL
);

CREATE INDEX "idx_courtcase__case_link_type" ON "courtcase" ("case_link_type");

CREATE INDEX "idx_courtcase__filing_prosecutor" ON "courtcase" ("filing_prosecutor");

CREATE INDEX "idx_courtcase__linked_cases" ON "courtcase" ("linked_cases");

CREATE INDEX "idx_courtcase__pretrial_registrar" ON "courtcase" ("pretrial_registrar");

ALTER TABLE "courtcase" ADD CONSTRAINT "fk_courtcase__case_link_type" FOREIGN KEY ("case_link_type") REFERENCES "caselinktype" ("id");

ALTER TABLE "courtcase" ADD CONSTRAINT "fk_courtcase__filing_prosecutor" FOREIGN KEY ("filing_prosecutor") REFERENCES "prosecutor" ("id");

ALTER TABLE "courtcase" ADD CONSTRAINT "fk_courtcase__linked_cases" FOREIGN KEY ("linked_cases") REFERENCES "courtcase" ("id");

ALTER TABLE "courtcase" ADD CONSTRAINT "fk_courtcase__pretrial_registrar" FOREIGN KEY ("pretrial_registrar") REFERENCES "judicialofficer" ("id");

CREATE TABLE "casecategory_court_cases" (
  "courtcase" INTEGER NOT NULL,
  "casecategory" INTEGER NOT NULL,
  CONSTRAINT "pk_casecategory_court_cases" PRIMARY KEY ("courtcase", "casecategory")
);

CREATE INDEX "idx_casecategory_court_cases" ON "casecategory_court_cases" ("casecategory");

ALTER TABLE "casecategory_court_cases" ADD CONSTRAINT "fk_casecategory_court_cases__casecategory" FOREIGN KEY ("casecategory") REFERENCES "casecategory" ("id");

ALTER TABLE "casecategory_court_cases" ADD CONSTRAINT "fk_casecategory_court_cases__courtcase" FOREIGN KEY ("courtcase") REFERENCES "courtcase" ("id");

CREATE TABLE "courtcase_bench" (
  "judicialofficer" INTEGER NOT NULL,
  "courtcase" INTEGER NOT NULL,
  CONSTRAINT "pk_courtcase_bench" PRIMARY KEY ("judicialofficer", "courtcase")
);

CREATE INDEX "idx_courtcase_bench" ON "courtcase_bench" ("courtcase");

ALTER TABLE "courtcase_bench" ADD CONSTRAINT "fk_courtcase_bench__courtcase" FOREIGN KEY ("courtcase") REFERENCES "courtcase" ("id");

ALTER TABLE "courtcase_bench" ADD CONSTRAINT "fk_courtcase_bench__judicialofficer" FOREIGN KEY ("judicialofficer") REFERENCES "judicialofficer" ("id");

CREATE TABLE "courtcase_law_firm" (
  "lawfirm" INTEGER NOT NULL,
  "courtcase" INTEGER NOT NULL,
  CONSTRAINT "pk_courtcase_law_firm" PRIMARY KEY ("lawfirm", "courtcase")
);

CREATE INDEX "idx_courtcase_law_firm" ON "courtcase_law_firm" ("courtcase");

ALTER TABLE "courtcase_law_firm" ADD CONSTRAINT "fk_courtcase_law_firm__courtcase" FOREIGN KEY ("courtcase") REFERENCES "courtcase" ("id");

ALTER TABLE "courtcase_law_firm" ADD CONSTRAINT "fk_courtcase_law_firm__lawfirm" FOREIGN KEY ("lawfirm") REFERENCES "lawfirm" ("id");

CREATE TABLE "issue" (
  "id" SERIAL CONSTRAINT "pk_issue" PRIMARY KEY,
  "issue" TEXT NOT NULL,
  "facts" TEXT NOT NULL,
  "counter_claim" BOOLEAN,
  "argument" TEXT NOT NULL,
  "argument_date" DATE,
  "argument_docx" TEXT NOT NULL,
  "rebuttal" TEXT NOT NULL,
  "rebuttal_date" DATE,
  "rebuttal_docx" TEXT NOT NULL,
  "hearing_date" DATE,
  "determination" TEXT NOT NULL,
  "dtermination_date" DATE,
  "determination_docx" TEXT NOT NULL,
  "resolved" BOOLEAN,
  "defense_lawyer" INTEGER NOT NULL,
  "prosecutor" INTEGER,
  "judicial_officer" INTEGER NOT NULL,
  "court_case" INTEGER NOT NULL,
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

ALTER TABLE "issue" ADD CONSTRAINT "fk_issue__court_case" FOREIGN KEY ("court_case") REFERENCES "courtcase" ("id");

ALTER TABLE "issue" ADD CONSTRAINT "fk_issue__defense_lawyer" FOREIGN KEY ("defense_lawyer") REFERENCES "lawyer" ("id");

ALTER TABLE "issue" ADD CONSTRAINT "fk_issue__judicial_officer" FOREIGN KEY ("judicial_officer") REFERENCES "judicialofficer" ("id");

ALTER TABLE "issue" ADD CONSTRAINT "fk_issue__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "document" (
  "id" SERIAL CONSTRAINT "pk_document" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "court_case" INTEGER,
  "issue" INTEGER,
  "document_admissibility" TEXT NOT NULL,
  "admitted" BOOLEAN,
  "judicial_officer" INTEGER,
  "filing_date" TIMESTAMP,
  "admisibility_notes" TEXT NOT NULL,
  "is_judgement" BOOLEAN,
  "is_court_order" BOOLEAN,
  "document" TEXT NOT NULL,
  "published" BOOLEAN,
  "publish_newspaper" TEXT NOT NULL,
  "publish_date" DATE,
  "validated" BOOLEAN,
  "filesize" DECIMAL(12, 2),
  "page_count" INTEGER,
  "paid" BOOLEAN
);

CREATE INDEX "idx_document__court_case" ON "document" ("court_case");

CREATE INDEX "idx_document__issue" ON "document" ("issue");

CREATE INDEX "idx_document__judicial_officer" ON "document" ("judicial_officer");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__court_case" FOREIGN KEY ("court_case") REFERENCES "courtcase" ("id");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__judicial_officer" FOREIGN KEY ("judicial_officer") REFERENCES "judicialofficer" ("id");

CREATE TABLE "document_document_types" (
  "document" INTEGER NOT NULL,
  "documenttype" INTEGER NOT NULL,
  CONSTRAINT "pk_document_document_types" PRIMARY KEY ("document", "documenttype")
);

CREATE INDEX "idx_document_document_types" ON "document_document_types" ("documenttype");

ALTER TABLE "document_document_types" ADD CONSTRAINT "fk_document_document_types__document" FOREIGN KEY ("document") REFERENCES "document" ("id");

ALTER TABLE "document_document_types" ADD CONSTRAINT "fk_document_document_types__documenttype" FOREIGN KEY ("documenttype") REFERENCES "documenttype" ("id");

CREATE TABLE "issue_argument_legal_references" (
  "issue" INTEGER NOT NULL,
  "legalreference" INTEGER NOT NULL,
  CONSTRAINT "pk_issue_argument_legal_references" PRIMARY KEY ("issue", "legalreference")
);

CREATE INDEX "idx_issue_argument_legal_references" ON "issue_argument_legal_references" ("legalreference");

ALTER TABLE "issue_argument_legal_references" ADD CONSTRAINT "fk_issue_argument_legal_references__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

ALTER TABLE "issue_argument_legal_references" ADD CONSTRAINT "fk_issue_argument_legal_references__legalreference" FOREIGN KEY ("legalreference") REFERENCES "legalreference" ("id");

CREATE TABLE "issue_plaintiff_lawyers" (
  "lawyer" INTEGER NOT NULL,
  "issue" INTEGER NOT NULL,
  CONSTRAINT "pk_issue_plaintiff_lawyers" PRIMARY KEY ("lawyer", "issue")
);

CREATE INDEX "idx_issue_plaintiff_lawyers" ON "issue_plaintiff_lawyers" ("issue");

ALTER TABLE "issue_plaintiff_lawyers" ADD CONSTRAINT "fk_issue_plaintiff_lawyers__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

ALTER TABLE "issue_plaintiff_lawyers" ADD CONSTRAINT "fk_issue_plaintiff_lawyers__lawyer" FOREIGN KEY ("lawyer") REFERENCES "lawyer" ("id");

CREATE TABLE "issue_rebuttal_legal_references" (
  "issue" INTEGER NOT NULL,
  "legalreference" INTEGER NOT NULL,
  CONSTRAINT "pk_issue_rebuttal_legal_references" PRIMARY KEY ("issue", "legalreference")
);

CREATE INDEX "idx_issue_rebuttal_legal_references" ON "issue_rebuttal_legal_references" ("legalreference");

ALTER TABLE "issue_rebuttal_legal_references" ADD CONSTRAINT "fk_issue_rebuttal_legal_references__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

ALTER TABLE "issue_rebuttal_legal_references" ADD CONSTRAINT "fk_issue_rebuttal_legal_references__legalreference" FOREIGN KEY ("legalreference") REFERENCES "legalreference" ("id");

CREATE TABLE "releasetype" (
  "id" SERIAL CONSTRAINT "pk_releasetype" PRIMARY KEY
);

CREATE TABLE "religion" (
  "id" SERIAL CONSTRAINT "pk_religion" PRIMARY KEY
);

CREATE TABLE "biodata" (
  "id" SERIAL CONSTRAINT "pk_biodata" PRIMARY KEY,
  "economic_class" INTEGER,
  "religion" INTEGER,
  "photo" BYTEA
);

CREATE INDEX "idx_biodata__economic_class" ON "biodata" ("economic_class");

CREATE INDEX "idx_biodata__religion" ON "biodata" ("religion");

ALTER TABLE "biodata" ADD CONSTRAINT "fk_biodata__economic_class" FOREIGN KEY ("economic_class") REFERENCES "economicclass" ("id");

ALTER TABLE "biodata" ADD CONSTRAINT "fk_biodata__religion" FOREIGN KEY ("religion") REFERENCES "religion" ("id");

CREATE TABLE "nextofkin" (
  "id" SERIAL CONSTRAINT "pk_nextofkin" PRIMARY KEY,
  "biodata" INTEGER NOT NULL,
  "childunder4" BOOLEAN
);

CREATE INDEX "idx_nextofkin__biodata" ON "nextofkin" ("biodata");

ALTER TABLE "nextofkin" ADD CONSTRAINT "fk_nextofkin__biodata" FOREIGN KEY ("biodata") REFERENCES "biodata" ("id");

CREATE TABLE "schedulestatustype" (
  "id" SERIAL CONSTRAINT "pk_schedulestatustype" PRIMARY KEY
);

CREATE TABLE "hearing" (
  "id" SERIAL CONSTRAINT "pk_hearing" PRIMARY KEY,
  "court_cases" INTEGER,
  "hearing_type" INTEGER NOT NULL,
  "schedule_status" INTEGER NOT NULL,
  "hearing_date" DATE,
  "reason" TEXT NOT NULL,
  "sequence" BIGINT,
  "yearday" BIGINT,
  "starttime" TIME,
  "endtime" TIME,
  "notes" TEXT NOT NULL,
  "completed" BOOLEAN,
  "adjourned_to" DATE,
  "transcript" TEXT NOT NULL,
  "atendance" TEXT NOT NULL,
  "next_hearing_date" DATE,
  "postponement_reason" TEXT NOT NULL
);

CREATE INDEX "idx_hearing__court_cases" ON "hearing" ("court_cases");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

CREATE INDEX "idx_hearing__schedule_status" ON "hearing" ("schedule_status");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__court_cases" FOREIGN KEY ("court_cases") REFERENCES "courtcase" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__hearing_type" FOREIGN KEY ("hearing_type") REFERENCES "hearingtype" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__schedule_status" FOREIGN KEY ("schedule_status") REFERENCES "schedulestatustype" ("id");

CREATE TABLE "hearing_adjudicating_officer" (
  "judicialofficer" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_adjudicating_officer" PRIMARY KEY ("judicialofficer", "hearing")
);

CREATE INDEX "idx_hearing_adjudicating_officer" ON "hearing_adjudicating_officer" ("hearing");

ALTER TABLE "hearing_adjudicating_officer" ADD CONSTRAINT "fk_hearing_adjudicating_officer__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_adjudicating_officer" ADD CONSTRAINT "fk_hearing_adjudicating_officer__judicialofficer" FOREIGN KEY ("judicialofficer") REFERENCES "judicialofficer" ("id");

CREATE TABLE "hearing_issues" (
  "issue" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_issues" PRIMARY KEY ("issue", "hearing")
);

CREATE INDEX "idx_hearing_issues" ON "hearing_issues" ("hearing");

ALTER TABLE "hearing_issues" ADD CONSTRAINT "fk_hearing_issues__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_issues" ADD CONSTRAINT "fk_hearing_issues__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

CREATE TABLE "hearing_lawyer_plaintiff" (
  "lawfirm" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_lawyer_plaintiff" PRIMARY KEY ("lawfirm", "hearing")
);

CREATE INDEX "idx_hearing_lawyer_plaintiff" ON "hearing_lawyer_plaintiff" ("hearing");

ALTER TABLE "hearing_lawyer_plaintiff" ADD CONSTRAINT "fk_hearing_lawyer_plaintiff__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_lawyer_plaintiff" ADD CONSTRAINT "fk_hearing_lawyer_plaintiff__lawfirm" FOREIGN KEY ("lawfirm") REFERENCES "lawfirm" ("id");

CREATE TABLE "hearing_lawyers_defense" (
  "lawfirm" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_lawyers_defense" PRIMARY KEY ("lawfirm", "hearing")
);

CREATE INDEX "idx_hearing_lawyers_defense" ON "hearing_lawyers_defense" ("hearing");

ALTER TABLE "hearing_lawyers_defense" ADD CONSTRAINT "fk_hearing_lawyers_defense__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_lawyers_defense" ADD CONSTRAINT "fk_hearing_lawyers_defense__lawfirm" FOREIGN KEY ("lawfirm") REFERENCES "lawfirm" ("id");

CREATE TABLE "subcounty" (
  "id" SERIAL CONSTRAINT "pk_subcounty" PRIMARY KEY,
  "county" INTEGER NOT NULL
);

CREATE INDEX "idx_subcounty__county" ON "subcounty" ("county");

ALTER TABLE "subcounty" ADD CONSTRAINT "fk_subcounty__county" FOREIGN KEY ("county") REFERENCES "county" ("id");

CREATE TABLE "town" (
  "id" SERIAL CONSTRAINT "pk_town" PRIMARY KEY
);

CREATE TABLE "court" (
  "id" SERIAL CONSTRAINT "pk_court" PRIMARY KEY,
  "court_station" INTEGER NOT NULL,
  "court_rank" INTEGER NOT NULL,
  "town" INTEGER NOT NULL
);

CREATE INDEX "idx_court__court_rank" ON "court" ("court_rank");

CREATE INDEX "idx_court__court_station" ON "court" ("court_station");

CREATE INDEX "idx_court__town" ON "court" ("town");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__court_rank" FOREIGN KEY ("court_rank") REFERENCES "courtrank" ("id");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__court_station" FOREIGN KEY ("court_station") REFERENCES "courtstation" ("id");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "court_judicial_officers" (
  "court" INTEGER NOT NULL,
  "judicialofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_court_judicial_officers" PRIMARY KEY ("court", "judicialofficer")
);

CREATE INDEX "idx_court_judicial_officers" ON "court_judicial_officers" ("judicialofficer");

ALTER TABLE "court_judicial_officers" ADD CONSTRAINT "fk_court_judicial_officers__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "court_judicial_officers" ADD CONSTRAINT "fk_court_judicial_officers__judicialofficer" FOREIGN KEY ("judicialofficer") REFERENCES "judicialofficer" ("id");

CREATE TABLE "policestation" (
  "id" SERIAL CONSTRAINT "pk_policestation" PRIMARY KEY,
  "town" INTEGER,
  "officer_commanding" INTEGER NOT NULL,
  "police_station_rank" INTEGER NOT NULL
);

CREATE INDEX "idx_policestation__officer_commanding" ON "policestation" ("officer_commanding");

CREATE INDEX "idx_policestation__police_station_rank" ON "policestation" ("police_station_rank");

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__officer_commanding" FOREIGN KEY ("officer_commanding") REFERENCES "policeofficer" ("id");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__police_station_rank" FOREIGN KEY ("police_station_rank") REFERENCES "policestationrank" ("id");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "complaint" (
  "id" SERIAL CONSTRAINT "pk_complaint" PRIMARY KEY,
  "active" TEXT NOT NULL,
  "ob_number" TEXT NOT NULL,
  "police_station" INTEGER NOT NULL,
  "daterecvd" TIMESTAMP NOT NULL,
  "datefiled" TIMESTAMP,
  "datecaseopened" TIMESTAMP,
  "casesummary" VARCHAR(2000) NOT NULL,
  "complaintstatement" TEXT NOT NULL,
  "circumstances" TEXT NOT NULL,
  "reportingofficer" INTEGER NOT NULL,
  "casefileinformation" TEXT NOT NULL,
  "p_request_help" BOOLEAN,
  "p_instruction" TEXT NOT NULL,
  "p_submitted" BOOLEAN,
  "p_submission_date" TIMESTAMP,
  "p_submission_notes" TEXT NOT NULL,
  "p_closed" TEXT NOT NULL,
  "closed" BOOLEAN,
  "p_evaluation" TEXT NOT NULL,
  "p_recommend_charge" BOOLEAN,
  "charge_sheet" TEXT NOT NULL,
  "charge_sheet_docx" TEXT NOT NULL,
  "evaluating_prosecutor_team" INTEGER
);

CREATE INDEX "idx_complaint__evaluating_prosecutor_team" ON "complaint" ("evaluating_prosecutor_team");

CREATE INDEX "idx_complaint__police_station" ON "complaint" ("police_station");

CREATE INDEX "idx_complaint__reportingofficer" ON "complaint" ("reportingofficer");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__evaluating_prosecutor_team" FOREIGN KEY ("evaluating_prosecutor_team") REFERENCES "prosecutorteam" ("id");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__police_station" FOREIGN KEY ("police_station") REFERENCES "policestation" ("id");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__reportingofficer" FOREIGN KEY ("reportingofficer") REFERENCES "policeofficer" ("id");

CREATE TABLE "complaint_complaint_categories" (
  "complaint" INTEGER NOT NULL,
  "complaintcategory" INTEGER NOT NULL,
  CONSTRAINT "pk_complaint_complaint_categories" PRIMARY KEY ("complaint", "complaintcategory")
);

CREATE INDEX "idx_complaint_complaint_categories" ON "complaint_complaint_categories" ("complaintcategory");

ALTER TABLE "complaint_complaint_categories" ADD CONSTRAINT "fk_complaint_complaint_categories__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_complaint_categories" ADD CONSTRAINT "fk_complaint_complaint_categories__complaintcategory" FOREIGN KEY ("complaintcategory") REFERENCES "complaintcategory" ("id");

CREATE TABLE "complaint_court_cases" (
  "complaint" INTEGER NOT NULL,
  "courtcase" INTEGER NOT NULL,
  CONSTRAINT "pk_complaint_court_cases" PRIMARY KEY ("complaint", "courtcase")
);

CREATE INDEX "idx_complaint_court_cases" ON "complaint_court_cases" ("courtcase");

ALTER TABLE "complaint_court_cases" ADD CONSTRAINT "fk_complaint_court_cases__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_court_cases" ADD CONSTRAINT "fk_complaint_court_cases__courtcase" FOREIGN KEY ("courtcase") REFERENCES "courtcase" ("id");

CREATE TABLE "party" (
  "complaints" INTEGER CONSTRAINT "pk_party" PRIMARY KEY,
  "statement" VARCHAR(1000) NOT NULL,
  "statementdate" TIMESTAMP,
  "complaint_role" INTEGER NOT NULL,
  "notes" TEXT NOT NULL,
  "dateofrepresentation" TIMESTAMP,
  "party_type" INTEGER NOT NULL,
  "relative" INTEGER NOT NULL,
  "relationship_type" TEXT NOT NULL,
  "biodata" INTEGER NOT NULL,
  "is_infant" BOOLEAN,
  "is_minor" BOOLEAN
);

CREATE INDEX "idx_party__biodata" ON "party" ("biodata");

CREATE INDEX "idx_party__complaint_role" ON "party" ("complaint_role");

CREATE INDEX "idx_party__party_type" ON "party" ("party_type");

CREATE INDEX "idx_party__relative" ON "party" ("relative");

ALTER TABLE "party" ADD CONSTRAINT "fk_party__biodata" FOREIGN KEY ("biodata") REFERENCES "biodata" ("id");

ALTER TABLE "party" ADD CONSTRAINT "fk_party__complaint_role" FOREIGN KEY ("complaint_role") REFERENCES "complaintrole" ("id");

ALTER TABLE "party" ADD CONSTRAINT "fk_party__complaints" FOREIGN KEY ("complaints") REFERENCES "complaint" ("id");

ALTER TABLE "party" ADD CONSTRAINT "fk_party__party_type" FOREIGN KEY ("party_type") REFERENCES "partytype" ("id");

ALTER TABLE "party" ADD CONSTRAINT "fk_party__relative" FOREIGN KEY ("relative") REFERENCES "party" ("complaints");

CREATE TABLE "instancecrime" (
  "parties" INTEGER NOT NULL,
  "crimes" INTEGER NOT NULL,
  "crime_detail" TEXT NOT NULL,
  "tffender_type" TEXT NOT NULL,
  "crime_date" TIMESTAMP,
  "date_note" TEXT NOT NULL,
  "place_of_crime" TEXT NOT NULL,
  "place_note" TEXT NOT NULL,
  CONSTRAINT "pk_instancecrime" PRIMARY KEY ("parties", "crimes")
);

CREATE INDEX "idx_instancecrime__crimes" ON "instancecrime" ("crimes");

ALTER TABLE "instancecrime" ADD CONSTRAINT "fk_instancecrime__crimes" FOREIGN KEY ("crimes") REFERENCES "crime" ("id");

ALTER TABLE "instancecrime" ADD CONSTRAINT "fk_instancecrime__parties" FOREIGN KEY ("parties") REFERENCES "party" ("complaints");

CREATE TABLE "instancecrime_issues" (
  "instancecrime_parties" INTEGER NOT NULL,
  "instancecrime_crimes" INTEGER NOT NULL,
  "issue" INTEGER NOT NULL,
  CONSTRAINT "pk_instancecrime_issues" PRIMARY KEY ("instancecrime_parties", "instancecrime_crimes", "issue")
);

CREATE INDEX "idx_instancecrime_issues" ON "instancecrime_issues" ("issue");

ALTER TABLE "instancecrime_issues" ADD CONSTRAINT "fk_instancecrime_issues__instancecrime_parties__instan_4f61111c" FOREIGN KEY ("instancecrime_parties", "instancecrime_crimes") REFERENCES "instancecrime" ("parties", "crimes");

ALTER TABLE "instancecrime_issues" ADD CONSTRAINT "fk_instancecrime_issues__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

CREATE TABLE "issue_defending_parties" (
  "party" INTEGER NOT NULL,
  "issue" INTEGER NOT NULL,
  CONSTRAINT "pk_issue_defending_parties" PRIMARY KEY ("party", "issue")
);

CREATE INDEX "idx_issue_defending_parties" ON "issue_defending_parties" ("issue");

ALTER TABLE "issue_defending_parties" ADD CONSTRAINT "fk_issue_defending_parties__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

ALTER TABLE "issue_defending_parties" ADD CONSTRAINT "fk_issue_defending_parties__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

CREATE TABLE "issue_injured_parties" (
  "party" INTEGER NOT NULL,
  "issue" INTEGER NOT NULL,
  CONSTRAINT "pk_issue_injured_parties" PRIMARY KEY ("party", "issue")
);

CREATE INDEX "idx_issue_injured_parties" ON "issue_injured_parties" ("issue");

ALTER TABLE "issue_injured_parties" ADD CONSTRAINT "fk_issue_injured_parties__issue" FOREIGN KEY ("issue") REFERENCES "issue" ("id");

ALTER TABLE "issue_injured_parties" ADD CONSTRAINT "fk_issue_injured_parties__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

CREATE TABLE "lawyer_representing" (
  "party" INTEGER NOT NULL,
  "lawyer" INTEGER NOT NULL,
  CONSTRAINT "pk_lawyer_representing" PRIMARY KEY ("party", "lawyer")
);

CREATE INDEX "idx_lawyer_representing" ON "lawyer_representing" ("lawyer");

ALTER TABLE "lawyer_representing" ADD CONSTRAINT "fk_lawyer_representing__lawyer" FOREIGN KEY ("lawyer") REFERENCES "lawyer" ("id");

ALTER TABLE "lawyer_representing" ADD CONSTRAINT "fk_lawyer_representing__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

CREATE TABLE "payment" (
  "id" SERIAL CONSTRAINT "pk_payment" PRIMARY KEY,
  "receiving_registrar" INTEGER NOT NULL,
  "lawyer_paying" INTEGER,
  "party_paying" INTEGER,
  "documents" INTEGER,
  "date_of_payment" TEXT NOT NULL,
  "paid" BOOLEAN,
  "payment_ref" TEXT NOT NULL,
  "phone_number" TEXT NOT NULL
);

CREATE INDEX "idx_payment__documents" ON "payment" ("documents");

CREATE INDEX "idx_payment__lawyer_paying" ON "payment" ("lawyer_paying");

CREATE INDEX "idx_payment__party_paying" ON "payment" ("party_paying");

CREATE INDEX "idx_payment__receiving_registrar" ON "payment" ("receiving_registrar");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__documents" FOREIGN KEY ("documents") REFERENCES "document" ("id");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__lawyer_paying" FOREIGN KEY ("lawyer_paying") REFERENCES "lawyer" ("id");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__party_paying" FOREIGN KEY ("party_paying") REFERENCES "party" ("complaints");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__receiving_registrar" FOREIGN KEY ("receiving_registrar") REFERENCES "judicialofficer" ("id");

CREATE TABLE "payment_detail" (
  "id" SERIAL CONSTRAINT "pk_payment_detail" PRIMARY KEY,
  "receipt_id" INTEGER NOT NULL,
  "fee" INTEGER NOT NULL,
  "purpose" TEXT NOT NULL,
  "unit" TEXT NOT NULL,
  "qty" TEXT NOT NULL,
  "unit_cost" TEXT NOT NULL,
  "amount" TEXT NOT NULL
);

CREATE INDEX "idx_payment_detail__fee" ON "payment_detail" ("fee");

CREATE INDEX "idx_payment_detail__receipt_id" ON "payment_detail" ("receipt_id");

ALTER TABLE "payment_detail" ADD CONSTRAINT "fk_payment_detail__fee" FOREIGN KEY ("fee") REFERENCES "fee" ("id");

ALTER TABLE "payment_detail" ADD CONSTRAINT "fk_payment_detail__receipt_id" FOREIGN KEY ("receipt_id") REFERENCES "payment" ("id");

CREATE TABLE "personaleffect" (
  "id" SERIAL CONSTRAINT "pk_personaleffect" PRIMARY KEY,
  "party" INTEGER NOT NULL,
  "personal_effects_category" INTEGER NOT NULL
);

CREATE INDEX "idx_personaleffect__party" ON "personaleffect" ("party");

CREATE INDEX "idx_personaleffect__personal_effects_category" ON "personaleffect" ("personal_effects_category");

ALTER TABLE "personaleffect" ADD CONSTRAINT "fk_personaleffect__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

ALTER TABLE "personaleffect" ADD CONSTRAINT "fk_personaleffect__personal_effects_category" FOREIGN KEY ("personal_effects_category") REFERENCES "personaleffectscategory" ("id");

CREATE TABLE "policeofficer_assigned_station" (
  "policestation" INTEGER NOT NULL,
  "policeofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_policeofficer_assigned_station" PRIMARY KEY ("policestation", "policeofficer")
);

CREATE INDEX "idx_policeofficer_assigned_station" ON "policeofficer_assigned_station" ("policeofficer");

ALTER TABLE "policeofficer_assigned_station" ADD CONSTRAINT "fk_policeofficer_assigned_station__policeofficer" FOREIGN KEY ("policeofficer") REFERENCES "policeofficer" ("id");

ALTER TABLE "policeofficer_assigned_station" ADD CONSTRAINT "fk_policeofficer_assigned_station__policestation" FOREIGN KEY ("policestation") REFERENCES "policestation" ("id");

CREATE TABLE "prison" (
  "id" SERIAL CONSTRAINT "pk_prison" PRIMARY KEY,
  "town" INTEGER NOT NULL
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

ALTER TABLE "prison" ADD CONSTRAINT "fk_prison__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "prisonofficer" (
  "id" SERIAL CONSTRAINT "pk_prisonofficer" PRIMARY KEY,
  "prison" INTEGER NOT NULL,
  "prison_officer_rank" INTEGER NOT NULL
);

CREATE INDEX "idx_prisonofficer__prison" ON "prisonofficer" ("prison");

CREATE INDEX "idx_prisonofficer__prison_officer_rank" ON "prisonofficer" ("prison_officer_rank");

ALTER TABLE "prisonofficer" ADD CONSTRAINT "fk_prisonofficer__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

ALTER TABLE "prisonofficer" ADD CONSTRAINT "fk_prisonofficer__prison_officer_rank" FOREIGN KEY ("prison_officer_rank") REFERENCES "prisonofficerrank" ("id");

CREATE TABLE "discipline" (
  "id" SERIAL CONSTRAINT "pk_discipline" PRIMARY KEY,
  "party" INTEGER NOT NULL,
  "prison_officer" INTEGER NOT NULL
);

CREATE INDEX "idx_discipline__party" ON "discipline" ("party");

CREATE INDEX "idx_discipline__prison_officer" ON "discipline" ("prison_officer");

ALTER TABLE "discipline" ADD CONSTRAINT "fk_discipline__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

ALTER TABLE "discipline" ADD CONSTRAINT "fk_discipline__prison_officer" FOREIGN KEY ("prison_officer") REFERENCES "prisonofficer" ("id");

CREATE TABLE "healthevent" (
  "id" SERIAL CONSTRAINT "pk_healthevent" PRIMARY KEY,
  "party" INTEGER NOT NULL,
  "reporting_prison_officer" INTEGER,
  "health_event_type" INTEGER NOT NULL,
  "startdate" TIMESTAMP,
  "enddate" TIMESTAMP,
  "notes" TEXT NOT NULL
);

CREATE INDEX "idx_healthevent__health_event_type" ON "healthevent" ("health_event_type");

CREATE INDEX "idx_healthevent__party" ON "healthevent" ("party");

CREATE INDEX "idx_healthevent__reporting_prison_officer" ON "healthevent" ("reporting_prison_officer");

ALTER TABLE "healthevent" ADD CONSTRAINT "fk_healthevent__health_event_type" FOREIGN KEY ("health_event_type") REFERENCES "healtheventtype" ("id");

ALTER TABLE "healthevent" ADD CONSTRAINT "fk_healthevent__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

ALTER TABLE "healthevent" ADD CONSTRAINT "fk_healthevent__reporting_prison_officer" FOREIGN KEY ("reporting_prison_officer") REFERENCES "prisonofficer" ("id");

CREATE TABLE "settlement" (
  "id" SERIAL CONSTRAINT "pk_settlement" PRIMARY KEY,
  "complaint" INTEGER NOT NULL,
  "terms" TEXT NOT NULL,
  "amount" DECIMAL(12, 2),
  "paid" BOOLEAN,
  "docx" TEXT NOT NULL,
  "settlor" INTEGER NOT NULL
);

CREATE INDEX "idx_settlement__complaint" ON "settlement" ("complaint");

CREATE INDEX "idx_settlement__settlor" ON "settlement" ("settlor");

ALTER TABLE "settlement" ADD CONSTRAINT "fk_settlement__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "settlement" ADD CONSTRAINT "fk_settlement__settlor" FOREIGN KEY ("settlor") REFERENCES "party" ("complaints");

CREATE TABLE "party_settlees" (
  "party" INTEGER NOT NULL,
  "settlement" INTEGER NOT NULL,
  CONSTRAINT "pk_party_settlees" PRIMARY KEY ("party", "settlement")
);

CREATE INDEX "idx_party_settlees" ON "party_settlees" ("settlement");

ALTER TABLE "party_settlees" ADD CONSTRAINT "fk_party_settlees__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

ALTER TABLE "party_settlees" ADD CONSTRAINT "fk_party_settlees__settlement" FOREIGN KEY ("settlement") REFERENCES "settlement" ("id");

CREATE TABLE "transcript" (
  "id" SERIAL CONSTRAINT "pk_transcript" PRIMARY KEY,
  "video" TEXT NOT NULL,
  "audio" TEXT NOT NULL,
  "add_date" TIMESTAMP,
  "asr_transcript" TEXT NOT NULL,
  "asr_date" TIMESTAMP,
  "edited_transcript" TEXT NOT NULL,
  "edit_date" TIMESTAMP,
  "certified_transcript" TEXT NOT NULL,
  "certfiy_date" TIMESTAMP,
  "locked" BOOLEAN,
  "hearing" INTEGER NOT NULL
);

CREATE INDEX "idx_transcript__hearing" ON "transcript" ("hearing");

ALTER TABLE "transcript" ADD CONSTRAINT "fk_transcript__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "vehicle" (
  "id" SERIAL CONSTRAINT "pk_vehicle" PRIMARY KEY,
  "police_station" INTEGER NOT NULL,
  "make" TEXT NOT NULL,
  "model" TEXT NOT NULL,
  "regno" TEXT NOT NULL
);

CREATE INDEX "idx_vehicle__police_station" ON "vehicle" ("police_station");

ALTER TABLE "vehicle" ADD CONSTRAINT "fk_vehicle__police_station" FOREIGN KEY ("police_station") REFERENCES "policestation" ("id");

CREATE TABLE "ward" (
  "id" SERIAL CONSTRAINT "pk_ward" PRIMARY KEY,
  "subcounty" INTEGER NOT NULL
);

CREATE INDEX "idx_ward__subcounty" ON "ward" ("subcounty");

ALTER TABLE "ward" ADD CONSTRAINT "fk_ward__subcounty" FOREIGN KEY ("subcounty") REFERENCES "subcounty" ("id");

CREATE TABLE "town_wards" (
  "ward" INTEGER NOT NULL,
  "town" INTEGER NOT NULL,
  CONSTRAINT "pk_town_wards" PRIMARY KEY ("ward", "town")
);

CREATE INDEX "idx_town_wards" ON "town_wards" ("town");

ALTER TABLE "town_wards" ADD CONSTRAINT "fk_town_wards__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

ALTER TABLE "town_wards" ADD CONSTRAINT "fk_town_wards__ward" FOREIGN KEY ("ward") REFERENCES "ward" ("id");

CREATE TABLE "warranttype" (
  "id" SERIAL CONSTRAINT "pk_warranttype" PRIMARY KEY
);

CREATE TABLE "commital" (
  "id" SERIAL CONSTRAINT "pk_commital" PRIMARY KEY,
  "prisons" INTEGER,
  "police_station" INTEGER,
  "parties" INTEGER NOT NULL,
  "casecomplete" BOOLEAN,
  "commit_date" DATE NOT NULL,
  "purpose" TEXT NOT NULL,
  "warrant_type" INTEGER NOT NULL,
  "warrant_docx" TEXT NOT NULL,
  "warrant_issue_date" DATE,
  "warrant_issued_by" TEXT NOT NULL,
  "warrant_date_attached" TIMESTAMP,
  "duration" INTERVAL DAY TO SECOND,
  "commital" INTEGER,
  "commital_type" INTEGER NOT NULL,
  "court_case" INTEGER,
  "concurrent" BOOLEAN,
  "life_imprisonment" BOOLEAN,
  "arrival_date" TIMESTAMP,
  "sentence_start_date" TIMESTAMP,
  "arrest_date" TIMESTAMP,
  "remaining_years" INTEGER,
  "remaining_months" INTEGER,
  "remaining_days" INTEGER,
  "cell_number" TEXT NOT NULL,
  "cell_type" INTEGER,
  "release_date" TIMESTAMP,
  "exit_date" TIMESTAMP,
  "reason_for_release" TEXT NOT NULL,
  "with_children" BOOLEAN,
  "release_type" INTEGER,
  "receiving_officer" INTEGER NOT NULL,
  "releasing_officer" INTEGER NOT NULL
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

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__cell_type" FOREIGN KEY ("cell_type") REFERENCES "celltype" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__commital" FOREIGN KEY ("commital") REFERENCES "commital" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__commital_type" FOREIGN KEY ("commital_type") REFERENCES "commitaltype" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__court_case" FOREIGN KEY ("court_case") REFERENCES "courtcase" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__parties" FOREIGN KEY ("parties") REFERENCES "party" ("complaints");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__police_station" FOREIGN KEY ("police_station") REFERENCES "policestation" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__prisons" FOREIGN KEY ("prisons") REFERENCES "prison" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__receiving_officer" FOREIGN KEY ("receiving_officer") REFERENCES "prisonofficer" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__release_type" FOREIGN KEY ("release_type") REFERENCES "releasetype" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__releasing_officer" FOREIGN KEY ("releasing_officer") REFERENCES "prisonofficer" ("id");

ALTER TABLE "commital" ADD CONSTRAINT "fk_commital__warrant_type" FOREIGN KEY ("warrant_type") REFERENCES "warranttype" ("id");

CREATE TABLE "investigationdiary" (
  "id" SERIAL CONSTRAINT "pk_investigationdiary" PRIMARY KEY,
  "complaint" INTEGER NOT NULL,
  "activity" TEXT NOT NULL,
  "location" TEXT NOT NULL,
  "outcome" TEXT NOT NULL,
  "equipmentresults" TEXT NOT NULL,
  "startdate" TIMESTAMP NOT NULL,
  "enddate" TIMESTAMP,
  "advocate_present" TEXT NOT NULL,
  "summons_statement" TEXT NOT NULL,
  "arrest_statement" TEXT NOT NULL,
  "arrest_warrant" TEXT NOT NULL,
  "search_seizure_statement" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "detained" TEXT NOT NULL,
  "detained_at" TEXT NOT NULL,
  "provisional_release_statement" TEXT NOT NULL,
  "warrant_type" INTEGER,
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

ALTER TABLE "investigationdiary" ADD CONSTRAINT "fk_investigationdiary__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "investigationdiary" ADD CONSTRAINT "fk_investigationdiary__warrant_type" FOREIGN KEY ("warrant_type") REFERENCES "warranttype" ("id");

CREATE TABLE "csi_equipment_investigation_entries" (
  "investigationdiary" INTEGER NOT NULL,
  "csi_equipment" INTEGER NOT NULL,
  CONSTRAINT "pk_csi_equipment_investigation_entries" PRIMARY KEY ("investigationdiary", "csi_equipment")
);

CREATE INDEX "idx_csi_equipment_investigation_entries" ON "csi_equipment_investigation_entries" ("csi_equipment");

ALTER TABLE "csi_equipment_investigation_entries" ADD CONSTRAINT "fk_csi_equipment_investigation_entries__csi_equipment" FOREIGN KEY ("csi_equipment") REFERENCES "csi_equipment" ("id");

ALTER TABLE "csi_equipment_investigation_entries" ADD CONSTRAINT "fk_csi_equipment_investigation_entries__investigationdiary" FOREIGN KEY ("investigationdiary") REFERENCES "investigationdiary" ("id");

CREATE TABLE "diagram" (
  "id" SERIAL CONSTRAINT "pk_diagram" PRIMARY KEY,
  "investigation_diary" INTEGER NOT NULL,
  "image" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "docx" TEXT NOT NULL
);

CREATE INDEX "idx_diagram__investigation_diary" ON "diagram" ("investigation_diary");

ALTER TABLE "diagram" ADD CONSTRAINT "fk_diagram__investigation_diary" FOREIGN KEY ("investigation_diary") REFERENCES "investigationdiary" ("id");

CREATE TABLE "experttestimony" (
  "requesting_officer" INTEGER NOT NULL,
  "investigation_entries" INTEGER NOT NULL,
  "experts" INTEGER NOT NULL,
  "task_given" TEXT NOT NULL,
  "summary_of_facts" TEXT NOT NULL,
  "statement" TEXT NOT NULL,
  "testimony_date" TIMESTAMP,
  "task_request_date" DATE,
  "docx" TEXT NOT NULL,
  "validated" BOOLEAN,
  CONSTRAINT "pk_experttestimony" PRIMARY KEY ("investigation_entries", "experts")
);

CREATE INDEX "idx_experttestimony__experts" ON "experttestimony" ("experts");

CREATE INDEX "idx_experttestimony__requesting_officer" ON "experttestimony" ("requesting_officer");

ALTER TABLE "experttestimony" ADD CONSTRAINT "fk_experttestimony__experts" FOREIGN KEY ("experts") REFERENCES "expert" ("id");

ALTER TABLE "experttestimony" ADD CONSTRAINT "fk_experttestimony__investigation_entries" FOREIGN KEY ("investigation_entries") REFERENCES "investigationdiary" ("id");

ALTER TABLE "experttestimony" ADD CONSTRAINT "fk_experttestimony__requesting_officer" FOREIGN KEY ("requesting_officer") REFERENCES "investigating_officer" ("police_officers");

CREATE TABLE "interview" (
  "id" SERIAL CONSTRAINT "pk_interview" PRIMARY KEY,
  "investigation_entry" INTEGER NOT NULL,
  "question" TEXT NOT NULL,
  "answer" TEXT NOT NULL,
  "validated" BOOLEAN,
  "language" TEXT NOT NULL
);

CREATE INDEX "idx_interview__investigation_entry" ON "interview" ("investigation_entry");

ALTER TABLE "interview" ADD CONSTRAINT "fk_interview__investigation_entry" FOREIGN KEY ("investigation_entry") REFERENCES "investigationdiary" ("id");

CREATE TABLE "investigating_officer_investigation_entries" (
  "investigating_officer" INTEGER NOT NULL,
  "investigationdiary" INTEGER NOT NULL,
  CONSTRAINT "pk_investigating_officer_investigation_entries" PRIMARY KEY ("investigating_officer", "investigationdiary")
);

CREATE INDEX "idx_investigating_officer_investigation_entries" ON "investigating_officer_investigation_entries" ("investigationdiary");

ALTER TABLE "investigating_officer_investigation_entries" ADD CONSTRAINT "fk_investigating_officer_investigation_entries__invest_37917e7f" FOREIGN KEY ("investigating_officer") REFERENCES "investigating_officer" ("police_officers");

ALTER TABLE "investigating_officer_investigation_entries" ADD CONSTRAINT "fk_investigating_officer_investigation_entries__invest_ffe7effd" FOREIGN KEY ("investigationdiary") REFERENCES "investigationdiary" ("id");

CREATE TABLE "investigationdiary_parties" (
  "party" INTEGER NOT NULL,
  "investigationdiary" INTEGER NOT NULL,
  CONSTRAINT "pk_investigationdiary_parties" PRIMARY KEY ("party", "investigationdiary")
);

CREATE INDEX "idx_investigationdiary_parties" ON "investigationdiary_parties" ("investigationdiary");

ALTER TABLE "investigationdiary_parties" ADD CONSTRAINT "fk_investigationdiary_parties__investigationdiary" FOREIGN KEY ("investigationdiary") REFERENCES "investigationdiary" ("id");

ALTER TABLE "investigationdiary_parties" ADD CONSTRAINT "fk_investigationdiary_parties__party" FOREIGN KEY ("party") REFERENCES "party" ("complaints");

CREATE TABLE "investigationdiary_vehicles" (
  "investigationdiary" INTEGER NOT NULL,
  "vehicle" INTEGER NOT NULL,
  CONSTRAINT "pk_investigationdiary_vehicles" PRIMARY KEY ("investigationdiary", "vehicle")
);

CREATE INDEX "idx_investigationdiary_vehicles" ON "investigationdiary_vehicles" ("vehicle");

ALTER TABLE "investigationdiary_vehicles" ADD CONSTRAINT "fk_investigationdiary_vehicles__investigationdiary" FOREIGN KEY ("investigationdiary") REFERENCES "investigationdiary" ("id");

ALTER TABLE "investigationdiary_vehicles" ADD CONSTRAINT "fk_investigationdiary_vehicles__vehicle" FOREIGN KEY ("vehicle") REFERENCES "vehicle" ("id");

CREATE TABLE "seizure" (
  "id" SERIAL CONSTRAINT "pk_seizure" PRIMARY KEY,
  "investigation_diary" INTEGER NOT NULL,
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
  "return_date" TIMESTAMP,
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
  "recovery_town" INTEGER,
  "destruction_pic" TEXT NOT NULL,
  "is_evidence" BOOLEAN,
  "immovable" BOOLEAN
);

CREATE INDEX "idx_seizure__investigation_diary" ON "seizure" ("investigation_diary");

CREATE INDEX "idx_seizure__recovery_town" ON "seizure" ("recovery_town");

ALTER TABLE "seizure" ADD CONSTRAINT "fk_seizure__investigation_diary" FOREIGN KEY ("investigation_diary") REFERENCES "investigationdiary" ("id");

ALTER TABLE "seizure" ADD CONSTRAINT "fk_seizure__recovery_town" FOREIGN KEY ("recovery_town") REFERENCES "town" ("id");

CREATE TABLE "exhibit" (
  "id" SERIAL CONSTRAINT "pk_exhibit" PRIMARY KEY,
  "investigation_entry" INTEGER NOT NULL,
  "photo" TEXT NOT NULL,
  "exhibit_no" TEXT NOT NULL,
  "docx" TEXT NOT NULL,
  "seizure" INTEGER NOT NULL
);

CREATE INDEX "idx_exhibit__investigation_entry" ON "exhibit" ("investigation_entry");

CREATE INDEX "idx_exhibit__seizure" ON "exhibit" ("seizure");

ALTER TABLE "exhibit" ADD CONSTRAINT "fk_exhibit__investigation_entry" FOREIGN KEY ("investigation_entry") REFERENCES "investigationdiary" ("id");

ALTER TABLE "exhibit" ADD CONSTRAINT "fk_exhibit__seizure" FOREIGN KEY ("seizure") REFERENCES "seizure" ("id")

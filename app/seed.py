"""RRU Initialization data.  (c) Nyimbi Odero, Oct 7th, 2016


What it does:
    This loads the Knec Database with data


How to Execute:
    python seed.py

    And watch the database load happen
    loads:
        subjects
        subjectPapers
        students
Todo:
    * Add Automatic reading of selected fields
    * Add an OCR module
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
 - Indent 2

"""

import csv, pickle
from knecdb import *

db = kDb()

# Load Subjects
with open('data/subjects.csv', 'rU') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        sb = Subject()
        sb.subj_code = row['Subject_code']
        sb.subj_name = row['Subject_names']
        sb.papers = row['PAPERS']
        sb.total_score = row['Total_score']
        db.s.add(sb)
        print row['Subject_code'], row['Subject_names'], row['Total_score'], row['PAPERS']
    db.s.commit()

# Load SubjectPapers
with open('data/subjectPaper.csv', 'rU') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        sbp = SubjectPaper()
        sbp.subject_code = row['Subject']
        sbp.paper_no = row['Paper']
        sbp.paper_code = row['Subject_code']
        sbp.total_score = row['Total_score']
        db.s.add(sbp)
        print row
    db.s.commit()


#Load Counties
with open('data/counties.csv', 'rU') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        cnt = County()
        cnt.county_num = row['county_code']
        cnt.name = row['county_name']
        # sbp.paper_code = row['Subject_code']
        # sbp.total_score = row['Total_score']
        db.s.add(cnt)
        print row
    db.s.commit()


# Load Subcounties
with open('data/subcounties.csv', 'rU') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        cnt = District()
        cnt.county_num = row['county_code']
        cnt.district_code = row['district_code']
        cnt.name = row['district_name']
        # sbp.paper_code = row['Subject_code']
        # sbp.total_score = row['Total_score']
        db.s.add(cnt)
        print row
        db.s.commit()

error_sc = []
with open('data/kcse_schools.csv', 'rU') as csvfile:
    # dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)  # , delimiter = ',')
    i, j, x = 0, 1, 10000
    for row in reader:
        try:
            sc = School()
            sc.school_code = row['School_code']
            sc.name = row['School_Name']
            sc.category = row['School_Category']
            sc.type = row['School_Type']
            sc.district_code = row['District_Code']
            t = row['District_Code']
            sc.county_num = t[:2]
            #sc.county_num = row['District_Code'][:2]
            db.s.add(sc)
            db.s.commit()
        except Exception as inst:
            print j, 'ERROR ROW'
            error_sc.append(row)
            print row
            print '--------------------------------------'
            # print sys.exc_info()[0]
            print inst
            print '--------'
        finally:
            if j > 1000: x = 2
            i += 1
            # We commit schools very 1k records
            if i > x:
                db.s.commit()
                print j
                i = 0

# Load Students
error_st =[]
with open('data/kst.csv', 'rU') as csvfile:
    # dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)  # , delimiter = ',')
    i, j, x = 0, 1, 10000
    for row in reader:
        try:
            st = Student()
            st.index_no = row['Index_number']
            st.name = row['Candidate_Name']
            st.yob = row['DoB']
            st.birth_cert = row['BirthNo']
            st.entry_code = 3 if row['EntryCode'] == '-' else row['EntryCode']
            st.citizenship = row['Citizenship']

            if row['Gender'] == 'M':
                gender = 'Male'
            else:
                gender = 'Female'

            st.gender = gender
            st.kcpe_index = row['KCPEINDEX']
            st.kcpe_year = row['KCPEEXAMYEAR']
            st.subj_count = 0
            st.disability = False if row['Disability_N'] == '' else True
            st.subj_1 = None if row['SUBJ1'] == '' else row['SUBJ1']
            st.subj_2 = None if row['SUBJ2'] == '' else row['SUBJ2']
            st.subj_3 = None if row['SUBJ3'] == '' else row['SUBJ3']
            st.subj_4 = None if row['SUBJ4'] == '' else row['SUBJ4']
            st.subj_5 = None if row['SUBJ5'] == '' else row['SUBJ5']
            st.subj_6 = None if row['SUBJ6'] == '' else row['SUBJ6']
            st.subj_7 = None if row['SUBJ7'] == '' else row['SUBJ7']
            st.subj_8 = None if row['SUBJ8'] == '' else row['SUBJ8']
            st.subj_9 = None if row['SUBJ9'] == '' else row['SUBJ9']
            st.subj_10 = None if row['SUBJ10'] == '' else row['SUBJ10']
            db.s.add(st)
            #db.s.commit()
            j += 1
        except Exception as inst:
            # write row to file
            print j, 'ERROR ROW'
            error_st.append(row)
            print row
            print '--------------------------------------'
            #print sys.exc_info()[0]
            print inst
            print '--------------------------------------'
        finally:
            # print j, row
            # at 520000 we commit individually
            if j > 520000: x= 2
            i += 1
            # We commit very 10k records
            if i > x:
                db.s.commit()
                print j
                i = 0

    db.s.commit()
    pickle.dump(error_st, open( "save_error_students.pickle", "wb" ))



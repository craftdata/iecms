from app.models import *
import csv, pickle
from flask_appbuilder.security.sqla.models import User, Role
from app import appbuilder, db
import random
from datetime import datetime

country = Country()
# Loadup Countries
with open('db/data/countriesy.csv','rU') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, quoting=csv.QUOTE_ALL)
    for row in reader:
        print(row)
        c = Country()
        c.code = row['code']
        c.name = row["name"]
        if c.name == 'Kenya':
            country = c
        c.continent= row["continent"]
        c.region= row["region"]
        c.surfacearea= row["surfacearea"]
        c.indepyear= row["indepyear"]
        c.population= row["population"]
        c.lifeexpectancy= row["lifeexpectancy"]
        c.gnp= row["gnp"]
        c.gnpold= row["gnpold"]
        c.localname= row["localname"]
        c.governmentform= row["governmentform"]
        c.headofstate= row["headofstate"]
        c.capital= row["capital"]
        c.code2= row["code2"]
        c.created_by_fk = 1
        c.changed_by_fk = 1
        db.session.add(c)
        db.session.commit()
        
with open('db/data/counties.csv', 'r') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    # cnt = db.session.Country.query.filter(Country.name == 'Kenya').first()
    for row in reader:
        c = County()
        c.country = country.id
        c.code = row["county_code"]
        c.name = row["county_name"]
        c.created_by_fk = 1
        c.changed_by_fk = 1
        db.session.add(c)
        db.session.commit()
        

with open('db/data/subcounties.csv', 'r') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        s = Subcounty()
        s.code = row["district_code"]
        s.county = row["county_code"]
        s.name = row["district_name"]
        s.created_by_fk = 1
        s.changed_by_fk = 1
        db.session.add(s)
        db.session.commit()
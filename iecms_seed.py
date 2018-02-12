from .models import *
import csv, pickle


with open('db/counties.csv', 'r') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(512))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        c = Country()
        c.

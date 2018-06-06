#!/usr/bin/env bash
# vim:set ts=4 et st=4 sts=4
# File              : gen.sh
# Date              : 14.03.2018
# Last Modified Date: 14.03.2018




# Backup any changes to sqlacodegen, so that it is in git
echo "Moving sqlacodegen:cogen.py"
rsync -avrumP /Users/nyimbi/.bin/anaconda3/lib/python3.6/site-packages/flask_sqlacodegen-1.1.6.1-py3.6.egg/sqlacodegen/ /Users/nyimbi/Dropbox/src/pjs/iecms/codegen/sqlacodegen


echo "Drop Database ctmp"
dropdb ctmp

echo "Drop Database iecms"
dropdb iecms

echo " Dropped Database ctmp"
createdb ctmp

echo " Dropped Database iecms"
createdb iecms

echo "Created Database iecms"
echo "Starting Generating the tables"
# Backup old pony file
cp pomy.py ../db/pony-"$(date)".py
# Take the latest pony file and use it
cp `ls pony* | tail -n1` pomy.py
cat p_connect.py >> pomy.py
python pomy.py
echo "Finished Generating the tables"

echo "Generating mod1.py - preliminary data model"
flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp --outfile mod1.py --flask --noinflect
echo "Finished generating preliminary data model -- proceding to generate view"

echo "Now starting fixup of the models and generating models.py"
python fixup_models.py mod1.py
echo "Models.py file created"

echo "Creating tables in IECMS "
## We haven't fixed up our views yet, so temp measure
cp views_template.py views.py

(
# Inside a subshell
cd ..
echo "GO FIX:   wtf_PageForm, exclude[]"/
# Back to where we started from
# cd app
)
# Because we can't use from .mixin import * we need to from mixin import *
echo " Now fixingup the views"
sed s/'from .mixins import'/'from mixins import'/ <models.py >model1.py
python fixup_views.py model1
# Done with this file
rm model1.py


echo " .......... Done fixingup the views"
LINES="$(cat views.py models.py | wc -l)"
echo "${LINES} lines of code that you did not have to write"
say "${LINES} Lines Generated"

echo " All DONE with generation - now to create the iecms db"

# All done with generation for the time being
# TO DO
(
# Inside a subshell
cd ..
fabmanager create-db
echo "IECMS Database Created"
echo "Adding features to the database"
# pgxn install multicorn
psql -d iecms < app/db_extensions.sql
echo "Features and Extensions added to the database"

#ipython -c "import app"

echo "Now run fabmanager create-db"

fabmanager create-db
fabmanager create-admin

fabmanager list-views > xv.txt
tail -n +4 xv.txt > xview.txt
rm xv.txt
sed 's/^View://g;s/ Route://g;s/ Perms://g'< xview.txt > view_list.csv
)


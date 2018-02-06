
echo "Copy the latest parsers"
cp ../fixup_models.py ../fixup_views.py .
echo "Drop Database ctmp"
dropdb ctmp
echo " Dropped Database ctmp"
createdb ctmp
echo "Created Database ctmp"
echo "Generating the tables"
python pony9.py
echo "Generating mod1.py - preliminary data model"
flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp  --flask --outfile mod1.py
echo "Finished generating preliminary data model -- proceding to generate view"
python fixup_views.py mod1
wc -l  <  views.py
echo "Lines of Code - You didn't have to write"

echo " Now fixingup the models"
python fixup_models.py
echo " All DONE -  copyng views and models to your app directory"

cp field_sets.py models.py views.py sec.py sec_models.py sec_views.py init__.py ../../app

# Find a way to trigger mixins

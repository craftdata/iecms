dropdb ctmp
echo " Dropped Database ctmp"
createdb ctmp
echo "Created Database ctmp"
echo "Generating the tables"
python pony9.py
echo "Generating mod1.py - preliminary data model"
flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp --outfile mod1.py
echo "Finished generating preliminary data model -- proceding to generate view"
python codeg.py mod1
wc -l  <  views.py
echo "Lines of Code - You didn't have to write"

echo " Now fixingup the models"
python fixup_models.py
echo " All DONE -  copy views and models to your app directory"

#!/usr/bin/env bash
dropdb ctmp; createdb ctmp;
python pony8.py
flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp --flask --outfile mod8.py
cp imps.txt models.py
cat mod8.py >> models.py

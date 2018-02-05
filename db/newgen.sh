#!/usr/bin/env sh
python pony8.py

# Now generate the SqlAlchemy Style file
sqlacodegen postgresql://nyimbi@localhost:5432/ctmp > mod1.py



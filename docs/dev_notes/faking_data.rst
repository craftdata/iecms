## Creating Fake Data
---------------------
You might want to install the pgxnclient library - connects you to all the wonderful PgSQL extensions on the pgxn.org network

We are using the faker_fdw to create a fake foreign table
pip install http://github.com/guedes/faker_fdw/archive/v0.1.2.zip

Then install the extension
CREATE EXTENSION multicorn;
CREATE SERVER faker_srv
 FOREIGN DATA WRAPPER multicorn
 OPTIONS (wrapper 'faker_fdw.FakerForeignDataWrapper');


Create a data source like this

CREATE FOREIGN TABLE fake.person (ssn varchar, name varchar, address text) 
         SERVER faker_srv OPTIONS (max_results '100');

         alter it like this to get phone numbers
ALTER FOREIGN TABLE fake.person ADD COLUMN phone_number varchar;

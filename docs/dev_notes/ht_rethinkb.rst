How to Install RethinkDb
-------------------------

brew update && brew install rethinkdb

brew services start rethinkdb

Install python driver
----------------------
pip install rethinkdb


In pgsql
---------
create extension multicorn;

create server myrethinkdb 
    foreign data wrapper multicorn 
    options (
        wrapper 'rethinkdb_fdw.rethinkdb_fdw.RethinkDBFDW', 
        host 'myhost', 
        port '28015', 
        database 'somerethinkdb'
        );

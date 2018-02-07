How to enable Mongo_fdw
-----------------------

#. `pip install pgxnclient`
#. `pgxn install mongo_fdw`


`CREATE EXTENSION IF NOT EXISTS mongo_fdw;
CREATE SERVER mongo_server
        FOREIGN DATA WRAPPER mongo_fdw
        OPTIONS (address '127.0.0.1', port '27017');
CREATE USER MAPPING FOR public
       SERVER mongo_server
       OPTIONS (username 'postgres', password '123456');

CREATE FOREIGN TABLE warehouse(
    _id NAME, -- ObjectIdが格納される
    id INT,
    name text
)  SERVER mongo_server
OPTIONS (DATABASE 'db', collection 'warehouse');

-- DROP FOREIGN TABLE WAREHOUSE;
-- DROP USER MAPPING FOR public SERVER mongo_server;
-- DROP SERVER mongo_server CASCADE;`

In MongoDB
----------

> use db
switched to db db
>  db.createUser({user: "postgres", pwd: "123456",roles:["readWrite", "dbAdmin"]});
Successfully added user: { "user" : "postgres", "roles" : [ "readWrite", "dbAdmin" ] }
> db.warehouse.insert({"id": NumberInt(1),"name":"Tarou"})
WriteResult({ "nInserted" : 1 })
> db.warehouse.find()
{ "_id" : ObjectId("593173a3877efdec0848b3f0"), "id" : 1, "name" : "Tarou" }


from `pgsql`
------------

foo=# SELECT * FROM warehouse WHERE id = 1;


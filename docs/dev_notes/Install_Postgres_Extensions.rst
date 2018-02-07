
## How to Install PostgreSQL extensions
----------------------------------------

Install the pgxn client
1). pip install pgxnclient

#. pgxn install quantile
   pgxn load -d mydb quantile

Or if you want to do it manuallu
psql dbname -c "CREATE EXTENSION quantile"


you are done



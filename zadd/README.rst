Additional Software
--------------------

**Challenges:**
#. There will be millions of files stored in the system. It is infeasible to store them on the filesystem - it would slow down dramatically when there are hundreds of thousands of files. We want a solution that is horizontally scaleable and can be sharded over many servers without human intervention of management -> Enter MongoDB (or some such), at the moment I am considering MongoDB.
* https://github.com/EnterpriseDB/mongo_fdw
  This is a foreign data wrapper for postgresql
* Also need to consider Amazon S3, but there is an issue with data residency - so this is not a good idea

#. MPESA: Need a service to listen to MPESA calls to ensure that the payment service is working and to verify payments. It will sit here.

#. SMS Notifications and other things like that

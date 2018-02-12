create extension multicorn;
-- create extension check_updates;
create extension count_distinct;
create extension postgis;
create extension pgcrypto;
create EXTENSION tablefunc;
create extension cube;
create extension earthdistance;
create extension fuzzystrmatch;
create extension postgres_fdw;
create extension timetravel;
create extension moddatetime;





-- Fake Data Generator
CREATE SERVER faker_srv
 FOREIGN DATA WRAPPER multicorn
 OPTIONS (wrapper 'faker_fdw.FakerForeignDataWrapper');

CREATE OR REPLACE FUNCTION sha1(bytea) returns text AS $$
    SELECT encode(digest($1, 'sha1'), 'hex')
$$ LANGUAGE SQL STRICT IMMUTABLE;


--CREATE TRIGGER mdt_moddatetime
--	BEFORE UPDATE ON mdt
--	FOR EACH ROW
--	EXECUTE PROCEDURE moddatetime (moddate);


create or replace function bytea_import(p_path text, p_result out bytea)
language plpgsql as $$
declare
  l_oid oid;
  r record;
begin
  p_result := '';
  select lo_import(p_path) into l_oid;
  for r in ( select data
             from pg_largeobject
             where loid = l_oid
             order by pageno ) loop
    p_result = p_result || r.data;
  end loop;
  perform lo_unlink(l_oid);
end;$$;


CREATE OR REPLACE FUNCTION sms_notification()
RETURNS trigger AS
$$
BEGIN
         INSERT INTO notification(contact,message,sent)
         VALUES(Kontact,Msg,false);

    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE or REPLACE FUNCTION make_hearing_notification(h as hearing)
	RETURNS trigger
AS $$
BEGIN
	if h["adjourned_to"] is not None:
		adj_str = "Adjourned to {0} because {1}".format(h["adjourned_to"], h["adjournment_reason"])
	else:
		adj_str = ""

	msg = " Court Case: Date {0}  "
	insert into notification(retry_count)
    values
	select * from notificationregister
	where notificationregister.id = hearing_no

END;
$$ LANGUAGE 'plpythonu';

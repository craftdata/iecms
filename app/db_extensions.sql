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


CREATE OR REPLACE FUNCTION sms_notification(in Kontact, in msg)
RETURNS trigger AS
$$
BEGIN
         INSERT INTO notification(contact,message,sent)
         VALUES(Kontact,Msg,false);

    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';


create function ncode_gen(the_num bigint)
returns text
as $$
global the_num
alpha33, prn =  ['ABCDEFGHJKMNPQRSTUVWXYZ0123456789', '']
while the_num:
    the_num, j = divmod(the_num, 33)
    prn = alpha33[j] + prn

z = 4 - len(prn)
if z > 0:
    prn = ("A" * z) + prn
return prn or alpha33[0]
$$ LANGUAGE plpythonu;

--create function s_scode()
--returns trigger as '
--BEGIN
-- NEW.school_code = scode_gen(NEW.sch_id);
-- return NEW;
--END' LANGUAGE 'plpgsql'
--
--
--CREATE TRIGGER scode_trigger
--BEFORE INSERT ON school
--FOR EACH ROW
--EXECUTE PROCEDURE s_scode()
--
--CREATE TRIGGER scode_trigger_after
--AFTER INSERT ON school
--FOR EACH ROW
--EXECUTE PROCEDURE s_scode()

--CREATE or REPLACE FUNCTION make_hearing_notification(h as hearing)
--	RETURNS trigger
--AS $$
--BEGIN
--	if h["adjourned_to"] is not None:
--		adj_str = "Adjourned to {0} because {1}".format(h["adjourned_to"], h["adjournment_reason"])
--	else:
--		adj_str = ""
--
--	msg = " Court Case: Date {0}  "
--	insert into notification(retry_count)
--    values
--	select * from notificationregister
--	where notificationregister.id = hearing_no
--
--END;
--$$ LANGUAGE 'plpythonu';



CREATE OR REPLACE FUNCTION public.notify_insert() RETURNS trigger AS
$BODY$
BEGIN
      IF TG_WHEN=’BEFORE’ OR TG_WHEN='AFTER' THEN
            IF TG_OP=’INSERT’ THEN
                  INSERT INTO notification (change_user, message) VALUES (NEW.changed_by_fk, 'There has been an addition to your court '|| TG_TABLE_NAME);
            ELSIF TG_OP=’UPDATE’ -- AND OLD.code IS DISTINCT FROM NEW.code THEN
                  INSERT INTO notification (change_user, message) VALUES (NEW.changed_by_fk, 'There has been a change to your court '|| TG_TABLE_NAME);
            END IF;
      END IF;
      RETURN NEW;
END$BODY$
LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER hearing
BEFORE INSERT OR UPDATE
ON public.sample FOR EACH ROW EXECUTE PROCEDURE public.notify_insert();

CREATE TRIGGER courtcase
BEFORE INSERT OR UPDATE
ON public.sample FOR EACH ROW EXECUTE PROCEDURE public.notify_insert();
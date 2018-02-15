
CREATE EXTENSION plpythonu;

create function scode_gen(the_num bigint)
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




create function s_scode()
returns trigger as '
BEGIN
 NEW.school_code = scode_gen(NEW.sch_id);
 return NEW;
END' LANGUAGE 'plpgsql'


CREATE TRIGGER scode_trigger
BEFORE INSERT ON school
FOR EACH ROW
EXECUTE PROCEDURE s_scode()

CREATE TRIGGER scode_trigger_after
AFTER INSERT ON school
FOR EACH ROW
EXECUTE PROCEDURE s_scode()

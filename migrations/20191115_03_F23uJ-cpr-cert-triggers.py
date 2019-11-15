"""
cpr-cert-triggers
"""

from yoyo import step

__depends__ = {'20191115_01_2H13h-change-event-opener-fk-to-be-on-delete-set-null', '20191115_02_ds0jT-alter-the-userid-foreign-key-on-timeenty'}

steps = [
    step("""CREATE TRIGGER cpr_opener_role
BEFORE INSERT ON cs542.UserRoles FOR EACH ROW
BEGIN
	declare cpr INT;
	SELECT cpr_certified into cpr from User WHERE userid=NEW.userid;
	IF (NEW.role='opener' and cpr=0) THEN
		signal sqlstate '25421' set message_text = 'Cannot set user as opener if they are not CPR Certified!';
	END IF;
END;"""),
    step("""CREATE TRIGGER cpr_opener_user
BEFORE UPDATE ON cs542.User FOR EACH ROW
BEGIN
	declare opener_role INT;
	SELECT COUNT(*) into opener_role from UserRoles WHERE userid=NEW.userid and role='opener';
	IF (NEW.cpr_certified=0 and opener_role=1) THEN
		signal sqlstate '25422' set message_text = 'Cannot unset user as cpr certified until they are demoted from being an opener!';
	END IF;
END;""")
]

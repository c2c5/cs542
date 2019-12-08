"""
trigger-password-change-logout
"""

from yoyo import step

__depends__ = {'20191013_01_z7Cn9-cascade-userroles-delete'}

steps = [
step("""CREATE TRIGGER logout_upon_password_change AFTER UPDATE ON cs542.User FOR EACH ROW 
BEGIN 
	IF NOT (NEW.password_hash <=> OLD.password_hash) THEN 
		DELETE FROM LoginSession WHERE userid=NEW.userid; 
	END IF; 
END;""")
]

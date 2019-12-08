"""
make trigger in events table
"""

from yoyo import step

__depends__ = {'20191125_01_ehaeU'}

steps = [
step("""CREATE TRIGGER event_time_insert BEFORE INSERT ON cs542.event FOR EACH ROW
BEGIN 
	IF NEW.start > NEW.end THEN 
		signal sqlstate '25500' set message_text = 'End time should not be earlier than start time!'; 
	END IF; 
END;"""),
step("""CREATE TRIGGER event_time_update BEFORE UPDATE ON cs542.event FOR EACH ROW
BEGIN 
	IF NEW.start > NEW.end THEN 
		signal sqlstate '25501' set message_text = 'End time should not be earlier than start time!'; 
	END IF; 
END;""")
]

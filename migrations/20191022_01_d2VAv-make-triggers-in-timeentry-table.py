"""
make triggers in timeEntry table
"""

from yoyo import step

__depends__ = {'20191021_01_yPkaO-make-end-in-timeentry-nullable'}

steps = [
step("""CREATE TRIGGER trig_timeentry BEFORE INSERT ON cs542.timeentry FOR each row
BEGIN 
	declare boo INT;
    declare boo1 INT;
    declare boo2 INT;
    declare boo3 INT;
    declare boo4 INT;
    SELECT paid into boo FROM User U WHERE userid = new.userid;
	SELECT paid_members_only into boo1 FROM event where eventid = new.eventid;  
    SELECT waiver into boo2 FROM user where userid = new.userid;
	SELECT max_participants into boo3 FROM event WHERE eventid = new.eventid;
    SELECT count(*) into boo4 FROM timeentry where eventid = new.eventid AND end is null;
    IF boo4 >= boo3 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because the event has reached the maximum number of participants';
    END IF;

    IF boo = 0 and boo1 = 0 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because waiver has not been signed';
    END IF;
    IF boo = 0 and boo1 = 1 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because membership has not been paid and waiver has not been signed';		    
    END IF;
    IF boo = 1 and boo1 = 0 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because waiver has not been signed';
    END IF;
    IF boo = 1 and boo1 = 1 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because waiver has not been signed';
    END IF;
    IF boo = 0 and boo1 = 1 and boo2 =1 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because membership has not been paid';
    END IF;
END;""")
]

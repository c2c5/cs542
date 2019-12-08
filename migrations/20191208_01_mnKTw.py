"""
make trigger for tournament
"""

from yoyo import step

__depends__ = {'20191125_01_ehaeU'}

steps = [
step("""CREATE TRIGGER tournament_insert BEFORE INSERT ON cs542.event FOR EACH ROW
BEGIN 
	IF ((NEW.tournament_result_unit is not NULL and NEW.tournament_result_ordering is NULL) or (NEW.tournament_result_unit is NULL and NEW.tournament_result_ordering is not NULL)) THEN 
		signal sqlstate '25500' set message_text = 'You should set both ordering and unit for the tournament!'; 
	END IF; 
END;"""),
step("""CREATE TRIGGER tournament_update BEFORE UPDATE ON cs542.event FOR EACH ROW
BEGIN 
	IF ((NEW.tournament_result_unit is not NULL and NEW.tournament_result_ordering is NULL) or (NEW.tournament_result_unit is NULL and NEW.tournament_result_ordering is not NULL)) THEN 
		signal sqlstate '25501' set message_text = 'You should set both ordering and unit for the tournament!'; 
	END IF; 
END;""")
]

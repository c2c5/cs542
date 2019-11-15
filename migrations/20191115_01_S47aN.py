"""

"""

from yoyo import step

__depends__ = {'20191107_02_Bl986-add-two-views-for-checkin-out'}

steps = [
step("""
CREATE or replace view checkin AS
SELECT student_name as Name, T.userid, eventid, end
FROM TimeEntry T, User U
WHERE T.userid = U.userid AND T.end is null;"""),
step("""
CREATE or replace view checkout AS
SELECT student_name as Name, T.userid, eventid, total_time
FROM TimeEntry T, User U
WHERE T.userid = U.userid AND T.end is not null;""")
]

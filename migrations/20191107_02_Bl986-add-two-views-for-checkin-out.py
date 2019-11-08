"""
add two views for checkin/out
"""

from yoyo import step

__depends__ = {'20191107_01_PImqT'}

steps = [
step("""
CREATE VIEW checkin AS
SELECT student_name as Name, eventid, end
FROM TimeEntry T, User U
WHERE T.userid = U.userid AND T.end is null
"""),
step("""
CREATE VIEW checkout AS
SELECT student_name as Name, eventid, total_time
FROM TimeEntry T, User U
WHERE T.userid = U.userid AND T.end is not null
""")
]

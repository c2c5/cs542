"""

"""

from yoyo import step

__depends__ = {'20191022_01_d2VAv-make-triggers-in-timeentry-table', '20191022_01_d2si0-add-opener-to-event'}

steps = [
step("""
CREATE view PE as
SELECT student_name AS Name, start, total_time 
FROM User U 
left join timeentry AS T
ON U.userid = T.userid 
WHERE U.pe_credit = 1;
""")
]

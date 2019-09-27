"""
Create Userdata View
"""

from yoyo import step

__depends__ = {'20190914_02_gA5Xf-create-tournamentparticipants', '20190916_01_KsWxH-create-UserRoles', '20190916_02_RbiMa-create-timeEntry', '20190917_01_Jttbg-auto-session-expiry-event'}

steps = [
    step("CREATE VIEW UserData AS SELECT userid, student_name, join_date, paid, waiver, cpr_certified, pe_credit FROM User;")
]

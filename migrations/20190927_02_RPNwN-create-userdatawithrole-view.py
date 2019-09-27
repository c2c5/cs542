"""
Create UserDataWithRole View
"""

from yoyo import step

__depends__ = {'20190927_01_ouV2L-create-userdata-view'}

steps = [
    step("CREATE VIEW UserDataWithRole AS SELECT U.*, IFNULL(GROUP_CONCAT(R.Role SEPARATOR ', '), '') AS roles FROM UserData U left outer join UserRoles R on U.userid=R.userid GROUP BY U.userid;")
]

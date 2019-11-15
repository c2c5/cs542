"""
change event opener fk to be on delete set null
"""

from yoyo import step

__depends__ = {'20191107_02_Bl986-add-two-views-for-checkin-out'}

steps = [
    step("ALTER TABLE cs542.event DROP FOREIGN KEY opener_id"),
    step("ALTER TABLE cs542.event ADD CONSTRAINT opener_id FOREIGN KEY(opener) REFERENCES user(userid) ON DELETE SET NULL")
]

"""
add-opener-to-event
"""

from yoyo import step

__depends__ = {'20191014_01_GoMDS-trigger-password-change-logout'}

steps = [
step("""ALTER TABLE cs542.event ADD opener SMALLINT UNSIGNED;"""),
step("""ALTER TABLE cs542.event ADD CONSTRAINT opener_id FOREIGN KEY(opener) REFERENCES user(userid) ON DELETE CASCADE;""")
]

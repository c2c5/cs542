"""
drop-user-salt
"""

from yoyo import step

__depends__ = {'20190913_01_rb2OO-create-users'}

steps = [
    step("ALTER TABLE User DROP password_salt;")
]

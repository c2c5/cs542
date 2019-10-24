"""

"""

from yoyo import step

__depends__ = {'20190913_01_rb2OO-create-users'}

steps = [
step(
"""CREATE TABLE UserRoles(
    userid SMALLINT UNSIGNED NOT NULL,
    role VARCHAR(6) NOT NULL,
    FOREIGN KEY (userid) REFERENCES User(userid),
    CHECK (role IN ('admin', 'setter', 'opener'))
);"""
)
]
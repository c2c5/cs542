"""
create route
"""

from yoyo import step

__depends__ = {'20190913_02_LViZ5-create-events'}

steps = [
step(
"""CREATE TABLE Route(
    routeid SMALLINT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    set_by SMALLINT UNSIGNED NOT NULL,
    difficulty TINYINT UNSIGNED NOT NULL,
    picture VARCHAR(32),
    FOREIGN KEY (set_by) REFERENCES User(userid),
    Check(17 >= difficulty >= 0)
); """
)
]

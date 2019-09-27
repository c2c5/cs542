"""
login sessions
"""

from yoyo import step

__depends__ = {'20190913_02_LViZ5-create-events', '20190916_01_77FxU-drop-user-salt'}

steps = [
step("""CREATE TABLE LoginSession(
    userid SMALLINT UNSIGNED PRIMARY KEY NOT NULL,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    token VARCHAR(60) NOT NULL UNIQUE,
    INDEX userid_ind (userid),
    FOREIGN KEY (userid)
        REFERENCES User(userid)
        ON DELETE CASCADE
);"""),
step("ALTER TABLE User MODIFY student_id VARCHAR(128);")
]

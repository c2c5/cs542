"""

"""

from yoyo import step

__depends__ = {'20190913_02_LViZ5-create-events'}


steps = [
step(
"""CREATE TABLE TimeEntry(
    eventid SMALLINT UNSIGNED NOT NULL,
    userid SMALLINT UNSIGNED NOT NULL,
    start TIMESTAMP NOT NULL,
    end TIMESTAMP NOT NULL,
    total_time MEDIUMINT UNSIGNED,
    PRIMARY KEY (eventid, userid),
    FOREIGN KEY (eventid) REFERENCES Event(eventid),
    FOREIGN KEY (userid) REFERENCES User(userid)
);"""
)
]
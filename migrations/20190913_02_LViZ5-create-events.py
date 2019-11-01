"""
create events
"""

from yoyo import step

__depends__ = {'20190913_01_rb2OO-create-users'}

steps = [
    step(
"""CREATE TABLE event (
    eventid SMALLINT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    max_participants TINYINT UNSIGNED,
    start DATETIME NOT NULL,
    end DATETIME NOT NULL,
    actual_start TIMESTAMP,
    actual_end TIMESTAMP,
    name VARCHAR(40) NOT NULL,
    description TEXT,
    cost TINYINT UNSIGNED,
    paid_members_only BOOLEAN NOT NULL DEFAULT TRUE,
    tournament_result_unit VARCHAR(10),
    tournament_result_ordering BOOLEAN,
    CHECK((start < end) and (actual_start <= actual_end))
);"""
)
]
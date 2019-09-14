"""
create tournamentParticipants
"""

from yoyo import step

__depends__ = {'20190914_01_FONOP-create-route'}

steps = [
step(
"""CREATE TABLE TournamentParticipants(
    eventid SMALLINT UNSIGNED NOT NULL,
    userid SMALLINT UNSIGNED NOT NULL,
    score DOUBLE,
    PRIMARY KEY(eventid, userid),
    FOREIGN KEY(eventid) REFERENCES Event(eventid),
    FOREIGN KEY(userid) REFERENCES User(userid)
);"""
)
]

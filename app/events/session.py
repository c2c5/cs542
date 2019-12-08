from util import database
import flask


def get_result(eventid, userid):
    db = database.get_db()
    with db.cursor() as cursor:
        get_result = 'SELECT score FROM tournamentparticipants WHERE userid=%s AND eventid=%s;'
        cursor.execute(get_result, (userid, eventid))
        result = cursor.fetchone()
        if result is None:
            return None
    return result['score']
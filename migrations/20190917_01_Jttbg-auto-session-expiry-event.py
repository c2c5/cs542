"""
auto-session-expiry-event
"""

from yoyo import step

__depends__ = {'20190916_02_CImKu-login-sessions'}

steps = [
step("""CREATE EVENT expireloginsession
ON SCHEDULE EVERY 1 HOUR
DO
DELETE FROM LoginSession
WHERE (NOW() - start_time) > 86400;""")
]

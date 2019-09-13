"""
Create users
"""

from yoyo import step

__depends__ = {}

steps = [
step(
"""CREATE TABLE User(
    userid SMALLINT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    student_id VARCHAR(60) NOT NULL UNIQUE,
    student_name VARCHAR(30) NOT NULL,
    join_date DATE NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    waiver BOOLEAN NOT NULL DEFAULT FALSE,
    cpr_certified BOOLEAN NOT NULL DEFAULT FALSE,
    password_hash VARCHAR(60) NOT NULL,
    password_salt VARCHAR(20) NOT NULL,
    pe_credit BOOLEAN NOT NULL DEFAULT FALSE
)"""
)
]

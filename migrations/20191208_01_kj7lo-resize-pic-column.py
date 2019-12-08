"""
resize-pic-column
"""

from yoyo import step

__depends__ = {'20191115_03_F23uJ-cpr-cert-triggers'}

steps = [
    step("ALTER TABLE Route MODIFY picture VARCHAR(64);")
]

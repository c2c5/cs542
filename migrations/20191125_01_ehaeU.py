"""
add display atttribute to event table
"""

from yoyo import step

__depends__ = {'20191115_03_F23uJ-cpr-cert-triggers'}

steps = [
    step("""ALTER TABLE event ADD display BOOLEAN DEFAULT 1;
    	""")
]

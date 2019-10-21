"""
make end in timeentry nullable
"""

from yoyo import step

__depends__ = {'20191014_01_GoMDS-trigger-password-change-logout'}

steps = [
    step("""ALTER TABLE `cs542`.`timeentry` 
CHANGE COLUMN `end` `end` TIMESTAMP NULL,
CHANGE COLUMN `total_time` `total_time` decimal(5,2) AS (TIMESTAMPDIFF(second, start, end) / 3600) stored;"""
         )
]

"""
alter the userid foreign key on timeenty 
"""

from yoyo import step

__depends__ = {'20191115_01_S47aN'}

steps = [
step("SET @droptable='';"),
step("""SELECT @droptable:=concat(@droptable, 'ALTER TABLE ', 'cs542.TimeEntry', ' DROP FOREIGN KEY ', constraint_name, ';') FROM information_schema.KEY_COLUMN_USAGE
WHERE
  constraint_schema = 'cs542' AND table_name = 'TimeEntry' AND   
  referenced_table_name = 'User';"""),
step("prepare stmt from @droptable;"),
step("execute stmt;"),
step("deallocate prepare stmt;"),
step("ALTER TABLE cs542.TimeEntry ADD CONSTRAINT TimeEntry_fk_userid FOREIGN KEY (userid) REFERENCES User(userid) ON DELETE CASCADE;"),
step("SET @droptable = NULL;")
]

"""
Cascade-Userroles-delete

"""

from yoyo import step

__depends__ = {'20190927_02_RPNwN-create-userdatawithrole-view'}

steps = [
step("SET @droptable='';"),
step("""SELECT @droptable:=concat(@droptable, 'ALTER TABLE ', 'cs542.UserRoles', ' DROP FOREIGN KEY ', constraint_name, ';') FROM information_schema.KEY_COLUMN_USAGE
WHERE
  constraint_schema = 'cs542' AND table_name = 'UserRoles' AND   
  referenced_table_name IS NOT NULL;"""),
step("prepare stmt from @droptable;"),
step("execute stmt;"),
step("deallocate prepare stmt;"),
step("ALTER TABLE cs542.UserRoles ADD CONSTRAINT UserRoles_fk_userid FOREIGN KEY (userid) REFERENCES User(userid) ON DELETE CASCADE;"),
step("SET @droptable = NULL;")
]

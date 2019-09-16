import pymysql

connection = pymysql.connect(host='localhost',
                             user='cs542',
                             password='cs542dbmsdatabaseproject',
                             db='cs542',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
import sqlite3
connection = sqlite3.connect('/home/pi/Desktop/ngc2264.LEMONdB') # La BD es muy cerda
print(connection)
cursor = connection.cursor()
cursor.execute("select * from cmp_stars where id<10")
for r in cursor:
    print(r)

connection.close()
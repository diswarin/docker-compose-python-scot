import pypyodbc as pyodbc # you could alias it to existing pyodbc code (not every code is compatible)
#import pprint; pp = pprint.PrettyPrinter(indent=4)
db_host = 'LENOVOKUM\WINCC'
db_name = 'FT_ServeDB'#CI_DB_1'
db_user = 'kum'
db_password = '123456'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
#connection_string = 'Driver={ODBC Driver 17for SQl Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pyodbc.connect(connection_string)
print(db)

SQL_QUERY = """
SELECT A1,A2 FROM CI_DB_1
"""
# Method 3, we obtain a list of dict's (represents the entire query)
cursor = db.cursor()
cursor.execute(SQL_QUERY)
print(cursor)
records = cursor.fetchall()
for r in records:
    print(r[1])
    print(r[0])

import pypyodbc as pyodbc # you could alias it to existing pyodbc code (not every code is compatible)
import dss

from fractions import Fraction

db_host = 'LENOVOKUM\WINCC'
db_name = 'FT_ServeDB'#CI_DB_1'
db_user = 'kum'
db_password = '123456'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
#connection_string = 'Driver={ODBC Driver 17for SQl Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pyodbc.connect(connection_string)
#print(db)
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
conn = dss.connect()

#fields = dss.getFieldNames(conn , 'ITEM_VAL')

fields       = dss.getFieldNames(conn , 'ITEM_HISTORY')
#print (fields)
#data_set = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'r')
data_set    	= dss.openDataset(conn, 'ITEM_VAL',['NAME','SAMPLE_TIME','ITEM_VALUE_STR'], 'ru')
records1     	= dss.readEqual(conn, data_set, 'STATIONS.testint')
records2     	= dss.readEqual(conn, data_set, 'STATIONS.testreal')
A1= str(r[0])
A2 = str(r[1])
print (A1)
print (A2)
records1['ITEM_VALUE_STR'] = A1
dss.updateRecord(conn ,data_set, records1)
records2['ITEM_VALUE_STR'] = A2
dss.updateRecord(conn ,data_set, records2)
print (records1)
print (records2)

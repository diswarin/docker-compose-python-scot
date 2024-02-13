import pandas
import sqlalchemy
import pypyodbc
import dss

from fractions import Fraction


conn = dss.connect()

#fields = dss.getFieldNames(conn , 'ITEM_VAL')

fields       = dss.getFieldNames(conn , 'ITEM_HISTORY')
#print (fields)
#data_set = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'r')
data_set    	= dss.openDataset(conn, 'ITEM_VAL',['NAME','SAMPLE_TIME','ITEM_VALUE_STR'], 'ru')
records1     	= dss.readEqual(conn, data_set, 'STATIONS.testint')
records2     	= dss.readEqual(conn, data_set, 'STATIONS.testreal')
records1['ITEM_VALUE_STR'] = "14"
dss.updateRecord(conn ,data_set, records1)
records2['ITEM_VALUE_STR'] = "84.5"
dss.updateRecord(conn ,data_set, records2)
print (records1)
print (records2)
 
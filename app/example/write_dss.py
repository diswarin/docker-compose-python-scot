import dss

from fractions import Fraction

from datetime import datetime


conn = dss.connect()
logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
logs_data = ['Conncet DSS Pass !!!',logs_now]
print (logs_data)

#fields = dss.getFieldNames(conn , 'ITEM_VAL')

fields       = dss.getFieldNames(conn , 'ITEM_VAL')
print (fields)
#data_set = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'r')
data_set    	= dss.openDataset(conn, 'ITEM_VAL',['NAME','SAMPLE_TIME','ITEM_VALUE'], 'ru')
records1     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI013_HH')
# records2     	= dss.readEqual(conn, data_set, 'STATIONS.testreal')
# records1['ITEM_VALUE_STR'] = "14"
# dss.updateRecord(conn ,data_set, records1)
# records2['ITEM_VALUE_STR'] = "84.5"
# dss.updateRecord(conn ,data_set, records2)
print (records1)
# print (records2)
 
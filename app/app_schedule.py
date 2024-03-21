import dss
from datetime import datetime
import schedule

def read_tag():
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
    print (records1)


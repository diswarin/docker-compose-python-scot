from datetime import datetime
import time
import csv 
import dss

logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
conn = dss.connect()
logs_now_read_tag = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
logs_data = ['Conncet DSS Pass !!!',logs_now_read_tag]
print (logs_data)

def read_tag():
    #fields = dss.getFieldNames(conn , 'ITEM_VAL')
    fields       = dss.getFieldNames(conn , 'ITEM_VAL')
    print (fields)
    #data_set = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'r')
    data_set    	= dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'ru')
    record_HMI201_BATCH_BUF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_BATCH_BUF')
    print (record_HMI201_BATCH_BUF)
    write_logs(record_HMI201_BATCH_BUF)
    record_HMI201_ORDER_BUF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_ORDER_BUF')
    print (record_HMI201_ORDER_BUF)
    write_logs(record_HMI201_ORDER_BUF)
    record_HMI201_PROD_BUFF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_PROD_BUFF')
    print (record_HMI201_PROD_BUFF)
    write_logs(record_HMI201_PROD_BUFF)

def write_logs(logs_data):
    this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    with open('logs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([this_moment,logs_data])

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat)
        # print()
        # print("GeeksforGeeks", end= ' ')
        time.sleep(1)
        time_sec -= 1
    print("START PROCESS NOW !!")


while(True):
    try:
        read_tag()  
        countdown(60)
    except:
        error_python = "{} : problem with script or manual !!!"
        print(error_python.format(logs_now))
        # print('problem with script or manual !!!')


from datetime import datetime
import time
import csv 

logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:$S')


while(True):
    try:
        logs_data = []
        this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        logs_data = ['TAG01','TAG02',this_moment]
        # Pass The CSV file object to writer() function
        spamWriter = csv.writer(open('logs.csv', 'wb'), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # Result = a writer object
        # Pass the data in the list as an argument into the writerow() function
        spamWriter.writerow(logs_data)
        # time.sleep(3)
        print(logs_data)
    except:
        error_python = "{} : problem with script or manual !!!"
        print(error_python.format(logs_now))
        # print('problem with script or manual !!!')


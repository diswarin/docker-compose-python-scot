import datetime
import time

import threading
logs_now = datetime.datetime.now()
suma_lock = threading.Lock()
suma = {
  'fir': 2,
  'sec': 3,
  'tot': 80
}

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat)
        # print()
        # print("GeeksforGeeks", end= ' ')
        time.sleep(1)
        time_sec -= 1
    print("Stop !!")

def doCalc():
    time.sleep(2.1)
    with suma_lock:
        suma['tot'] -= suma['sec']
    print 'second action: ' + str(suma['tot'])

def first():
    while int(suma['tot']) > 0:
        time.sleep(0.5)
        print 'first action: ' + str(suma['tot'])
        with suma_lock:
            suma['tot'] -= suma['fir']  
hello_python = "{} : My Python 2.7 Docker !!!"
print(hello_python.format(logs_now))
# threading.Thread(target=first).start()
# threading.Thread(target=countdown(50)).start()
# threading.Thread(target=doCalc).start()

countdown(5)

# time.sleep(3)       
# print '_' * 10

# hack: tell 'first' to exit
with suma_lock:
    suma['tot'] = 0

for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

done_python = "{} : DONE !!!"
print(done_python.format(logs_now))
# countdown(5)
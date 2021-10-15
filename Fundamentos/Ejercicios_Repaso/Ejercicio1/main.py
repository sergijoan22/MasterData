import time
import datetime

now = datetime.datetime.now()

while True:
    print(now.strftime("%H:%M:%S"))
    time.sleep(5)
    now = datetime.datetime.now()

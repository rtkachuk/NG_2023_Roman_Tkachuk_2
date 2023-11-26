import threading
import time

lock = threading.Lock()
number = 0

def calculate(threadNumber):
    global number
    print ("Thread #" + str(threadNumber) + ":" + "Waiting for variable!")
    while number < 100:
        with lock:
            print ("Thread #" + str(threadNumber) + ":" + "Got control!")
            number = number + 1
            print ("Thread #" + str(threadNumber) + ":" + str(number))
            time.sleep(0.1)

threads = []
for number in range(0,30):
    threads.append(threading.Thread(target=calculate, args=(number, )))

for thread in threads:
    thread.start()
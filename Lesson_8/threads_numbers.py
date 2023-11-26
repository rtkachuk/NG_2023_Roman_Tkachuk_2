import threading

def calculate(threadNumber):
    for number in range(0, 10000000):
        print ("Thread #" + str(threadNumber) + ":" + str(number))

threads = []
for number in range(0,15):
    threads.append(threading.Thread(daemon=True, target=calculate, args=(number, )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join(1)
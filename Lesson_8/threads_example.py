import threading

def showLetters(threadNumber, txt):
    print ("NewLine: ")
    for letter in txt:
        print ("Thread #" + str(threadNumber) + ":" + letter)

text = '''Hello world!
How are you?!
Where are you been?
Python is awesome!'''

threads = []
lines = text.split('\n')
for line in lines:
    threads.append(threading.Thread(target=showLetters, args=(lines.index(line), line, )))

for thread in threads:
    thread.start()
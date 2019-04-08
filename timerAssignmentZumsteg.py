import threading
import time

def displayTime():
    print(time.time())

def displayAgain():
    time.sleep(10.0)
    print(time.time())

#t will create the current time
t = time.time()
#first thread will display the first time
t1 = threading.Thread(target = displayTime() , args = t)
#second thread will display time after 10 seconds of wait time
t2 = threading.Thread(target = displayAgain(), args = t)

#starts the threads
t1.start()
t2.start()

#will wait for first thread to post before starting the second thread
t1.join()
t2.join()
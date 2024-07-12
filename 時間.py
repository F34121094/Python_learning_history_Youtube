import threading
import time

def eat():
    time.sleep(3)
    print("Eating")
def walk():
    time.sleep(4)
    print("Walking")
def drink():
    time.sleep(5)
    print("Drinking")
x = threading.Thread(target = eat,args=())
x.start()
x = threading.Thread(target = walk,args=())
x.start()
x = threading.Thread(target = drink,args=())
x.start()
# eat()
# drink()
# drink()

print(threading.active_count())
print(threading.enumerate())

import threading
import time

def gowno(a):
    for _ in range(0,10):
        print(a)
        time.sleep(0.1)

def dupa(a):
    for _ in range(0,10):
        print(a)
        time.sleep(0.1)

x = threading.Thread(target=gowno, args=(2, ))
y = threading.Thread(target=dupa, args=(6 ,))
x.start()
y.start()
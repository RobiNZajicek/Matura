import threading 
import time


def teaking_thrash():
    time.sleep(5)
    print('I took out the thrash')
def dishes():
    time.sleep(8)
    print('I did the dishes')
def clean_room():
    time.sleep(5)
    print('I have cleaned my room')

t1=threading.Thread(target=teaking_thrash)
t2=threading.Thread(target=dishes)
t3=threading.Thread(target=clean_room)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
    
print('all done')

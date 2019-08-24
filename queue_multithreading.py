import threading 
import time
from queue import Queue 

number_thread=20
number_jobs=30
def func1():
        time.sleep(0.5)

def jobs(q):
    while True:
        if q.get() is None:
                break
        func1()
        q.task_done()


q = Queue()
thread_list =[]

# start threads
for i in range(number_thread):
    thread_list.append(threading.Thread(target=jobs,args=(q,)))
    thread_list[i].start()

start = time.time()


for i in range(number_jobs):
    q.put(i)

# wait untill all jons in queue is done
q.join()

# stop threads
for i in range(number_thread):
    q.put(None)
for t in thread_list:
    t.join()

print("time finish {} in seconds with multithreading".format(time.time()-start))

start = time.time()
for i in range(number_jobs):
    func1()
print("time finish {} in seconds without multithreading".format(time.time()-start))

import threading 
import time
from queue import Queue 

number_thread=20
number_jobs=30
def func1():
    time.sleep(1)

def jobs(q):
    while not q.empty():
        q.get()
        func1()
        q.task_done()


q = Queue()
for i in range(number_jobs):
    q.put(i)



thread_list =[]
for i in range(number_thread):
    thread_list.append(threading.Thread(target=jobs,args=(q,)))
    thread_list[i].start()
start = time.time()

q.join()
for i in range(number_thread):
    thread_list[i].join()

print("time finish {} in seconds with multithreading".format(time.time()-start))

start = time.time()
for i in range(number_jobs):
    func1()
print("time finish {} in seconds without multithreading".format(time.time()-start))

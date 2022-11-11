#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:01:13 2022

@author: mikelin
"""
import _thread
import threading

myLock = threading.Lock()

class myThread(threading.Thread):
    def __init__(self,id,name):
        threading.Thread.__init__(self)
        self.id=id
        self.name=name
    def run(self):
        myLock.acquire()
        thread_proc(self.name, "new threading module", 4)
        myLock.release()
    
def thread_proc(tname,msg,repeat):
#    global lock
#    while lock==1:
#        pass
#    lock=1
    print('Repeat the messge '+str(repeat)+' times')
    i=1
    while i<=repeat:
        print(tname,i,msg)
        i+=1
#    lock=0

def decorThread(func,tname,msg,repeat):
    func(tname,msg+'-appended',repeat)
        
if (__name__=='__main__'):
#    lock=0
    try:
        t1 = _thread.start_new_thread(thread_proc, ('Thread 1','hello world',5))
        t2 = _thread.start_new_thread(thread_proc, ('Thread 2','here I come',10))
        t3 = _thread.start_new_thread(thread_proc, ('Thread 3','end of the world is here',3))
        t4 = _thread.start_new_thread(thread_proc, ('Thread 4','the sky is falling',20))
    except:
        print('Failure to create thread')
thread_proc('non-threaded call', 'outside of any thread', 6)

myCalc = lambda arg1, arg2, arg3, arg4 : (arg1+arg2)*(arg3/arg4)
print('myCalc returns : '+str(myCalc(1, 2, 3, 4)))

decorThread(thread_proc,'decorator', 'decrator says hello', 4)

threading1 = myThread(1,"threading1")
threading2 = myThread(2, 'threading2')
threading1.start()
threading2.start()
print('Threading nname = '+threading1.getName())


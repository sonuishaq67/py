import threading

class MyThread(threading.Thread):
    def __init__(self,str):
        threading.Thread.__init__(self)
        self.str=str
    def run(self):
        print(self.str)
        
t1= MyThread('hello')
t2=MyThread('thread2sdkjbvakjfvbafvikaevb')
t1.start()
t2.start()
t1.join()
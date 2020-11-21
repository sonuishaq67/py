from threading import *
from time import *


class Theater:
    def __init__(self, str):
        self.str = str

    def movieshow(self):
        for i in range(0, 6):
            print(self.str, " : ", i)
            sleep(0.1)


obj1 = Theater('Cut ticket')
obj2 = Theater('Show Chair')

t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

t1.start()
t1.daemon
t2.start()
import threading


def display():
    print('Hello this is my thread '+threading.currentThread().getName())


for i in range(5):
    t = threading.Thread(target=display)
    t.start()

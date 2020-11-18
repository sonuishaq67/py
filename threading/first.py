import threading

print("let's find the current thread")

print('Curren thread', threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print('MAin thread running')
else:
    print('current thread isnt main thread')

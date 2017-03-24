## periodic.py
##
## A simple way to periodically call a function.
##

import time, threading
def foo():
    print(time.ctime())
    threading.Timer(1, foo).start()

foo()

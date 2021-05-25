#!/usr/bin/env python3


import threading
import time


def do(name="main"):
    for c in range(100):
        print("%s Run %d ...." % (name, c))
        time.sleep(0.5)

class Kyo(threading.Thread):
    def __init__(self, name="Kyo"):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        do(self.name)


if __name__ == "__main__":
    #  s = Kyo("KYOKYOKYO")
    #  s.start()
    t = threading.Thread(target=do, args=("Kyo", ))
    t.start()
    do()




from myro import *
from threading import Thread
import time
import globals

class Timer(Thread):

    def __init__(self):
        super(Timer, self).__init__()
        self.start_time = time.time()

    def run(self):
        while time.time() - self.start_time < 150:
            None
        globals.times_up = True
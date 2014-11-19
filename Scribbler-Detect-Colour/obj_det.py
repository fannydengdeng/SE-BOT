from myro import *
from threading import Thread

class ObjDet(Thread):

    def __init__(self):
        super(ObjDet, self).__init__()
        self.obs_found = obs()

    def run(self):
        while True:
            self.obs_found = obs()

MAX_SIDE = 1375

def obs():
        if  check(1) > MAX_SIDE:
            return True
        elif check(0) > MAX_SIDE-150:
            return True
        elif check(2) > MAX_SIDE-150:
            return True
        else:
            return False

def check(side):
        sumLeft = 0
        for count in range(0, 10):
            sumLeft += getObstacle(side)
        return sumLeft/count
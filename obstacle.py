from myro import *

def main():
	smooth()
	while True:
		if (obs()):
			turnLeft()
			move()
			turnRight()
		else:
			move()
			turnRight()
			
def obs():
	if (getObstacle(1) > 850):
		return True
	return False
		
def turnRight():
	stop()
	motors(0.8, -0.8)
	wait(1)
	stop()

def turnLeft():
	stop()
	motors(-0.8, 0.8)
	wait(1)
	stop()
	
def move():
	motors(1, 1)
	wait(0.5)
	stop

def smooth():
	while (not obs()):
		motors(1,1)
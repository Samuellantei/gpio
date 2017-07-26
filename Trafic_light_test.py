from gpiozero import LED
from time import sleep
from gpiozero import MotionSensor

motion_detector = MotionSensor(17)

led1 = LED (18)
led2 = LED (23)
led3 = LED (24)

def red_led():
	led1.on()
	sleep(10)
	led1.off()
	sleep(0)
	
def dot():
	led2.on()
	sleep(0.5)
	led2.off()
	sleep(0.5)
	
def yellow_led():
	dot()
	dot()
	dot()
	
def green_led():
	led3.on()
	sleep(1)
	led3.off()
	sleep(0)	

while motion_detector.motion_detected:
		print "Train Detected"
		yellow_led()
		print "Stop Now Train Passing"
                red_led()
else:
		print "Safe to cross"
		green_led()


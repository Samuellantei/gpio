from gpiozero import LED
from time import sleep
from gpiozero import MotionSensor

motion_detector = MotionSensor(17)

led1 = LED (18)
led2 = LED (23)
led3 = LED (24)

def red_led():
	led1.on()
	led2.off()
	led3.off()
	sleep(3)
		
def dot():
	led2.on()
	led1.off()
	led3.off()
	sleep(0.5)
	led2.off()
	sleep(0.5)
	
def yellow_led():
	dot()
	dot()
	dot()
	
def green_led():
	led3.on()
	led1.off()
	led2.off()
	
while True:
	motion_detector.wait_for_motion()
	while motion_detector.motion_detected:
		print "Train Detected"
		yellow_led()
		print "Stop Now Train Passing"
		while motion_detector.motion_detected:	
			red_led()
	print "Safe to cross"
	green_led()

#GPIO.cleanup()

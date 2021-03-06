from gpiozero import LED
from time import sleep
from gpiozero import MotionSensor
from gpiozero import LED, Button

motion_detector = MotionSensor(17)
led1 = LED (18)
led2 = LED (23)
led3 = LED (24)
button = Button(27)

def red_led():
        led1.on()
        led2.off()
        led3.off()
        sleep(10)

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

def pedestrians():
	dot()
	dot()
	print "Pedestrains crossing-Please wait"
	dot()
	dot()
	dot()
	dot()
	red_led()

button.when_pressed = pedestrians 
button.when_released = green_led

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

GPIO.cleanup()
GPIO.cleanup()
GPIO.cleanup()
GPIO.cleanup()
GPIO.cleanup()
GPIO.cleanup()
GPIO.cleanup()



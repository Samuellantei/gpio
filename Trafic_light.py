import RPi.GPIO as GPIO
import time

red_light = 18
yellow_light = 23
green_light = 24
RUNNING = True

# use gpio not the numbers
GPIO.setmode(GPIO.BCM)
# set up the gpio channels
GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(yellow_light, GPIO.OUT)
GPIO.setup(green_light, GPIO.OUT)

# We define a function to control the traffic light
def trafficState(red, yellow, green):
    GPIO.output(red_light, red)
    GPIO.output(yellow_light, yellow)
    GPIO.output(green_light, green)


print "Traffic Light Simulation. Press CTRL + C to quit"

try:
    while RUNNING:
        # Green for longer time
        trafficState(0,0,1)
        time.sleep(13)
        # Yellow for shooter time
        trafficState(0,1,0)
        time.sleep(3)
        # Red for constant till Green
        trafficState(1,0,0)
        time.sleep(10)

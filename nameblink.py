from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

def dot():
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)

def dash():
	led.on()
	sleep(0.5)
	led.off()
	sleep(1)

def E():
    dash()
    dot()
    dot()
    dash()
    
def r():
    dash()
    dot()
    dash()
    dot()

def i():
    dash()
    dot()
    dash()
    dash()

def c():
    dash()
    dot()
    dash()
    dash()

def say_my_name():
    E()
    r()
    i()
    c()

button.when_pressed = say_my_name

pause()

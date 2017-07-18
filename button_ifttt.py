from gpiozero import LED, Button
from signal import pause
import urllib2

led = LED(17)
button = Button(2)

def ifttt():
        print"done"
        urllib2.urlopen("https://maker.ifttt.com/trigger/button_press/with/key/buzlMV-GV1w2mefCNazOyd").read()

button.when_pressed = ifttt

pause()


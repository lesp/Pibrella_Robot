"""
Raspberry Pi Robot.
Using Pibrella.

Les Pounder 12th April 2014
"""

#Import libraries

import pibrella
import time
import signal

#Setup variables

speed = 5

def forward():
    pibrella.output.e.on()
    pibrella.output.f.on()
    pibrella.light.red.on()
    time.sleep(speed)
    pibrella.output.e.off()
    pibrella.output.f.off()
    pibrella.light.red.off()


#turn right

def right():
    pibrella.output.f.on()
    pibrella.light.amber.on()
    time.sleep(speed)
    pibrella.output.f.off()
    pibrella.light.amber.off()

#turn left

def left():
    pibrella.output.e.on()
    pibrella.light.green.on()
    time.sleep(speed)
    pibrella.output.e.off()
    pibrella.light.green.off()


def button_changed(pin):
    forward()
    left()
    right()

pibrella.button.changed(button_changed)

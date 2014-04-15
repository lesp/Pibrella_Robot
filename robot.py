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

turn = 4
fwd = 5

#Setup the functions to easily control our robot

def forward():
    pibrella.light.red.blink(0.5, 0.5)
    pibrella.output.e.on()
    pibrella.output.f.on()
    time.sleep(fwd)
    pibrella.output.e.off()
    pibrella.output.f.off()
    pibrella.light.red.off()

#turn right

def right():
    pibrella.output.f.on()
    pibrella.light.red.blink(0.5, 0.5)
    time.sleep(turn)
    pibrella.output.f.off()
    pibrella.light.red.off()

#turn left

def left():
    pibrella.output.e.on()
    pibrella.light.red.blink(0.5, 0.5)
    time.sleep(turn)
    pibrella.output.e.off()
    pibrella.light.red.off()
    


def demo(pin):
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    

pibrella.button.changed(demo)

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

def forward():
    pibrella.output.e.on()
    pibrella.output.f.on()
    pibrella.light.red.on()
    time.sleep(fwd)
    pibrella.output.e.off()
    pibrella.output.f.off()
    pibrella.light.red.off()


#turn right

def right():
    pibrella.output.f.on()
    pibrella.light.amber.on()
    time.sleep(turn)
    pibrella.output.f.off()
    pibrella.light.amber.off()

#turn left

def left():
    pibrella.output.e.on()
    pibrella.light.green.on()
    time.sleep(turn)
    pibrella.output.e.off()
    pibrella.light.green.off()


def demo(pin):
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    

pibrella.button.changed(demo)

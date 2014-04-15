"""
Raspberry Pi Robot.
Using Pibrella.

Les Pounder 12th April 2014
Added easygui to the program
"""

#Import libraries

import pibrella
import time
import signal
import easygui as eg

#Setup variables

turn = 2.5
fwd = 3

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

while True:
    direction = eg.buttonbox(msg='Which direction?',choices=('Left','Forward','Right'))
    if direction == 'Forward':
        forward()
    elif direction == 'Left':
        right()
    else:
        left()

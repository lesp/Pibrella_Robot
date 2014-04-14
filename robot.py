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

#Ultrasonic Sensor Setup

pibrella.output.h.on()

pibrella.output.g.on()
time.sleep(0.00001)
pibrella.output.g.off()

while pibrella.input.a.on() == 0:
    start = time.time()
while pibrella.input.a.on() == 1:
    stop = time.time()
    pibrella.input.a.off()
    pibrella.output.h.off()

elapsed = stop - start
distance = elapsed * 34000
distance = distance / 2


#Setup the functions to easily control our robot

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

import cwiid
import time
import pibrella
import signal

button_delay = 0.5
turn = 2.5
fwd = 3

def forward():
    pibrella.light.red.blink(0.5, 0.5)
    pibrella.output.e.on()
    pibrella.output.f.on()
    time.sleep(fwd)
    pibrella.output.e.off()
    pibrella.output.f.off()
    pibrella.light.red.off()

def left():
    pibrella.output.f.on()
    pibrella.light.red.blink(0.5, 0.5)
    time.sleep(turn)
    pibrella.output.f.off()
    pibrella.light.red.off()

def right():
    pibrella.output.e.on()
    pibrella.light.red.blink(0.5, 0.5)
    time.sleep(turn)
    pibrella.output.e.off()
    pibrella.light.red.off()

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']


  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    left()
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    right()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    forward()
    wii.rumble = 1
    time.sleep(button_delay)
    wii.rumble = 0
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'      
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)

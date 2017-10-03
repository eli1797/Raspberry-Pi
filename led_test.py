import RPi.GPIO as GPIO
import time

#Guided by ExplainingComputers Raspberry Pi GPIO control video

GPIO.setmode(GPIO.BOARD)
#tells RPi numbering system for the pins

GPIO.setup(7,GPIO.OUT)
#using pin 7 as an output

for x in range(0,3):
    print "LED On"
    GPIO.output(7,True)
    time.sleep(1)
    print "LED Off"
    GPIO.output(7,False)
    time.sleep(1)
GPIO.cleanup()

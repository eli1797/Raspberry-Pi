# imports (curses for keyboard control)
import curses
import RPi.GPIO as GPIO
import time

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

#Tell RPi the numbering system for the pins
GPIO.setmode(GPIO.BOARD)

#using pin 7 as an output
GPIO.setup(7,GPIO.OUT)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == ord('o'):
                GPIO.output(7,True)
            elif char == curses.KEY_UP:
                print("up")
            elif char == curses.KEY_DOWN:
                print("down")
            elif char == curses.KEY_RIGHT:
                print("right")
            elif char == curses.KEY_LEFT:
                print("left")
            elif char == 10:
                print("off")
                GPIO.output(7,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()

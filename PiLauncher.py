# getting the main GPIO library
import RPi.GPIO as GPIO
# getting the time library
import time

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warnings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 
pads = [18,17,15,14] 

#setting the mode for all pins so all will be switched on 
GPIO.setup(pads, GPIO.OUT)

def launchPad(padNo) :
    GPIO.output(padNo, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(padNo, GPIO.LOW)
    time.sleep(1)



#for loop where pin = 18 next 17 ,15, 14 
def testPads() :
    for pad in pads :
        launchPad(pad)


#cleaning all GPIO's 
GPIO.cleanup()
print "Shutdown All relays"

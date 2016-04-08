 #!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import RPi.GPIO as gpio
import time
import atexit
import sys

#gpio.setwarnings(False)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor1.setSpeed(255)
myMotor2.setSpeed(255)
myMotor3.setSpeed(255)
myMotor4.setSpeed(255)
def moveForward():
        print "Move Forward"
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor3.run(Adafruit_MotorHAT.FORWARD);
        myMotor4.run(Adafruit_MotorHAT.FORWARD);
        print "\tSpeed up..."
	for i in range(255):
		myMotor1.setSpeed(i)
                myMotor2.setSpeed(i)
                myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(100)):
		myMotor1.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)                      
		time.sleep(0.01)
def moveBackward():
        print "Move Backward"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
        print "\tSpeed up..."
	for i in range(255):
		myMotor1.setSpeed(i)
                myMotor2.setSpeed(i)
                myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(100)):
		myMotor1.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)                      
		time.sleep(0.01)
	
def turnRight():
        print "Turn Right"
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
        print "\tSpeed up..."
	for i in range(255):
		myMotor1.setSpeed(i)
                myMotor2.setSpeed(i)
                myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(100)):
		myMotor1.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)                      
		time.sleep(0.01) 
        	
def turnLeft():
        print "Turn Left"
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
 	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
        print "\tSpeed up..."
	for i in range(255):
		myMotor1.setSpeed(i)
                myMotor2.setSpeed(i)
                myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(100)):
		myMotor1.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)                      
		time.sleep(0.01)  
        	
def spinRight():
        print "Rotate Right"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	print "\tSpeed up..."
	for i in range(255):
		myMotor1.setSpeed(i)
                myMotor2.setSpeed(i)
                myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(100)):
		myMotor1.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)                      
		time.sleep(0.01)
	
def spinLeft():
        print "Rotate Left"
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	print "\tSpeed up..."
	for i in range(255):
		myMotor1.setSpeed(i)
                myMotor2.setSpeed(i)
                myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(100)):
		myMotor1.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
                myMotor4.setSpeed(i)                      
		time.sleep(0.01)
        
        
def allStop():
        print "Stop"
        myMotor1.run(Adafruit_MotorHAT.RELEASE);
        myMotor2.run(Adafruit_MotorHAT.RELEASE);
        myMotor3.run(Adafruit_MotorHAT.RELEASE);
        myMotor4.run(Adafruit_MotorHAT.RELEASE);
        time.sleep(0.01)
        


moveForward()
allStop()
moveBackward()
allStop()
turnRight()
allStop()
turnLeft()
allStop
spinRight()
allStop()
spinLeft()
allStop()

	

        

	

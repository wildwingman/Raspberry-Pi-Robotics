#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import RPi.GPIO as gpio
import time
import atexit
import sys
import Tkinter as tk

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
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor3.run(Adafruit_MotorHAT.FORWARD);
        myMotor4.run(Adafruit_MotorHAT.FORWARD);
def moveBackward():
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
def turnRight():
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
def turnLeft():
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.REALESE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
def spinRight():
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
def spinLeft():
        myMotor1.run(Adafruit_MotorHAT.Forward)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
        
        
def allStop():
        myMotor1.run(Adafruit_MotorHAT.RELEASE);
        myMotor2.run(Adafruit_MotorHAT.RELEASE);
        myMotor3.run(Adafruit_MotorHAT.RELEASE);
        myMotor4.run(Adafruit_MotorHAT.RELEASE);



while (True):
	print "Forward! "
	myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
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

	print "Release"
	myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)

	print "Backward! "
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

	print "Release"
	myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)
	
        print "Turn Right!"
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

	print "Release"
	myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)

	print "Turn Left!"
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

	print "Release"
	myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)
	


	print "Spin Right! "
	myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
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

	print "Release"
	myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)


        print "spin Left! "
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

	
        


	
	continue

       

gpio.cleanup()


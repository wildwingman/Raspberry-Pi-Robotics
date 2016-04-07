#!/usr/bin/env python
#Created By Michael D. Harris with some code examples from @CarmelitoA
#using the Adafruit DC motor Pi Hat --http://www.adafruit.com/product/2348
import pygame #for more info on keyboard events -- https://www.pygame.org/docs/ref/key.html
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor # follow the learning guide for the setup https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi
import atexit

# Default Adafruit Motor Hat i2c address
mh = Adafruit_Motor_HAT(addr=0x60) 


def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)
#setup on the Adafruit DC motor Pi Hat
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)


atexit.register(turnOffMotors)


# set the speed to 255 (max speed)
myMotor1.setSpeed(255)
myMotor2.setSpeed(255)
myMotor3.setSpeed(255)
myMotor4.setSpeed(255)
# Defineing  Motor Direction
#Moving Forward
def moveFoward():
        print "Move Forward"
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor3.run(Adafruit_MotorHAT.FORWARD);
        myMotor4.run(Adafruit_MotorHAT.FORWARD); 
        return;

#moving backward
def moveBackward():
        print "Move Backward"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
	return;

#Turn Right
def turnRight():
        print "Turn Right"
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
 	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	
	return;

#Turn turnLeft():
def turnLeft():
        print "Turn Left"
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	
	return;

#Spi Right
def rotateRight():
        print "Rotate Right"
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD) 
	return;

#Spin left
def rotateLeft():
        print "Rotate Left"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	
	return;


pygame.init()
tscreen = pygame.display.set_mode([400,400]) #this seems to work without a montior connected and also when .py is run via SSH
pygame.display.set_caption("Adafruit Motor Hat Keyboard controller")

def funcPygameKey(events):
    # Variables accessible outside this function
    global speed
    global maxSpeed
    global minSpeed
    for event in events:
        if event.type == pygame.QUIT:
        	print 'quite pygame'
        elif event.type == pygame.KEYDOWN:
            # checking if a key is pressed
            if event.key == pygame.K_w: #change the mapping if your not comfotable refer to the url for mapping - https://www.pygame.org/docs/ref/key.html
                print 'Key w -foward pressed'
                #print speed
                moveFoward()
            elif event.key == pygame.K_s:
                print 'Key s -backward pressed'
                moveBackward()
            elif event.key == pygame.K_a:
                print 'Key a -left turn pressed'
                turnLeft()
            elif event.key == pygame.K_d:
                print 'Key d -right turn pressed'
                turnRight()
            elif event.key == pygame.K_e:
                print 'Key e -Rotate Right pressed'
                rotateRight()
            elif event.key == pygame.K_q:
                print 'Key q -Rotate Right pressed'
                rotateLeft()
            
        elif event.type == pygame.KEYUP:
            # checking if a key is released
            if event.key == pygame.K_w:
                print 'Key w-Foward released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE); 
            elif event.key == pygame.K_s:
                print 'Key s-Backward released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
                
            elif event.key == pygame.K_a:
                print 'Key a -Left Turn released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_d:
                print 'Key d -Right Turn released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_q:
                print 'Key q -Rotate Left released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_e:
                print 'Key e -Rotate Right released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);     
            


try:
	print 'Program running- use your keyboard as a controller'
	while True:
		funcPygameKey(pygame.event.get())

 		time.sleep(0.05)


except KeyboardInterrupt:

	print 'you choose to exit out of the keyboard controller'


       

#!/usr/bin/python
from Adafruit_MotorHAT_Motors import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

def __init__(self):    
    releaseMotor(1)
    releaseMotor(2)
    releaseMotor(3)
    releaseMotor(4)

def releaseMotor(num):
    if (num < 1) or (num > 4):
            raise NameError('Motor must be between 1 and 4 inclusive')
    motor = mh.getMotor(num)
    motor.run(Adafruit_MotorHAT.RELEASE)

def brakeMotor(self, num):
    if (num < 1) or (num > 4):
            raise NameError('Motor must be between 1 and 4 inclusive')
    motor = mh.getMotor(num)
    motor.run(Adafruit_MotorHAT.BRAKE)

def forwardMotor(self, num):
    if (num < 1) or (num > 4):
            raise NameError('Motor must be between 1 and 4 inclusive')
    motor = mh.getMotor(num)
    motor.run(Adafruit_MotorHAT.FORWARD)

def backwardMotor(self, num):
    if (num < 1) or (num > 4):
            raise NameError('Motor must be between 1 and 4 inclusive')
    motor = mh.getMotor(num)
    motor.run(Adafruit_MotorHAT.BACKWARD)

def setMotorSpeed(self, motornum, speed):
    if (motornum < 1) or (motornum > 4):
            raise NameError('Motor must be between 1 and 4 inclusive')
    motor = mh.getMotor(motornum)
    motor.setSpeed(speed)
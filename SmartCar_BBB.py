#-*- coding:utf-8 -*-
#!/usr/bin/env python
__author__ = 'quanpower@gmail.com'

import Adafruit_BBIO.GPIO as GPIO
import time

# SET PINS
LeftMotorPin1 = "P8_7"
LeftMotorPin2 = "P8_8"
RightMotorPin1 = "P8_9"
RightMotorPin2 = "P8_10"
TrigPin = "P8_11"
EchoPin = "P8_12"

CurrDist = 0

pins = [LeftMotorPin1,LeftMotorPin2,RightMotorPin1,RightMotorPin2,TrigPin]

def setup():
    # 输出模式
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print "pin %s has been set to GPIO.OUT" % pin
    # SET PIN_12 TO INPUT
    GPIO.setup(EchoPin, GPIO.INPUT)

def forward():
    GPIO.output(LeftMotorPin1, GPIO.HIGH)
    GPIO.output(LeftMotorPin2, GPIO.LOW)
    GPIO.output(RightMotorPin1, GPIO.HIGH)
    GPIO.output(RightMotorPin2, GPIO.LOW)
    print "forward"

def backward():
    GPIO.output(LeftMotorPin1, GPIO.LOW)
    GPIO.output(LeftMotorPin2, GPIO.HIGH)
    GPIO.output(RightMotorPin1, GPIO.LOW)
    GPIO.output(RightMotorPin2, GPIO.HIGH)
    print "backward"
    time.sleep(1)

def halt():
    GPIO.output(LeftMotorPin1, GPIO.HIGH)
    GPIO.output(LeftMotorPin2, GPIO.HIGH)
    GPIO.output(RightMotorPin1, GPIO.HIGH)
    GPIO.output(RightMotorPin2, GPIO.HIGH)
    time.sleep(0.5)

def turn_left():
    GPIO.output(LeftMotorPin1, GPIO.LOW)
    GPIO.output(LeftMotorPin2, GPIO.HIGH)
    GPIO.output(RightMotorPin1, GPIO.HIGH)
    GPIO.output(RightMotorPin2, GPIO.LOW)
    print "turn left"
    time.sleep(1)
    halt()

def turn_right():
    GPIO.output(LeftMotorPin1, GPIO.HIGH)
    GPIO.output(LeftMotorPin2, GPIO.LOW)
    GPIO.output(RightMotorPin1, GPIO.LOW)
    GPIO.output(RightMotorPin2, GPIO.HIGH)
    print "turn right"
    time.sleep(1)
    halt()

def measuring_distance():
    GPIO.output(TrigPin, GPIO.LOW)
    time.sleep(0.000002)

    GPIO.output(TrigPin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin, GPIO.LOW)

    while GPIO.input(EchoPin)==0:
        start = time.time()

    while GPIO.input(EchoPin)==1:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300

    # That was the distance there and back so halve the value
    distance = distance / 2

    print "Distance : %.1f" % distance


def loop():
    while True:
        forward()
        time.sleep(1)
        backward()
        time.sleep(1)
        turn_left()
        time.sleep(1)
        turn_right()
        time.sleep(1)
        measuring_distance()

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    # 初始化GPIO
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        # 恢复GPIO口状态
        destroy()

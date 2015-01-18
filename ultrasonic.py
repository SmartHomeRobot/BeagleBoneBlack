#-*- coding:utf-8 -*-
#!/usr/bin/env python
__author__ = 'quanpower@gmail.com'

import Adafruit_BBIO.GPIO as GPIO
import time

TrigPin = "P8_11"
EchoPin = "P8_12"

def setup():
    GPIO.setup(TrigPin, GPIO.OUT)
    GPIO.setup(EchoPin, GPIO.IN)
    print "pin %s has been set to GPIO.OUT" % TrigPin
    print "pin %s has been set to GPIO.IN" % EchoPin

def measuring_distance():
    GPIO.output(TrigPin, GPIO.LOW)
    time.sleep(0.000002)
    print "pin %s has benn set to GPIO.LOW" % TrigPin
    GPIO.output(TrigPin, GPIO.HIGH)
    time.sleep(0.000015)
    print "pin %s has benn set to GPIO.HIGH" % TrigPin
    GPIO.output(TrigPin, GPIO.LOW)
    print "pin %s has benn set to GPIO.LOW" % TrigPin

    print "pin EchoPin 's GPIO.input value is %f" % GPIO.input(EchoPin)

    while not GPIO.input(EchoPin):
        pass
    start = time.time()
    print "pin EchoPin 's GPIO.input value is %f" % GPIO.input(EchoPin)
    print "start time is %s" % start

    while GPIO.input(EchoPin):
        pass
    print "pin EchoPin 's GPIO.input value is %f" % GPIO.input(EchoPin)
    stop = time.time()
    print "stop time is %s" % stop

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300

    # That was the distance there and back so halve the value
    distance = distance / 2

    print "Distance : %.1f" % distance

def destroy():
    GPIO.cleanup()

def loop():
    while True:
        measuring_distance()

if __name__ == '__main__':
    # 初始化GPIO
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        # 恢复GPIO口状态
        destroy()
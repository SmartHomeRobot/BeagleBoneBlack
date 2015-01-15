#-*- coding:utf-8 -*-
#!/usr/bin/env python
__author__ = 'quanpower@gmail.com'

import Adafruit_BBIO.GPIO as GPIO
import time

pins = ["P8_7","P8_8","P8_9","P8_10","P8_11","P8_12"]

def setup():
    # 输出模式
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print "pin %s has been set to GPIO.OUT" % pin

def forward():
    GPIO.output("P8_7", GPIO.HIGH)
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_9", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    print "forward"

def backward():
    GPIO.output("P8_7", GPIO.LOW)
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.LOW)
    GPIO.output("P8_10", GPIO.HIGH)
    print "backward"
    time.sleep(1)

def halt():
    GPIO.output("P8_7", GPIO.HIGH)
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.HIGH)
    time.sleep(0.5)

def turn_left():
    GPIO.output("P8_7", GPIO.LOW)
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    print "turn left"
    time.sleep(1)
    halt()

def turn_right():
    GPIO.output("P8_7", GPIO.HIGH)
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_9", GPIO.LOW)
    GPIO.output("P8_10", GPIO.HIGH)
    print "turn right"
    time.sleep(1)
    halt()

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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio
from time import sleep

PIN = 25
FREQ = 50
RANGE = 100

pi = pigpio.pi()

pi.set_mode(PIN, pigpio.OUTPUT)
pi.set_PWM_frequency(PIN, FREQ)
pi.set_PWM_range(PIN, RANGE)

try:
    d = 0
    r = 10
    while True:
        pi.set_PWM_dutycycle(PIN, d)
        sleep(0.1)
        d += r
        if d >= RANGE or d <= 0:
            r *= -1

except KeyboardInterrupt:
    pass

pi.set_mode(PIN, pigpio.INPUT)
pi.stop()

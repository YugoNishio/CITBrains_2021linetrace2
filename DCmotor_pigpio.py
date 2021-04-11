#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# DC Motor control with TA7291P - pigpio
 
import pigpio
import time
  
PIN1 = 19
PIN2 = 13
   
pi1 = pigpio.pi()
pi1.set_mode(PIN1, pigpio.OUTPUT)
pi1.set_mode(PIN2, pigpio.OUTPUT)
pi1.set_PWM_frequency(PIN1, 50)
pi1.set_PWM_range(PIN1, 100)
pi1.set_PWM_dutycycle(PIN1, 0)
pi1.set_PWM_frequency(PIN2, 50)
pi1.set_PWM_range(PIN2, 100)
pi1.set_PWM_dutycycle(PIN2, 0)
    
def set_motor(pi1, a, b, t):
    pi1.write(PIN1, a)
    pi1.write(PIN2, b)
    time.sleep(t)

def set_1motor_pwm(pi1, a, b, t):
    set_motor(pi1, a, b, 0.2)
    for i in range(25, 100, 25):
        pi1.set_PWM_dutycycle(PIN1, i)
        time.sleep(t)
                                    # set_motor(pi1, 0, 0, 2.0) # stop (neutral)
    set_motor(pi1, 1, 1, 2.0) # brake
    pi1.set_PWM_dutycycle(PIN1, 0)

def set_2motor_pwm(pi1, a, b, t):
    set_motor(pi1, a, b, 0.2)
    for i in range(25, 100, 25):
        pi1.set_PWM_dutycycle(PIN2, i)
        time.sleep(t)
                                        # set_motor(pi1, 0, 0, 2.0) # stop (neutral)
        set_motor(pi1, 1, 1, 2.0) # brake
        pi1.set_PWM_dutycycle(PIN2, 0)

try:
    set_motor(pi1, 0, 0, 0.5) # stop (neutral)
    set_1motor_pwm(pi1, 1, 0, 1.0) # normal rotation
    set_1motor_pwm(pi1, 1, 0, 1.0) # normal rotation
    set_2motor_pwm(pi1, 0, 1, 1.0) # reverse rotation
    set_2motor_pwm(pi1, 0, 1, 1.0) # reverse rotation
                                                                    
except KeyboardInterrupt:
    print ("done.")
                                                                         
set_motor(pi1, 0, 0, 0.5) # stop (neutral)
pi1.set_mode(PIN1, pigpio.INPUT)
pi1.set_mode(PIN2, pigpio.INPUT)
pi1.stop()

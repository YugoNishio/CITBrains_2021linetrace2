#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# DC Motor control with TA7291P - pigpio
 
import pigpio
import time
  
PIN1 = 13
PIN2 = 19
   
pi1 = pigpio.pi()
pi1.set_mode(PIN1, pigpio.OUTPUT)
pi1.set_mode(PIN2, pigpio.OUTPUT)
    
def set_motor(pi1, a, b, t):
    pi1.write(PIN1, a)
    pi1.write(PIN2, b)
    time.sleep(t)
                 
try:
    set_motor(pi1, 0, 0, 0.5) # stop (neutral)
                      
    for i in range(4):
        set_motor(pi1, 1, 0, 0.3) # normal rotation
        set_motor(pi1, 1, 1, 2.0) # brake
                                             
    for i in range(4):
        set_motor(pi1, 0, 1, 0.3) # reverse rotation
        set_motor(pi1, 1, 1, 2.0) # brake
                                                                    
except KeyboardInterrupt:
    print ("done.")
                                                                         
set_motor(pi1, 0, 0, 0.5) # stop (neutral)
pi1.set_mode(PIN1, pigpio.INPUT)
pi1.set_mode(PIN2, pigpio.INPUT)
pi1.stop()

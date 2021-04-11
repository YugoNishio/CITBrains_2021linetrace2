#coding:utf-8
import pigpio
import time
pi1 = pigpio.pi()

rPIN1 = 13
rPIN2 = 19
lPIN1 = 18
lPIN2 = 12
rline = 16
lline = 20

pi1.set_mode(rPIN1, pigpio.OUTPUT)
pi1.set_mode(rPIN2, pigpio.OUTPUT)
pi1.set_mode(lPIN1, pigpio.OUTPUT)
pi1.set_mode(lPIN2, pigpio.OUTPUT)

pi1.set_mode(rline, pigpio.INPUT)
pi1.set_mode(lline, pigpio.INPUT)

def set_rmotor(pi1,a,b,t):
  pi1.write(rPIN1,a)
  pi1.write(rPIN2,b)
  time.sleep(t)

def set_lmotor(pi1,c,d,t):
  pi1.write(lPIN1,c)
  pi1.write(lPIN2,d)
  time.sleep(t)

def set1(PIN_name):
  pi1.set_PWM_frequency(PIN_name, 1000)
  pi1.set_PWM_range(PIN_name, 255)
  pi1.set_PWM_dutycycle(PIN_name, 0)

set1(rPIN1)
set1(rPIN2)
set1(lPIN1)
set1(lPIN2)

def move_right():
  print("right")
  set_rmotor(pi1,1,0,0.2)
  set_lmotor(pi1,1,0,0.2)
  pi1.set_PWM_dutycycle(rPIN1, 170)
  pi1.set_PWM_dutycycle(rPIN2, 170)
  pi1.set_PWM_dutycycle(lPIN1, 200)
  pi1.set_PWM_dutycycle(lPIN2, 200)
  time.sleep(t)

def move_left():
  print("left")
  set_rmotor(pi1,1,0,0.2)
  set_lmotor(pi1,1,0,0.2)
  pi1.set_PWM_dutycycle(rPIN1, 200)
  pi1.set_PWM_dutycycle(rPIN2, 200)
  pi1.set_PWM_dutycycle(lPIN1, 170)
  pi1.set_PWM_dutycycle(lPIN2, 170) 
  time.sleep(t)

try:
  while True:
    set_rmotor(pi1,1,0,0.2)
    set_lmotor(pi1,1,0,0.2)
    #pi1.set_PWM_dutycycle(rPIN1, 250)
    #pi1.set_PWM_dutycycle(rPIN2, 250)
    #pi1.set_PWM_dutycycle(lPIN1, 250)
    #pi1.set_PWM_dutycycle(lPIN2, 250)
    #set_rmotor(pi1,1,0,0.2)
    #set_lmotor(pi1,1,0,0.2)
    if(pi1.read(rline)==1):
      move_left()
    if(pi1.read(lline)==1):
      move_right()
    else:
      pi1.stop()

except(KeyboardInterrupt):
  print("done.")
pi1.stop()

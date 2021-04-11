coding:utf-8
import pigpio
import time
pi1 = pigpio.pi()

rPIN1 = 13
rPIN2 = 19
lPIN1 = 18
lPIN2 = 12
rline =1
lline =3

pi1.set_mode(rPIN1,pigpio.OUTPUT)
pi1.set_mode(rPIN2,pigpio.OUTPUT)
pi1.set_mode(lPIN1,pigpio.OUTPUT)
pi1.set_mode(lPIN2,pigpio.OUTPUT)

pi1.set_mode(rline,pigpio.INPUT)
pi1.set_mode(lline,pigpio.INPUT)


def set1(PIN_name):
  pi1.set_PWM_frequency(PIN_name, 50)
  pi1.set_PWM_range(PIN_name, 255)
  pi1.set_PWM_dutycycle(PIN_name, 0)

set1(rPIN1)
set1(rPIN2)
set1(lPIN1)
set1(lPIN2)

def move_right():
  print("right")
  pi1.set_PWM_dutycycle(rPIN1, 70)
  pi1.set_PWM_dutycycle(rPIN2, 70)
  pi1.set_PWM_dutycycle(lPIN1, 100)
  pi1.set_PWM_dutycycle(lPIN2, 100)
  sleep(0.1)


def move_left():
  print("left")
  pi1.set_PWM_dutycycle(rPIN1, 100)
  pi1.set_PWM_dutycycle(rPIN2, 100)
   pi1.set_PWM_dutycycle(lPIN1, 70)
  pi1.set_PWM_dutycycle(lPIN2, 70) 
  sleep(0.1)



try:
  while True: 
    pi1.set_PWM_dutycycle(rPIN1, 50)
    pi1.set_PWM_dutycycle(rPIN2, 50)
    pi1.set_PWM_dutycycle(lPIN1, 50)
    pi1.set_PWM_dutycycle(lPIN2, 50) 
    if(pi.read(rline)==0):
      move_left()
    else if(pi.reag(lline)==0):
      move_right()
    else:
      pi1.stop()


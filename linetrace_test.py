#!/usr/bin/python
import RPi.GPIO as GPIO
#import pigpio as GPIO
import time
#pi = pigpio.pi()

GPIO.setmode(GPIO.BCM)

#--------------pin declaration--------------------
motor_pin_right = 13
motor_right_in1 = 17 
motor_right_in2 = 27
sensor_right = 22

motor_pin_left = 12
motor_left_in1 = 23
motor_left_in2 = 24
sensor_left = 9
#--------------------------------------------------

#----------------pin setup------------------------------
GPIO.setup(motor_pin_right, GPIO.OUT)
GPIO.setup(motor_right_in1, GPIO.OUT)
GPIO.setup(motor_right_in2, GPIO.OUT)
GPIO.setup(sensor_right,GPIO.IN)                                                       


GPIO.setup(motor_pin_left, GPIO.OUT)
GPIO.setup(motor_left_in1, GPIO.OUT)
GPIO.setup(motor_left_in2, GPIO.OUT)
GPIO.setup(sensor_left,GPIO.IN)
#---------------------------------------------------------

#---------------pwm object-------------------
servo_left = GPIO.PWM(motor_pin_left, 100)
servo_right = GPIO.PWM(motor_pin_right, 100)
#--------------------------------------------


#---------------------event detect-------------------------------------
GPIO.add_event_detect(sensor_left, GPIO.FALLING,bouncetime=50)
GPIO.add_event_detect(sensor_right, GPIO.FALLING,bouncetime=50)


def switch_callback_right(gpio_pin):
    print("right_falling")
    servo_right.ChangeDutyCycle(50)
    servo_left.ChangeDutyCycle(30)

def switch_callback_left(gpio_pin):
    print("left_falling")
    servo_right.ChangeDutyCycle(30)
    servo_left.ChangeDutyCycle(50)


GPIO.add_event_callback(sensor_left, switch_callback_left)     
GPIO.add_event_callback(sensor_right, switch_callback_right)   
#------------------------------------------------------------------------


#----------pwm start----------------------------

servo_right.start(30)
servo_left.start(30)
#--------------------------------------------

#-----------waiting event (main function)---------------------------

try:
    while True:
        time.sleep(0.05)
except KeyboardInterrupt:
    servo_right.stop()
    servo_left.stop()
    GPIO.cleanup()

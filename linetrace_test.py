#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#日本語を入れるとエラーが出るので使う時日本語コメントは消す

#--------------pin declaration--------------------
#ピン番号の宣言小川
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
#各ピンの設定をしている。
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
#pwmオブジェクトの宣言
servo_left = GPIO.PWM(motor_pin_left, 100)
servo_right = GPIO.PWM(motor_pin_right, 100)
#--------------------------------------------


#---------------------event detect-------------------------------------
#あるピンでイベントが発生した時に何か処理をする事を宣言
GPIO.add_event_detect(sensor_left, GPIO.FALLING,bouncetime=50)
GPIO.add_event_detect(sensor_right, GPIO.FALLING,bouncetime=50)

#呼ばれる関数の定義
def switch_callback_right(gpio_pin):
    print("right_falling")
    servo_right.ChangeDutyCycle(50)
    servo_left.ChangeDutyCycle(30)

def switch_callback_left(gpio_pin):
    print("left_falling")
    servo_right.ChangeDutyCycle(30)
    servo_left.ChangeDutyCycle(50)

#イベントが起こった時に呼ばれる関数を登録
GPIO.add_event_callback(sensor_left, switch_callback_left)     
GPIO.add_event_callback(sensor_right, switch_callback_right)   
#------------------------------------------------------------------------


#----------pwm start----------------------------
#モータの動作開始
servo_right.start(30)
servo_left.start(30)
#--------------------------------------------

#-----------waiting event (main function)---------------------------
#メイン関数の様になる部分。ここがループして上で定義したイベントが起こるのを待ち、イベントが起こったら関数を呼ぶ。
try:
    while True:
        time.sleep(0.05)
except KeyboardInterrupt:
    servo_right.stop()
    servo_left.stop()
    GPIO.cleanup()

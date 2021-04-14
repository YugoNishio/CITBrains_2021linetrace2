import pigpio
import time

sensor1=1
sensor2=3

pi=pigpio.pi()

pi.set_mode(sensor1,pigpio.OUTPUT)
pi.set_mode(sensor2,pigpio.INPUT)

def distance():
    pi.write(sensor,1)

    time.sleep(3)
    pi.write(sensor1,0)

    while pi.read(sensor2 )== 0:
        print('far')

    while pi.read(sensor2) == 1:
        print('near')

pi.stop()


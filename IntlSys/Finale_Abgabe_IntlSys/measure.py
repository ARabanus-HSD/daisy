# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
import time
import stepper
from machine import Pin
from log import logToFile


# Ultraschall senor
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

# ULN2003 stepper motor
# used pins: 26 -> IN4, 25 -> IN3, 33 -> IN2, 32 -> IN1
s1 = stepper.create(Pin(26,Pin.OUT),Pin(25,Pin.OUT),Pin(33,Pin.OUT),Pin(32,Pin.OUT), delay=2)


# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

thing = 'prisma'

angle_size = 5.625 # laut specsheet des steppers!
steps = (4075.7728395061727/8)/60
rotation_steps = 61
num_rots = 10
sensor_slot = '4'


with open(f'logfile_{thing}_meta.txt', 'a') as f:
    f.write(f'objekt: {thing}\n')
    f.write(f'measurements per rot {rotation_steps}')
    f.write(f'num rots: {num_rots}')
    # f.write(f'angle size: {angle_size}\n')
    # f.write(f'num_steps: {steps}\n')
    # f.write(f"sensor slot: {sensor_slot}\n")
    f.close()

for i in range(rotation_steps*num_rots):
    distance = str(sensor.distance_cm())
    
    print(i, distance)
    
    to_log = distance
    
    with open(f'logfile_{thing}.txt', 'a') as f:
        f.write(to_log)
        f.write("\n")
        f.close()
    
    # s1.step(2)
    s1.step(steps)
    # s1.angle(angle_size)
    # s1.angle(360,-1)
    time.sleep(0.5)
    # Begin loging to file
    
    # Stop loging to file


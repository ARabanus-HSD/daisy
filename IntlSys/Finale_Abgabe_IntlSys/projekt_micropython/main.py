# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from time import sleep
# import stepper
from machine import Pin

# Ultraschall senor
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

# ULN2003 stepper motor
import time

# used pins: 26 25 33 32
s1 = stepper.create(Pin(26,Pin.OUT),Pin(25,Pin.OUT),Pin(33,Pin.OUT),Pin(32,Pin.OUT), delay=2)


# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    
    # s1.step(1)
    # s1.step(100,-1)
    # s1.angle(1)
    # s1.angle(360,-1)
    time.sleep(0.5)
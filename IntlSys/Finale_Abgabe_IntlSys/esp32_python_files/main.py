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


steps = 72
# step_size = 2
angle_size = 5

print("Object: apple charger (ipad)")
print(f"angle_size={angle_size}")
print("distance, unit (cm)")

for i in range(steps):
    distance = sensor.distance_cm()
    
    print(i, 'd,', distance, ',\n')
    
    file = open("logfile.txt", "w")
    file.write(distance)
    file.close()
    
    # s1.step(2)
    # s1.step(100,-1)
    s1.angle(angle_size)
    # s1.angle(360,-1)
    time.sleep(1)
    # Begin loging to file
    os.dupterm(logToFile())
    
    # Stop loging to file
    os.dupterm(None)

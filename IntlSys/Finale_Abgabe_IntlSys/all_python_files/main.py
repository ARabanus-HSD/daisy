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

angle_size = 5 # degree per step
object = "apple_charger" # which object (dont use space please!)
hcsr04_distance = "" # slot in which distance sensor is located
total_num_rot = 3
measurement_number = 1
additional_param = "_" + "pulldown"

steps = total_num_rot * 360 / angle_size

print("Object: apple charger (ipad)")
print(f"angle_size={angle_size}")
print("distance, unit (cm)")

# object, angle_size, total_num_rot, hcsr04_distance
header = f"{object}, {angle_size}, {hcsr04_distance}, {total_num_rot}, {measurement_number},"

file = open(f"logfile_{object}_{angle_size}_{hcsr04_distance}_{total_num_rot}_{measurement_number}.txt", "w")
file.write(header)
file.close()

for i in range(steps):
    distance = f"{object}, {angle_size}, {hcsr04_distance}, {total_num_rot}, {measurement_number} {str(sensor.distance_cm())},"
    
    print(i, 'd,', distance)
    
    file = open("logfile.txt", "w")
    file.write(distance)
    file.close()
    
    # s1.step(2)
    # s1.step(100,-1)
    s1.angle(angle_size)
    # s1.angle(360,-1)
    time.sleep(1)

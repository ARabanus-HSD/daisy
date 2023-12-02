import machine
from time import sleep

led = machine.Pin(1, machine.Pin.OUT)

while True:
    led.ON()
    sleep(1)
    led.OFF()
    sleep(1)
# Complete project details at https://RandomNerdTutorials.com/micropython-mqtt-publish-ds18b10-esp32-esp8266/

from hcsr04 import HCSR04
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
from machine import Pin
esp.osdebug(None)
import gc

gc.collect()

ssid = 'hopscotch'
password = 'eins2drei'
mqtt_server = '192.168.191.42'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.106'

client_id = ubinascii.hexlify(machine.unique_id())

topic_pub_distance = b'esp/hcsr04/ultrasonic_distance'

last_message = 0
message_interval = 5

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

def connect_mqtt():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server)
  #client = MQTTClient(client_id, mqtt_server, user=your_username, password=your_password)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def read_sensor():
    distance = sensor.distance_cm()
    return distance

try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
      distance = read_sensor()
      print(distance)
      client.publish(topic_pub_temp, distance)
      last_message = time.time()
  except OSError as e:
    restart_and_reconnect()


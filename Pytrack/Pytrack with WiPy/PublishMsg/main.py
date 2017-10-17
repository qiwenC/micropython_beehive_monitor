import machine
import math
import network
import os
import time
import utime
import json
from machine import RTC
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS # library of the GPS
from pytrack import Pytrack
from LIS2HH12 import LIS2HH12 # library of the acceleration
from network import WLAN
from mqtt import MQTTClient # library of the MQTT

def sub_cb(topic,msg):
    print(msg)
# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect("YOUR_AP_NAME",auth=(WLAN.WPA2,"YOUR_AP_PASSWORD"),timeout = 5000)
while not wlan.isconnected():
    time.sleep_ms(50)
print("connected")

import gc
time.sleep(2)
gc.enable() # enable garbage collection

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
lis2 = LIS2HH12(py)
chrono = Timer.Chrono()
chrono.start()
#set up the mqtt client and server
client = MQTTClient(client_id ="example_client",server ="io.adafruit.com",user=
"YOUR_ADAFRUIT_USER_NAME",password = "YOUR_ADAFRUIT_AIOKEY",port =1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="YOUR_FEEDS_TOPIC") # usrname/feeds/topicname



#sd = SD()
#os.mount(sd, '/sd')
#f = open('/sd/gps-record.txt', 'w')
while (True):
    # get coordinates and accelerations
    coord = l76.coordinates()
    acc = lis2.acceleration()
    lat = str(coord[0])
    print (lat)
    lon = str(coord[1])
    print (lon)
    value = str(acc[0]) # set value as the x axis of the acceleration

    # if the coordinate connot be found, sending -1 to the adafruit.
    if lon == 'None'and lat == 'None':
        value = "-1"
        lon = ""
        lat = ""
    
    data = {
        'value' : value,
        'lon' : lon,
        'lat' : lat
    }
    print("coord: {}".format(coord))

    # convert the format from string to json
    mesg = json.dumps(data)

    # publish message
    client.publish(topic = "YOUR_FEEDS_TOPIC",msg = mesg)
    time.sleep(1)
    #f.write("{} - {}\n".format(coord, rtc.now()))
#f.close()

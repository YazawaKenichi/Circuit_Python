# L チカ
#参考 https://uepon.hatenadiary.com/entry/2021/06/10/225800

import digitalio
from board import *
import time

led = digitalio.DigitalInOut(GP25)
led.direction = digitalio.Direction.OUTPUT

while True:
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)

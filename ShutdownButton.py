#パソコンをシャットダウンするだけ
#参考：https://uepon.hatenadiary.com/entry/2021/06/10/225800

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull = digitalio.Pull.UP)
led.value = False

while True:
    if not button.value:
        led.value = True
        keyboard.send(Keycode.WINDOWS, Keycode.D)
        keyboard.send(Keycode.ALT, Keycode.F4)
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.ENTER)
        led.value = False
        time.sleep(0.1)

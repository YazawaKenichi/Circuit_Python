#パソコンをシャットダウンするだけ Ctrl Alt Del version
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
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        time.sleep(0.5)
        keyboard.send(Keycode.SHIFT, Keycode.TAB)
        time.sleep(0.5)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.5)
        keyboard.send(Keycode.DOWN)
        time.sleep(0.5)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.1)
        led.value = False

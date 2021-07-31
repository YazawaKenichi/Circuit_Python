#くぁｗせｄｒｆｔｇｙふじこｌｐを入力するだけ
#参考：https://uepon.hatenadiary.com/entry/2021/06/10/225800

import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import keyboard
from adafruit_hid.keycode import keycode

def keyInput(keycodeName):
    keyboard.send(keycodeName)

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull = digitalio.Pull.UP)
led.value = False

while True:
    if not button.value:
        led.value = True
        keyboard.send(Keycode.ALT, Keycode.GRAVE_ACCENT)
        keyInput(Keycode.Q)
        keyInput(Keycode.A)
        keyInput(Keycode.W)
        keyInput(Keycode.S)
        keyInput(Keycode.E)
        keyInput(Keycode.D)
        keyInput(Keycode.R)
        keyInput(Keycode.G)
        keyInput(Keycode.Y)
        keyInput(Keycode.H)
        keyInput(Keycode.U)
        keyInput(Keycode.J)
        keyInput(Keycode.I)
        keyInput(Keycode.K)
        keyInput(Keycode.O)
        keyInput(Keycode.L)
        keyInput(Keycode.P)
        keyboard.send(Keycode.ALT, Keycode.GRAVE_ACCENT)
        led.value = False

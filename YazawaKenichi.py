#Yazawa Kenichi を入力するだけ
#参考：https://uepon.hatenadiary.com/entry/2021/06/10/225800

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

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
        keyboard.send(Keycode.ALT, Keycode.GRAVE_ACCENT)   #日本語入力に切り替える
        keyInput(Keycode.Y)    #日本語入力するときは小文字の y で問題ない
#        keyboard.send(Keycode.SHIFT, Keycode.Y) #英語入力するときは大文字の Y にしてほしい
        keyInput(Keycode.A)
        keyInput(Keycode.Z)
        keyInput(Keycode.A)
        keyInput(Keycode.W)
        keyInput(Keycode.A)
        keyInput(Keycode.SPACE)
        keyInput(Keycode.ENTER)    #日本語入力するときは一旦変換して確定してほしい
        keyInput(Keycode.K)    #日本語入力するときは小文字の k で問題ない
#        keyboard.send(Keycode.SHIFT, Keycode.K) #英語入力するときは大文字の K にしてほしい
        keyInput(Keycode.E)
        keyInput(Keycode.N)
        keyInput(Keycode.N)    #日本語入力するときは n を二回入力してほしい
        keyInput(Keycode.I)
        keyInput(Keycode.C)
        keyInput(Keycode.H)
        keyInput(Keycode.I)
        keyInput(Keycode.SPACE)    #日本語入力するときは変換してほしい
        keyInput(Keycode.ENTER)    #日本語入力するときは確定してほしい
        keyInput(Keycode.ENTER) #最後に改行

        keyboard.send(Keycode.ALT, Keycode.GRAVE_ACCENT)
        led.value = False
        time.sleep(0.1)

#問題点：日本語入力を可能にするために ALT + GRAVE_ACCENT を実行するわけだが、
# 一瞬なりとも ALT を入力してしまうのでリボンにジャンプしてしまう場合が出てきてしまう。
# 仕方なく英語オンリーの入力をせざるを得なかった。

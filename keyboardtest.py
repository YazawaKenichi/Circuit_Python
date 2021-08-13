#暴走したときのために緊急停止ボタンをつけました。
import board
import time
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode

keyboard = Keyboard(usb_hid.devices)

"""initialize"""
# led の定義と初期化
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

i = 0

# プログラム実行開始合図
while 3 > i:
    led = True
    time.sleep(1/6)
    led = False
    time.sleep(1/6)
    i += 1

# 暴走防止
emergency = digitalio.DigitalInOut(board.GP15)
emergency.direction = digitalio.Direction.INPUT
emergency.pull = digitalio.Pull.UP

# 縦線はデータを読み取る。そのための GPIO のピンアサインをする。（列の初期化）
# GP0 が一番左の列になるように配線すればいい。
col = ([digitalio.DigitalInOut(board.GP0), 
    digitalio.DigitalInOut(board.GP1), 
    digitalio.DigitalInOut(board.GP2), 
    digitalio.DigitalInOut(board.GP3), 
    digitalio.DigitalInOut(board.GP4), 
    digitalio.DigitalInOut(board.GP5)])
i = 0
while len(col) > i:
    col[i].direction = digitalio.Direction.INPUT
    col[i].pull = digitalio.Pull.UP
    i += 1

# 横線は LOW と HIGH を入れ替える。そのための GPIO のピンアサインをする。（行の初期化）
# GP22 が一番上の行になるように配線すればいい。
lines = ([digitalio.DigitalInOut(board.GP22), 
    digitalio.DigitalInOut(board.GP21), 
    digitalio.DigitalInOut(board.GP20), 
    digitalio.DigitalInOut(board.GP19), 
    digitalio.DigitalInOut(board.GP18)])
i = 0
while len(lines) > i:
    lines[i].direction = digitalio.Direction.OUTPUT
    lines[i] = True # 全て HIGH にして初期化状態を作る
    i += 1
i = 0
j = 0

# 二次元配列の定義。全キーボードの ON OFF 状態を格納する。
# Keycode[行][列]
"""
status = ([[False, False, False, False, False, False], 
    [False, False, False, False, False, False], 
    [False, False, False, False, False, False], 
    [False, False, False, False, False, False], 
    [False, False, False, False, False, False]])
"""

# 二次元配列に対するキーコードを定義
keyarray = ([[Keycode.CAPS_LOCK, Keycode.ONE, Keycode.TWO, 
    Keycode.THREE, Keycode.FOUR, Keycode.FIVE], 
    [Keycode.TAB, Keycode.Q, Keycode.W, 
    Keycode.E, Keycode.R, Keycode.T], 
    [Keycode.CAPS_LOCK, Keycode.A, Keycode.S, 
    Keycode.D, Keycode.F, Keycode.G], 
    [Keycode.LEFT_SHIFT, Keycode.Z, Keycode.X, 
    Keycode.C, Keycode.V, Keycode.B], 
    [Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.LEFT_ALT, 
    Keycode.DELETE, Keycode.SPACE, 0]])
"""~initialize"""

"""main"""
# メイン処理
while 1:    # 実行可能になったら 1 にしろ
    while not emergency.value:
        i = 0
        j = 0
        while len(lines) > i:
            lines[i] = False    # linei+1s の電位を下げてこの行の読み取りを開始する。
            while len(col) > j:  # colj+1 の電位を読み取って状況を把握する
                if col[j].value == False:
                    keyboard.send(keyarray[i][j])   # i, j のキーコードを出力する
                j += 1
            j = 0
            lines[i] = True    # 読み取りのために下げた電位をもとにも土素
            i += 1
        time.sleep(0.075)    # チャタリング防止
    if not emergency.value:
        led = True
"""~main"""

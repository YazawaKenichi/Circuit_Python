#このプログラムを一度書き込んでしまうと、上書きできないように暴走します！絶対に実行しないでください！

import board
import time
#import usb_hid #書き込むときはここのコメントアウトをはずせ
import digitalio
#from adafruit_hid.keyboard import Keyboard #書き込むときはここのコメントアウトをはずせ
#from adafruit_hid.keyboard import Keycode  #書き込むときはここのコメントアウトをはずせ

keyboard = Keyboard(usb_hid.devices)

"""initialize"""
# led の定義と初期化
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led = False

i = 0

# プログラム実行開始合図
while 3 > i:
    led = True
    time.sleep(1/6)
    led = False
    time.sleep(1/6)
    i += 1

# 縦線はデータを読み取る。そのための GPIO のピンアサインをする。（列の初期化）
# GP0 が一番左の列になるように配線すればいい。
col = ([digitalio.DigitalInOut(board.GP0), digitalio.DigitalInOut(board.GP1),
        digitalio.DigitalInOut(board.GP2), digitalio.DigitalInOut(board.GP3),
        digitalio.DigitalInOut(board.GP4), digitalio.DigitalInOut(board.GP5)])
i = 0
while len(col) > i:
    col[i].direction = digitalio.Direction.INPUT
    col[i].pull = digitalio.Pull.UP
    i += 1

# 横線は LOW と HIGH を入れ替える。そのための GPIO のピンアサインをする。（行の初期化）
# GP22 が一番上の行になるように配線すればいい。
lines = ([digitalio.DigitalInOut(board.GP22), digitalio.DigitalInOut(board.GP21),
    digitalio.DigitalInOut(board.GP20), digitalio.DigitalInOut(board.GP19),
    digitalio.DigitalInOut(board.GP18)])
i = 0
while len(lines) > i:
    lines[i].direction = digitalio.Direction.OUTPUT
    lines[i] = True   # 全て HIGH にして初期化状態を作る
    i += 1
i = 0
j = 0

# 二次元配列の定義。全キーボードの ON OFF 状態を格納する。
# Keycode[行][列]
"""
status = ([[False, False, False, False, False, False],
[False, False, False, False, False, False], [False, False, False, False, False, False ],
[False, False, False, False, False, False ],
[False, False, False, False, False, False ]])
"""

# 二次元配列に対するキーコードを定義
keyarray = ([[Keycode.CAPS_LOCK, Keycode.ONE, Keycode.TWO,
    Keycode.THREE, Keycode.FOUR, Keycode.FIVE],
    [Keycode.TAB, Keycode.Q, Keycode.W, Keycode.E,
    Keycode.R, Keycode.T], [
    Keycode.CAPS_LOCK, Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G],
    [Keycode.LEFT_SHIFT, Keycode.Z, Keycode.X, Keycode.C,
    Keycode.V, Keycode.B], [Keycode.LEFT_CONTROL, Keycode.WINDOWS,
    Keycode.LEFT_ALT, Keycode.DELETE, Keycode.SPACE, 0]])

"""~initialize"""

"""main"""
# メイン処理
while 1:    # 実行可能になったら 1 にしろ
    i = 0
    j = 0
    while len(lines) > i:
        lines[i] = False    # linei+1s の電位を下げてこの行の読み取りを開始する。
        while len(col) > j:  # colj+1 の電位を読み取って状況を把握する
            if not col[j] == True:
                keyboard.send(keyarray[i][j])   # i, j のキーコードを出力する
            j += 1
        j = 0
        lines[i] = False    # 読み取りのために下げた電位をもとにも土素
        i += 1
    time.sleep(0.5)    # チャタリング防止
"""~main"""

import board
import time
import usb_hid
import digitalio
import math
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode

keyboard = Keyboard(usb_hid.devices)

"""initialize"""
#led の定義と初期化
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

i = 0

#プログラム実行開始合図
while 3 > i:
    led.value = True
    time.sleep(1/6)
    led.value = False
    time.sleep(1/6)
    i += 1

"""
#debug 用 LED の定義
leds = [digitalio.DigitalInOut(board.GP10), digitalio.DigitalInOut(board.GP11), digitalio.DigitalInOut(board.GP12), digitalio.DigitalInOut(board.GP13)]
i = 0
while len(leds) > i:
    leds[i].direction = digitalio.Direction.OUTPUT
    leds[i].value = 0
    i += 1
i = 0
"""

#縦線はデータを読み取る。そのための GPIO のピンアサインをする。（列の初期化）
col = [digitalio.DigitalInOut(board.GP0), digitalio.DigitalInOut(board.GP1), digitalio.DigitalInOut(board.GP2), digitalio.DigitalInOut(board.GP3), digitalio.DigitalInOut(board.GP4), digitalio.DigitalInOut(board.GP5)]
i = 0
while len(col) > i:
    col[i].switch_to_input(pull = digitalio.Pull.UP)
    i += 1

#横線は LOW と HIGH を入れ替える。そのための GPIO のピンアサインをする。（行の初期化）
lines = [digitalio.DigitalInOut(board.GP22), digitalio.DigitalInOut(board.GP21), digitalio.DigitalInOut(board.GP20), digitalio.DigitalInOut(board.GP19), digitalio.DigitalInOut(board.GP18)]
i = 0
while len(lines) > i:
    lines[i].direction = digitalio.Direction.OUTPUT
    lines[i].value = True #全て HIGH にして初期化状態を作る
    i += 1
i = 0
j = 0

#関数内かどうかを判断する変数を用意
scanning = False
linecolshifting = False

#二次元配列の定義。全キーボードの ON OFF 状態を格納する。
#status[行][列]
status = [[False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False ], [False, False, False, False, False, False ], [False, False, False, False, False, False ]]

#二次元配列に対するキーコードを定義
keyarray = [[keycode.CAPS_LOCK, keycode.ONE, keycode.TWO, keycode.THREE, keycode.FOUR, keycode.FIVE], [keycode.TAB, keycode.Q, keycode.W, keycode.E, keycode.R, keycode.T], [keycode.CAPS_LOCK, keycode.A, keycode.S, keycode.D, keycode.F, keycode.G], [keycode.LEFT_SHIFT, keycode.Z, keycode.X, keycode.C, keycode.V, keycode,B], [keycode.LEFT_CONTROL, keycode.WINDOWS, keycode.LEFT_ALT, keycode.DELETE, keycode.SPACE]]

#押下されていたキーの数をカウントする
pushcount = 0

#スレーヴに関する変数
#slave_col[10] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    #スレーヴから送られてきた各列の値を代入していく
"""~initialize"""

"""define"""
#キーをスキャンして状態を確認してキーコードを USB に置く
def linecolshift():
    i = 0
    j = 0
    linecolshifting = True
    while len(lines) > i:
        lines[i].value = 0    #linei+1s の電位を下げてこの行の読み取りを開始する。
        while len(col) > j:  #colj+1 の電位を読み取って状況を把握する
            status[i][j] = not col[j]    #colfactbuf に 6bit でキーの状態を加算していく
            if col[j] == False:
                keyboard.send(keyarray[i][j])   #i, j のキーコードを出力する
            j += 1
        j = 0
        lines[i] = 1    #読み取りのために下げた電位をもとにも土素
        i += 1
    i = 0
    j = 0
    linecolsifting = False

#キースキャンを開始する関数を用意
def keyscan():
    scanning = True
    linecolshift()  #行と列の読み取りをシフトしていく関数
    scanning = False

def slave():
    #スレーヴからのスキャン結果を取得するだけ
    hogehoge = 0
"""~define"""

"""debug define"""
"""
def debug():
    leds[0].value = True
    time.sleep(1)
    leds[0].value = False
    leds[1].value = True
    time.sleep(1)
    leds[1].value = False
    leds[2].value = True
    time.sleep(1)
    leds[2].value = False
    leds[3].value = True
    time.sleep(1)
    leds[3].value = False
"""
"""~debug define"""

"""main"""
#メイン処理
while 1:    #実行可能になったら 1 にしろ
#    debug()
    keyscan()
#    slave() #スレーヴのスキャン結果を取得する関数
    time.sleep(0.05)    #チャタリング防止
"""~main"""

#タクトスイッチを使ってオンボードの LED を点灯させる。
#参考 https://uepon.hatenadiary.com/entry/2021/06/10/225800

import board    //ラズパイボードである以上必要
import digitalio    //DigitalIO を利用するために必要

led = digitalio.DigitalInOut(board.GP25)    //led を GP25 に設定
led.direction = digitalio.Direction.OUTPUT  //GP25 を OUTPUT に設定
button = digitalio.DigitalInOut(board.GP13) //button を GP13 に設定
button.switch_to_input(pull = digitalio.Pull.Down)  //

while True:
    led.value = button.value

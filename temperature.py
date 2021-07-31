#温度を標準出力に出力する
#参考：https://hellobreak.net/raspberrypi-pico-temperature-0205/

import machine  #ADC クラスを使用するために必要
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = snesor_temp.read_u16() * conversion_factor #reading は電圧の値が入る
    temperature = 27 - (reading - 0.706) / 0.001721 #電圧をセ氏に変換する
    print(temperature)
    utime.sleep(1)

#問題：machine と utime とかいうモジュールが存在しないんだけど...
#これ CircuitPython 使ってるのが悪いんじゃね？
#UF2 で書いたら成功するか？？？

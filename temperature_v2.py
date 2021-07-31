#温度計を作ってみる
#参考：https://learn.adafruit.com/circuitpython-basics-analog-inputs-and-outputs/analog-to-digital-converter-inputs

import board
import time
import digitalio
import analogio
import busio

busio.UART(tx, rx, *, baudrate = 9600, bits = 8, parity = None, stop = 1, timeout = 1000, receiver_buffer_size = 64)
uart = busio.UART(TX, RX, baudrate = 115200)

sensor = analogio.AnalogIn(board.A4)
conversion_factor = 3.3 / 65535

while True:
    voltage = sensor.value * conversion_factor
    temperature = 27 - (voltage - 0.706) / 0.001721
    print(temperature)
    time.sleep(1)


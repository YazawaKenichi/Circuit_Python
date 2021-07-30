import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull = digitalio.Pull.UP)

while True:
    led.value = not button.value

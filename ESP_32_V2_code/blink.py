import time
import digitalio
import board

led = digitalio.DigitalInOut(board.IO48)
led.direction = digitalio.Direction.OUTPUT
while True:
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.2)

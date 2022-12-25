import time
import digitalio
import board

led = digitalio.DigitalInOut(board.IO47)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(30)
led.value = False
time.sleep(30)
import time 
import board
import digitalio
import busio
from adafruit_ms8607 import MS8607
import adafruit_adxl37x
import adafruit_lis331


led = digitalio.DigitalInOut(board.IO48)
led.direction = digitalio.Direction.OUTPUT
i2c = busio.I2C(board.IO8, board.IO7)

sensor = MS8607(i2c)
accelerometer = adafruit_adxl37x.ADXL375(i2c, 0x1d)
lis = adafruit_lis331.H3LIS331(i2c, 0x19)

while True:
    led.value = True
    time.sleep(1)
    print("\n------------------------------------------------\n")
    print("Pressure: %.2f hPa" % sensor.pressure)
    print("Temperature: %.2f C" % sensor.temperature)
    print("Humidity: %.2f %% rH" % sensor.relative_humidity)
    print("ADXL375BCCZ Acceleration %f %f %f m/s^2" % accelerometer.acceleration)
    print("H3LIS331DLTR Acceleration : X: %.2f, Y:%.2f, Z:%.2f ms^2" % lis.acceleration)
    print("\n------------------------------------------------\n")


    led.value = False
    time.sleep(1)


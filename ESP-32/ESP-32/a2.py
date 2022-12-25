import time
import board
import busio
import adafruit_lis331

i2c = busio.I2C(board.IO8, board.IO7)
# uncomment this line and comment out the one after if using the H3LIS331
lis = adafruit_lis331.H3LIS331(i2c, 0x19)
#lis = adafruit_lis331.LIS331HH(i2c)

while True:
    print("Acceleration : X: %.2f, Y:%.2f, Z:%.2f ms^2" % lis.acceleration)
    time.sleep(0.1)
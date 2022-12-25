import adafruit_sdcard
import board
import busio
import digitalio
import storage

spi = busio.SPI(board.IO12, MOSI=board.IO13, MISO=board.IO11)
cs = digitalio.DigitalInOut(board.IO1)

sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
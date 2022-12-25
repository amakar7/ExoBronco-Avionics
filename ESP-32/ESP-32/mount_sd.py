import board
import bitbangio
import adafruit_sdcard
import storage

sdcard = adafruit_sdcard(
    clock=board.IO5,
    command=board.IO6,
    data=board.IO39,
    frequency=25000000)

vfs = storage.VfsFat(sdcard)

storage.mount(vfs, "/sd")
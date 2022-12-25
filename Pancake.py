import time
from time import sleep 
import board
import digitalio
import busio
from adafruit_ms8607 import MS8607
from analogio import AnalogIn
import adafruit_adxl37x
import adafruit_lis331
import adafruit_bno055
import bitbangio
import storage
import adafruit_rfm9x
import adafruit_sdcard
import adafruit_bmp3xx

class BroncoStack:
    def __init__(self):
        #Define dictionary with all the sensors on the board
        self.hardware = {
            'IMU1':False,
            'IMU2':False,
            'BARO1':False,
            'BARO2':False,
            'ACCEL1':False,
            'ACCEL2':False,
            'GPS':False,
            'RADIO':False,
            'SD':False,
            }
        #Define I2C bus
        self.i2c = busio.I2C(board.IO9, board.IO8)

        #Define Uart
        self.UART1 = busio.UART(board.TX,board.RX,baudrate = 9600)
        
        #Define SPI for Radio
        self.spi = busio.SPI(board.IO12, MOSI=board.IO13, MISO=board.IO11)
        self.CS = digitalio.DigitalInOut(board.IO10)
        self.RESET = digitalio.DigitalInOut(board.IO21)

        #Define Radio FREQ
        self.RADIO_FREQ_MHZ = 433.0

        #Define CS pin for SDCARD
        self.cs_SD = digitalio.DigitalInOut(board.IO1)
        
        
        #Define LED
        self.led = digitalio.DigitalInOut(board.IO48)
        self.led.direction = digitalio.Direction.OUTPUT

        #Define Vbatt (Find Pin and Define it)
        self.Vbat = AnalogIn(board.IO15)

        self.Avionics_State = 'nomral'
        
        self.last_val = 0xFFFF

        
        

        
        #Init accel1
        try:
            self.ACCEL1 =adafruit_adxl37x.ADXL375(self.i2c, 0x1d)
            self.hardware['ACCEL1'] = True
        except Exception as e:
            self.debug: print("ERROR Accelerometer 1",e)
        
        #Init IMU1
        try:
            self.IMU1 = adafruit_bno055.BNO055_I2C(self.i2c)
            self.hardware['IMU1'] = True
        except Exception as e:
            self.debug: print ("ERROR IMU1",e)
        
        #Init IMU2
        try:
            self.IMU2 = adafruit_bno055.BNO055_I2C(self.i2c, 0x29)
            self.hardware['IMU2'] = True
        except Exception as e:
            self.debug: print ("ERROR IMU2",e)

        
        #Init accel2
        try:
            self.ACCEL2 =adafruit_lis331.H3LIS331(self.i2c, 0x19)
            self.hardware['ACCEL2'] = True
        except Exception as e:
            self.debug: print("ERROR Accelerometer 2",e)

        #Init baro1
        try:
            self.BARO1 = MS8607(self.i2c)
            self.hardware['BARO1'] = True
        except Exception as e:
            self.debug: print("ERROR barometer 1",e)
        
        #Init baro2
        try:
            self.BARO2 = adafruit_bmp3xx.BMP3XX_I2C(self.i2c)
            self.BARO2.pressure_oversampling = 8
            self.BARO2.temperature_oversampling = 2
            self.hardware['BARO2'] = True
        except Exception as e:
            self.debug: print("ERROR barometer 2",e)

        #Init Radio
        try:
            self.rfm9x = adafruit_rfm9x.RFM9x(self.spi, self.CS, self.RESET, self.RADIO_FREQ_MHZ)
            self.rfm9x.tx_power = 23
            self.hardware['RADIO'] = True
        except Exception as e:
            self.debug: print("ERROR Radio",e)

        #Init SD_Card
        try:
            self.sdcard= adafruit_sdcard.SDCard(self.spi, self.cs_SD)
            self.vfs = storage.VfsFat(self.sdcard)
            storage.mount(self.vfs, "/sd")
            self.fs=self.vfs
            self.logfile="/sd/log.txt"
            self.hardware['SD'] = True
        except Exception as e:
            self.debug: print("ERROR barometer 1",e)
        
        
    def pressure_B1(self):
        if self.hardware['BARO1']:
            return self.BARO1.pressure

    def pressure_B2(self):
        if self.hardware['BARO2']:
            return self.BARO2.pressure
    
    def temperature_B1(self):
        if self.hardware['BARO1']:
            return self.BARO1.temperature

    def temperature_B2(self):
        if self.hardware['BARO2']:
            return self.BARO2.temperature

    def relative_humidity_B1(self):
        if self.hardware['BARO1']:
            return self.BARO1.relative_humidity
    
    def acceleration_1(self):
        if self.hardware['ACCEL1']:
            return self.ACCEL1.acceleration

    def acceleration_2(self):
        if self.hardware['ACCEL2']:
            return self.ACCEL2.acceleration
    

    def gyro_1(self):
        if self.hardware['IMU1']:
            return self.IMU1.gyro

    def gyro_2(self):
        if self.hardware['IMU2']:
            return self.IMU2.gyro
    
    def mag_1(self):
        if self.hardware['IMU1']:
            return self.IMU1.magnetic
    
    def mag_2(self):
        if self.hardware['IMU2']:
            return self.IMU2.magnetic


    def radio_send(self,message):
        if self.hardware['RADIO']:
            self.rfm9x.send(bytes(str(message),"utf-8"))
            return

    def radio_recive(self):
        if self.hardware['RADIO']:
            self.packet = self.rfm9x.receive()
            return self.packet
    
    def SD_Write(self,data):
        with open(self.logfile, "w") as f:
            self.t = int(time.monotonic())
            f.write('{},{}\n'.format(self.t,data))
    
    def SD_Read(self):
        with open(self.logfile, "r") as f:
            print("Read line from file:")
            print(f.readline(), end='')

            
    def avionicstate(self,state):
        if 'PAD' in state:
            self.Avionics_State = 'PAD'
        if 'FLIGHT' in state:
            self.Avionics_State = 'FLIGHT'
    


pancake = BroncoStack()
        








        
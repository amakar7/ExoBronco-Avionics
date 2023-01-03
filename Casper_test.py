from PyQt5 import QtWidgets, uic
import sys
import serial.tools.list_ports
import time
import serial
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice


app = QtWidgets.QApplication([])
ui = uic.loadUi(r"C:\Users\amaka\OneDrive - Cal Poly Pomona\UMBRA\AVIONICS_Software\Casper.ui")
ui.setWindowTitle("Casper Test GUI")

serial = QSerialPort()
serial.setBaudRate(115200)
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comboBox.addItems(portList)

def onRead():
    if not serial.canReadLine(): return    
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    print(rxs)
    ui.label_19.setText(rxs)

def Open_Button():
    serial.setPortName(ui.comboBox.currentText())
    serial.open(QIODevice.ReadWrite)
    

def Close_Button():
    serial.close()

def read():
    return
 

serial.readyRead.connect(onRead)
ui.pushButton.clicked.connect(Open_Button)
ui.pushButton_2.clicked.connect(Close_Button)







ui.show()
app.exec()
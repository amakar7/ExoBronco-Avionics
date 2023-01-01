try:
  import ulab.numpy as np
except ImportError:
  import numpy as np
import time
from Pancake import pancake

error1 = 0.01
error2 = 0.01
dt = 0.04
kalmanState = 1
kalmanUncertaninty = 1

def kalman_filt(sigma,sigma_2,t,input,measurment):
  global kalmanState
  global kalmanUncertaninty 
  
  Q = np.array([[sigma*sigma,0],[0,sigma*sigma]])
  R = np.array([[sigma_2*sigma_2,0],[0,sigma_2*sigma_2]])
  A = np.array([[1,t],[0,1]])
  B = np.array([[1/2*t*t],[t]])
  u = np.array([float(input)])
  P = np.array([[]])
  z = np.array([measurment])
  H = np.array([[1,0]])

  kalmanState = A*kalmanState+B*u
  kalmanUncertaninty = A*kalmanUncertaninty*A+Q
  kalmanGain = (kalmanUncertaninty*H)/(H*kalmanUncertaninty+R)
  kalmanState = kalmanState+kalmanGain*(z-H*kalmanState)
  kalmanUncertaninty = (1-kalmanGain*H)*kalmanUncertaninty


  return kalmanState[0][0]

while True:
  i = 0
  raw_dat =str(pancake.acceleration_1())
  split_dat = raw_dat.split(",")
  Az = split_dat[2].replace(")","")
  B1_alt = float(pancake.Alt_B1())
  print(kalman_filt(error1,error2,dt,Az,B1_alt))
  print(B1_alt)
  print("------------------------------------------------")
  i = i+1
  dt = i*dt




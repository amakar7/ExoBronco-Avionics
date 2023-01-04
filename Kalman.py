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
  AccDat = pancake.acceleration_1()
  Ax = AccDat[0]
  Ay = AccDat[1]
  Az = AccDat[2]

  AnglePitch = (np.atan(Ax/(np.sqrt((Ay*Ay)+(Az*Az)))))*(180/np.pi)
  AngleRoll = (np.atan(Ay/(np.sqrt((Ax*Ax)+(Az*Az)))))*(180/np.pi)
  
  print("The pitch is: {}".format(AnglePitch))
  print("The roll is: {}".format(AngleRoll))
  print('-------------------------------------------------------')
  time.sleep(1) 



  
  





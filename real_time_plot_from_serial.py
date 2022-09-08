import serial, sys
import time
import matplotlib.pyplot as plt
from ard_serial_read_class import ard_serial_read

ard_serial=ard_serial_read()
data0=[0]*4
data=[data0]*100
ser = serial.Serial(sys.argv[1],sys.argv[2])

while True:
  try:
    array=ard_serial.read_serial(ser)
    if len(array)==4:
      data.pop(-1)
      data.insert(0,array)
      rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
      x=range(0, 100, 1)
      plt.clf()
      plt.plot(x,rez[0])
      plt.plot(x,rez[1])
      plt.plot(x,rez[2])
      plt.plot(x,rez[3])
      plt.pause(0.1)
  except KeyboardInterrupt:
    print(str(data))
    print ('exiting')
    break
exit()
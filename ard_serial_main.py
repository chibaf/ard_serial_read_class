import serial, sys
import time
from ard_serial_read_class import ard_serial_read

ard_serial=ard_serial_read()
ser = serial.Serial(sys.argv[1],sys.argv[2])

while True:
  data=ard_serial.read_serial(ser)
  print(data)

class ard_serial_read:

  def read_serial(self,ser):
    import serial
    line = ser.readline()
    while True:
      try:
        line2=line.strip().decode('utf-8')
        break
      except UnicodeDecodeError:
        continue
    data = [float(val) for val in line2.split(",")]
    return data
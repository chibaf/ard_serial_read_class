def ard_serial_sub(ser):

	import serial, sys
class ard_serial_read:

  def read_serial(self,ser):
    import serial
    line = ser.readline()
    try:
      line2=line.strip().decode('utf-8')
    except UnicodeDecodeError:
      print("decode error")
      exit()
    data = [float(val) for val in line2.split(",")]
    return data
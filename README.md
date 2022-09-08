# ard_serial_read_class
reading serial from arduino

sin4.ino: generating four sine curve and send them via serial

ard_serial_read_class.py: read serial from arduino, return data of four sine curve

ard_serial_main.py: test driver for ard_serial_read_class.py 

usage: python3 ard_serial_main.py /dev/tty.usbmodem14201 9600

real_time_plot_from_serial.py: plotting four sine curve via serial

usage: python3 real_time_plot_from_serial.py /dev/tty.usbmodem14201 9600


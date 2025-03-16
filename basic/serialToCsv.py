import serial
from csv import writer

while(1):
    with serial.Serial('/dev/tty.usbmodem11103', 115200, timeout=1) as ser:
        # x = ser.read()          # read one byte
        # s = ser.read(10)        # read up to ten bytes (timeout)
        line = ser.readline()   # read a '\n' terminated line
        line_decoded = line.decode('utf-8').strip()
        value = float(line_decoded)
        print(type(value))
        print("The Value is: ", value)
        with open('data.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([value])
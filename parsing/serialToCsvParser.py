import serial
from csv import writer


while(1):
    with serial.Serial('/dev/tty.usbmodem11103', 115200, timeout=1) as ser:


        line = ser.readline()   # read a '\n' terminated line
        line_decoded = line.decode('utf-8')

        L = [float(x) for x in line_decoded.split(', ')]
        print("\nThe values are", L) 
        with open('event.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(L)
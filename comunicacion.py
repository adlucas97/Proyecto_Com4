import serial, time
import RPi.GPIO as GPIO

arduino = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
muestra = []
while(True):
    rawString = arduino.readline()
    print(rawString) 

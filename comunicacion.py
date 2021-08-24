import serial, time
import RPi.GPIO as GPIO

arduino = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
inicio = time.time()
tiempo = 0
muestra = []
while(tiempo<5):    #toma muestras por 5 sec
    rawString = arduino.readline()
    print(rawString) 
    muestra.append(rawString)
    tiempo = time.time()-inicio

print(muestra)
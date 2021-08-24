import serial, time
# import RPi.GPIO as GPIO

arduino = serial.Serial('/dev/ttyACM0',9600)    #cambiar el string por el nombre del puerto conectado al arduino
time.sleep(2)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
inicio = time.time()
tiempo = 0
muestras = []
while(tiempo<5):    #toma muestras por 5 sec
    rawString = arduino.readline()
    print(rawString)
    muestras.append(int(rawString.decode('utf-8')))
    tiempo = time.time()-inicio

print(muestras)
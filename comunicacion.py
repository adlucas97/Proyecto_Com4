import serial, time
# import RPi.GPIO as GPIO

arduino = serial.Serial('COM8',9600)    #cambiar el string por el nombre del puerto conectado al arduino
time.sleep(2)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
inicio = time.time()
tiempo = 0
muestras = []
while(tiempo<8):    #toma muestras por 5 sec
    rawString = arduino.readline()
    print(rawString)
    muestra = int(rawString.decode('utf-8'))
    if(muestra != 0):
        muestras.append(muestra)
    tiempo = time.time()-inicio

print(muestras)
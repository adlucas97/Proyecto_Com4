import serial, time
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
# import RPi.GPIO as GPIO

arduino = serial.Serial('COM8',9600)    #cambiar el string por el nombre del puerto conectado al arduino
time.sleep(2)
print("Hablar")

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
inicio = time.time()
tiempo = 0
muestras = []
while(tiempo<5):    #toma muestras por 5 sec
    rawString = arduino.readline()
    #print(rawString)
    muestra = int(rawString.decode('utf-8', 'ignore'))
    if(muestra != 800 and muestra != 801 and muestra !=802):
        muestras.append(muestra)
    tiempo = time.time()-inicio

print(muestras)
x = np.array(muestras)
media = st.mean(x)
desviacion = st.stdev(x)
varianza = st.variance(x)
potencia = st.mean(x**2 for x in x)
magnitud = st.mean(abs(numeros) for numeros in x)
prod = np.multiply(x[0:len(x)-1], x[1:len(x)])
cruces = len(np.sort(prod[prod<800]))
#Impresión de resultados
print('Media :', media)
print('Desviacion Estandar :', desviacion)
print('Varianza :', varianza)
print('Potencia Media: ', potencia)
print('Magnitud Media: ', magnitud)
print('Cruces en 0: ', cruces)

plt.plot(x, 'g-')
plt.grid()
plt.title('Análisis de señales de voz - Primera')
plt.xlabel('Índice');
plt.ylabel('Registro');
plt.show()



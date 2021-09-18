from datetime import datetime
import serial, time
# import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


arduino = serial.Serial('/dev/ttyACM1',9600)    #cambiar el string por el nombre del puerto conectado al arduino
time.sleep(2)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
inicio = time.time()
tiempo = 0
muestras = []
x_data = []
y_data = []
muestra = 0


figure = plt.figure()
line, = plt.plot_date(x_data, y_data, '-')
# cont = 0

# def grafica(frame):
#     rawString = arduino.readline()
#     print(str(cont) + ' - ' + str(rawString))
#     if (rawString.decode != None):
#         muestra = int(rawString.decode('utf-8'))
#         x_data.append(datetime.now())
#         y_data.append(muestra)

#     line.set_data(x_data, y_data)
#     figure.gca().relim()
#     figure.gca().autoscale_view()
#     return line

# animacion = FuncAnimation(figure, grafica, interval = 20)
# plt.show()

def muestreo():
    rawString = arduino.readline()
    print(rawString)
    muestra = int(rawString.decode('utf-8')) 
    return muestra

def parametros(frame):
    x_data.append(datetime.now())
    y_data.append(muestra)
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line

while(tiempo<5):    #toma muestras por 5 sec
    # rawString = arduino.readline()
    # print(rawString)
    muestra = muestreo()
    # x_data.append(datetime.now())
    # y_data.append(muestra)
    # line.set_data(x_data, y_data)
    # figure.gca().relim()
    # figure.gca().autoscale_view() 
    if(muestra != 0):
        muestras.append(muestra)
    tiempo = time.time()-inicio
    animacion = FuncAnimation(figure, parametros)
    plt.show()
print(muestras)



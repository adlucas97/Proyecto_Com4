from datetime import datetime
import serial, time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from threading import Thread


arduino = serial.Serial('/dev/ttyACM1',9600)    #cambiar el string por el nombre del puerto conectado al arduino
time.sleep(2)

inicio = time.time()
tiempo = 0
muestras = []
x_data = []
y_data = []
muestra = 0

figure = plt.figure()
line, = plt.plot_date(x_data, y_data, '-')

cola_datos=[]

def muestreo():
    global cola_datos
    tiempo = 0
    while(True):
        rawString = arduino.readline()
        print(rawString)
        try:
            cola_datos.append(int(rawString.decode('utf-8')))
        except:
            cola_datos.append(0)
        #tiempo = time.time()-inicio

    return 'Finaliza muestreo'

f1 = Thread(target=muestreo)
f1.start()


def parametros(frame):
    global cola_datos
    try:
        muestra = cola_datos.pop(0)
    except:
        muestra = -1
    print("------------ "+ str(muestra))
    x_data.append(datetime.now())
    if(len(x_data)>=50):
        x_data.pop(0)
    y_data.append(muestra)
    line.set_data(x_data, y_data)
    figure.gca().relim(y_data)
    figure.gca().autoscale_view()
    return line



animacion = FuncAnimation(figure, parametros, interval = 1)
plt.show()

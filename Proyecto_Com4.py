from re import split
import cv2
import argparse as arg
import pytesseract
import psycopg2
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
from time import sleep
from datetime import datetime
import os
from datetime import datetime

#--------Funcion para grabar el audio y reconocimiento de voz
def Grabar_Audio():   
    r = sr.Recognizer()
    mic = sr.Microphone()
    # sr.Microphone.list_microphone_names()
    with mic as source:
        try:
            # print('Ajustando ruido ambiental')
            r.adjust_for_ambient_noise(source)
            print('Grabando audio...')
            audio = r.listen(source,timeout=4,phrase_time_limit=7)
            # audio = r.record(source, offset=0, duration=4)
            print('Audio grabado')
            data = r.recognize_google(audio, language='es-GT')
            print(f"La informacion reconocida es: {data}")
        except:
            print("Error al grabar")
            data = 'error'
    return data
    

def verificacion(str_audio):
    if ('primera' in str_audio)or ('segunda' in str_audio) or ('moderna' in str_audio) or ('pfizer' in str_audio)or ('astrazeneca' in str_audio)or ('sputnik' in str_audio):
        grabacion_correcta = True
    else:
        grabacion_correcta = False
    return(grabacion_correcta)

def verificacion(str_audio, tipo):
    meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    Dosis = ['primera','segunda']
    vacunas=['moderna','pfizer','astrazeneca', 'sputnik']
    grabacion_correcta = False
    if tipo == 'mes':
        for palabra in meses:
            if palabra in str_audio:
                grabacion_correcta = True
                return grabacion_correcta, palabra
            else:
                grabacion_correcta = False
    if tipo == 'dosis':
        for palabra in Dosis:
            if palabra in str_audio:
                grabacion_correcta = True
                return grabacion_correcta, palabra
            else:
                grabacion_correcta = False
    if tipo == 'vacuna':
        for palabra in vacunas:
            if palabra in str_audio:
                grabacion_correcta = True
                return grabacion_correcta, palabra
            else:
                grabacion_correcta = False
    else:
        return grabacion_correcta, 'x'



def reproducir_audio(texto, numero):
    print(texto)
    ruta = f'audio{str(numero)}.mp3'
    s = gTTS(texto, lang='es-us')
    s.save(ruta)
    sleep(1)
    playsound(ruta)


try:
    connection = psycopg2.connect(host = 'localhost', database = 'ProyectoCom4', user = 'postgres', password = 'Adrian3345@')
    print('Conexion exitosa')
except:
    print('fallo en conexión')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS ESQUEMA")
# cursor.execute("DROP TABLE IF EXISTS SEGUNDA_DOSIS")

Tabla_dosis1 = """CREATE TABLE ESQUEMA(
    DPI CHAR(100) PRIMARY KEY,
    NOMBRE CHAR(100) NOT NULL,
    PRIMER_APELLIDO CHAR(100) NOT NULL,
    SEGUNDO_APELLIDO CHAR(100),
    VACUNA CHAR(20),
    FECHA_DE_NACIMIENTO DATE,
    EDAD INT,
    FECHA_DE_PRIMERA_DOSIS DATE,
    FECHA_DE_segunda_DOSIS DATE     
) """
# Tabla_dosis2 = """CREATE TABLE SEGUNDA(
#     DPI CHAR(100) PRIMARY KEY,
#     NOMBRE CHAR(100) NOT NULL,
#     PRIMER_APELLIDO CHAR(100) NOT NULL,
#     SEGUNDO_APELLIDO CHAR(100),
#     EDAD INT,
#     FECHA_DE_NACIMIENTO CHAR(50),
#     FECHA_PRIMERA_DOSIS CHAR(50),
#     VACUNA CHAR(20)
# ) """
cursor.execute(Tabla_dosis1)
# cursor.execute(Tabla_dosis2)
connection.commit()

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\tesseract.exe'

image = cv2.imread("DPI_PRUEBA.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#borroso = cv2.bilateralFilter(image,5,21,51)
borroso = cv2.GaussianBlur(image, (5,5), 0)
umbral_gaussiano=cv2.adaptiveThreshold(borroso, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY_INV, 11, 4)
#umbral_gaussiano=cv2.Canny(image, 90,210)
# cv2.imshow("Original", image)
dpi = umbral_gaussiano[200:280, 0:420]
# cv2.imshow("DPI 80x420 Pixeles", DPI)
nombres = umbral_gaussiano[210:300, 450:750]
# cv2.imshow("Nombres 90x300 Pixeles", nombres)
apellidos = umbral_gaussiano[330:420, 450:750]
# cv2.imshow("Apellidos 90x300 Pixeles", apellidos)
sexo = umbral_gaussiano[530:590, 450:750]
# cv2.imshow("Sexo 60x300 Pixeles", sexo)
nacimiento = umbral_gaussiano[610:670, 450:750]
# cv2.imshow("Nacimiento 90x300 Pixeles", nacimiento)
# cv2.imshow("Umbral", umbral_gaussiano)

text_img = pytesseract.image_to_string(image)
text_adapt_thre_dpi = pytesseract.image_to_string(dpi)
DPI = text_adapt_thre_dpi.replace(' ', '' )
print(DPI)
# print(text_adapt_thre_dpi)
text_adapt_thre_nombres = pytesseract.image_to_string(nombres)
Nombres = text_adapt_thre_nombres.split()
print(Nombres)
# print(text_adapt_thre_nombres)
text_adapt_thre_apellidos = pytesseract.image_to_string(apellidos)
Apellidos = text_adapt_thre_apellidos.split()
# print(text_adapt_thre_apellidos)
text_adapt_thre_sexo = pytesseract.image_to_string(sexo)
sexo = text_adapt_thre_sexo.split()
# print(text_adapt_thre_sexo)
text_adapt_thre_nacimiento = pytesseract.image_to_string(nacimiento)
nacimiento = text_adapt_thre_nacimiento.split()
print(text_adapt_thre_nacimiento)
# print(nacimiento)
#-----------------Calculo de edad---------------------
fecha_nacimiento = nacimiento[0]
if '0CT' in fecha_nacimiento:
    fecha_nacimiento = fecha_nacimiento[0:2]+'-OCT-'+fecha_nacimiento[5:9]
    print(fecha_nacimiento)
date_nacimiento = datetime.strptime(fecha_nacimiento,'%d-%b-%Y')
print(date_nacimiento)
date_edad = str((datetime.today() - date_nacimiento)/365.25)
edad = int(date_edad[0:2])
print(edad)
print("---------------------------------------")
    
#-----------------inicio programa----------------------------------
cont_audio = 0
# while(True):
# reproducir_audio(f"Bienvenido {Nombres[0]} {Apellidos[0]}, espere en lo que se cargan sus datos al sistema", cont_audio)
# cont_audio+=1
reproducir_audio("Datos cargados. Por favor diga qué dósis se va a administrar",cont_audio)
cont_audio +=1
grabacion = Grabar_Audio()
verificado, dosis = verificacion(grabacion, 'dosis')
while(verificado == False):
    reproducir_audio("Por favor, indique nuevamente qué dosis se va a poner",cont_audio)
    cont_audio+=1
    grabacion = Grabar_Audio()
    verificado, dosis = verificacion(grabacion, 'dosis')
#-------------------------primera dosis -------------------------
if 'primera' in grabacion:
    fecha_de_vacunacion = str(datetime.today())
    fecha_de_vacunacion = fecha_de_vacunacion[0:10]
    print (fecha_de_vacunacion)
    reproducir_audio('Por favor indique qué vacuna se va a administrar',cont_audio)
    cont_audio += 1
    grabacion = Grabar_Audio()
    verificado, vacuna = verificacion(grabacion, 'vacuna')
    while(verificado == False):
        reproducir_audio("Por favor, indique nuevamente qué vacuna se va a poner", cont_audio)
        cont_audio+=1
        grabacion = Grabar_Audio()
        verificado, vacuna = verificacion(grabacion, 'vacuna')
    mesa = random.randint(1,5)
    reproducir_audio(f'por favor diríjase a la mesa {mesa} para recibir su vacuna {vacuna}', cont_audio)
    cont_audio +=1
    insertar = 'insert into public.ESQUEMA(DPI, Nombre, Primer_Apellido, Segundo_Apellido, Vacuna, Fecha_de_Nacimiento, Edad, Fecha_de_primera_dosis) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    parametros = (DPI,Nombres[0], Apellidos[0], Apellidos[1], vacuna, fecha_nacimiento,str(edad), fecha_de_vacunacion)
    cursor.execute(insertar,parametros)
    connection.commit()

    
    cursor.execute(f"select fecha_de_vacunacion from esquema where DPI = '{DPI}'")
    visualizacion = cursor.fetchall()
    visualizacion = visualizacion[0]
    visualizacion = visualizacion[0]


    
#---------------Segunda Dosis-------------------------------------------------------------
if 'segunda' in grabacion:


    reproducir_audio("Por favor indique qué vacuna se va a administrar", cont_audio)
    cont_audio+=1
    grabacion = Grabar_Audio()
    verificado = verificacion(grabacion)
    while(verificado == False):
        reproducir_audio("Por favor, indique nuevamente qué vacuna se va a poner", cont_audio)
        cont_audio+=1
        grabacion = Grabar_Audio()
        verificado = verificacion(grabacion)
    if 'moderna' in grabacion:
        mesa = random.randint(1,5)
        reproducir_audio(f'dirijase a la mesa {mesa} para recibir su vacuna de Moderna', cont_audio) 
    if 'astrazeneca' in grabacion:
        mesa = random.randint(1,5)
        reproducir_audio(f'dirijase a la mesa {mesa} para recibir su vacuna de AstraZeneca', cont_audio) 
    if 'pfizer' in grabacion:
        mesa = random.randint(1,5)
        reproducir_audio(f'dirijase a la mesa {mesa} para recibir su vacuna de Pfizer', cont_audio) 
    if 'sputnik' in grabacion:
        mesa = random.randint(1,5)
        reproducir_audio(f'dirijase a la mesa {mesa} para recibir su vacuna de sputnik', cont_audio)

for a in range (cont_audio):
    os.remove(f'audio{a}.mp3')
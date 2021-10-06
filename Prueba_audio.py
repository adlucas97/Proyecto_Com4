"""
pip install SpeechRecognition

Depencencias
pyaudio (microfono)

Idiomas soportados si se usa Google
https://cloud.google.com/speech-to-text/docs/languages
"""

from os import error
import speech_recognition as sr
import random
from time import sleep
from datetime import datetime


def Grabar_Audio():   
    r = sr.Recognizer()
    mic = sr.Microphone()
    # sr.Microphone.list_microphone_names()
    with mic as source:
        try:
            # print('Ajustando ruido ambiental')
            r.adjust_for_ambient_noise(source)
            print('Grabando audio...')
            audio = r.listen(source,timeout=3,phrase_time_limit=5)
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

# while(True):
print("Bienvenido, espere en lo que se cargan sus datos al sistema")
sleep(2)
print("Datos cargados. Por favor diga qué dósis se va a administrar")
sleep(1)
grabacion = Grabar_Audio()
verificado = verificacion(grabacion)
while(verificado == False):
    print("Por favor, indique nuevamente qué dosis se va a poner")
    grabacion = Grabar_Audio()
    verificado = verificacion(grabacion)
if 'primera' in grabacion:
    fecha_de_vacunacion = datetime.today()
    print('Por favor indique qué vacuna se va a administrar')
    grabacion = Grabar_Audio()
    verificado = verificacion(grabacion)
    while(verificado == False):
        print("Por favor, indique nuevamente qué vacuna se va a poner")
        grabacion = Grabar_Audio()
        verificado = verificacion(grabacion)
    if 'moderna' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de Moderna') 
    if 'astrazeneca' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de AstraZeneca') 
    if 'pfizer' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de Pfizer') 
    if 'sputnik' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de sputnik') 
if 'segunda' in grabacion:
    grabacion = Grabar_Audio()
    verificado = verificacion(grabacion)
    while(verificado == False):
        print("Por favor, indique nuevamente qué vacuna se va a poner")
        grabacion = Grabar_Audio()
        verificado = verificacion(grabacion)
    if 'moderna' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de Moderna') 
    if 'astrazeneca' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de AstraZeneca') 
    if 'pfizer' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de Pfizer') 
    if 'sputnik' in grabacion:
        mesa = random.randint(1,5)
        print(f'dirijase a la mesa {mesa} para recibir su vacuna de sputnik')




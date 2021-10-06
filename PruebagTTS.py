from gtts import gTTS
from playsound import playsound

mesa =5
texto = "Bienvenido Francisco Hernández, su vacuna es pfizer"
s = gTTS(texto, lang='es-us')
s.save('audio.mp3')
playsound('audio.mp3')
from PIL import Image
import pytesseract

img = Image.open('/home/pi/Documents/Proyecto_Com4/Pruebas/fotos/pruebas/dpi2.jpeg')
text = pytesseract.image_to_string(img)
print(text)
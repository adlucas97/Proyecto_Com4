import cv2
import argparse as arg
import pytesseract


cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
leido, frame = cap.read()

if leido == True:
    cv2.imwrite("foto.jpg", frame)
    print("Foto tomada correctamente")
else:
    print("Error al acceder a la cámara")

"""
    Finalmente liberamos o soltamos la cámara
"""
# cap.release()



# if(leido):
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\tesseract.exe'

image = cv2.imread("foto.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#borroso = cv2.bilateralFilter(image,5,21,51)
borroso = cv2.GaussianBlur(image, (7,7), 0)
umbral_gaussiano=cv2.adaptiveThreshold(borroso, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY_INV, 11, 4)
#umbral_gaussiano=cv2.Canny(image, 90,210)
cv2.imshow("Original", image)
DPI = umbral_gaussiano[200:280, 0:420]
cv2.imshow("DPI 80x420 Pixeles", DPI)
nombres = umbral_gaussiano[210:300, 450:750]
cv2.imshow("Nombres 90x300 Pixeles", nombres)
apellidos = umbral_gaussiano[330:420, 450:750]
cv2.imshow("Apellidos 90x300 Pixeles", apellidos)
sexo = umbral_gaussiano[530:590, 450:750]
cv2.imshow("Sexo 60x300 Pixeles", sexo)
nacimiento = umbral_gaussiano[610:670, 450:750]
cv2.imshow("Nacimiento 90x300 Pixeles", nacimiento)
cv2.imshow("Umbral", umbral_gaussiano)

text_img = pytesseract.image_to_string(image)
text_adapt_thre_dpi = pytesseract.image_to_string(DPI)
print(text_adapt_thre_dpi)
text_adapt_thre_nombres = pytesseract.image_to_string(nombres)
print(text_adapt_thre_nombres)
text_adapt_thre_apellidos = pytesseract.image_to_string(apellidos)
print(text_adapt_thre_apellidos)
text_adapt_thre_sexo = pytesseract.image_to_string(sexo)
print(text_adapt_thre_sexo)
text_adapt_thre_nacimiento = pytesseract.image_to_string(nacimiento)
print(text_adapt_thre_nacimiento)

cv2.waitKey(0)
# else:
# print("Error")


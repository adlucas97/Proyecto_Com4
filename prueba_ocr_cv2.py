import cv2
import numpy as np
import pytesseract

img = cv2.imread("/home/pi/Documents/Proyecto_Com4/Pruebas/fotos/pruebas/dpi1.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, None, fx=2.5, fy=2.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,53,23)

text_img = pytesseract.image_to_string(img)
text_gray = pytesseract.image_to_string(gray)
text_adapt_thre = pytesseract.image_to_string(adaptive_threshold)

print('--------------------------------------------img----------------------------')
print(text_img)
print('--------------------------------------------gray----------------------------')
print(text_gray)
print('--------------------------------------------adaptive threshold----------------------------')
print(text_adapt_thre)

# cv2.imshow("Img",img)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("adapt_thre",adaptive_threshold)
cv2.waitKey(0)
import cv2
import argparse as arg
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ap = arg.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
borroso = cv2.GaussianBlur(image, (5,5), 0)
umbral_gaussiano=cv2.adaptiveThreshold(borroso, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY_INV, 11, 4)
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
#cv2.imshow("Original", image)

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

#height_img,width_img= DPI.shape

#boxes = pytesseract.image_to_boxes(nombres)
#for b in boxes.splitlines():
#    print(b[0])
#    b = b.split(' ')
#    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#    cv2.rectangle(nombres,(x,height_img-y),(w,height_img-h),(0,0,255),4)


# cv2.imshow("Img",img)
#cv2.imshow("img",DPI)
# cv2.imshow("gray",gray)
# cv2.imshow("adapt_thre",adaptive_threshold)
cv2.waitKey(0)


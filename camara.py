from picamera import PiCamera
from time import sleep
import cv2

camera = PiCamera()
camera.start_preview(alpha = 192)
sleep(5)
camera.capture("/home/pi/Desktop/pic.jpg")
camera.stop_preview()

img = cv2.imread("/home/pi/Desktop/pic.jpg")
cv2.imshow("IMG",img)
cv2.waitKey(0)
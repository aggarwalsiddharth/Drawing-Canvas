import cv2
import numpy as np

def nothing(self):
    pass


img = np.zeros((50,750,3),np.uint8)
cv2.namedWindow('Color')
cv2.createTrackbar('RED','Color',0,255,nothing)
cv2.createTrackbar('GREEN','Color',0,255,nothing)
cv2.createTrackbar('BLUE','Color',0,255,nothing)

canvas = np.ones((750,750,3),np.uint8)*255
pressed = False
radius = 2
def click(event,x,y,flags,param):
    global canvas,pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas,(x,y),radius,colour,-1)
    
    if event == cv2.EVENT_MOUSEMOVE and pressed==True:
        cv2.circle(canvas,(x,y),radius,colour,-1)
    
    if event == cv2.EVENT_LBUTTONUP:
        pressed=False
cv2.namedWindow('Drawing Canvas')
cv2.setMouseCallback('Drawing Canvas',click)
while True:
    cv2.imshow('Drawing Canvas',canvas)
    cv2.imshow('Color',img)
    r = cv2.getTrackbarPos('RED','Color')
    g = cv2.getTrackbarPos('GREEN','Color')
    b = cv2.getTrackbarPos('BLUE','Color')
    colour = (r,g,b)
    
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()


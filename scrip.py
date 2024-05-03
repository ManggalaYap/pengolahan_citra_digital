import cv2 

load = cv2.imread('sasuke.jpg', 1)
width, height = load.shape[1], load.shape[0]

rotate = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
img_rotate = cv2.warpAffine(load, rotate, (width, height))

cv2.imshow('Image Rotate', img_rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
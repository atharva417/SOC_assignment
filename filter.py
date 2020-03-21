import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
img = cv2.imread('apple.jpg',cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([150,150,0])
upper_red = np.array([180,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('applefilter.png',res)

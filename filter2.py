import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
img = cv2.imread('test1.jpg',cv2.IMREAD_COLOR)
img[:,:,2] = 0
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('applefilter2.png',img)

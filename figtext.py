import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
img = cv2.imread('test1.jpg',cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (100,100), (255,0,0), 10)
cv2.rectangle(img, (15,25), (150,100), (0,255,255),5)
cv2.circle(img,(200,300), 55, (255,255,0), -1)
font= cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'SOC', (0,130), font, 1, (150,255,255), 5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test1figtext.png', img)

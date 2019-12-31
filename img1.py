import cv2
import matplotlib.pyplot as plt 
import numpy as np 
img=cv2.imread('/Users/vamshikrishna/Downloads/road.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

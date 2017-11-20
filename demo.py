import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/apple/Desktop/banner.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
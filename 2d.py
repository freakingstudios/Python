import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('image.jpg',0)

# Create a depth map using the Sobel filter
depth = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)

# Normalize the depth map
depth_norm = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)

# Apply the depth map to the original image
img_3d = np.dstack((img, depth_norm, np.zeros_like(depth_norm)))

# Display the original and 3D image
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_3d)
plt.title('3D Image'), plt.xticks([]), plt.yticks([])
plt.show()

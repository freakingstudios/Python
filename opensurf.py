import cv2

# Load the image
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create the OpenSURF object
#surf = cv2.xfeatures2d.SURF_create()

sift = cv2.xfeatures2d.SIFT_create()
# Detect keypoints and descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw the keypoints on the image
img = cv2.drawKeypoints(gray, keypoints, img)

# Show the image with keypoints
cv2.imshow("Image", img)
cv2.waitKey(0)

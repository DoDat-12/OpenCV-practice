# TODO: CV2 BASIC FUNCTIONS
import cv2
import numpy as np

print("Package Imported")

img = cv2.imread("../Resources/DoDatLogo1.png")

# convert image into grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur image
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)

# edge detector - canny edge detector
# Find the edges in the image
imgCanny = cv2.Canny(img, 100, 100)

# define the kernel
kernel = np.ones((5, 5), np.uint8)
# np.uint8 - unsigned int 8 - color value from 0 to 255

# increase the thickness of the edges
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# The kernel need to import numpy
# iterations - the thickness

# make the edges thinner
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
# the bigger iterations, the thinner the edge

# show images
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
# TODO: RESIZING AND CROPPING
# OpenCV convention
# trục Oxy - Ox như cũ, Oy ngược xuống dưới
# O (0, 0) at the top left
import cv2

img = cv2.imread("../Resources/DoDatLogo1.png")

# find the size of the image
print(img.shape)
# Result (500, 500, 3) - (height, width, 3 means BGR)
# BGR - Blue, Green, Red

# TODO: RESIZING
imgResize = cv2.resize(img, (300, 300))
# (300, 300) - (width, height)
print(imgResize.shape)

# TODO: CROPPING
# image is just matrix or an array of pixels
# img has shape (500, 500)
imgCropped = img[0:300, 200:400]
# [0:300, 200:500] means
# height from 0 to 300
# width from 200 to 500

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
# TODO: WARP PERSPECTIVE
import cv2
import numpy as np

img = cv2.imread("../Resources/cards.jpg")

width, height = 250, 350

# define 4 corner points of the card
pts1 = np.float32([[26, 328], [228, 273], [319, 575], [146, 662]])

# define which corner we are referring to
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

# define the transformation matrix required for the perspective
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)
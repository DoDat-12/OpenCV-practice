# TODO: SHAPES AND TEXTS - HOW TO DRAW OR ADD TEXTS ON IMAGE
import cv2
import numpy as np

img = np.zeros((200, 200, 3), np.uint8)
# zero - 0 means black
# 200, 200 is height, width, 3 means BGR
# np.unit8 - unsigned int 8 - value from 0 to 255

# coloring image
img[:] = (100, 0, 0)
# [:] - same with crop in chapter03
# [:] means full range

# drawing line
# (image, starting point, ending point, color, thickness)
cv2.line(img, (50, 50), (100, 100), (0, 255, 0), 2)
# (50, 50) - width, height

# drawing rectangle
cv2.rectangle(img, (0, 0), (70, 30), (0, 0, 255), 1)
# fill the rectangle - REPLACE 1 WITH CV2.FILLED

cv2.circle(img, (150, 150), 10, (255, 255, 0), cv2.FILLED)
# (image, center point, radius, color, thickness

cv2.putText(img, "OpenCV", (20, 150), cv2.FONT_HERSHEY_PLAIN, 2, (0, 150, 0), 2)
# (image, string, starting location, font, scale, color, thickness)

# check size
print(img.shape)
print(img)

cv2.imshow("Image", img)
cv2.waitKey(0)

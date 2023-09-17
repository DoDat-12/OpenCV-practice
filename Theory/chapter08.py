# TODO: CONTOURS/SHAPE DETECTION
# https://youtu.be/WQeoO7MI0Bs?t=4539
# define what is the shape of the object

import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
# Stack Image function in chapter 6

def getContours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.RETR_EXTERNAL
    # it retrieves the extreme outer contours
    # there are other alternatives that will detect all the contours they will not be filtered out
    # this one is specifically good if you want to find the outer details the outer corners
    # cv2.CHAIN_APPROX_NONE - get full contours
    for cnt in contours:
        # find the area of the cnt
        area = cv2.contourArea(cnt)
        # print(area)
        # draw

        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
            # area < 500 -> no draw
            # calculate the curve length - help us approximate the corner of our shape
            peri = cv2.arcLength(cnt, True)
            # closed = True - đường kín
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # approximate the corner point, how many corner points we have
            print(len(approx))
            # give us each point of corner
            objCor = len(approx)
            x, y, width, height = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                apsRatio = width/float(height)
                if 0.95 < apsRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imgContour, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x + width//2 - 10, y + height//2 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)
            # // là / sau đó làm tròn


path = "../Resources/shapes.jpg"
img = cv2.imread(path)
imgContour = img.copy()

# pre-process the image
# convert it into gray scale + find the edge
# find the corner point
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

getContours(imgCanny)

# cv2.imshow("Original", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
imgStack = stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv2.imshow("Stack", imgStack)
cv2.waitKey(0)


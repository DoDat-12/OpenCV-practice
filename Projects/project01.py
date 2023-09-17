# PROJECT 1 - VIRTUAL PAINT
# TODO: Find color, using webcam, place points wherever we find our colors to create the paint example
# Setting up webcam - chapter01.py
# Finding color - chapter07.py
# Detect object - chapter08.py

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# FIRST - DETECT THE COLOR

# this list just detect for yellow
myColors = [[15, 136, 216, 40, 255, 255]]
# Hue Min, Sat Min, Val Min, Hue Max, Sat Max, Val Max

myColorValues = [[28, 165, 255]]
# BGR

myPoints = []
# [x, y, colorId]
def findColor(image, Colors, ColorValues):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    count = 0
    newPoint = []
    for color in Colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, ColorValues[count], cv2.FILLED)
        # cv2.imshow("Img", mask)
        if x != 0 and y != 0:
            newPoint.append([x, y, count])
        count += 1
    return newPoint

# SECOND - DETECT THE OBJECT THAT WE FOUND COLOR
# get our contours

def getContours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, width, height = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, width, height = cv2.boundingRect(approx)
    return x + width//2, y
    # return the location

def drawOnCanvas(Points, ColorValue):
    for point in Points:
        cv2.circle(imgResult, (point[0], point[1]), 10, ColorValue[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
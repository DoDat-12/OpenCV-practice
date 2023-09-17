# TODO: READ IMAGES - VIDEOS - WEBCAM
import cv2

# cv2 stands for computer vision
print("Package Imported")

# TODO: IMPORT AN IMAGE

# img = cv2.imread("Resources/DoDatThumbnail1.png")
# function imread() to read an image and return to variable img

# cv2.imshow("Output", img)
# function imshow() to display image
# first argument is the name of the window
# second argument defines which image we want to show

# cv2.waitKey(0)
# function waitKey() - add delay time (millisecond), so we can see the image before it disappears
# 0 means infinite delay

# TODO: IMPORT A VIDEO

# cap = cv2.VideoCapture("Resources/whiplash.mp4")

# video is just a sequence of images -> need while loop
# while True:
#     success, img = cap.read()
# save image in the variable img and then tell us whether it was done successfully or not
# success is a boolean variable

#     cv2.imshow("Video", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# add delay and look for the word 'q' type on keyboard to break the loop
# if video is short and end before press 1, it will automatically turn off

# TODO: Using Web-Cam

cap = cv2.VideoCapture(0)
# 0 - it will use the default webcam
# If you have another webcam, type in the ID
# cap - a webcam object

# define the size of camera
cap.set(3, 640)
# define the height with id 3
cap.set(4, 480)
# define the width with id 4
cap.set(10, 100)
# define the brightness with id 10

while True:
    success, img = cap.read()
    cv2.imshow("Webcam Pro Vip", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
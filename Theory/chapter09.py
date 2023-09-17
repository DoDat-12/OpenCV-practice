# TODO: FACE DETECTION
# method using - VIOLA & JONES
# to detect faces, we need to collect lots of
#   positives - faces
#   negatives - non faces
# using positives and negatives to train and create a cascade file (XML file) that helps us find faces
# in this course we use a pretend file for faces provided by OpenCV

# OPENCV CASCADES - detect different things such as eyes, full body, ...

import cv2

# add cascade
faceCascade = cv2.CascadeClassifier("../Resources/haarcascade_frontalface_default.xml")

# read image
img = cv2.imread("../Resources/peaky.jpg")
# convert image into gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.13, 5)
# 1.13 - scaleFactor - Là hệ số thu phóng được sử dụng để thu nhỏ hình ảnh trước khi phát hiện khuôn mặt.
# 5 - the minimum neighbors - Là số hàng xóm tối thiểu được yêu cầu để xác nhận một khu vực là khuôn mặt.
# minimum neighbors càng cao thì càng chính xác nhưng tốc độ sẽ chậm đi

# create bounding box on the faces
for (x, y, width, height) in faces:
    cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
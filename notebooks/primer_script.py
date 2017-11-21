import cv2
import matplotlib.pyplot as lt

img = cv2.imread('curl.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT()
kp, des = sift.detectAndCompute(gray, None)

lt.imshow(cv2.drawKeypoints(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), kp))
lt.show()
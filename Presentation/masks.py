import numpy as np
import os, sys, time
import cv2
import utils.drawmatches

# Add the root path (the path above this one) to the pythonpath.
sys.path.insert(0, '../')

from utils.drawmatches import drawMatches

# Read images
im1 = cv2.imread('../FotosConMarcos/168-2743-15592gaussiano.jpg')
im2 = cv2.imread('../FotosConMarcos/28661-18003-19405gaussiano.jpg')

print np.shape(im1), np.shape(im2)

# Initialize SIFT detector
sift = cv2.SIFT()

keypoints1, descriptors1 = sift.detectAndCompute(im1, None)
keypoints2, descriptors2 = sift.detectAndCompute(im2, None)

print np.shape(keypoints1), np.shape(keypoints2)

# Display keypoints on images
cv2.imshow('Image', cv2.drawKeypoints(im1, keypoints1))
cv2.waitKey(0)
cv2.imshow('Image', cv2.drawKeypoints(im2, keypoints2))
cv2.waitKey(0)

# Going further: Matching keypoints from the two images

bf = cv2.BFMatcher()
matches = bf.match(descriptors1, descriptors2)
matches = sorted(matches, key=lambda val: val.distance)

print len(matches)

# Show the matches
out = drawMatches(cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY), keypoints1, cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY), keypoints2, matches[:20])
cv2.imwrite('matches.jpg', out)
cv2.imshow('Image', out)
cv2.waitKey(0)

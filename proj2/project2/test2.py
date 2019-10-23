import cv2
import numpy
import math
leftimage = cv2.imread('right.jpg')
rightimage = cv2.imread('left.jpg')
newimage = leftimage
img1keypoints, des1 = cv2.xfeatures2d.SIFT_create().detectAndCompute(leftimage,None)
img2keypoints, des2 = cv2.xfeatures2d.SIFT_create().detectAndCompute(rightimage,None)


matches = cv2.BFMatcher().knnMatch(des1,des2,2)

valid = 0
hits = []
orig = []
dest = []
print(len(newimage[0]))
for leftpoint,rightpoint in matches:
    if leftpoint.distance < rightpoint.distance:
        valid = valid + 1
        hits.append(leftpoint)
count = 0
count2 = -1
imagesize = len(newimage[0])
print("imagesize," ,imagesize)
while count2 < len(leftimage) - 1:
    count = 0
    count2 = count2 + 1
    newimage = numpy.resize(newimage[count2],imagesize * 2)


# count = 0
# count2 = -1
# while count2 < len(leftimage) - 1:
#     count = 0
#     count2 = count2 + 1
#
#     while count < len(leftimage) - 1:
#         count  = count + 1
#         # print(1)
#         numpy.append(newimage[count2],newimage[count2])
# print(len(newimage[0]))
# numpy.resize(newimage[0],len(newimage[0]) * 2)
# print(len(newimage[0]))
# print(len(newimage[0]))
if valid > 1:
    for pixel in hits:
        orig.append(img1keypoints[pixel.queryIdx].pt)
        dest.append(img2keypoints[pixel.trainIdx].pt )

    orig = numpy.float32(orig)
    dest = numpy.float32(dest)
    M, mask = cv2.findHomography(orig, dest, cv2.RANSAC, 5.0)
    print(leftimage.shape)
    h,w,c = leftimage.shape

    newimage = cv2.warpPerspective(leftimage,M,(leftimage.shape[1] + w, leftimage.shape[0] ))


    newimage[0:leftimage.shape[0],0:leftimage.shape[1]] = rightimage
    cv2.imwrite("resultimage.jpg", newimage)
else:
    print("no match")

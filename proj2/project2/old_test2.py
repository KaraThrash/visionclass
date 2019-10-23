import cv2
import numpy as np
import math
leftimage = cv2.imread('right.jpg')

# leftimage = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)
rightimage = cv2.imread('left.jpg')

# rightimage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = cv2.xfeatures2d.SIFT_create().detectAndCompute(leftimage,None)
kp2, des2 = cv2.xfeatures2d.SIFT_create().detectAndCompute(rightimage,None)
# gray= cv2.cvtColor(leftimage,cv2.COLOR_BGR2GRAY)
# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)
# img=cv2.drawKeypoints(gray,kp,leftimage,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imwrite('sift_keypoints.jpg',img)

matches = cv2.BFMatcher().knnMatch(des1,des2,k=2)
good = []
for m,n in matches:
    if m.distance < 0.4*n.distance:
        good.append(m)

if len(good) > 10:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ])
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ])
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    print(leftimage.shape)
    h,w,c = leftimage.shape

    dst = cv2.warpPerspective(leftimage,M,(leftimage.shape[1] + w, leftimage.shape[0] ))


    dst[0:leftimage.shape[0],0:leftimage.shape[1]] = rightimage
    cv2.imwrite("original_image_stitched.jpg", dst)
else:
    print("Not enought matches are found - %d/%d", (len(good)/MIN_MATCH_COUNT))

"""
Image Stitching Problem
(Due date: Oct. 23, 3 P.M., 2019)
The goal of this task is to stitch two images of overlap into one image.
To this end, you need to find feature points of interest in one image, and then find
the corresponding ones in another image. After this, you can simply stitch the two images
by aligning the matched feature points.
For simplicity, the input two images are only clipped along the horizontal direction, which
means you only need to find the corresponding features in the same rows to achieve image stiching.

Do NOT modify the code provided to you.
You are allowed use APIs provided by numpy and opencv, except cv2.findHomography() and
APIs that have stitch, Stitch, match or Match in their names, e.g., cv2.BFMatcher() and
cv2.Stitcher.create().
"""
import cv2
import numpy as np
import random

def solution(left_img, right_img):
    """
    :param left_img:
    :param right_img:
    :return: you need to return the result image which is stitched by left_img and right_img
    """

    img1keypoints, des1 = cv2.xfeatures2d.SIFT_create().detectAndCompute(left_img,None)
    img2keypoints, des2 = cv2.xfeatures2d.SIFT_create().detectAndCompute(right_img,None)
    newimage = left_img 

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
    # imagesize = len(newimage[0])
    # print("imagesize," ,imagesize)
    while count2 < len(left_img) - 1:
        count = 0
        count2 = count2 + 1
        # newimage = np.resize(newimage[count2],imagesize * 2)


    # count = 0
    # count2 = -1
    # while count2 < len(left_img) - 1:
    #     count = 0
    #     count2 = count2 + 1
    #
    #     while count < len(left_img) - 1:
    #         count  = count + 1
    #         # print(1)
    #         np.append(newimage[count2],newimage[count2])
    # print(len(newimage[0]))
    # np.resize(newimage[0],len(newimage[0]) * 2)
    # print(len(newimage[0]))
    # print(len(newimage[0]))
    if valid > 1:
        for pixel in hits:
            orig.append(img1keypoints[pixel.queryIdx].pt)
            dest.append(img2keypoints[pixel.trainIdx].pt)

        orig = np.float32(orig)
        dest = np.float32(dest)
        M, mask = cv2.findHomography(orig, dest, cv2.RANSAC, 5.0)
        print(left_img.shape)
        h,w,c = left_img.shape

        newimage = cv2.warpPerspective(left_img,M,(left_img.shape[1] + w, left_img.shape[0] ))


        newimage[0:left_img.shape[0],0:left_img.shape[1]] = right_img

    else:
        print("no match")
    return newimage
    # raise NotImplementedError

if __name__ == "__main__":
    left_img = cv2.imread('left.jpg')
    right_img = cv2.imread('right.jpg')
    result_image = solution(left_img, right_img)
    cv2.imwrite('results/task2_result.jpg',result_image)

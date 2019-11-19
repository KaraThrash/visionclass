"""
Denoise Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to denoise image using median filter.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint:
Please complete all the functions that are labeled with '#to do'.
You are suggested to use utils.zero_pad.
"""

import math
import utils
import numpy as np
import json
import cv2
from matplotlib import pyplot as plt
def median_filter(img):
    """
    Implement median filter on the given image.
    Steps:
    (1) Pad the image with zero to ensure that the output is of the same size as the input image.
    (2) Calculate the filtered image.
    Arg: Input image.
    Return: Filtered image.
    """
    # TODO: implement this function.
    # paddedimg = utils.zero_pad(img,len(img[0]),len(img))
    count = len(img[0])
    padrow = []
    padrow2 = []
    paddedimg = []
    padrow.append(0)
    padrow2.append(0)
    padrow.append(0)
    padrow2.append(0)
    while count > 0:
        padrow.append(0)
        padrow2.append(0)
        count = count - 1
    paddedimg.append(padrow)
    for row in img:
        newrow = []
        newrow.append(0)
        paddedimg.append(newrow)

        for pixel in row:
            newpixel = pixel
            newrow.append(newpixel)
        newrow.append(0)
    paddedimg.append(padrow2)

    denoiseimg = img
    rowcount = -1
    colcount = -1

    for row in img:
        denoiserow = []
        # denoiseimg.append(denoiserow)
        rowcount = rowcount + 1
        colcount = -1
        for pixel in row:
            colcount = colcount + 1
            pixelavg = 0
            pixelavgcount = 0
            pixelavg = pixelavg + paddedimg[rowcount ][colcount ]
            pixelavg = pixelavg + paddedimg[rowcount ][colcount + 1]
            pixelavg = pixelavg + paddedimg[rowcount ][colcount + 2]
            pixelavg = pixelavg + paddedimg[rowcount + 1][colcount ]
            pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 1]
            pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 2]
            pixelavg = pixelavg + paddedimg[rowcount + 2][colcount ]
            pixelavg = pixelavg + paddedimg[rowcount + 2][colcount + 1]
            pixelavg = pixelavg + paddedimg[rowcount + 2][colcount + 2]
            # pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 1]

            if paddedimg[rowcount ][colcount ] != 0:
                pixelavgcount = pixelavgcount + 1
            if paddedimg[rowcount ][colcount + 1] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount ][colcount + 2] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 1][colcount ] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 1][colcount + 1] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 1][colcount + 2] != 0:
                pixelavgcount = pixelavgcount + 1
            if paddedimg[rowcount + 1][colcount ] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 2][colcount + 1] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 2][colcount + 2] != 0:
                pixelavgcount = pixelavgcount + 1


            pixelavg = pixelavg / pixelavgcount
            # denoiserow.append(pixelavg)
            if pixelavg < pixel:
                denoiseimg[rowcount][colcount] = pixelavg
            else:
                denoiseimg[rowcount][colcount] = pixel



    utils.write_image(denoiseimg,'results/task2_result.jpg')

    count = len(img[0])
    padrow = []
    padrow2 = []
    paddedimg = []
    padrow.append(0)
    padrow2.append(0)
    padrow.append(0)
    padrow2.append(0)
    while count > 0:
        padrow.append(0)
        padrow2.append(0)
        count = count - 1
    paddedimg.append(padrow)
    for row in denoiseimg:
        newrow = []
        newrow.append(0)
        paddedimg.append(newrow)

        for pixel in row:
            newpixel = pixel
            newrow.append(newpixel)
        newrow.append(0)
    paddedimg.append(padrow2)

    denoiseimg2 = img
    rowcount = -1
    colcount = -1
    for row in img:
        # denoiseimg.append(denoiserow)
        rowcount = rowcount + 1
        colcount = -1
        for pixel in row:
            colcount = colcount + 1
            pixelavg = 0
            pixelavgcount = 0
            medianarray = []

            medianarray.append(paddedimg[rowcount ][colcount ])
            medianarray.append(paddedimg[rowcount ][colcount + 1])
            medianarray.append( paddedimg[rowcount ][colcount + 2])
            medianarray.append( paddedimg[rowcount + 1][colcount ])
            medianarray.append( paddedimg[rowcount + 1][colcount + 1])
            medianarray.append( paddedimg[rowcount + 1][colcount + 2])
            medianarray.append( paddedimg[rowcount + 2][colcount ])
            medianarray.append( paddedimg[rowcount + 2][colcount + 1])
            medianarray.append( paddedimg[rowcount + 2][colcount + 2])
            # pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 1]

            if paddedimg[rowcount ][colcount ] != 0:
                pixelavgcount = pixelavgcount + 1
            if paddedimg[rowcount ][colcount + 1] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount ][colcount + 2] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 1][colcount ] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 1][colcount + 1] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 1][colcount + 2] != 0:
                pixelavgcount = pixelavgcount + 1
            if paddedimg[rowcount + 1][colcount ] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 2][colcount + 1] != 0:
                pixelavgcount = pixelavgcount + 1
            if  paddedimg[rowcount + 2][colcount + 2] != 0:
                pixelavgcount = pixelavgcount + 1

            medianarray.sort()
            pixelavg = pixelavg / pixelavgcount
            # denoiserow.append(pixelavg)
            denoiseimg2[rowcount][colcount] =  medianarray[4]

            # pixelavg = pixelavg + paddedimg[rowcount ][colcount ]
            # pixelavg = pixelavg + paddedimg[rowcount ][colcount + 1]
            # pixelavg = pixelavg + paddedimg[rowcount ][colcount + 2]
            # pixelavg = pixelavg + paddedimg[rowcount + 1][colcount ]
            # pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 1]
            # pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 2]
            # pixelavg = pixelavg + paddedimg[rowcount + 2][colcount ]
            # pixelavg = pixelavg + paddedimg[rowcount + 2][colcount + 1]
            # pixelavg = pixelavg + paddedimg[rowcount + 2][colcount + 2]
            # # pixelavg = pixelavg + paddedimg[rowcount + 1][colcount + 1]
            #
            # if paddedimg[rowcount ][colcount ] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if paddedimg[rowcount ][colcount + 1] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if  paddedimg[rowcount ][colcount + 2] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if  paddedimg[rowcount + 1][colcount ] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if  paddedimg[rowcount + 1][colcount + 1] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if  paddedimg[rowcount + 1][colcount + 2] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if paddedimg[rowcount + 1][colcount ] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if  paddedimg[rowcount + 2][colcount + 1] != 0:
            #     pixelavgcount = pixelavgcount + 1
            # if  paddedimg[rowcount + 2][colcount + 2] != 0:
            #     pixelavgcount = pixelavgcount + 1
            #
            #
            # pixelavg = pixelavg / pixelavgcount
            # # denoiserow.append(pixelavg)
            # if pixelavg < pixel:
            #     denoiseimg[rowcount][colcount] = pixelavg
            # else:
            #     denoiseimg[rowcount][colcount] = pixel

    utils.write_image(denoiseimg2,'results/task2_result2.jpg')
    # cv2.imwrite('results/task2_result.jpg',denoiseimg)

def mse(img1, img2):
    """
    Calculate mean square error of two images.
    Arg: Two images to be compared.
    Return: Mean square error.
    """
    # TODO: implement this function.


if __name__ == "__main__":
    img = utils.read_image('lenna-noise.png')
    gt = utils.read_image('lenna-denoise.png')

    result = median_filter(img)
    error = mse(gt, result)

    with open('results/task2.json', "w") as file:
        json.dump(error, file)
    utils.write_image(result,'results/task2_result.jpg')

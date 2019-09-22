"""
Image Filtering
(Due date: Sep. 25, 3 P.M., 2019)

The goal of this task is to experiment with image filtering and familiarize you with 'tricks', e.g., padding, commonly used by computer vision 'researchers'.

Please complete all the functions that are labelled with '# TODO'. Steps to complete those functions are provided to make your lives easier. When implementing those functions, comment the lines 'raise NotImplementedError' instead of deleting them. The functions defined in 'utils.py'
are building blocks you could use when implementing the functions labelled with 'TODO'.

I strongly suggest you read the function 'zero_pad' and 'crop' that are defined in 'utils.py'. You will need them!

Do NOT modify the code provided to you.
Do NOT use ANY API provided by opencv (cv2) and numpy (np) in your code.
Do NOT import ANY library (function, module, etc.).
"""

import argparse
import copy
import os

import cv2
import numpy as np

import utils

# low_pass filter and high-pass filter
low_pass = [[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]]
#high_pass = [[-1/9, -1/9, -1/9], [-1/9, 17/9, -1/9], [-1/9, -1/9, -1/9]]
# high_pass2 = [[1,2,1], [-1/9, 17/9, -1/9], [-1,-2,-1]]
# high_pass = [[1,0,1], [2, 0, -2], [1,0,-1]]
high_pass = [[1,1,1],[1,1,1],[1,1,1]]
def parse_args():
    parser = argparse.ArgumentParser(description="cse 473/573 project 1.")
    parser.add_argument(
        "--img-path",
        type=str,
        default="./data/proj1-task1.jpg",
        help="path to the image"
    )
    parser.add_argument(
        "--filter",
        type=str,
        default="high-pass",
        choices=["low-pass", "high-pass"],
        help="type of filter"
    )
    parser.add_argument(
        "--result-saving-dir",
        dest="rs_dir",
        type=str,
        default="./results/",
        help="directory to which results are saved (do not change this arg)"
    )
    args = parser.parse_args()
    return args


def read_image(img_path, show=False):
    """Reads an image into memory as a grayscale array.
    """
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if not img.dtype == np.uint8:
        pass

    if show:
        show_image(img)

    img = [list(row) for row in img]
    return img

def show_image(img, delay=1000):
    """Shows an image.
    """
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', img)
    cv2.waitKey(delay)
    cv2.destroyAllWindows()

def write_image(img, img_saving_path):
    """Writes an image to a given path.
    """
    if isinstance(img, list):
        img = np.asarray(img, dtype=np.uint8)
    elif isinstance(img, np.ndarray):
        if not img.dtype == np.uint8:
            assert np.max(img) <= 1, "Maximum pixel value {:.3f} is greater than 1".format(np.max(img))
            img = (255 * img).astype(np.uint8)
    else:
        raise TypeError("img is neither a list nor a ndarray.")

    cv2.imwrite(img_saving_path, img)

def convolve2d(img, kernel):
    """Convolves a given image and a given kernel.

    Steps:
        (1) flips the kernel
        (2) pads the image # IMPORTANT
            this step handles pixels along the border of the image, and ensures that the output image is of the same size as the input image
        (3) calucates the convolved image using nested for loop

    Args:
        img: nested list (int), image.
        kernel: nested list (int), kernel.

    Returns:
        img_conv: nested list / 9(int), convolved image.
    """
    count = 0
    newimg = img
    oldimg = img

    print(len(oldimg))
    print(len(oldimg[1]))
    count  = 0
    # for row in oldimg:
    #     row.insert(0,0)
    #     row.insert(len(row),0)
    #     row.insert(len(row),0)
    #
    #
    # emptylist = []
    # emptylist = (emptylist + (len(newimg[0]) + 1) * [0])[:(len(newimg[0]) )]
    # oldimg.insert(0,emptylist)
    # oldimg.insert(len(oldimg),emptylist)
    # print(len(oldimg))
    # print(len(oldimg[1]))
    accumulator = 0
    rowcount = -1
    colcount = -1
    oldimg = utils.zero_pad(oldimg,1,1)
    for row in img:
        rowcount = rowcount + 1
        colcount = -1
        for pixel in row:
            colcount = colcount + 1
            accumulator = 0
            accumulator = accumulator + (oldimg[rowcount ][colcount ] * kernel[0][0])
            accumulator = accumulator + (oldimg[rowcount ][colcount + 1]  * kernel[0][1])
            accumulator = accumulator + (oldimg[rowcount ][colcount + 2] * kernel[0][2])
            accumulator = accumulator + (oldimg[rowcount + 1][colcount ] * kernel[1][0])
            accumulator = accumulator + (oldimg[rowcount + 1][colcount + 1] * kernel[1][1])
            accumulator = accumulator + (oldimg[rowcount + 1][colcount + 2] * kernel[1][2])
            accumulator = accumulator + (oldimg[rowcount + 2][colcount ] * kernel[2][0])
            accumulator = accumulator + (oldimg[rowcount + 2][colcount + 1] * kernel[2][1])
            accumulator = accumulator + (oldimg[rowcount + 2][colcount + 2] * kernel[2][2])

            # accumulator = accumulator + ((oldimg[rowcount - 2][colcount - 2] * 2) * kernel[0][0])
            # accumulator = accumulator + ((oldimg[rowcount - 2][colcount - 1] * 2)  * kernel[0][1])
            # accumulator = accumulator + ((oldimg[rowcount - 2][colcount] * 2) * kernel[0][2])
            # accumulator = accumulator + ((oldimg[rowcount - 1][colcount - 2] * 2) * kernel[1][0])
            # accumulator = accumulator + ((oldimg[rowcount - 1][colcount - 1] * 2) * kernel[1][1])
            # accumulator = accumulator + ((oldimg[rowcount - 1][colcount] * 2) * kernel[1][2])
            # accumulator = accumulator + ((oldimg[rowcount][colcount - 2] * 2) * kernel[2][0])
            # accumulator = accumulator + ((oldimg[rowcount ][colcount - 1] * 2) * kernel[2][1])
            # accumulator = accumulator + ((oldimg[rowcount][colcount] * 2) * kernel[2][2])

            # for krow in kernel:
            #     for kel in krow:
            #         newval = kel * pixel
            #         accumulator = newval + accumulator

            newimg[rowcount ][colcount ] = (newimg[rowcount ][colcount ] * 2) - (accumulator / 9)
    print(newimg[1])
    # kernel = high_pass2
    # rowcount = -1
    # colcount = -1
    # newimg2 = oldimg
    # for row in img:
    #     rowcount = rowcount + 1
    #     colcount = -1
    #     for pixel in row:
    #         colcount = colcount + 1
    #         accumulator = 0
    #         accumulator = accumulator + (oldimg[rowcount - 2][colcount - 2] * kernel[0][0])
    #         accumulator = accumulator + (oldimg[rowcount - 2][colcount - 1] * kernel[0][1])
    #         accumulator = accumulator + (oldimg[rowcount - 2][colcount] * kernel[0][2])
    #         accumulator = accumulator + (oldimg[rowcount - 1][colcount - 2] * kernel[1][0])
    #         accumulator = accumulator + (oldimg[rowcount - 1][colcount - 1] * kernel[1][1])
    #         accumulator = accumulator + (oldimg[rowcount - 1][colcount] * kernel[1][2])
    #         accumulator = accumulator + (oldimg[rowcount][colcount - 2] * kernel[2][0])
    #         accumulator = accumulator + (oldimg[rowcount ][colcount - 1] * kernel[2][1])
    #         accumulator = accumulator + (oldimg[rowcount][colcount] * kernel[2][2])
    #         # for krow in kernel:
    #         #     for kel in krow:
    #         #         newval = kel * pixel
    #         #         accumulator = newval + accumulator
    #         newimg2[rowcount ][colcount ] = (accumulator / 9) + (newimg[rowcount ][colcount ])
    return  newimg
    # TODO: implement this function.
    #raise NotImplementedError

def main():
    args = parse_args()

    img = read_image(args.img_path)

    if args.filter == "low-pass":
        kernel = low_pass
    elif args.filter == "high-pass":
        kernel = high_pass
    else:
        raise ValueError("Filter type not recognized.")

    if not os.path.exists(args.rs_dir):
        os.makedirs(args.rs_dir)
    print(kernel[0])
    filtered_img = convolve2d(img, kernel)
    write_image(filtered_img, os.path.join(args.rs_dir, "{}.jpg".format(args.filter)))


if __name__ == "__main__":
    main()

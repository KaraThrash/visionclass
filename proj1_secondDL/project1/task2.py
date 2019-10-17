"""
Template Matching
(Due date: Sep. 25, 3 P.M., 2019)

The goal of this task is to experiment with template matching techniques, i.e., normalized cross correlation (NCC).

Please complete all the functions that are labelled with '# TODO'. When implementing those functions, comment the lines 'raise NotImplementedError' instead of deleting them. The functions defined in 'utils.py'
and the functions you implement in 'task1.py' are of great help.

Do NOT modify the code provided to you.
Do NOT use ANY API provided by opencv (cv2) and numpy (np) in your code.
Do NOT import ANY library (function, module, etc.).
"""


import argparse
import json
import os

import utils
import task1
from task1 import *


def parse_args():
    parser = argparse.ArgumentParser(description="cse 473/573 project 1.")
    parser.add_argument(
        "--img-path",
        type=str,
        default="./data/task2-test.jpg",
        help="path to the image")
    parser.add_argument(
        "--template-path",
        type=str,
        default="./data/template-test.jpg",
        help="path to the template"
    )
    parser.add_argument(
        "--result-saving-path",
        dest="rs_path",
        type=str,
        default="./results/task2.json",
        help="path to file which results are saved (do not change this arg)"
    )
    args = parser.parse_args()
    return args

def norm_xcorr2d(patch, template):
    """Computes the NCC value between a image patch and a template.

    The image patch and the template are of the same size. The formula used to compute the NCC value is:
    sum_{i,j}(x_{i,j} - x^{m}_{i,j})(y_{i,j} - y^{m}_{i,j}) / (sum_{i,j}(x_{i,j} - x^{m}_{i,j}) ** 2 * sum_{i,j}(y_{i,j} - y^{m}_{i,j})) ** 0.5
    This equation is the one shown in Prof. Yuan's ppt.

    Args:
        patch: nested list (int), image patch.
        template: nested list (int), template.

    Returns:
        value (float): the NCC value between a image patch and a template.
    """
    ncc = 0.0
    count = -1
    for pix in patch:
        print("loop")
        count = count + 1
        ncc = ncc + pix * template[count] / np.sqrt((template[count]**2)*(pix**2))
    # np.sum((a*b))/(np.sqrt((np.sum(a**2))*(np.sum(b**2))))
    return ncc
    # raise NotImplementedError

def match(img, template):
    """Locates the template, i.e., a image patch, in a large image using template matching techniques, i.e., NCC.

    Args:
        img: nested list (int), image that contains character to be detected.
        template: nested list (int), template image.

    Returns:
        x (int): row that the character appears (starts from 0).
        y (int): column that the character appears (starts from 0).
        max_value (float): maximum NCC value.
    """
    rowcount = 0 #len(img)
    colcount = 0
    bestx = 0
    besty = 0
    bestavg = 10
    #img = utils.flip_y(img)
    while rowcount < (len(img) - 5):
        tempavg = avg4(img[rowcount],template[0],template[1],img[rowcount + 1],template[2],img[rowcount + 2],colcount)
        if tempavg < bestavg:
            bestavg = tempavg
            besty = rowcount
            bestx = colcount
        colcount = colcount + 1
        if colcount >= (len(img[0]) - 5):
            rowcount = rowcount + 1
            colcount = 0
    tempint = 0.0
    tempint = tempint + img[besty][bestx]
    tempint = tempint + img[besty][bestx + 1]
    tempint = tempint + img[besty][bestx + 2]
    print(bestavg/tempint)
    # print(bestx)

    ncc = (-1 + (bestavg/tempint))
    # ncc = norm_xcorr2d(img[besty][bestx :len(template[0]  )],template[0])

    newimg = img
    count = 0
    count2 = 0
    while count < 5:
        count2 = 0
        while count2 < 5:
            newimg[besty + count][bestx + count2] = 255
            count2 += 1
        count += 1

    task1.write_image(newimg,  "1.png")
    # json.dumps({"x":1,"y":2,"value":(-1 + (bestavg/tempint))})
    return bestx,besty,(-1 + (bestavg/tempint))
    # {"x":"1","y":"2","value":str(-1 + (bestavg/tempint))}
    # {"x":1,"y":2,"value":(-1 + (bestavg/tempint))}


def avg4(img1,img2,img3,img4,img5,img6,column):
    tempint = float(abs(int(img1[column]) - int(img2[0])))
    tempint = tempint + abs(int(img1[column + 1]) - int(img2[1]))
    tempint = tempint + abs(int(img1[column + 2]) - int(img2[2]))
    tempint = tempint + abs(int(img1[column + 3]) - int(img2[3]))
    tempint = tempint + abs(int(img1[column + 4]) - int(img2[4]))
    tempint = tempint + abs(int(img4[column]) - int(img3[0]))
    tempint = tempint + abs(int(img4[column + 1]) - int(img3[1]))
    tempint = tempint + abs(int(img4[column + 2]) - int(img3[2]))
    tempint = tempint + abs(int(img4[column + 3]) - int(img3[3]))
    tempint = tempint + abs(int(img4[column + 4]) - int(img3[4]))
    tempint = tempint + abs(int(img6[column]) - int(img5[0]))
    tempint = tempint + abs(int(img6[column + 1]) - int(img5[1]))
    tempint = tempint + abs(int(img6[column + 2]) - int(img5[2]))
    tempint = tempint + abs(int(img6[column + 3]) - int(img5[3]))
    tempint = tempint + abs(int(img6[column + 4]) - int(img5[4]))
    return tempint / 15.0  #( abs(img1[column] - img2[0]) + abs(img1[column + 1] - img2[1]) + abs(img1[column + 2] - img2[2]) + abs(img1[column + 3] - img2[3])  ) / 4

def save_results(coordinates, template, template_name, rs_directory):
    results = {}
    results["coordinates"] = sorted(coordinates, key=lambda x: x[0])
    results["templat_size"] = (len(template), len(template[0]))
    with open(os.path.join(rs_directory, template_name), "w") as file:
        json.dump(results, file)


def main():
    args = parse_args()

    img = read_image(args.img_path)
    # template = utils.crop(img, xmin=10, xmax=30, ymin=10, ymax=30)
    # template = np.asarray(template, dtype=np.uint8)
    # cv2.imwrite("./data/proj1-task2-template.jpg", template)
    template = read_image(args.template_path)

    x, y, max_value = match(img, template)
    # The correct results are: x: 17, y: 129, max_value: 0.994
    with open(args.rs_path, "w") as file:
        json.dump({"x": x, "y": y, "value": max_value}, file)


if __name__ == "__main__":
    main()

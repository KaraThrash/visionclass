"""
K-Means Segmentation Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to segment image using k-means clustering.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint:
Please complete all the functions that are labeled with '#to do'.
You are allowed to add your own functions if needed.
You should design you algorithm as fast as possible. To avoid repetitve calculation, you are suggested to depict clustering based on statistic histogram [0,255].
You will be graded based on the total distortion, e.g., sum of distances, the less the better your clustering is.
"""


import utils
import numpy as np
import json
import time


def kmeans(img,k):
    """
    Implement kmeans clustering on the given image.
    Steps:
    (1) Random initialize the centers.
    (2) Calculate distances and update centers, stop when centers do not change.
    (3) Iterate all initializations and return the best result.
    Arg: Input image;
         Number of K.
    Return: Clustering center values;
            Clustering labels of all pixels;
            Minimum summation of distance between each pixel and its center.
    """
    # TODO: implement this function.

    # NOTE: max is 245

    cluster1 = 0
    clusterb = 255
    avg1 = 0
    distsuma = 0
    count1 = 0
    avgb = 0
    distsumb = 0
    countb = 0
    for row in img:

        for pixel in row:
            if abs(pixel - cluster1) > abs(pixel - clusterb):
                avgb = avgb + pixel
                countb = countb + 1
                avgb = avgb / countb
                distsumb = distsumb + abs(pixel - clusterb)
            elif abs(pixel - cluster1) < abs(pixel - clusterb):
                avg1 = avg1 + pixel
                count1 = count1 + 1
                avg1 = avg1 / count1
                distsuma = distsuma + abs(pixel - cluster1)
            else:#NOTE: if equidistant put in the smaller pool
                if count1 > countb:
                    avg1 = avg1 + pixel
                    count1 = count1 + 1
                    avg1 = avg1 / count1
                    distsuma = distsuma + abs(pixel - cluster1)
                else:
                    avgb = avgb + pixel
                    countb = countb + 1
                    avgb = avgb / countb
                    distsumb = distsumb + abs(pixel - clusterb)
    if avg1 > 0:
        cluster1 = cluster1 + 1
        if cluster1 > 255:
            cluster1 = 255
    elif avg1 < 0:
        cluster1 = cluster1 - 1
        if cluster1 < 0:
            cluster1 = 0
    if avgb > 0:
        clusterb = clusterb + 1
        if clusterb > 255:
            clusterb = 255
    elif avgb < 0:
        clusterb = clusterb - 1
        if clusterb < 0:
            clusterb = 0
# {"distance": 5437045, "centers": [94, 161], "time": 115.57173490524292}
# {"distance": 5437045, "centers": [94, 161], "time": 64.89245796203613}
# {"distance": 5439599, "centers": [95, 160], "time": 27.1616051197052}
    centers, labels, bestsumdistance ,distsuma,distsumb = kmeans2(img,k,cluster1,clusterb,count1,countb,distsuma,distsumb)
    bestcenters = centers
    bestlabels = labels
    iteratecount = 0
    print(bestsumdistance)
    while iteratecount < 125:
        iteratecount = iteratecount + 1
        cluster1 = iteratecount
        clusterb = 255 - iteratecount
        if cluster1 >= 255:
            cluster1 = 255
        if clusterb < 0:
            clusterb = 0
        if clusterb >= 255:
            clusterb = 255
        if cluster1 < 0:
            cluster1 = 0
        centers, labels, newsumdistance ,distsuma,distsumb = kmeans2(img,k,cluster1,clusterb,count1,countb,distsuma,distsumb)
        if newsumdistance < bestsumdistance:
            bestsumdistance = newsumdistance
            bestcenters = centers
            bestlabels = labels

    return (bestcenters, bestlabels, bestsumdistance)

def kmeans2(img,k,cluster1,clusterb,lastcount1,lastcountb,distsuma,distsumb):


    avg1 = 0
    distsuma = 0
    count1 = 0
    avgb = 0
    distsumb = 0
    countb = 0
    for row in img:

        for pixel in row:
            if abs(pixel - cluster1) > abs(pixel - clusterb):
                avgb = avgb + pixel
                countb = countb + 1
                avgb = avgb / countb
                distsumb = distsumb + abs(pixel - clusterb)
            else:
                avg1 = avg1 + pixel
                count1 = count1 + 1
                avg1 = avg1 / count1
                distsuma = distsuma + abs(pixel - cluster1)
    if avg1 > 0:
        cluster1 = cluster1 + 1
        if cluster1 > 255:
            cluster1 = 255
    elif avg1 < 0:
        cluster1 = cluster1 - 1
        if cluster1 < 0:
            cluster1 = 0
    if avgb > 0:
        clusterb = clusterb + 1
        if clusterb > 255:
            clusterb = 255
    elif avgb < 0:
        clusterb = clusterb - 1
        if clusterb < 0:
            clusterb = 0
    if avg1 > 0:
        cluster1 = cluster1 + 1
        if cluster1 > 255:
            cluster1 = 255
    elif avg1 < 0:
        cluster1 = cluster1 - 1
        if cluster1 < 0:
            cluster1 = 0
    if avgb > 0:
        clusterb = clusterb + 1
        if clusterb > 255:
            clusterb = 255
    elif avgb < 0:
        clusterb = clusterb - 1
        if clusterb < 0:
            clusterb = 0
    if count1 == lastcount1:
        return ([cluster1,clusterb],img,distsuma + distsumb,distsuma,distsumb)
    else:
        kmeans2(img,k,cluster1,clusterb,count1,countb,distsuma,distsumb)


def visualize(centers,labels):
    """
    Convert the image to segmentation map replacing each pixel value with its center.
    Arg: Clustering center values;
         Clustering labels of all pixels.
    Return: Segmentation map.
    """
    # TODO: implement this function.
    newimg = labels
    # newimg = [[0] * len(labels[0])] * len(labels)
    rowcount = -1
    colcount = 0
    for row in labels:
        # newimgrow = []
        rowcount = rowcount + 1
        colcount = -1
        # newimg.append(newimgrow)
        for pixel in row:
            colcount = colcount + 1
            if abs(pixel - centers[0]) > abs(pixel - centers[1]):
                newimg[rowcount][colcount] = centers[1]
                # newimgrow.append(centers[1])
            else:
                newimg[rowcount][colcount] = centers[0]
                # newimgrow.append(centers[0])
    return newimg

if __name__ == "__main__":
    img = utils.read_image('lenna.png')
    k = 2

    start_time = time.time()
    centers, labels, sumdistance = kmeans(img,k)
    result = visualize(centers, labels)
    end_time = time.time()

    running_time = end_time - start_time
    print(running_time)

    centers = list(centers)
    with open('results/task1.json', "w") as jsonFile:
        jsonFile.write(json.dumps({"centers":centers, "distance":sumdistance, "time":running_time}))
    utils.write_image(result, 'results/task1_result.jpg')

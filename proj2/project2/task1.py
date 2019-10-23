"""
RANSAC Algorithm Problem
(Due date: Oct. 23, 3 P.M., 2019)
The goal of this task is to fit a line to the given points using RANSAC algorithm, and output
the names of inlier points and outlier points for the line.

Do NOT modify the code provided to you.
Do NOT use ANY API provided by opencv (cv2) and numpy (np) in your code.
Do NOT import ANY library (function, module, etc.).
You can use the library random
Hint: It is recommended to record the two initial points each time, such that you will Not
start from this two points in next iteration.
"""
import random
import math

def solution(input_points, t, d, k):
    """
    :param input_points:
           t: t is the perpendicular distance threshold from a point to a line
           d: d is the number of nearby points required to assert a model fits well, you may not need this parameter
           k: k is the number of iteration times
           Note that, n for line should be 2
           (more information can be found on the page 90 of slides "Image Features and Matching")
    :return: inlier_points_name, outlier_points_name
    inlier_points_name and outlier_points_name is two list, each element of them is str type.
    For example: If 'a','b' is inlier_points and 'c' is outlier_point.
    the output should be two lists of ['a', 'b'], ['c'].
    Note that, these two lists should be non-empty.
    """
    # TODO: implement this function.

    #
    # input_points = [{'name': 'a', 'value': (0.0, 1.0)}, {'name': 'b', 'value': (2.0, 1.0)},
    #                 {'name': 'c', 'value': (3.0, 1.0)}, {'name': 'd', 'value': (0.0, 3.0)},
    #                 {'name': 'e', 'value': (1.0, 2.0)}, {'name': 'f', 'value': (1.5, 1.5)},
    #                 {'name': 'g', 'value': (1.0, 1.0)}, {'name': 'h', 'value': (1.5, 2.0)}]
    # A = 1.0 - 2.0
    # B = 1.5 - 2.0
    # C = (A * 1.5) + (B * 2.0)
    # print(abs(A*1.0 + B*1.0 + C))
    # print(math.sqrt(A*A + B*B))
    # print(B * B)
    # d = ((abs(A*1.0 + B*1.0 + C)) / (math.sqrt(A*A + B*B)))
    # print(d)
    # avglist = []











    #ax +by +c = 0
    # d = abs(Am + Bn + C) / sqrt(A^2 + B^2)
    # A = qy - py
    # B = px - qx
    # C = Apx + Bpy
    nodelist = []
    for el in input_points:
        nodelist.append(el)


    avglist = []
    bestline = (0,0,0,0)
    bestinlineavg = 10000.0
    inlineavg = 10000.0
    bestinline = 0
    bestoutline = 0
    inliners = 0
    outliners = 0
    countp = -1
    countq = 0
    inlinelist = []
    outlinelist = []
    tempinlinelist = []
    tempoutlinelist = []
    for point_q in nodelist:
        countq = -1
        countp = countp + 1
        # inliners = 0
        # outliners = 0
        # inlineavg = 0.0
        for point_p in nodelist:
            countq = countq + 1

            if point_q["name"] != point_p["name"]:
                tempinlinelist = []
                tempoutlinelist = []
                # slope = (point_p["value"][1]-point_q["value"][1]) / (point_p["value"][1] - point_q["value"][0])
                inliners = 0
                outliners = 0
                inlineavg = 0.0
                # yintercept =(point_q["value"][1] * point_p["value"][0]) - (point_q["value"][0] * point_p["value"][1]) / (point_p["value"][0] - point_q["value"][0])
                A = point_q["value"][1] - point_p["value"][1]
                B = point_p["value"][0] - point_q["value"][0]
                C = A*point_p["value"][0] + B*point_p["value"][1]
                # print("A:",A,"B",B,"C:",C)
                # print("", point_p["value"], "", point_q["value"])
                countd = 0
                tempinlinelist.append(point_p["name"])
                tempinlinelist.append(point_q["name"])
                for point_d in nodelist:
                    if point_d["name"] != point_p["name"] and point_q["name"] != point_d["name"]:

                        countd = countd + 1
                        # print("point D:", countd)
                        # print(abs(A*point_d["value"][0] + B*point_d["value"][1] + C))
                        # print(math.sqrt(A*A + B*B))
                        # print(abs(A*point_d["value"][0] + B*point_d["value"][1] + C) / math.sqrt(A*A + B*B))
                        # A = point_q["value"][1] - point_p["value"][1]
                        # B = point_p["value"][0] - point_q["value"][0]
                        # C = (A*point_p["value"][0]) + (B*point_p["value"][1])
                        dist = (abs(A*point_d["value"][0] + B*point_d["value"][1] + C)) / (math.sqrt(A*A + B*B))
                        # print("for point ", point_d["value"][0],",",point_d["value"][1], "D: ", d)

                        # slope = (y1-y2)/(x1-x2)
                        if (point_p["value"][0] - point_q["value"][0]) != 0 and (point_p["value"][0] - point_q["value"][0] ) != 0:
                            slope = (point_p["value"][1] - point_q["value"][1]) / (point_p["value"][0] - point_q["value"][0])
                            # yintercept = (x1*y2 - x2*y1)/(x1-x2)
                            yintercept = ((point_p["value"][0] * point_q["value"][1]) - (point_q["value"][0] * point_p["value"][1])) / (point_p["value"][0] - point_q["value"][0] )
                            dist = math.sqrt( ((yintercept + (slope * point_d["value"][0]) - point_d["value"][1]) * (yintercept + (slope * point_d["value"][0]) - point_d["value"][1])) /((slope * slope) + 1)  )

                            if dist <= t:
                                inliners = inliners + 1
                                inlineavg = inlineavg + dist
                                tempinlinelist.append(point_d["name"])
                            else:
                                # print("outlier",point_d["value"],"D: ", d)
                                outliners = outliners + 1
                                tempoutlinelist.append(point_d["name"])
                # print(point_q,point_p)
                # print("inliners:",inliners,"avg",inlineavg)
                # print("outliners:",outliners)

                if inliners >= d:
                    inlineavg = inlineavg / inliners
                    # avglist.append(("p: ",point_p["name"],"q: ",point_q["name"],":inliners:",inliners," : outliners: ",outliners ))
                    # inlineavg = inlineavg / (inliners )

                    if inlineavg < bestinlineavg :
                        # bestinlineavg = inlineavg
                        # print("Better! old average: ",bestinlineavg," new average: ",inlineavg)
                        bestinlineavg = inlineavg
                        inlinelist = tempinlinelist
                        outlinelist = tempoutlinelist
                    # else:
                    #     print("WORSE! old average: ",bestinlineavg," new average: ",inlineavg)
                # else:
                    # print("no D! old average: ",bestinlineavg," new average: ",inlineavg)
    # print("Bestline ", bestline)
    # # print("avg ", bestinlineavg)
    # print("inliners ", bestinline)
    # print(avglist)
    # for el in avglist:
    #     print(el)
    return (inlinelist,outlinelist)
    # raise NotImplementedError


if __name__ == "__main__":
    input_points = [{'name': 'a', 'value': (0.0, 1.0)}, {'name': 'b', 'value': (2.0, 1.0)},
                    {'name': 'c', 'value': (3.0, 1.0)}, {'name': 'd', 'value': (0.0, 3.0)},
                    {'name': 'e', 'value': (1.0, 2.0)}, {'name': 'f', 'value': (1.5, 1.5)},
                    {'name': 'g', 'value': (1.0, 1.0)}, {'name': 'h', 'value': (1.5, 2.0)}]

    t = 0.5
    d = 3
    k = 100
    inlier_points_name, outlier_points_name = solution(input_points, t, d, k)  # TODO
    # assert len(inlier_points_name) + len(outlier_points_name) == 8
    f = open('./results/task1_result.txt', 'w')
    f.write('inlier points: ')
    for inliers in inlier_points_name:
        f.write(inliers + ',')
    f.write('\n')
    f.write('outlier points: ')
    for outliers in outlier_points_name:
        f.write(outliers + ',')
    f.close()

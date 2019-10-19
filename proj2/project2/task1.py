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

    avglist = []
    pairlist = []
    countp = 0
    countq = 0
    countd = -1

    while countq < 3.2:
        countq = countq + 0.01
        # (countq, 3 - countq)
        # (3 - countq, 3 - countq)
        # (3 - countq,  countq)
        # (countq, countq)
        pairlist.append(((round(countq,2) + 0.1,  round(countq,2)),(3.2 - round(countq,2),  3.2 - round(countq,2))))
        pairlist.append(((0,  5.2 - round(countq,2)),(3.2 - round(countq,2),  0)))
        pairlist.append(((3.2 - round(countq,2),  3.21 - round(countq,2)),(3.23 - round(countq,2),  3.22 - round(countq,2))))
        # pairlist.append(((3.2 - countq, countq),(countq,3.2 - countq)))
        # pairlist.append((countq,  countq))
        # pairlist.append((3.2 - countq,  countq))
        # countq = -1
        # countd = -1
        # while countq < len(input_points) - 1:
        #     countd = -1
        #     countq = countq + 1
        #
        #     if countq != countp:
        #         dlist = []
        #         pairlist.append((countp,countq,dlist))
        #         while countd < len(input_points) - 1:
        #             if countd != countp and countd != countq and countq != countp:
        #                 dlist.append(countd)
        #             countd = countd + 1

    bestline = (0,0,0,0)
    bestinlineavg = 10000.0
    inlineavg = 10000.0
    bestinline = 0
    bestoutline = 0
    for el in pairlist:
        print(el)
    for el in pairlist:

        inliners = 0
        outliners = 0
        inlineavg = 0.0
        ppoint = el[0]
        qpoint = el[1]
        # dlist = el[2]
        # yintercept =(point_q["value"][1] * point_p["value"][0]) - (point_q["value"][0] * point_p["value"][1]) / (point_p["value"][0] - point_q["value"][0])
        A = qpoint[1] - ppoint[1]
        B = ppoint[0] - qpoint[0]
        C = A*ppoint[0] + B*ppoint[1]
        for dpoint in input_points:
            d = (abs(A*dpoint[0] + B*dpoint[1] + C)) / (math.sqrt(A*A + B*B))
            if d <= 0.5:
                inliners = inliners + 1
                inlineavg = inlineavg + d
            else:
                # print("outlier",dpoint["value"],"D: ", d)
                outliners = outliners + 1

        # print("inliners:",inliners,"avg",inlineavg)
        # print("outliners:",outliners)
        if inliners > 3:
            avglist.append((qpoint,ppoint,":total:",inliners," : out: ",outliners ))
            inlineavg = inlineavg / (inliners )

        # if inlineavg > 0 and inlineavg < bestinlineavg:
        #     bestinlineavg = inlineavg
        #     bestinline = inliners
        #     bestline = (point_p["value"][0],point_p["value"][1],point_q["value"][0],point_q["value"][1])

# print("Bestline ", bestline)
# print("avg ", bestinlineavg)
# print("inliners ", bestinline)
# # print(avglist)
    for el in avglist:
        print(el)









    #
    #
    #
    # while countp < len(input_points) - 1:
    #     countp = countp + 1
    #     countq = -1
    #     countd = -1
    #     while countq < len(input_points) - 1:
    #         countd = -1
    #         countq = countq + 1
    #
    #         if countq != countp:
    #             dlist = []
    #             pairlist.append((countp,countq,dlist))
    #             while countd < len(input_points) - 1:
    #                 if countd != countp and countd != countq and countq != countp:
    #                     dlist.append(countd)
    #                 countd = countd + 1
#     bestline = (0,0,0,0)
#     bestinlineavg = 10000.0
#     inlineavg = 10000.0
#     bestinline = 0
#     bestoutline = 0
#     for el in pairlist:
#         print(el)
#     for el in pairlist:
#
#         inliners = 0
#         outliners = 0
#         inlineavg = 0.0
#         ppoint = input_points[el[0]]
#         qpoint = input_points[el[1]]
#         dlist = el[2]
#         # yintercept =(point_q["value"][1] * point_p["value"][0]) - (point_q["value"][0] * point_p["value"][1]) / (point_p["value"][0] - point_q["value"][0])
#         A = qpoint[1] - ppoint[1]
#         B = ppoint[0] - qpoint[0]
#         C = A*ppoint[0] + B*ppoint[1]
#         for dpoint in dlist:
#             d = (abs(A*input_points[dpoint][0] + B*input_points[dpoint][1] + C)) / (math.sqrt(A*A + B*B))
#             if d <= 0.5:
#                 inliners = inliners + 1
#                 inlineavg = inlineavg + d
#             else:
#                 # print("outlier",dpoint["value"],"D: ", d)
#                 outliners = outliners + 1
#
#         # print("inliners:",inliners,"avg",inlineavg)
#         # print("outliners:",outliners)
#         if inliners > 0:
#         avglist.append((ppoint,qpoint,dpoint,":total:",inliners," : avg: ",inlineavg / (inliners )))
#         inlineavg = inlineavg / (inliners )
#
#             # if inlineavg > 0 and inlineavg < bestinlineavg:
#             #     bestinlineavg = inlineavg
#             #     bestinline = inliners
#             #     bestline = (point_p["value"][0],point_p["value"][1],point_q["value"][0],point_q["value"][1])
#
# # print("Bestline ", bestline)
# # print("avg ", bestinlineavg)
# # print("inliners ", bestinline)
# # # print(avglist)
#     for el in avglist:
#         print(el)





































    #ax +by +c = 0
    # d = abs(Am + Bn + C) / sqrt(A^2 + B^2)
    # A = qy - py
    # B = px - qx
    # C = Apx + Bpy
    # bestline = (0,0,0,0)
    # bestinlineavg = 10000.0
    # inlineavg = 10000.0
    # bestinline = 0
    # bestoutline = 0
    # inliners = 0
    # outliners = 0
    # countp = -1
    # countq = 0
    # for point_q in input_points:
    #     countq = -1
    #     countp = countp + 1
    #     # inliners = 0
    #     # outliners = 0
    #     # inlineavg = 0.0
    #     for point_p in input_points:
    #         countq = countq + 1
    #
    #         if point_q != point_p:
    #             # slope = (point_p["value"][1]-point_q["value"][1]) / (point_p["value"][1] - point_q["value"][0])
    #             inliners = 0
    #             outliners = 0
    #             inlineavg = 0.0
    #             # yintercept =(point_q["value"][1] * point_p["value"][0]) - (point_q["value"][0] * point_p["value"][1]) / (point_p["value"][0] - point_q["value"][0])
    #             A = point_q["value"][1] - point_p["value"][1]
    #             B = point_p["value"][0] - point_q["value"][0]
    #             C = A*point_p["value"][0] + B*point_p["value"][1]
    #             # print("A:",A,"B",B,"C:",C)
    #             # print("", point_p["value"], "", point_q["value"])
    #             countd = 0
    #             for point_d in input_points:
    #                 if point_d != point_p and point_q != point_d:
    #                     countd = countd + 1
    #                     # print("point D:", countd)
    #                     # print(abs(A*point_d["value"][0] + B*point_d["value"][1] + C))
    #                     # print(math.sqrt(A*A + B*B))
    #                     # print(abs(A*point_d["value"][0] + B*point_d["value"][1] + C) / math.sqrt(A*A + B*B))
    #                     # A = point_q["value"][1] - point_p["value"][1]
    #                     # B = point_p["value"][0] - point_q["value"][0]
    #                     # C = (A*point_p["value"][0]) + (B*point_p["value"][1])
    #                     d = (abs(A*point_d["value"][0] + B*point_d["value"][1] + C)) / (math.sqrt(A*A + B*B))
    #                     # print("for point ", point_d["value"][0],",",point_d["value"][1], "D: ", d)
    #                     if d <= 0.5:
    #                         inliners = inliners + 1
    #                         inlineavg = inlineavg + d
    #                     else:
    #                         print("outlier",point_d["value"],"D: ", d)
    #                         outliners = outliners + 1
    #             print(point_q,point_p)
    #             print("inliners:",inliners,"avg",inlineavg)
    #             print("outliners:",outliners)
    #             if inliners > 0:
    #                 avglist.append((point_p,point_q,":total:",inlineavg,inliners," : avg: ",inlineavg / (inliners )))
    #                 inlineavg = inlineavg / (inliners )
    #
    #                 if inlineavg > 0 and inlineavg < bestinlineavg:
    #                     bestinlineavg = inlineavg
    #                     bestinline = inliners
    #                     bestline = (point_p["value"][0],point_p["value"][1],point_q["value"][0],point_q["value"][1])
    #
    # print("Bestline ", bestline)
    # print("avg ", bestinlineavg)
    # print("inliners ", bestinline)
    # # print(avglist)
    # for el in avglist:
    #     print(el)
    # return (1,1)
    # raise NotImplementedError


if __name__ == "__main__":
    # input_points = [{'name': 'a', 'value': (0.0, 1.0)}, {'name': 'b', 'value': (2.0, 1.0)},
    #                 {'name': 'c', 'value': (3.0, 1.0)}, {'name': 'd', 'value': (0.0, 3.0)},
    #                 {'name': 'e', 'value': (1.0, 2.0)}, {'name': 'f', 'value': (1.5, 1.5)},
    #                 {'name': 'g', 'value': (1.0, 1.0)}, {'name': 'h', 'value': (1.5, 2.0)}]
    input_points = [(0.0, 1.0), (2.0, 1.0),
                    (3.0, 1.0),  (0.0, 3.0),
                     (1.0, 2.0), (1.5, 1.5),
                    (1.0, 1.0),(1.5, 2.0)]
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

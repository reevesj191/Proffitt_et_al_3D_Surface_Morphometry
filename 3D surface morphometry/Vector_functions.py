########################################################################################################################
# Title: Vector Functions                                                                                              #
# Author: Jonathan S. Reeves                                                                                           #
# Summary: Make sure that file is in the same folder as the damage extraction scripts.                                 #
########################################################################################################################

from math import sqrt

def distance_3d(coord_1, coord_2):


    x1, y1, z1 = [i for i in coord_1]
    x2, y2, z2 = [i for i in coord_2]

    x = (x1 - x2)**2
    y = (y1 - y2)**2
    z = (z1 - z2)**2

    return sqrt((x+y+z))


def perimeter(points, line_idx):

    a = 0
    dists = []
    while a+3 <= len(line_idx):

        idx = line_idx[a:(a + 3)]
        print(idx)
        ## This is a work around
        if len(idx) != 0:
            d1 = idx[1]
            d2 = idx[2]
            print(points[d1])
            print(points[d2])
            d = distance_3d(coord_1=points[d1],
                        coord_2=points[d2])
            dists.append(d)
        else:
            pass

        a = a + 3
    return(sum(dists))

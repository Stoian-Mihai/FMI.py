from matplotlib import pyplot as plt
import random


def cross(p,q,r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    if val > 1:
        return 1
    else:
        return 2

def Hull(points):
    random.shuffle(points)
    if len(points) < 3:
        return 0

    hull = []
    l = 0
    for i in range(len(points)):
        if points[i][0] < points[l][0]:
            l = i

    p = l
    q = 0

    while(True):
        hull.append(points[p])

        q = (p+1)%len(points)
        for i in range(len(points)):
            if cross(points[p],points[i],points[q]) == 2:
                q = i
        p = q
        if points[p] in hull:
            break

    if len(hull) == 4:
        if cross(hull[0],hull[1],hull[2]) != 0 and cross(hull[1],hull[2],hull[3]) != 0:
            if cross(hull[0],hull[1],hull[2]) == 0:
                del(hull[2])
            else:
                if cross(hull[0], hull[1], hull[3]) == 0:
                    del(hull[3])
                else:
                    if cross(hull[1], hull[2], hull[3]) == 0:
                        del(hull[3])


    print('Convex hull points:')
    print(hull)
    nonhull = []
    for point in points:
        if point not in hull:
            nonhull.append(point)
    print('Non hull points:')
    print(nonhull)

    if len(hull) == 4:
        print('I:')
        print(hull[0], hull[2])
        print('J:')
        print(hull[1], hull[3])
    else:
        if len(hull) == 3:
            print('I:')
            print(hull[0],hull[1],hull[2])
            print('J:')
            print(nonhull[0])
        else:
            print('I:')
            print(hull[0],hull[1])
            print('J:')
            print(nonhull[0], nonhull[1])

points = [(0,0),(3,0),(4,0),(2,0)]
#points = [(2, 5), (3, 9), (4, 1), (0, 1)]
#points = [(2, 9), (8, 1), (6, 2), (3, 5)]

print(points)
Hull(points)
for point in points:
    plt.scatter(point[0],point[1])
plt.show()
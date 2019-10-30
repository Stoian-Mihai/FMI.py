from matplotlib import pyplot as plt
import math
points = [(26,77),(12,37),(14,18),(19,96),(71,95),(91,9),(98,43),(66,77),(2,75),(94,91)]

for point in points:
    plt.scatter(point[0],point[1])
#plt.show()

def plotWithLineOn(x):
    plt.clf()
    for i in range(0,100):
        plt.scatter(x,i, color='red', zorder=10)

    for point in points:
        plt.scatter(point[0], point[1])

    plt.show()

def distance(a, b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

def bruteForce():
    minDist = distance(points[0],points[1])
    minPoints = (points[0],points[1])
    for point1 in points:
        for point2 in points:

            if minDist > distance(point1,point2) and point1 != point2:
                minDist = distance(point1,point2)
                minPoints = (point1,point2)
    print(minDist)
    print(minPoints)


def divimp(v):
    if len(v) == 2:
        return distance(v[0],v[1])
    left = v[0][0]
    right = v[len(v) - 1][0]

    middle = (left+right)/2
    plotWithLineOn(middle)
    ind = 0
    for ind in range(len(v)):
        if v[ind][0] >= middle:
            break

    lowRight = divimp(v[ind:])
    lowLeft = divimp(v[:ind])
    if lowLeft < lowRight:
        return lowLeft
    return lowRight


points.sort()
print(points)

#plotWithLineOn(-1)
divimp(points)

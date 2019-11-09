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

def bruteForce(points):
    if len(points) < 2:
        return -1
    minDist = distance(points[0],points[1])
    minPoints = (points[0],points[1])
    for point1 in points:
        for point2 in points:

            if minDist > distance(point1,point2) and point1 != point2:
                minDist = distance(point1,point2)
                minPoints = (point1,point2)
    return minDist
    #print(minPoints)

def stripClose(points, line, mindist):
    minstrip = mindist
    for i in range(len(points)):
        if points[i][0] > line-mindist:
            #print(points[i])
            for j in range(i, len(points)):
                #print(points[j])
                if points[j][0] > line and points[j][1] > points[i][1] and points[j][0] < line+mindist:
                    minstrip = min(minstrip, distance(points[i], points[j]))
        if points[i][0] > line+mindist:
            break
    return minstrip

def divimp(v):
    if len(v) <= 3:
        return bruteForce(v)
    left = v[0][0]
    right = v[len(v) - 1][0]

    middle = (left+right)/2
    #plotWithLineOn(middle)
    ind = 0
    for ind in range(len(v)):
        if v[ind][0] >= middle:
            break

    lowRight = divimp(v[ind:])
    lowLeft = divimp(v[:ind])
    lowDist = min(lowRight, lowLeft)
    if lowRight == -1:
        lowDist = lowLeft
    elif lowLeft == -1:
        lowDist = lowRight
    stripDist = stripClose(points, middle, lowDist)
    lowDist = min(lowDist, stripDist)
    return lowDist

points.append((46, 3))
points.append((52, 10))

points.sort()
print(points)

d = 5

#plotWithLineOn(50)

print(divimp(points))

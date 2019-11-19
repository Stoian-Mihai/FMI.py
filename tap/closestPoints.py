from matplotlib import pyplot as plt
import math
points = [(26,77),(12,37),(14,18),(19,96),(71,95),(91,9),(98,43),(66,77),(2,75),(94,91)]

for point in points:
    plt.scatter(point[0],point[1])
#plt.show()

def binary_searchX(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

def merge(l1, l2):
    sorted_list = []

    l1 = l1[:]
    l2 = l2[:]

    while (l1 and l2):
        if (l1[0][1] <= l2[0][1]):
            item = l1.pop(0)
            sorted_list.append(item)
        else:
            item = l2.pop(0)
            sorted_list.append(item)

    sorted_list.extend(l1 if l1 else l2)

    return sorted_list

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
        return -1, (0,0)
    minDist = distance(points[0],points[1])
    minPoints = (points[0],points[1])
    for point1 in points:
        for point2 in points:

            if minDist > distance(point1,point2) and point1 != point2:
                minDist = distance(point1,point2)
                minPoints = (point1,point2)
    return minDist, minPoints
    #print(minPoints)


def stripClose(strip,d):
    size = len(strip)
    minstrip=d
    minPoints = ()
    for i in range(0,size):
        j=i+1
        while(j<size  and (strip[j][1]-strip[i][1])<minstrip):
            if distance(points[i], points[j]) < minstrip:
                minstrip = distance(points[i], points[j])
                minPoints = (points[i], points[j])
            j+=1
    return minstrip, minPoints

def divimp(v):
    if len(v) <= 3:
        minDist, minPoints = bruteForce(v)

        return minDist, minPoints, sorted(v,key=lambda x:x[1])
    left = v[0][0]
    right = v[len(v) - 1][0]

    middle = (left+right)/2
    #plotWithLineOn(middle)
    ind = int(len(v)/2)
    lowRight, minPointsRight, yRight = divimp(v[ind:])
    lowLeft, minPointsLeft, yLeft = divimp(v[:ind])

    Y = merge(yRight, yLeft)

    lowDist = min(lowRight, lowLeft)
    if lowRight == -1:
        lowDist = lowLeft
    elif lowLeft == -1:
        lowDist = lowRight

    lilY = []
    for el in Y:
        if el[0] > middle-lowDist:
            lilY.append(el)
    stripDist, stripPoints = stripClose(lilY, lowDist)
    lowDist = min(lowDist, stripDist)
    minPoints = (0,0)
    if lowDist == lowRight:
        minPoints = minPointsRight
    elif lowDist == lowLeft:
        minPoints = minPointsLeft
    elif lowDist == stripDist:
        minPoints = stripPoints
    return lowDist, minPoints, Y

points.append((46, 3))
points.append((52, 10))

points.sort()
print(points)

d = 5

#plotWithLineOn(50)

print(divimp(points)[0],divimp(points)[1] )

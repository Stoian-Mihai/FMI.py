from matplotlib import collections as mc
import pylab as pl

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def onSegment(x1, y1, x2, y2, x3, y3):  # trebuie ca P sa fie pe dreapta AB
    A = (x1, y1)
    B = (x2, y2)
    P = (x3, y3)
    minX = min(A[0], B[0])
    maxX = max(A[0], B[0])
    minY = min(A[1], B[1])
    maxY = max(A[1], B[1])

    if minX <= P[0] and maxX >= P[0]:
        if minY <= P[1] and maxY >= P[1]:
            return True
    return False


def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


def onLine(points, x, y):  # verificam daca este pe latura
    for i in range(0, len(points) - 1):
        X = area(points[i][0], points[i][1], x, y, points[i + 1][0], points[i + 1][1])
        if X == 0 and onSegment(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], x, y):
            return True
    return False


def InExterior(points, x, y):  # verificam daca este in exterior
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                if isInside(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1], x,
                            y) == True:
                    print("E in interior!")
                    return
    print("E in exterior!")


points = [(0, 0), (0, 2), (2, 2), (2, 0)]
x = 0
y = 4

if onLine(points, x, y):
    print("E pe latura!")
else:
    InExterior(points, x, y)


lines = []
for i in range(len(points)-1):
        lines.append([points[i], points[i+1]])
lines.append([points[0], points[-1]])
print(lines)
lc = mc.LineCollection(lines, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
pl.plot(x,y,'bo')
pl.show()
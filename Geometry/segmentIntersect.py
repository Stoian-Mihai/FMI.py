import matplotlib.pyplot as plt
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)

def slope(A,B):
    try:
        m = (A[1]-B[1]) / (A[0]-B[0])
        return m
    except:
        return None

def onSegment(A,B,P):
    minX = min(A[0],B[0])
    maxX = max(A[0],B[0])
    minY = min(A[1],B[1])
    maxY = max(A[1],B[1])

    if minX <= P[0] and maxX >= P[0]:
        if minY <= P[1] and maxY >= P[1]:
            return True
    return False


# A = (3,5)
# B = (1,5)
# C = (2,2)
# D = (2,6)
A = (1,1)
B = (3,1)
C = (2,1)
D = (4,1)
plt.scatter(A[0],A[1])
plt.scatter(B[0],B[1])
plt.scatter(C[0],C[1])
plt.scatter(D[0],D[1])
plt.show()



if slope(A,B) != slope(C,D):
    P = line_intersection((A, B), (C, D))
    if onSegment(A,B,P) and onSegment(C,D,P):
        print(P)
    else:
        print("Segments do not intersect")
else:
    intersectionA = None
    intersectionB = None
    # result = AB
    if (onSegment(C,B,A) and onSegment(A,D,B)) or (onSegment(D,B,A) and onSegment(A,C,B)):
        intersectionA = A
        intersectionB = B
    # result = AC
    if (onSegment(D,C,A) and onSegment(A,B,C)) or (onSegment(B,C,A) and onSegment(A,D,C)):
        intersectionA = A
        intersectionB = C
    # result = AD
    if (onSegment(B,D,A) and onSegment(A,C,D))or (onSegment(C,D,A) and onSegment(A,B,D)):
        intersectionA = A
        intersectionB = D
    # result = BC
    if (onSegment(A,C,B) and onSegment(B,D,C)) or (onSegment(D,C,B) and onSegment(B,A,C)):
        intersectionA = B
        intersectionB = C
    # result = BD
    if (onSegment(A,D,B) and onSegment(B,C,D)) or (onSegment(C,D,B) and onSegment(B,A,D)):
        intersectionA = B
        intersectionB = D
    # result = CD
    if (onSegment(A,D,C) and onSegment(C,B,D)) or (onSegment(B,D,C) and onSegment(C,A,D)):
        intersectionA = C
        intersectionB = D

    A, B = B, A
    C, D = D, C

    # result = AB
    if (onSegment(C, B, A) and onSegment(A, D, B)) or (onSegment(D, B, A) and onSegment(A, C, B)):
        intersectionA = A
        intersectionB = B
    # result = AC
    if (onSegment(D, C, A) and onSegment(A, B, C)) or (onSegment(B, C, A) and onSegment(A, D, C)):
        intersectionA = A
        intersectionB = C
    # result = AD
    if (onSegment(B, D, A) and onSegment(A, C, D)) or (onSegment(C, D, A) and onSegment(A, B, D)):
        intersectionA = A
        intersectionB = D
    # result = BC
    if (onSegment(A, C, B) and onSegment(B, D, C)) or (onSegment(D, C, B) and onSegment(B, A, C)):
        intersectionA = B
        intersectionB = C
    # result = BD
    if (onSegment(A, D, B) and onSegment(B, C, D)) or (onSegment(C, D, B) and onSegment(B, A, D)):
        intersectionA = B
        intersectionB = D
    # result = CD
    if (onSegment(A, D, C) and onSegment(C, B, D)) or (onSegment(B, D, C) and onSegment(C, A, D)):
        intersectionA = C
        intersectionB = D
    if not (onSegment(A,B,C) or onSegment(B,A,C) or onSegment(A,B,D) or onSegment(B,A,D) or onSegment(C,D,A)
             or onSegment(C,D,B) or onSegment(D,C,A) or onSegment(C,D,A)):
        intersectionA = None
        intersectionB = None

    if intersectionA and intersectionB:
        print(intersectionA, intersectionB)
    else:
        print("Segments do not intersect")

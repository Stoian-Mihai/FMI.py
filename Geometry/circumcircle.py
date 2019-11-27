import math
e = 0.0000001
def dist(A,B):
    distance = (B[1] - A[1]) * (B[1] - A[1]) + (B[0] - A[0]) * (B[0] - A[0])
    return distance
def cos(O, A, B):
    OA = dist(O,A)
    OB = dist(O,B)
    AB = dist(A,B)
    cosinus = (OA + OB - AB) / (2*math.sqrt(OA*OB))
    return cosinus
def cross(A, B, C):
    val = (B[1] - A[1]) * (C[0] - B[0]) - (B[0] - A[0]) * (C[1] - B[1])
    if val == 0:
        return 0 #coliniar
    if val > 0:
        return 1 #inverntrigonometric
    else:
        return 2 #trigonometric

A1 = (0,0)
A2 = (0,2)
A3 = (2,2)
A4 = (5,1)
#A4 = (1,1)
# A1 = (0,0)
# A2 = (2,2)
# A3 = (2,0)
# A4 = (0,2)
# A1 = (0,4)
# A2 = (3,4)
# A3 = (4,2)
# A4 = (3,0)
if cross(A2,A3,A4) == cross(A3,A4,A1) == cross(A4,A1,A2) == cross(A1,A2,A3):
    print("convex")
else:
    print("nu este convex")

# In[44]:

cosA2 = cos(A2,A1,A3)
cosA4 = cos(A4,A1,A3)


if abs(cosA2+cosA4) < e:
    print("A4 este pe cerc")
elif cosA2+cosA4 < 0:
    print("A4 este in interior")
else:
    print("A4 este in exteriorul cercului")


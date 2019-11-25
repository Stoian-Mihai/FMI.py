# The robot can go only down or right
# Find the maximum points path in O(nm)

import copy

table = []
table.append([2,1,4])
table.append([1,3,2])
table.append([1,6,1])


for i in range(len(table)):
    table[i].append(0)
table.append([0]*len(table[1]))

distTable = copy.deepcopy(table)
for i in range(0,len(distTable)-1).__reversed__():
    for j in range(0,len(distTable[i])-1).__reversed__():
        distTable[i][j] = distTable[i][j] + max(distTable[i+1][j],distTable[i][j+1])

i = 0
j = 0
while i != len(table)-1 and j != len(table[1])-1:
    print(i,j)
    if distTable[i+1][j] > distTable[i][j+1]:
        i = i+1
    else:
        j = j+1

print(distTable)
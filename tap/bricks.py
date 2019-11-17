bricks =[(9,2),(9,3),(9,1),(8,3),(8,2),(8,4),(7,5),(7,6)]
ln = [0] * len(bricks)
nr = [0] * len(bricks)
solar = [0] * len(bricks)
bricks.sort()
print(bricks)
nr[0] = 1
ln[0] = bricks[0][0]

for i in range(1,len(bricks)):
    brickLen = bricks[i][0]
    brickColor = bricks[i][1]
    #Going back till we meet a len smaller than 8
    k = 0
    for k in reversed(range(0,i)):
        if bricks[k][0] != brickLen:
            break

    newBrickLen = bricks[k][0]
    numberOfSol = 0
    sol = []

    len = 0

    if k == 0:
        len = brickLen
        numberOfSol = 1
    else:
        #Going back and checking only  for the new len
        len = brickLen + ln[k]
        for k in reversed(range(0,k+1)):
            newBrick = bricks[k]
            if newBrick[0] != newBrickLen:
                break
            if newBrick[1] == brickColor:
                continue
            numberOfSol += nr[k]
            sol.append(k)


    ln[i] = len
    nr[i] = numberOfSol
    solar[i] = sol

print(ln)
indx = ln.index(max(ln))
print(nr)
print(solar)
print(indx)
print('\n')
print(bricks[indx])

while True:
    try:
        print(bricks[solar[indx][0]])
        indx = solar[indx][0]
    except:
        break

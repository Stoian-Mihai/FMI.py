def applyTurn(direction):
    if direction is 'E':
        direction = 'S'
        return direction
    if direction is 'S':
        direction = 'W'
        return direction
    if direction is 'W':
        direction = 'N'
        return direction
    if direction is 'N':
        direction = 'E'
        return direction

def applyMoveWithPrint(sX, sY, direction, type, count):
    if type is 'F':
        if direction is 'E':
            for i in range(1,count + 1):
                sX = sX + 1
                print(sX,sY)
            return sX, sY, direction
        if direction is 'S':
            for i in range(1,count + 1):
                sY = sY + 1
                print(sX, sY)
            return sX, sY, direction
        if direction is 'W':
            for i in range(1,count + 1):
                sX = sX - 1
                print(sX, sY)
            return sX, sY, direction
        if direction is 'N':
            for i in range(1,count + 1):
                sY = sY - 1
                print(sX, sY)
            return sX, sY, direction

    if type is 'T':
        for i in range(0,count):
            direction = applyTurn(direction)
    return sX, sY, direction

def applySmallFowardMove(sX, sY, direction):
    if direction is 'E':
        sX = sX + 1
        return sX, sY, direction
    if direction is 'S':
        sY = sY + 1
        return sX, sY, direction
    if direction is 'W':
        sX = sX - 1
        return sX, sY, direction
    if direction is 'N':
        sY = sY - 1
        return sX, sY, direction


    #for i in range(1,count):
       # sX, sY, direction = applySmallFowardMove(sX,sY,direction)



speed = 1

#inpt = 'F 1 T 1 F 5'
inpt = 'F 1 T 3 F 2 T 1 F 1 T 1 F 4 T 3 F 1 T 3 F 2 T 1 F 1'
inpt = inpt.split(' ')

a = ''
sX  = 0
sY  = 2
sX = int(sX)
sY = int(sY)
direction = 'E'

tick = -1
speedCount = 0.0
aux1 = 1
arr = []
for b in inpt:
    if a is '':
        a = b
        continue
    #print(a,b)
    #sX, sY, direction, speed, speedCount = \
    b = int(b)
    if a is 'T':
        for i in range(0,b):
            direction = applyTurn(direction)
        a = ''
        continue
    # type is F
    i = 1
    while i <= b:
        tick = tick + 1

        speedCount = speedCount + speed
        arr.append((sX,sY))
        if(speedCount >= aux1):
        #while(speedCount >= aux1):
            sX, sY, direction = applySmallFowardMove(sX,sY,direction)
            sX, sY, direction = applySmallFowardMove(sX, sY, direction)
            aux1 = aux1 + 1
            i = i + 2
        print(tick, sX, sY)
        #speedCount = speedCount + speed
        # speedCount = speedCount + speed

        arr.append((sX, sY))

    a = ''
    #print(sX, sY)

#print(arr)
# f = open("inputFile","r")
# inn = f.readlines()
# for i in range(0,len(inn)):
#     inn[i] = inn[i].replace('\n', '')
#
# aliensCount = int( inn[0] )
# alienSpawn = []
#
# for i in range(1,aliensCount + 1):
#     alienSpawn.append(inn[i])
#
# queriesCount = int(inn[1 + aliensCount])
#
# for i in range(1 + aliensCount + 1, 1 + aliensCount + queriesCount + 1):
#     aux2 = inn[i].split(' ')
#     afterTick = int(aux2[0])
#     alien = int(aux2[1])
#     theTick = afterTick - int(alienSpawn[alien])
#     p,l = arr[theTick]
#     print(afterTick, alien, p, l)


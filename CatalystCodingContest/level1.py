
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

def applyMove(sX, sY, direction, type, count):
    if type is 'F':
        if direction is 'E':
            sX = sX + count
            return sX, sY, direction
        if direction is 'S':
            sY = sY + count
            return sX, sY, direction
        if direction is 'W':
            sX = sX - count
            return sX, sY, direction
        if direction is 'N':
            sY = sY - count
            return sX, sY, direction

    if type is 'T':
        for i in range(0,count):
            direction = applyTurn(direction)
    return sX, sY, direction



inpt = 'F 1 T 1 F 5'
inpt = inpt.split(' ')

a = ''
sX  = 0
sY  = 0
sX = int(sX)
sY = int(sY)
direction = 'E'

for b in inpt:
    if a is '':
        a = b
        continue
    #print(a,b)
    sX, sY, direction = applyMove(sX, sY, direction, a, int(b))
    a = ''
    #print(sX, sY)

print(sX, sY)
# Find the smallest subset of overlapping intervals that fit a bigInterval

bigInterval = (10,20)
#bigInterval = (13,28)
intervals = [(10,12),(4,15),(5,11),(14,18),(14,21)]
#intervals = [(1,12),(3,20),(15,19),(25,34),(17,23),(24,25),(13,20),(11,16),(23,27)]
intervals.sort(key=lambda x:x[1], reverse=True)

#print(intervals)

left = bigInterval[0]
result = []
while(True):
    bestOption = ()
    for i in range(0,len(intervals)):
        currentInterval = intervals[i]
        if currentInterval[0] <= left:
            if bestOption == ():
                bestOption = currentInterval
            else:
                if bestOption[1] < currentInterval[1]:
                    bestOption = currentInterval

    left = bestOption[1]
    result.append(bestOption)
    if bestOption[1] >= bigInterval[1]:
        break


print(result)
# in:
# 6
# 11 13 10 15 12 7
# out:
# 11 10 7
# 13 12
# 15

import heapq

v = [11,13,10,15,12,7]
sub = []
for _ in range(len(v)):
    sub.append([])
for el in v:
    for i in range(0,len(v)):
        if(len( sub[i] )==0):
            sub[i].append(el)
            break
        else:
            if(sub[i][-1] > el):
                sub[i].append(el)
                break

sub2 = [x for x in sub if x != []]
sub = sub2
print(sub)
for i in range(len(sub)):
    sub[i].reverse()
result = []
for i in range(len(v)):
    small_pile = sub[0]
    result.append(small_pile.pop(0))
    if small_pile:
        heapq.heapreplace(sub, small_pile)
    else:
        heapq.heappop(sub)


print(result)
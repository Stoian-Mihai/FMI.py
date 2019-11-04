# in:
# 6
# 11 13 10 15 12 7
# out:
# 11 10 7
# 13 12
# 15



import heapq
def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][-1] < x:
            lo = mid+1
        else:
            hi = mid
    return lo



v = [11,13,10,15,12,7]
sub = []

for el in v:
    i = binary_search(sub, el)
    if i  >=  len(sub):
        sub.append([])
        sub[i].append(el)
    else:
        if sub[i][-1] > el:
            sub[i].append(el)



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
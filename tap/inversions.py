inv = 0

def merge(a, b):
    c = []
    i = 0
    j = 0
    global inv
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            inv += 1
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    return c


def smallSort(v):
    s = []
    if len(v) == 2:
        if v[0]<v[1]:
            s = v
        else:
            s = [v[1], v[0]]
    else:
        return v
    return s

def mergeSort(v, i, j):
    mid = (i+j)//2
    if len(v[i:j]) <= 2:
        return smallSort(v[i:j])
    return merge(mergeSort(v, i, mid), mergeSort(v, mid, j))


arr = [2, 4, 1, 3, 5]

arr = mergeSort(arr,0, len(arr))
print(arr)
print(inv)

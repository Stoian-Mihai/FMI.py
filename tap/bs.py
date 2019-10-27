v = [-7,-1,0,2,3,5,7]
ind = [0,1,2,3,4,5,6]
def find(v, ind):
    m = int(len(v)/2)
    if len(v) == 0:
        return False
    if len(v) == 1 and v[0] != ind[0]:
        return False
    if v[m] == ind[m]:
        return v[m]
    if v[m] < ind[m]:
        return find(v[m:], ind[m:])
    else:
        return find(v[:m], ind[:m])

print(find(v, ind))

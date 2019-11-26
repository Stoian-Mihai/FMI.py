import copy

n = 6
V = [1,-5,9,8,12,-5]

T = []
for i in range(0,n+1):
    T.append([])
a = copy.deepcopy(T)
for i in range(0, n+1):
    for j in range(0,n+1):
        T[i].append(0)


for i in range(0, n):
    T[i][i] = V[i]

for i in range(0,n):
    T[i][i+1] = max(T[i][i],T[i+1][i+1])
    if T[i][i+1] == T[i][i]:
        T[i+1][i] = i
    else:
        T[i+1][i] = i+1


for gap in range(2,n):
    for i in range(0,n-gap):
        j = i+gap
        T[i][j] = max(V[i]+min(T[i+1][j-1],T[i+2][j]),
                      V[j]+min(T[i+1][j-1],T[i][j-2]))

        if T[i][j] == V[i]+min(T[i+1][j-1],T[i+2][j]):
            T[j][i] = i
        else:
            T[j][i] = j

for i in range(0,n):
    print(T[i][:-1])

print("JOC:")
i = 0
j = 5
pct_calc = 0
while(1):
    print(V[i:j + 1])
    if T[j][i] == i:
        a = V[i]
        i += 1
    else:
        a = V[j]
        j -= 1
    pct_calc += V[i]
    print('calculatorul a ales ' + str(a))

    print(V[i:j+1])
    el = input()
    a = 0
    if int(el) == V[i]:
        a = V[i]
        i += 1
    else:
        a = V[j]
        j -= 1
    print('ai ales' + str(a))

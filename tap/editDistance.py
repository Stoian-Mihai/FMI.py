s1 = 'carte'
s2 = 'antet'
T = [[i] for i in range(0, len(s2)+1)]
for i in range(0,len(T)):
    for j in range(1,len(s1)+1):
        T[i].append(j)

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            T[i][j] = T[i-1][j-1]
        else:
            T[i][j] = 1 + min(T[i-1][j-1], T[i-1][j], T[i][j-1])


i = len(s2)
j = len(s1)

while i != 0 or j != 0:
    minT = min(T[i - 1][j - 1], T[i - 1][j], T[i][j - 1])
    if s2[i - 1] == s1[j - 1]:
        print('pastram '+s2[i-1])
        i -= 1
        j -= 1
    elif minT == T[i-1][j-1]:
        print('inlocuim '+s2[i-1]+'-'+s1[j-1])
        i -= 1
        j -= 1
    elif minT == T[i-1][j]:
        print('inseram '+s2[i-1])
        i -= 1
    else:
        print('stergem '+s1[j-1])
        j -= 1



print(T[len(s2)][len(s1)])
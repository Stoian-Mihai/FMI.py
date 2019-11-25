s1 = 'harpa'
s2 = 'armura'

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


print(T[len(s2)][len(s1)])
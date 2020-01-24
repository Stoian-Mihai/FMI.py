# https://www.youtube.com/watch?v=WPr1jDh3bUQ

s = "banana"
d = [0]*len(s)
for i in range(len(d)):
    d[i] = [0]*len(s)

# Checking for 1 char long strings
for i in range(len(d)):
    d[i][i] = True

# Checking for 2 char long strings
for i in range(len(d)-1):
    if (s[i] == s[i+1]):
        d[i][i+1] = True
    else:
        d[i][i+1] = False


for gap in range(2, len(d)):
    for i in range(0, len(d)-gap):
        j = i+gap
        if s[i] != s[j]:
            d[i][j] = False
        else:
            d[i][j] = d[i+1][j-1]


for i in d:
    print(i)

cuts = [0]*len(s)

for i in range(len(s)):
    temp = 999
    if d[0][i]:
        cuts[i]=0
    else:
        for j in range(i):
            if d[j+1][i] and temp > cuts[j]+1:
                temp = cuts[j]+1

        cuts[i] = temp

print(cuts)

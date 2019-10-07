history = []
score = {}
n = int(input())
for i in range(0,n):
    inp = input().split(' ')
    if inp[0] not in score.keys():
        score[inp[0]] = int(inp[1])
    else:
        score[inp[0]] += int(inp[1])
    history.append((inp[0],inp[1]))

maxp = (list(score.keys())[0],score[list(score.keys())[0]])
for par in list(score.keys()):
    if score[par] > maxp[1]:
        maxp = (par, score[par])

print(str(maxp[0]) + ' is winner!')
winnerScore = maxp[1]
for el in history:
    if int(el[1]) > winnerScore:
        print(el)
adjList = {}
n = 8
adjList[1] = [2,3]
adjList[2] = [1,4,5]
adjList[3] = [6,7,1]
adjList[5] = [2,8]
adjList[4] = []
adjList[6] = []
adjList[7] = []
adjList[8] = []

ok = [1] * (n+1)
vis = [0] * (n+1)
def DF(i):
    ok[i] = 0
    for j in adjList[i]:
        if vis[j] == 0:
            vis[j] = 1
            DF(j)

        if(ok[j]== 1):
            ok[i] = 1

    if ok[i] == 0:
        print(i)
        ok[i] = 1

print(1)
DF(1)
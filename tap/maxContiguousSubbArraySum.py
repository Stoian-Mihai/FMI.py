# Subsecventa de suma maxima
# https://www.youtube.com/watch?v=2MmGzdiKR9Y

arr = [-2,1,-3,4,-1,2,1,-5,4]
dp = [0]*len(arr)
past = [0]*len(arr)
dp.append(arr[0])
for i in range(1,len(arr)):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    if dp[i] == arr[i]:
        past[i] = i
    else:
        past[i] = i-1

ind = dp.index((max)(dp))
while past[ind] != ind:
    print(arr[past[ind]])
    ind = past[ind]




arr = [3,2,1,5,6,4]
k = 3

while True:
    if len(arr) is 1:
        print(arr[0])
        break
    pivot = arr[0]
    arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
    i = 0
    j = 1
    while arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1
    if arr[i] > arr[len(arr)-1]:
        arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
    else:
        i += 1
        arr[i], arr[len(arr) - 1] = arr[len(arr) - 1], arr[i]
    #print(arr)
    if i < k:
        arr = arr[i+1:]
        k = k - i - 1
    elif i > k:
        arr = arr[:i]
        #k = k - i - 1
    elif i == k:
        print(arr[i])
        break
    #print(k)

# The array is a mountain array
# Find the peak element
# We use divide et impera
# and we go with the upper trend
arr = [2,4,5,9,10,12,9,7,4,3]

def findPeak(arr, left, right):
    mid = int((left+right)/2)
    dbg = arr[mid]
    if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
        return arr[mid]
    if arr[mid]<arr[mid+1]: # right
        return findPeak(arr, mid, right)
    elif arr[mid]<arr[mid-1]: # left
        return findPeak(arr, left, mid)

print(findPeak(arr,0,len(arr)))
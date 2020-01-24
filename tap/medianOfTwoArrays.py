a = [1,3,8,9,15]
b = [7,11,18,19,21,25]

start = 0
end = len(a)

while True:
    partitionA = (start + end)//2
    partitionB = (len(a)+len(b)+1)//2 - partitionA
    Aleft = a[0:partitionA]
    Aright = a[partitionA:]
    Bleft = b[0:partitionB]
    Bright = b[partitionB:]
    if Aleft[-1] <= Bright[0] and Bleft[-1] <= Aright[0]:
        print(max(Aleft[-1], Bleft[-1]))
        break
    else:
        if not Bleft[-1] <= Aright[0]: #going right
            start = partitionA + 1
        elif not Aleft[-1] <= Bright[0]: #going left
            end = partitionA - 1


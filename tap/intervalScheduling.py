# Examen tap 2018 iarna
# Interval Scheduling
# Given n Intervals we need to find the maximum subset of intervals
# that doesn't overlap
# Solution:
# We need to sort the intervals basted on the end time of the interval
# And pick only those that don't overlap
# https://www.youtube.com/watch?v=nUShpavQae8


intervals = [(2,4),(1,5),(3,7),(5,6),(7,8)]
intervals.sort(key=lambda x:x[1])
print(intervals)
solution = []
solution.append(intervals[0])
for i in range(1,len(intervals)):
    if solution[-1][1] < intervals[i][0]:
        solution.append(intervals[i])
print(solution)
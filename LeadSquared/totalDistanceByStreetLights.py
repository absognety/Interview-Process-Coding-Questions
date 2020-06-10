"""
Coding Test - Round 1

Given N street lights, and an array of tuples which signify the start and 
end distances of street covered by that street light.

Find the total distance covered by all the street lights

Ex:1
    N = 1
    arr = [(5,10)]
    Number of street lights = 1
    and distance covered by street light i is 5m to 10m which is 10-5 = 5m
    
Ex:2  
    N = 2
    arr = [(5,10),(8,12)]
    Number of street lights = 2
    street light 0 = 10 - 5 = 5
    street light 1 = 12 - 8 = 4
    common region = 10 - 8 = 2
    total distance = (5 + 4 - 2) = 7
    
"""

def total_distance(intervals):
    if not intervals:
        return 0
    if len(intervals) == 1:
        return abs(intervals[0][0] - intervals[0][1])
    result = 0
    common = 0
    intervals = sorted(intervals,key=lambda x: x[0])
    for i in range(len(intervals)):
        result += abs(intervals[i][0] - intervals[i][1])
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            common += abs(intervals[i][1] - intervals[i+1][0])
    result = abs(result - common)
    return result

if __name__ == '__main__':
    arr1 = [(5,10)]
    print (total_distance(arr1))
    arr2 = [(5,10),(8,12)]
    print (total_distance(arr2))
    
    #subset testcase
    arr3 = [(2,9),(3,6)]
    print (total_distance(arr3))
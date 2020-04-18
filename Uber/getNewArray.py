"""
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except 
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
[2, 3, 6].
"""

def productOfArray(arr):
    prod = 1
    for a in arr:
        prod = prod * a
    return prod

def newArray(arr):
    n = len(arr)
    new_arr = [None]*n
    for i in range(n):
        item = arr.pop(i)
        x = productOfArray(arr)
        new_arr[i] = x
        arr.insert(i,item)
    return new_arr
    
if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        arr = list(map(int,input().strip().split()))
        print (newArray(arr))
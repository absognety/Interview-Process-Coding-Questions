"""
Daily Coding Problem #1
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the 
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def isPairWithGivenSum(arr,n,x):
    left,right = 0,n-1
    arr = sorted(arr)
    while left < right:
        if ((arr[left] + arr[right]) < x):
            left += 1
        elif (arr[left] + arr[right] == x):
            return True
        elif (arr[left] + arr[right] > x):
            right -= 1
    return False

if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        arr = list(map(int,input().strip().split()))
        n = len(arr)
        x = int(input())
        print (isPairWithGivenSum(arr,n,x))
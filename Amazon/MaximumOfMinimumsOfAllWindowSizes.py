#User function Template for python3
"""
Given an integer array A[] of size N. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to n.

Input:
The first line contains an integer T denoting the total number of test cases. In each test cases, the first line contains an integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
In each seperate line, print the array of numbers of size N for each of the considered window size 1, 2 , ..., N respectively.

User Task:
The task is to complete the function printMaxOfMin() which finds the maximum of minimum of every window size.

Constraints:
1 <= T <= 50
1 <= N <= 10^5
1 <= A[i] <= 10^6

Example:
Input: 
2
7
10 20 30 50 10 70 30
3
10 20 30
Output: 
70 30 20 10 10 10 10 
30 20 10

Explaination:
Testcase 1:
First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10}, {70} and {30}. Maximum of these minimums is 70.
Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10}, and {30}. Maximum of these minimums is 30.
Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. Maximum of these minimums is 20.
Similarly other elements of output are computed.
Testcase 2: First element in output indicates maximum of minimums of all windows of size 1.Minimums of windows of size 1 are {10} , {20} , {30}. Maximum of these minimums are 30 and similarly other outputs can be computed. 
"""
'''
Function Arguments :
      @param  : a(given array), n (size of array)
      @return : None, print the required Maxofmin array.
'''

def printMaxOfMin(a,n):
    # code here
    s = []
    left = [0 for i in range(n+1)]
    right = [0 for i in range(n+1)]
    left[:n] = [-1]*n
    right[:n] = [n]*n
    for i in range(0,n):
        while (len(s) != 0 and a[s[-1]] >= a[i]):  
            s.pop() 
        if (len(s) != 0):
            left[i] = s[-1]
        s.append(i)
    while (len(s) != 0):
        s.pop()
    for i in range(n-1,-1,-1):
        while (len(s) != 0 and a[s[-1]] >= a[i]):
            s.pop() 
        if (len(s) != 0):
            right[i] = s[-1]
        s.append(i)
    ans = [0]*(n+1)
    for i in range(0,n):
        length = right[i] - left[i] - 1
        ans[length] = max(ans[length],a[i])
    for i in range(n-1,0,-1):
        ans[i] = max(ans[i],ans[i+1])
    for i in range(1,n+1):
        print (ans[i],end=" ")
    print ("")
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        printMaxOfMin(a,n)

# } Driver Code Ends
{
#Initial Template for Python 3
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        segragate012(a,n)
        print(*a)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
''' Your task to is sort the array a of 0s,1s and 2s
    of size n. You dont need to return anything.'''
def segragate012(a,n):
    #code here
    c0 = a.count(0)
    c1 = a.count(1)
    c2 = a.count(2)
    for i in range(c0):
        a[i] = 0
    for i in range(c0,c0+c1):
        a[i] = 1
    for i in range(c0+c1,c0+c1+c2):
        a[i] = 2
    #print (" ".join(str(i) for i in a),end="")
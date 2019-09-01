{
# Initial Template for Python 3
import math
def main():
    T = int(input())
    while(T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        print(equilibriumPoint(A, N))
        T -= 1
if __name__ == "__main__":
    main()

}
''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3
# Complete this function
def equilibriumPoint(A, N):
    # Your code here
    if len(A)==1:
        return 1
    else:
        eqlist = []
        for i in range(1,N-1):
            if sum(A[:i]) == sum(A[i+1:]):
                eqlist.append(i+1)
        if sum(A[1:]) == 0:
            eqlist.insert(0,1)
        if sum(A[:N-1]) == 0:
            eqlist.append(N)
    if eqlist:
        return min(eqlist)
    else:
        return -1
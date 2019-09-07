{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            stockBuySell(arr,n)
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def stockBuySell(A,n):
    if A == sorted(A):
        print ("(" + str(0) + " " + str(n-1) + ")",end=" ")
    elif A == sorted(A,reverse=True):
        print ("No Profit",end = " ")
    else:
        local_min = []
        local_max = []
        for i,v in enumerate(A):
            if i == 0:
                if v < A[i+1]:
                    local_min.append(i)
            elif i == n-1:
                if v > A[i-1]:
                    local_max.append(i)
            else:
                if A[i-1] <= v and v >= A[i+1]:
                    local_max.append(i)
                if A[i-1] >= v and v <= A[i+1]:
                    local_min.append(i)
        if len(local_max) == len(local_min):
            for i in range(len(local_max)):
                x = " ".join([str(local_min[i]),str(local_max[i])])
                print ("("+x+")",end=" ")
        else:
            x = " ".join([str(max(local_min)),str(max(local_max))])
            print ("("+x+")",end = " ")
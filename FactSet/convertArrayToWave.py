{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def convertToWave(A,N):
    #Your code here
    temp=0
    for i in range(N-1):
        if i%2 == 0:
            if A[i] < A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
            else:
                continue
        else:
            if A[i] > A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
            else:
                continue
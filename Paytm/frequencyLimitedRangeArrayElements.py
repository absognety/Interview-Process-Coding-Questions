{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        printfrequency(A,N)
        
        print()
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def printfrequency(A,N):
    #Your Code here
    import collections
    freq_dict = collections.Counter(A)
    for i in range(1,N+1):
        print (freq_dict[i],end=" ")
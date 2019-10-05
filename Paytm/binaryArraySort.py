{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            
            binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def binSort(arr, n): 
    #Your code here
    
    
    '''
    No need to print the array
    '''
    c0 = arr.count(0)
    c1 = arr.count(1)
    for i in range(c0):
        arr[i] = 0
    for i in range(c0,c0+c1):
        arr[i] = 1
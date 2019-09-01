{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            print(maxIndexDiff(arr,n))
            
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def maxIndexDiff(arr, n): 
    ##Your code here
    maxxDiff = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<=arr[j]:
                if maxxDiff < j - i:
                    maxxDiff = j - i
    return maxxDiff
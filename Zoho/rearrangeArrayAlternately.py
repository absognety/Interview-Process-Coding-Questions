{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            arre = rearrange(arr,n)
            
            for i in arre:
                print(i,end=" ")
            
            print()
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def rearrange(arr, n): 
    ##Your code here
    if n%2 == 0:
        for i in range(n//2):
            arr.append(arr[n-1-i])
            arr.append(arr[i])
    else:
        for i in range(n//2):
            arr.append(arr[n-1-i])
            arr.append(arr[i])
        arr.append(arr[math.floor(n/2)])
    arr[:] = arr[n:]
    return arr
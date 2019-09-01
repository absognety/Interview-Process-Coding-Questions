{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(missingNumber(arr,n))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def missingNumber(arr,n):
    #Your code here
    poss = [x for x in arr if x > 0]
    if poss:
        if poss == list(range(1,n+1)):
            return max(poss)+1
        else:
            min_poss = min(poss)
            max_poss = max(poss)
            total_range = list(range(1,max_poss+1))
            missingNumbers = set(total_range) - set(poss)
            return min(missingNumbers)
    else:
        return 0
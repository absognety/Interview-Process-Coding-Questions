{
import math
//Position this line where user code will be pasted.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(josephus(n,k))
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#Complete this function
def josephus(n,k):
    #Your code here
    if n == 1:
        return n
    return ((josephus(n-1,k)+k-1)%n + 1)
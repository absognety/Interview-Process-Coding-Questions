{
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        possibleWords(a,N)
        
        print()
       
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def possibleWords(a,N):
    ##Your code here
    import itertools
    ph = {'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9}
    my_sts = []
    for x in a:
        for k,v in ph.items():
            if v == x:
                my_sts.append(k)
    if len(my_sts)>1:
        res = list(itertools.product(*my_sts))
        res = [''.join(u) for u in res]
        print (' '.join(i for i in res))
    else:
        print (' '.join(list(my_sts[0])))
{
#Initial Template for Python 3
    
def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=input().strip().split()
        
        winner(arr,n)
        print()
        
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def winner(arr,n):
    #Your code here
    import collections
    votes = collections.Counter(arr)
    maxVotes = max(votes.values())
    if len(set(votes.values())) != len(votes.values()):
        maxVoteNames = []
        for k,v in votes.items():
            if v == maxVotes:
                maxVoteNames.append(k)
        print (min(maxVoteNames),maxVotes,end="")
    else:
        for k,v in votes.items():
            if v == maxVotes:
                print (k,maxVotes,end="")
                return
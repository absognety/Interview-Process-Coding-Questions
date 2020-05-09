"""
This question is asked in Interview
    
There are n stairs, a person standing at the bottom wants to reach the 
top. The person can climb either 1 stair or 2 stairs at a time. Count 
the number of ways, the person can reach the top.

Example:
    number of stairs = 5
    steps allowed = 1 or 2
"""

def countWays(n,m):
    """
    Solution to above problem:
        Pros: 
            It will consider all the possible steps from 1 to given m.
        Cons:
            No control by external user (if user wants to give only certain step values
            say in the form of an array).
    """
    res = [None] * (n+1)
    temp = 0
    res[0] = 1
    for i in range(1,n+1):
        s = i - m - 1
        e = i - 1
        if s >= 0:
            temp -= res[s]
        temp += res[e]
        res[i] = temp
        print (res)
    return res[n]

if __name__ == '__main__':
    n,m = 5,2
    print (countWays(n,m))
    n,m = 5,3
    print (countWays(5,3))


def countWays1(n,args):
    """
    Solution that mitigates the cons of above solution
    Give allowed step values in the form of an array (here it is args)
    """
    m = len(args)
    count = [0 for i in range(n + 1)] 
      
    # base case 
    count[0] = 1
      
    # Count ways for all values up  
    # to 'N' and store the result 
    for i in range(1, n + 1): 
        for j in range(m): 
  
            # if i >= arr[j] then 
            # accumulate count for value 'i' as 
            # ways to form value 'i-arr[j]' 
            if (i >= args[j]): 
                count[i] += count[i - args[j]] 
      
    # required number of ways  
    return count[n] 

if __name__ == '__main__':
    print (countWays1(5,[2,3]))
    print (countWays1(5,[1,3,4]))
    print (countWays1(4,[1,3,4]))
    print (countWays1(10,[1,3,4]))
    print (countWays1(6,[3,2]))
    print (countWays1(5,[1,2,3]))
    print (countWays1(4,[1]))
    print (countWays1(4,[2]))
    print (countWays1(6,[3]))
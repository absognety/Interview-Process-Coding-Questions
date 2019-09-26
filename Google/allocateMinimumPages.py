import math
def isValid(arr,n,k,mi):
    std = 1
    curr = 0
    for i in range(n):
        if curr + arr[i] > mi:
            curr = arr[i]
            std += 1
            if std > k:
                return False
        else:
            curr += arr[i]
    return True

def allocMinPages(arr,n,k):
    if k > n:
        return -1
    s,totalpage = 0,0
    for i in range(n):
        totalpage += arr[i]
        s = max(s,arr[i])
    e = totalpage
    finalAns = s
    while s <= e:
        mid = math.floor((s+e)/2)
        if isValid(arr,n,k,mid):
            finalAns = mid
            e = mid - 1
        else:
            s = mid + 1
    return finalAns
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        M = int(input())
        print (allocMinPages(arr,N,M))
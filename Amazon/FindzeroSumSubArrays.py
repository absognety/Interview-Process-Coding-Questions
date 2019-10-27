def subArrayExists(arr,n):
    ##Your code here
    hashMap = {}
    out = []
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]
        if sum1==0:
            out.append((0,i))
        al = []
        if sum1 in hashMap:
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it]+1,i))
        al.append(i)
        hashMap[sum1] = al
    return len(out)
    
    
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print (subArrayExists(arr,n))
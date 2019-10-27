def contains123(arr):
    c = {'1','2','3'}
    tracker = []
    arr = sorted(arr)
    for i in arr:
        a = set(str(i))
        if a.issubset(c):
            print (i,end=" ")
            tracker.append(1)
        else:
            tracker.append(0)
    if len(set(tracker))==1 and 0 in tracker:
        print (-1,end="")

if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        contains123(arr)
        print ('\n',end="")
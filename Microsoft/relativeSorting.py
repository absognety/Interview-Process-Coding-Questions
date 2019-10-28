def relativeSorting(A1,A2):
    common_elements = set(A1).intersection(set(A2))
    extra = set(A1).difference(set(A2))
    out = []
    for i in A2:
        s = [i] * A1.count(i)
        out.extend(s)
    extra_out = []
    for j in extra:
        u = [j] * A1.count(j)
        extra_out.extend(u)
    out = out + sorted(extra_out)
    return " ".join(str(i) for i in out)
    
if __name__ == '__main__':
    t = int(input())
    for tcase in range(t):
        N,M = list(map(int,input().strip().split()))
        A1 = list(map(int,input().strip().split()))
        A2 = list(map(int,input().strip().split()))
        print (relativeSorting(A1,A2))
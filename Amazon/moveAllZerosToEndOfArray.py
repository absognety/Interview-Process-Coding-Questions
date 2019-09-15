def moveZerosToEnd(arr):
    arr_0 = [x for x in arr if x!=0]
    zeros = [0] * (len(arr)-len(arr_0))
    ans = arr_0 + zeros
    return " ".join(str(u) for u in ans)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        print (moveZerosToEnd(arr))
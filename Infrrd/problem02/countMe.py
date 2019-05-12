def countMe(arrA,arrL,arrR,arrX):
    resultCount = []
    for b in range(len(arrX)):
        targetX = arrX[b]
        p = arrL[b]
        q = arrR[b]
        resultCount.append(countOfNums(arrA[p-1:q],targetX))
    return (" ".join(str(i) for i in resultCount))

def countOfNums(array,target):
    C = 0
    for x in array:
        if target%x == 0:
            C += 1
    return (C)

if __name__ == '__main__':
    sizeOfA = int(input())
    arrA = list(map(int,input().strip().split()))
    numQ = int(input())
    arrL = list(map(int,input().strip().split()))
    arrR = list(map(int,input().strip().split()))
    arrX = list(map(int,input().strip().split()))
    print (countMe(arrA,arrL,arrR,arrX))
    
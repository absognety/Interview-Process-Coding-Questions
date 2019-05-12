import collections

def maximumRows(binary_matrix,K):
    N = len(binary_matrix)
    M = len(binary_matrix[0])
    numOf1s = [collections.Counter(x)[1] for x in binary_matrix]
    #Number of flips <= K
    maximum1s = max(numOf1s)
    #numOfRows_Maximum1s = collections.Counter(numOf1s)[maximum1s]
    total = []
    for i in range(len(binary_matrix)):
        xyPairs1 = []
        for j in range(M):
            if binary_matrix[i][j] == 1:
                xyPairs1.append(j)
        total.append(xyPairs1)
    maximum1sRows = [k for k,v in enumerate(numOf1s) if v == maximum1s]
    #maxmimize first Row
    finalCountList = []
    for e in maximum1sRows:
        row = set(total[e])
        UniversalSet = set(range(M))
        needInc = UniversalSet-row
        checkList = sorted(list(set(range(N)) - {e}))
        a = checkList[0]
        b = checkList[len(checkList)-1]
        countList = []
        for u in total[a:b+1]:
            count = 0
            if needInc & set(u):
                count += len(needInc & set(u))
            countList.append(count)
        finalCountList.append(countList)
    return (len(finalCountList)//K)
        
        
if __name__ == '__main__':
    N,M,K = list(map(int,input().strip().split()))
    binary_matrix = []
    for I in range(N):
        row = list(map(int,input().strip().split()))
        binary_matrix.append(row)
    print (maximumRows(binary_matrix,K))
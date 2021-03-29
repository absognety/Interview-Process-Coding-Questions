"""
find the count of champ numbers in given range [X,Y] (inclusive)
Champ numbers are numbers which have all the digits as unique
and no digit should be greater than 5

"""

def countChampNumbers(X,Y):
    count = 0
    for i in range(X,Y+1):
        if len(str(i)) == 1 and i <= 5:
            print (i)
            count += 1
        else:
            if len(set(str(i))) == len(str(i)):
                if not (('6' in str(i)) or ('7' in str(i)) or 
                        ('8' in str(i)) or ('9' in str(i))):
                    print(i)
                    count += 1
    return count
    
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        X,Y = list(map(int, input().strip().split()))
        print (countChampNumbers(X,Y))
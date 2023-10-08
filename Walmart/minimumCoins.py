# Given a value V, if we want to make a change for V cents, and we have a finite supply of 
# each of C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change? 
# If it’s not possible to make a change, print -1.

# Examples:  
# finite supply is just coin values provided in the list, cannot use more than those

# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents 

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents

from typing import List
import itertools
def minCoins(coins:List[int],value:int) -> int:
    if value == 0:
        return 0
    maxlength = len(coins)
    for l in range(1,maxlength,1):
        combinations = list(itertools.combinations(coins,l))
        for c in combinations:
            if sum(c)==value:
                return f"Minimum {l} coins required, we can use coins of {(','.join([str(i) for i in c]))} cents"
            else:
                continue
    return -1


if __name__ == '__main__':
    coins = list(map(int,input().strip().split(' ')))
    value = int(input())
    print (minCoins(coins,value))
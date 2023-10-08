# Given a value V, if we want to make a change for V cents, and we have an infinite supply of 
# each of C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change? 
# If it’s not possible to make a change, print -1.

# Examples:  

# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents 

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents

from typing import List
import sys
def minimumCoinsRecursive(coins:List[int],value:int) -> int:
    if value == 0:
        return 0
    coins_l = len(coins)
    res = sys.maxsize
    for i in range(coins_l):
        if coins[i] <= value:
            sub_res = minimumCoinsRecursive(coins,value-coins[i])
            if ((sub_res != sys.maxsize) & (sub_res + 1 < res)):
                res = sub_res + 1
    return res

if __name__ == '__main__':
    coins = list(map(int,input().strip().split(' ')))
    print (coins)
    value = int(input())
    print (value)
    print (minimumCoinsRecursive(coins,value))
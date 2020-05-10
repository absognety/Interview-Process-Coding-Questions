"""
Coding Test - Round 1

Given an array of N integers (negative integers allowed) which say likings of
N foods by a customer

Time taken to prepare a food arr[i] is i

like-time co-efficient of food is defined as i*arr[i]. Sum of like-time
co-efficients can be obtained by doing the add up of i*arr[i]

Find the maximum sum of like-time co-efficients that can be achieved from
a given array.

Hint: Consider all combinations of likings from a given array.

Here is the idea:

"""

import itertools

def maxSumLikeTimeCoeff(arr,N):
    all_sums = []
    for r in range(1,N+1):
        combinations = set(itertools.combinations(arr,r))
        for x in combinations:
            sums = 0
            for i in range(len(x)):
                sums += (i+1) * x[i]
            all_sums.append(sums)
    return max(all_sums)

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().strip().split()))
    print (maxSumLikeTimeCoeff(arr,N))
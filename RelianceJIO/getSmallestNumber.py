#!/usr/bin/python3.8

"""
P(N) gives all the numbers that divide given number N

find the smallest number number Y such that Y > X and P(Y) != P(X), given 
number X
"""
import math
def div_count(n):
    # sieve method for 
    # prime calculation 
    hh = [1] * (n + 1); 
      
    p = 2
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0
        p += 1
  
    # Traversing through  
    # all prime numbers 
    total = 1
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
  
            # calculate number of divisor 
            # with formula total div =  
            # (p1+1) * (p2+1) *.....* (pn+1) 
            # where n = (a1^p1)*(a2^p2)....  
            # *(an^pn) ai being prime divisor 
            # for n and pi are their respective  
            # power in factorization 
            count = 0
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p)
                    count += 1
                total *= (count + 1)
                  
    return total


def smallestNumber(n,ndn):
    MAX_INT = math.inf
    p = n + 1
    while (p < MAX_INT):
        if div_count(p) != ndn:
            break
        p += 1
    return p

if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        n = int(input())
        print (smallestNumber(n, ndn=div_count(n)))
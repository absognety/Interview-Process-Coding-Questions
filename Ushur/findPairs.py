"""
Given a list of numbers and each number represents a different color of
a sock, Find the number of pairs that can be formed from given list of
socks

"""

import collections
def find_pairs(n,socks):
    num_pairs = 0
    freqs = collections.Counter(socks)
    for s,c in freqs.items():
        if c >= 2:
            num_pairs += (c//2)
    return num_pairs


if __name__ == '__main__':
    N = 9
    socks = [1,2,2,1,3,4,5,2,2]
    print (find_pairs(N, socks))
    
    N = 10
    socks = [1,1,2,1,3,4,5,2,2,0]
    print (find_pairs(N, socks))
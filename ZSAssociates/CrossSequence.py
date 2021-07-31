"""
Given an array A, Integer K

Find the Kth Smallest element of array which is generated from
calculating the absolute differences of the cartesian product of the 
array elements


Example:
    A = [4,2,1]
    K = 5
    N = size(A) = 3
    
    S = [|4-4|,|4-2|,|4-1|,|2-4|,|2-2|,|2-1|,|1-4|,|1-2|,|1-1|]
    S = [0,2,3,2,0,1,3,1,0]
    S = [0,0,0,1,1,2,2,3,3,3] (sorted)
    5th Smallest element (assuming 1-indexing) is 4
"""

import itertools
def solve(N,A,K):
    cartesian_product = itertools.product(A,A)
    abs_diffs = [abs(i-j) for i,j in cartesian_product]
    return sorted(abs_diffs)[K-1]

if __name__ == '__main__':
    A = [4,2,1]
    N = len(A)
    K = 5
    print (solve(N,A,K))
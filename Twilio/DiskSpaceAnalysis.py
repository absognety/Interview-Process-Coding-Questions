# Number of Computers: n = 4
# Space = [8,2,4,6]
# x = 2, The segment length

# The free disk space of computers in each of these segments is [8,2],[2,4] and [4,6]
# The minimum of these three segments are 2, 2 and 4 - [2,2,4]
# Maximum of these is 4

from typing import List
import math

def segment(x:int, space:List[int]) -> int:
    m,M = x-1,x
    segments_generated = [space[i*(M-m):i*(M-m)+M] for i in range(math.ceil((len(space)-m)/(M-m)))]
    return max([min(segment) for segment in segments_generated])

if __name__ == '__main__':
    num_computers = 7
    space = [8,2,4,6,10,15,18]
    segment_length = 3

    print (segment(x = segment_length,
                   space=space))
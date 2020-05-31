"""
what is the minimum starting number to maintain such that the running sum will
always be atleast 1

Example: 
    arr = [3,-6,5,-2,1]
    4 is the mininum number we need to start with
    Let's check:
        4 + 3 = 7
        7 + (-6) = 1
        1 + 5 = 6
        6 + (-2) = 4
        4 + 1 = 5
        so it's 4.
        
    arr = [-4,3,-2,1]
    5 is the minimum number we need to start with
    Let's check:
        5 + (-4) = 1
        1 + 3 = 4
        4 + (-2) = 2
        2 + 1  3
        so it's 5 
"""
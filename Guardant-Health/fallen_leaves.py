"""
Coding Test - Hackerrank

Given an array that has number of leaves on N trees (size of array = N)(arr[i]
represents number of leaves for ith tree),
percentage, array of days (can be in any order), starting and ending arrays

Scenario:
    every day from each tree, given percentage of leaves will be fallen.
    
    Task:
        There are q queries,each query has day[q].starting[q] and ending[q]
        find out for each query how many leaves are fallen in total from
        all the trees with given start and end indices.
        
    Example:
        arr = [10,20,30,20,10]
        percentage = 30
        days = [1,1,2]
        starting = [2,1,1]
        ending = [4,3,4]
        
        after first day number of fallen leaves in the given range of starting[0]
        and ending[0] is 6 + 9 + 6 = 21 (required answer)
        Remaining leaves after first day = [7,14,21,14,7]
        
In this way answer all the queries

"""
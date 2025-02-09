"""
Populate the list according to following fashion

Given a list of elements [a0, a1, a2, ......, an-1] of length n

Return a list of length n such that it has the following traversal

Input: [a0, a1, a2, ......, an-1]
Output: [a0, an-1, a1, an-2, a2, an-3,........]
"""

def solution(numbers):
    size_of_arr = len(numbers)
    result = list()
    for ind in range(size_of_arr):
        if len(result) == size_of_arr:
            break
        result.append(numbers[ind])
        if (ind != size_of_arr - ind - 1):
            result.append(numbers[size_of_arr - ind - 1])
    return result

if __name__ == '__main__':
    input1 = [2, 5, -10, -4, 0, 8]
    print (solution(input1))

    input2 = [1, 20, 3, 8, 5]
    print (solution(input2))

    input3 = [10, -1, 0, 8, 9, -1, 5, -5, 6, 9, 20, 10]
    print (solution(input3))
"""

Write a function that converts camel_case string into snake case:
    
    Example:
        
        HackerEarth => hacker_earth
        OddOrEven => odd_or_even
        macOS => mac_o_s
        primeCheck => prime_check
        
    Explanation:
        Camel case string is string with uppercase and lowercase characters
        mixed up like illustrated above
        
        Snake case strings are lowercase with underscores in place of uppercase
        characters which are in the middle

"""
import re
def convert_string(s:str) -> str:
    store_indices = []
    slist = list(s)
    for ind,val in enumerate(s):
        if val.isupper() and ind!=0:
            store_indices.append(ind)
            
    c = len(store_indices)
    l = 0
    while (l <= c-1):
        slist.insert(store_indices[l]+l,'_')
        l += 1
    return ''.join(slist).lower()


if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        s = input()
        print (convert_string(s))
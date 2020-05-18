"""
Given a string, sort/modify the characters of string according to below rules:
    
    1. characters having prime ascii values should come before characters
    having composite ascii values.
    
    2. if two characters have same prime ascii value, then the character with
    less value should come first.
    
    3. if two characters have same composite ascii value, then the character
    with greater value should come first
    
"""

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def sort_string(s,n):
    prime_chars = []
    composite_chars = []
    for c in s:
        if isPrime(ord(c)):
            prime_chars.append(c)
        else:
            composite_chars.append(c)
    prime_dict = [(c,ord(c)) for c in prime_chars]
    composite_dict = [(d,ord(d)) for d in composite_chars]
    prime_dict = sorted(prime_dict,key=lambda x: x[1])
    composite_dict = sorted(composite_dict,key=lambda y:y[1],reverse=True)
    result = [k1 for k1,v1 in prime_dict] + [k2 for k2,v2 in composite_dict]
    return ''.join(result)

if __name__ == '__main__':
    n = int(input())
    s = input()
    print (sort_string(s,n))
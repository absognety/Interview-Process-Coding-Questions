"""
Longest balanced substring given a string containing only parenthesis (open and
closed curly braces)

Refer https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/
along with the length, also print the start and end indices of this longest substring

Refer below custom addition to the existing code

"""


def findMaxLen(string): 
    n = len(string) 
  
    # Create a stack and push -1 as initial index to it. 
    stk = [] 
    stk.append(-1) 
  
    # Initialize result 
    result = 0
    tracker = []
  
    # Traverse all characters of given string 
    for i in range(n): 
      
        # If opening bracket, push index of it 
        if string[i] == '{': 
            stk.append(i) 
  
        else:    # If closing bracket, i.e., str[i] = '}' 
      
            # Pop the previous opening bracket's index 
            stk.pop() 
      
            # Check if this length formed with base of 
            # current valid substring is more than max  
            # so far 
            if len(stk) != 0: 
                if result < i - stk[len(stk)-1]:
                    result = i - stk[len(stk)-1]
                    tracker.append((result,i))
  
            # If stack is empty. push current index as  
            # base for next valid substring (if any) 
            else: 
                stk.append(i) 
  
    return result,tracker

#string = "{{{}"
#string = "}{}{}}"
string = "{}{{}}}}}"
result,tracker = findMaxLen(string)
for t in tracker:
    if t[0] == result:
        end_index = t[1]
        
# length of longest substring (balanced)
print (result)

# print (start and end locations of that substring)
print (" ".join([str(end_index - result + 2),str(end_index + 1)]))
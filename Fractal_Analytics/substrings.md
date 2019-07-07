
2. Get the number of distinct substrings possible for a given string, you can use the below operations:  
  
   - a. Remove 0 or more characters from left side of the string.  
   - b. Remove 0 or more characters from right side of string.  
   - c. Remove 0 or more characters from both left and right side of string.  
     
Examples:  
```
Input  : str = “ababa”
Output : 10
Total number of distinct substring are 10, which are,
"", "a", "b", "ab", "ba", "aba", "bab", "abab", "baba"
and "ababa"
```  
```
Input : abcd
Output : abcd abc ab a bcd bc b cd c d
All Elements are Distinct
```  
```
Input : aaa
Output : aaa aa a aa a a
All elements are not Distinct
```  

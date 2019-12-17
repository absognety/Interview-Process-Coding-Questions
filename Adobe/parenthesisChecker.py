{
#Initial Template for Python 3
import atexit
import io
import sys
#Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  : s (given string containing parenthesis) 
		@return : boolean True or False
'''

def isMatchingPair(c1,c2):
    if (c1=='(') & (c2==')'):
        return True
    elif (c1=='{') & (c2=='}'):
        return True
    elif (c1=='[') & (c2==']'):
        return True
    else:
        return False
        
def ispar(s):
    # code here
    import queue
    stack = queue.LifoQueue()
    
    for i in range(len(s)):
        if ((s[i] == '{') | (s[i] == '[') | (s[i] == '(')):
            stack.put(s[i])
        if ((s[i] == '}') | (s[i] == ']') | (s[i] == ')')):
            if stack.empty():
                return False
            elif not isMatchingPair(stack.get(),s[i]):
                return False
        
    if stack.empty():
        return True
    else:
        return False
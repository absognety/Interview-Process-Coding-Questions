{
#Initial Template for Python 3
import atexit
import io
import sys
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
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
        exp = str(input())
        print(InfixtoPostfix(exp))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments :
		@param  : exp (given infix expression)
		@return : string
'''
def InfixtoPostfix(exp):
    #code here
    import string
    stack = []
    prec = {'^':4,'*':3,'/':3,'+':2,'-':2,'(':1}
    postfixexp = []
    tokens = list(exp)
    for token in tokens:
        if ((token in string.ascii_lowercase) | (token in "0123456789") | (token in string.ascii_uppercase)):
            postfixexp.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            if len(stack)!=0:
                topToken = stack.pop()
                while topToken != '(':
                    postfixexp.append(topToken)
                    topToken = stack.pop()
        else:
            if len(stack) != 0:
                while (len(stack)!=0) and (prec[stack[-1]] >= prec[token]):
                    postfixexp.append(stack.pop())
            stack.append(token)
    while len(stack)!=0:
        postfixexp.append(stack.pop())
    return "".join(postfixexp)
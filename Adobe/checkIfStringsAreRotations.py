{
#Initial Template for Python 3
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s1=str(input())
        s2=str(input())
        if(areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is tocheck if the given two strings
	are rotations of each other.
	Function Arguments: s1 and s2 (given strings)
	Return Type:boolean
'''
def areRotations(s1,s2):
    if (len(s1) == 1 or len(s2) == 1) & (s1 != s2):
        return False
    #code here
    if (len(s1) == len(s2)) & (set(s1)==set(s2)) & (s2 in s1+s2) & (s1 in s1+s2):
        return True
    else:
        return False
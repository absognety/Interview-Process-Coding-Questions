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
        s=str(input())
        index=repeatingCharacter(s)
        if(index==-1):
            print(-1)
        else:
            print(s[index])
            
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the lefmost index of the repeating 
	character whose first appereance is left most or return
	-1 if all characters are distinct.
	
	Function Arguments: s (given string)
	Return Type: integer
'''
def repeatingCharacter(s):
    #code here
    import collections
    freqs = collections.Counter(s)
    if len(set(freqs.values())) == 1 and 1 in set(freqs.values()):
        return -1
    else:
        inds = []
        for k,v in freqs.items():
            if v > 1:
                inds.append(s.index(k))
        return min(inds)
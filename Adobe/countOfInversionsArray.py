# GeeksForGeeks Code - Copied#
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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(Inversion_Count(a,n))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return total number of inversions
	present in the array.
	
	Function Arguments: array a and size n
	Return Type: Integer 
'''
def Inversion_Count(arr,n):
    if a == sorted(a):
        return 0
    temp_arr = [0]*n
    return mergesort(arr,temp_arr,0,n-1)
    
def mergesort(arr,temp_arr,left,right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        inv_count = mergesort(arr,temp_arr,left,mid)
        inv_count += mergesort(arr,temp_arr,mid+1,right)
        inv_count += merge(arr,temp_arr,left,mid,right)
    return inv_count
    
def merge(arr,temp_arr,left, mid, right): 
    # Merge the temp arrays back into arr[l..r] 
    i = left     # Initial index of first subarray 
    j = mid+1     # Initial index of second subarray 
    k = left     # Initial index of merged subarray 
    invcount = 0
    while i <= mid and j <= right: 
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i] 
            i += 1
        else: 
            temp_arr[k] = arr[j]
            invcount += (mid - i + 1)
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there 
    # are any 
    while i <= mid: 
        temp_arr[k] = arr[i] 
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there 
    # are any 
    while j <= right: 
        temp_arr[k] = arr[j] 
        j += 1
        k += 1
        
    for lr in range(left, right + 1): 
        arr[lr] = temp_arr[lr] 
    return invcount

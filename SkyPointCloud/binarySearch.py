"""
Can you write the binary search algorithm for reverse sorted array?

"""
def binarySearch(arr,x):
    arr = sorted(arr,reverse=True)
    l = 0
    r = len(arr) - 1
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
   
        elif arr[mid] > x: 
            l = mid + 1
  
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return "not present"

if __name__ == '__main__':
    mylist = [1,3,5,7,9,8,5,88,79]
    n = len(mylist)
    print (binarySearch(mylist,5))
    print (binarySearch(mylist,88))
    print (binarySearch(mylist,79))
    print (binarySearch(mylist,20))
    print (binarySearch(mylist,1))
{
#Initial Template for Python 3
#Contributed by : Nagendra Jha
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
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a= []
        for i in range(n):
            a.append(LinkedList())
        list_info = list(map(int,input().strip().split()))
        curr_ind = 0
        curr_list_ind = 0
        while curr_ind < len(list_info):
            nodes= list_info[curr_ind]
            curr_ind+=1
            for i in range(nodes):
                a[curr_list_ind].append(list_info[curr_ind])
                curr_ind += 1
            curr_list_ind += 1
        heads = []
        for i in range(n):
            heads.append(a[i].head)
        printList(merge(heads,n))

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the head of the new formed linked list.
	
	Function Arguments: array "heads" (containing heads of linked lists), n size of array a.
	Return Type: head node.;
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def merge(heads,n):
    #code here
    newll = LinkedList()
    new_list = []
    for h in heads:
        curr_node = h
        while curr_node != None:
            new_list.append(curr_node.data)
            curr_node = curr_node.next
    new_list = sorted(new_list)
    for ele in new_list:
        newll.append(ele)
    return newll.head
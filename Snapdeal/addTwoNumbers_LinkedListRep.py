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
        n_a = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_a = nodes_a[::-1] # reverse the input array
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        n_b =int(input())
        b = LinkedList()  # create a new linked list 'b'.
        nodes_b = list(map(int, input().strip().split()))
        nodes_b = nodes_b[::-1]  # reverse the input array
        for x in nodes_b:
            b.append(x)  # add to the end of the list
        result_head = addBoth(a.head,b.head)
        printList(result_head)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Function to add two numbers represented 
	in the form of the linked list.
	
	Function Arguments: head_a and head_b (heads of both the linked lists)
	Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def addBoth(head_a,head_b):
    #code here
    result = LinkedList()
    num1 = ""
    curr_node = head_a
    while curr_node != None:
        num1 += str(curr_node.data)
        curr_node = curr_node.next
    num1 = num1[::-1]
    num2 = ""
    curr_node = head_b
    while curr_node != None:
        num2 += str(curr_node.data)
        curr_node = curr_node.next
    num2 = num2[::-1]
    num = int(num1) + int(num2)
    num = str(num)[::-1]
    for i in num:
        result.append(i)
    return result.head
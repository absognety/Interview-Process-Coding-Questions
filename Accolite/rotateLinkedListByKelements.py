{
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print("")
if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while(t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = rotateList(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa

}
''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
# This function should rotate list counter-
# clockwise by k and return new head (if changed) 
def rotateList(head, k):
    # code here
    global llist
    llist = LinkedList()
    C = 0
    curr_node = head
    part1 = []
    part2 = []
    while curr_node != None:
        if C <= k-1:
            part1.append(curr_node.data)
        elif C > k-1:
            part2.append(curr_node.data)
        C += 1
        curr_node = curr_node.next
    total = reversed(part2 + part1)
    for i in total:
        llist.push(i)
    return llist.head
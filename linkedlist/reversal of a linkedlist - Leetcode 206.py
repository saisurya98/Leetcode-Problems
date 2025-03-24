# node object
class Node:
    def __init__(self,val):
        self.val = val
        self.next=None

# create nodes
node1=Node(1)
node2=Node(10)
node3=Node(2)
node4=Node(30)
node5=Node(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

def traverse(head):
    curr=head
    while curr is not None:
        print(curr.val,end='->')
        curr=curr.next

def reverseList(head):
        # initialize
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

print('before')
print(traverse(node1))
print('after')
reverse=reverseList(node1)
print(traverse(reverse))

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.prev=node4
node4.prev=node3
node3.prev=node2
node2.prev=node1

curr_forwad=node1
print('forward')
while curr_forwad is not None:
    print(curr_forwad.data,end='->')
    curr_forwad=curr_forwad.next
print('end of forward traversal')

print('backward')
curr_backward=node5
while curr_backward is not None:
    print(curr_backward.data,end='->')
    curr_backward=curr_backward.prev
print('end of backward traversal')


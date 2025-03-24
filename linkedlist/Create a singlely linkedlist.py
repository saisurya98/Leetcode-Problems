# node object
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

# create nodes
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
# node5.next=None

curr=node1
while curr is not None:
    print(curr.data,end='->')
    curr=curr.next
print('null')






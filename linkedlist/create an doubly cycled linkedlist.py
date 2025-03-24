class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=Node(1)
node2=Node(3)
node3=Node(7)
node4=Node(9)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node1

startnode=node1
currnode=node1
print(currnode.data,end='->')
currnode=currnode.next
while currnode!=startnode:
    print(currnode.data, end='->')
    currnode=currnode.next
print('end')

node4.prev=node3
node3.prev=node2
node2.prev=node1
node1.prev=node4

endnode=node4
curr_node=node4
print(curr_node.data,end='->')
curr_node=curr_node.prev

while curr_node!=endnode:
    print(curr_node.data,end='->')
    curr_node=curr_node.prev
print('end')
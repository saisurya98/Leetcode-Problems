class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

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

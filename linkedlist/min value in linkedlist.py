class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

# create nodes
node1=Node(100)
node2=Node(20)
node3=Node(32)
node4=Node(14)
node5=Node(-5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

def minvalue(head):
    curr=head
    min_val=curr.data
    curr=curr.next
    while curr is not None:
        if curr.data<min_val:
            min_val=curr.data
        curr=curr.next
    return min_val
def traverse(head):
    curr=head
    while curr is not None:
        print(curr.data,end='->')
        curr=curr.next
print(traverse(node1))
print('the min in the above linekdlist is', minvalue(node1))

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(1)
node2=Node(3)
node3=Node(7)
node4=Node(11)

node1.next=node2
node2.next=node3
node3.next=node4

def travseralofnodes(head):
    current=head
    while current is not None:
        print(current.data,end='->')
        current=current.next
    print('........')

def deletion(head, deletenode):
    current=head
    # starting case
    if current==deletenode:
        current=current.next
        return current
    while current.next is not None and current.next!=deletenode:
        current=current.next
    # ending case
    if current.next==None:
        return head
    current.next=current.next.next
    return head

print("Before deletion:")
travseralofnodes(node1)

# Delete node4
node1 = deletion(node1, node2)

print("\nAfter deletion:")
travseralofnodes(node1)

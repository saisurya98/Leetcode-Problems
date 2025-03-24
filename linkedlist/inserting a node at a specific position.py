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

def travese(head):
    curr = head
    while curr is not None:
        print(curr.data, end='->')
        curr = curr.next
    print('null')

def insert(head,newNode,position):
    # at start
    if position==1:
        newNode.next=head
        return newNode
    # go untill the prev position
    cur=head
    for _ in range(position-2):
        if cur is None:
            break
        cur=cur.next
    # insert
    newNode.next=cur.next
    cur.next=newNode
    return head
print("Original list:")
travese(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insert(node1, newNode, 2)

print("\nAfter insertion:")
travese(node1)



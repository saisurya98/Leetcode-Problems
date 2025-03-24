 # node object
class Node:
    def __init__(self,val):
        self.val = val
        self.next=None

# create nodes
node1=Node(1)
node2=Node(1)
node3=Node(2)
node4=Node(3)
node5=Node(3)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

def traverse(head):
    curr=head
    while curr is not None:
        print(curr.val,end='->')
        curr=curr.next

def deleteDuplicates(head):
    curr = head
    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
print('before removal of duplicates',traverse(node1))
dele=deleteDuplicates(node1)
print('after removal of duplicates',traverse(dele))

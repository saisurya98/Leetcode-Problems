class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def travseralofnodes(head):
    current = head
    while current is not None:
        print(current.data, end=' -> ')
        current = current.next
    print('None')

def mergesort(list1, list2):
    if list1 is None and list2 is None:
        return None
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    dummy = Node(0)  # Use a dummy node with a placeholder value
    curr = dummy
    while list1 is not None and list2 is not None:
        if list1.data == list2.data:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

            curr.next = list2
            list2 = list2.next
            curr = curr.next
        elif list1.data < list2.data:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        else:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

    if list1 is not None:
        curr.next = list1
    if list2 is not None:
        curr.next = list2

    return dummy.next

# Create linked lists for testing
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(4)
node_4 = Node(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

# Test the traversal and merging functions
print('List 1: ', end='')
travseralofnodes(node1)
print('List 2: ', end='')
travseralofnodes(node_1)

print('After merging in sorted order:')
merged_head = mergesort(node1, node_1)
travseralofnodes(merged_head)

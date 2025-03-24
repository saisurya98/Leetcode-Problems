# DFS ( go depth wise) - implemeneted by using stack ( use recursive call stack)
#1) Pre order- Node,Left,Right
#2) In order - Left, Node, Right
#3) Post order- left, right, Node

#BFS( level order traversal)- implemented by Queue

#binary search tree - all stuff on left side of node is less and all stuff on right side of node is more
# it is true recursively.
# search should be O(Log2 N)

# in order traversal for a binary search tree will be in ascending order

class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)

#      1
#   2     3
# 4   5  10

A=TreeNode(1)
B=TreeNode(2)
A.left=B
C=TreeNode(3)
A.right=C
D=TreeNode(4)
B.left=D
E=TreeNode(5)
B.right=E
F=TreeNode(10)
C.left=F

# print(A)

# Pre order Traversal - DFS TC- O(N), SC-O(N) uses recursive call stack
def pre_order(root):
    if not root:
        return
    print(root)
    pre_order(root.left)
    pre_order(root.right)
print('preorder DFS')

print(pre_order(A))

# IN order Traversal - DFS, TC-O(N) SC-O(N)
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root)
    in_order(root.right)
print('inorder DFS')
print(in_order(A))

# Post order Travsersal - DFS TCO(N), SC-O(N)

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root)
print('post_order DFS')
print(post_order(A))


# Iterative approach for Preorder Traversal
def iterative_preorder(root):
    stk=[root]
    while stk:
        node=stk.pop()
        print(node)

        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
print('iterative_preorder DFS')
print(iterative_preorder(A))

# BFS - Level order Traversal TC- SC- O(N)
from collections import deque
def level_order(root):
    q=deque()
    q.append(root)
    while q:
        node=q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
print('level_order DFS')
level_order(A)












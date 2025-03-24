# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans=True


        def height(root):
            if root is None:
                return 0

            
            height_left=height(root.left)
            height_right=height(root.right)

            if abs(height_left-height_right)>1:
                self.ans=False
            
            return 1+max(height_left,height_right)

        height(root)

        return self.ans
            
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
solution = Solution()
result = solution.isBalanced(root)
print(result)



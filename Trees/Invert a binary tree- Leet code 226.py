# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    input_values = [4, 2, 7, 1, 3, 6, 9]
    root = create_tree(input_values)

    print("Original Tree:")
    print_tree(root)

    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("Inverted Tree:")
    print_tree(inverted_root)
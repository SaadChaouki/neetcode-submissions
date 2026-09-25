# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # If the root is null, we don't need to do anything. 
        if not root:
            return root

        # Swapping
        root.left, root.right = root.right, root.left

        # Recursion
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root




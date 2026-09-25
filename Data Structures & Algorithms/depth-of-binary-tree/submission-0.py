# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._traverse_tree(root, 0)

    def _traverse_tree(self, root: Optiona[TreeNode], depth) -> int:
        if not root:
            return depth
        left = self._traverse_tree(root.left, depth = depth + 1)
        right = self._traverse_tree(root.right, depth = depth + 1)
        return max(left, right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # The breaking condition is that they don't have children 
        if not p and not q:
            return True

        if not p and q:
            return False

        if not q and p:
            return False

        # The recrusion part. 
        is_left_equal = self.isSameTree(p.left, q.left)
        is_right_equal = self.isSameTree(p.right, q.right)

        # Is equal.
        is_equal_node = (p.val == q.val)

        return min(is_equal_node, is_left_equal, is_right_equal)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left        # both on the left
            elif p.val > node.val and q.val > node.val:
                node = node.right       # both on the right
            else:
                return node             # they split here, or one of them is this node


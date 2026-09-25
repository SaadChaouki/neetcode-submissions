# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # IT's a valid vinary search tree if:
        # left.val < root.val
        # right.val > root.val
        # left is BST
        # right is BST

        # We need to do it with DFS here. We can probably do it with BFS as well.  
        # Let's start with the DFS solution.

        # Creating a flag that will be updated if we find that something is not right.

        def dfs(node, left, right):
            # If we reach the end just stop.
            if not node: 
                return True

            if not (left < node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))

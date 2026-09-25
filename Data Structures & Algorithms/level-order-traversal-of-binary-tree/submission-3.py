# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # We need to essentially keep going down the tree and collecting
        # the left and right in each sequence but we only have one root. 

        return self._dfs_solution(root)


    def _dfs_solution(self, root):
        indices = self._level_order(root)

        mapp = defaultdict(list)

        for val, index in indices:
            mapp[index].append(val)

        return list(mapp.values())

    def _level_order(self, root: Optional[TreeNode], depth = 0) -> List[List[int]]:
        
        if not root:
            return []
        
        left_sol = self._level_order(root.left, depth + 1)
        right_sol = self._level_order(root.right, depth + 1)

        current_sol = [(root.val, depth)] + left_sol + right_sol

        return current_sol


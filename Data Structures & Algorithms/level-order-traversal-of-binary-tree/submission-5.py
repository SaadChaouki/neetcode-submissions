# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # We need to essentially keep going down the tree and collecting
        # the left and right in each sequence but we only have one root. 

        return self._bfs_solution(root)

    def _bfs_solution(self, root):

        if not root:
            return []
        
        # We create a list to hold the solution.
        solution: list = []

        # We create a queue. The queue has the root as the starting point.
        queue = deque([root])

        # The loop wll continune until the queue is empty.
        while len(queue) > 0:

            # Creating the solution for that specific level.
            level = []

            # Going through the queue. At the first level it'll have only one 
            # element so that's a single level.
            for i in range(len(queue)):

                # Take the item from the queue.
                node = queue.popleft()
                level.append(node.val)

                # Adding the children to the queue.
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            # Appending the level to the solutions
            solution.append(level)

        return solution


    # This is the solution using DFS instead. It's not optimal compared to
    # BFS but it still works. It can be optimized further however. 
    def _dfs_solution(self, root):

        # Creating a list with the results
        res = []

        # Recursive function for the DFS approach.
        def dfs(node, depth):
            if not node:
                return

            # Adding the level.
            if depth == len(res): res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return res
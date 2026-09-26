"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Ok can we do it in BFS? We create a queue, get the item,
        # That will be one level essentially, mark each node as visited to 
        # not repeat it again.

        # First things first, if there's nothing just return nothing.
        if not node: return None

        # We don't need to handle the no neighbors since it's automaticlaly handled below.

        # Ok now that these two cases are dealt with, we'll have have neighbors.
        # Creating the queue that will hold the neighbors. 
        q = deque([node])

        # Create a set to keep track of the seen values so that it doesn't become infinite?
        seen_nodes = set()

        # Creating a dicitonary to track the node.
        old_to_new = { }
        old_to_new[node] = Node(val = node.val)

        # Creating a list that will hold the solution.
        while q:
            
            # Pop a single node frmo the queue. We're popping from the left
            # here because it's FIFO. This is O(1)
            current_node = q.popleft()

            # Creating a copy of the node since it was never seen before.
            if current_node not in old_to_new:
                old_to_new[current_node] = Node(val = current_node.val)

            # Marking the node as seen.
            seen_nodes.add(current_node.val)

            # Create the solution for that current node.
            current_node_solution = []

            # Adding all the neighbors.
            for neighbor in current_node.neighbors:
                
                # Checking if the neighbor already has a copy. If not, create
                # a copy for it.
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(val = neighbor.val)

                # Adding the copy neighbor to the current node's neighbor. 
                old_to_new[current_node].neighbors.append(old_to_new[neighbor])

                # Marking the neighbor as seen. This is a bit duplicative tho.
                if neighbor.val not in seen_nodes and neighbor not in q:
                    q.append(neighbor)

        return old_to_new[node]


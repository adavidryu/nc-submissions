"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Maps each original node to its cloned node
        old_to_new = {}

        def dfs(node):
            # Return the existing clone to avoid cycles and duplicate work
            if node in old_to_new:
                return old_to_new[node]

            # Clone the current node before recursively cloning its neighbors
            copy = Node(node.val)
            old_to_new[node] = copy

            # Connect the clone to the cloned versions of all its neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        # Handle an empty graph
        return dfs(node) if node else None
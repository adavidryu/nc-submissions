# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if not node:
                return 0
            
            is_good = False
            
            if node.val >= cur_max:
                is_good = True
            
            cur_max = max(cur_max, node.val)

            left = dfs(node.left, cur_max)
            right = dfs(node.right, cur_max)

            if is_good:
                return 1 + left + right
            
            return left + right
        
        return dfs(root, root.val)

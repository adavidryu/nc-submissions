# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        j = 0

        def dfs(node): 
            if not node:
                return
            
            left = dfs(node.left)

            nonlocal j
            j += 1

            if j == k:
                return node.val
    
            right = dfs(node.right)

            return left or right
        
        return dfs(root)
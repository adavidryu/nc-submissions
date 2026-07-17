# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def dfs(node): 
            nonlocal count
            nonlocal answer

            if not node:
                return
            
            left = dfs(node.left)

            count += 1

            if count == k:
                answer = node.val
    
            right = dfs(node.right)

            return count
        
        dfs(root)
        return answer
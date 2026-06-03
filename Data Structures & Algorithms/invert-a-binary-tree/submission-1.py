# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]

        while stack:
            popped = stack.pop()
            popped.left, popped.right = popped.right, popped.left
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
        
        return root





        

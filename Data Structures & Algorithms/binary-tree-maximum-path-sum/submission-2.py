class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res = max(
                res,
                node.val + max(left, 0) + max(right, 0)
            )

            return node.val + max(left, right, 0)

        dfs(root)
        return res
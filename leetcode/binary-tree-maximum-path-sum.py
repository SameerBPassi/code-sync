# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def dfs(node):
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            curr_path = node.val + left_gain + right_gain
            res[0] = max(res[0], curr_path)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return res[0]
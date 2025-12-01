# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.ans = float('inf')

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return self.ans

        self.minDiffInBST(root.left)

        if self.prev is not None:
            self.ans = min(self.ans,root.val - self.prev.val)
        self.prev = root

        self.minDiffInBST(root.right)

        return self.ans

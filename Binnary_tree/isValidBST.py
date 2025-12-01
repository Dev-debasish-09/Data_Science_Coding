# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helperbst(root,min,max):
            if root is None:
              return True
            if min is not None and root.val <= min:
                return False  
            if max is not None and root.val >= max:
                return False
            return helperbst(root.left,min,root.val) and helperbst(root.right,root.val,max)
        return helperbst(root,None,None)

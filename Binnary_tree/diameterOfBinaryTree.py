# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height,right_height) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_dia = self.diameterOfBinaryTree(root.left)
        right_dia = self.diameterOfBinaryTree(root.right)
        curr_dia = self.height(root.left)+ self.height(root.right)
        return max(curr_dia,max(left_dia,right_dia))


                            (NOT OPTIMIZED)
-----------------------------------------------------------------------------------------------------------
                            (OPTIMIZED)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def height(self,root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        self.ans = max(self.ans,left_height+right_height)
        return max(left_height,right_height) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.ans

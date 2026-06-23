# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten the tree into a linked list in-place.
        The final linked list should follow preorder traversal:
        Root -> Left -> Right
        """

        def dfs(node):
            # Base case: empty subtree
            if not node:
                return None

            # Recursively flatten left and right subtrees
            # and get their tail nodes
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            # If left subtree exists,
            # insert it between node and right subtree
            if node.left:

                # Connect tail of flattened left subtree
                # to the beginning of flattened right subtree
                left_tail.right = node.right

                # Move entire left subtree to the right
                node.right = node.left

                # Set left pointer to None
                node.left = None

            # Return the tail of the flattened subtree
            #
            # Priority:
            # 1. right_tail (if right subtree exists)
            # 2. left_tail  (if only left subtree exists)
            # 3. node itself (leaf node)
            return right_tail or left_tail or node

        dfs(root)

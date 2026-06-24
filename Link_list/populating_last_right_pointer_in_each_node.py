"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        lefttail = root

        while lefttail.left:
            head = lefttail

            while head:
                # Connection 1: Same parent (Left child -> Right child)
                head.left.next = head.right
                # Connection 2: Different parents (Right child -> Next parent's Left child)
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            
            lefttail = lefttail.left
        
        return root

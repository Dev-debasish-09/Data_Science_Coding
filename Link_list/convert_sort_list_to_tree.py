# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        # create the array from the linklist 

        while head:
            nums.append(head.val)
            head = head.next
        # building a tree 
        def build(left,right):
            if left > right:
                return None
            # mid will be the heading node or root node
            mid = (left + right) // 2
            # assign the root node
            root = TreeNode(nums[mid])
            # root left we directly do this because once we get the root node rest are recursively happen
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)

            return root
        
        return build(0,len(nums)-1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and not head.next:
            return 
        
        #step-1 find the middle of the linked list 
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #step-2 reverse the second half
        prev, curr = None, slow.next
        slow.next = None # split list into two part

        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # step-3 merge the two halves
        first,second = head,prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2

        

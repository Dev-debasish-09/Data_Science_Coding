# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # creating a dummy node to avoid future probleam
        dummy.next = head # dummy next link with the head

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next # deleting the n th node from the last 

        return dummy.next # return that dummy.next iteration that is our result 
      # here fast is just there to find element from last and the slow actually skip the need 
       #value so this is the process of substract the node
        

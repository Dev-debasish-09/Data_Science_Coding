# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1) # create a dummy list for convenience
        curr = dummy_head # curr is pointing the result list that will traverse the whole journey
        temp1 = l1 # pointing l1
        temp2 = l2 # pointing l2
        carry = 0 # carrying 0 it will take care the 10th place
        while (temp1 != None or temp2!= None):
            sum = carry # identify the sum first
            if temp1: # if the value are not empty
                sum += temp1.val # adding the pointer value
            if temp2:# if the value are not empty
                sum += temp2.val
            new_node = ListNode(sum%10) # making the newnode value of the first place 
            carry = sum // 10 # value as carry

            curr.next = new_node # pointer moving and forming a link between the list 
            curr = curr.next # here it is moving 

            if temp1 :
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        if carry: # when carry contain a value
            new_node = ListNode(carry) # making new node
            curr.next = new_node # moving the pointer 
        return dummy_head.next # return the real value after dummy node 

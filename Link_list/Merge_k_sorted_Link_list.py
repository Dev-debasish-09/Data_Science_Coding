# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        # Approach - 1 (append in array short and make the ll)

        arr = [] # initialize a empty array

        # Collect all values
        for head in lists: # itterate through whole the lists
            while head: # if head is not null
                arr.append(head.val) 
                head = head.next

        # Sort values
        arr.sort()

        # Create new linked list
        dummy = ListNode(0)
        curr = dummy

        for val in arr: # itterate over the array and forming the link list 
            curr.next = ListNode(val) # pointing the next value by a linklist node
            curr = curr.next
        return dummy.next 


        # Approach - 2 (Recursively merge)

        def merge(l1, l2): # merge synatx which i use below 
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2: # when both are not null
                if l1.val <= l2.val: # if the first value is small 
                    curr.next = l1 # adding to the new linklist 
                    l1 = l1.next # moving forward
                else:
                    curr.next = l2 # adding the other to the new linklist 
                    l2 = l2.next # moving the second list forward

                curr = curr.next # end curr is moving 

            if l1: # if one of them have not null progress
                curr.next = l1
            else:
                curr.next = l2

            return dummy.next 

        if not lists:
            return None

        result = lists[0] # starting with the first linklist 

        for i in range(1, len(lists)): # iterate over the len of the list 
            result = merge(result, lists[i]) # merging the result with the new list in the list

        return result


        # Approach - 3 (Min heap Approach )
      # for this you have to import the heapq library 
        heap = [] # the array you can call it like a bukket where we store and comapring the smallest then remove
        for i,node in enumerate(lists):
            if node: # if node is not null 
                heapq.heappush(heap,(node.val,i,node)) # in the bucket we have a array node value(for campare) index(for traversal) and the node(for track the future entry) 
        
        dummy = ListNode(0)
        curr = dummy # adding the values to the dummy 

        while heap:
            val,idx,node = heapq.heappop(heap) # pop the value which is minimum 

            curr.next = node # curr linking with the minimum value 
            curr = curr.next # then traverse 

            if node.next:
                heapq.heappush(heap,(node.next.val,idx,node.next)) # the minimum place filled by the next item of the list 
        return dummy.next



            

        

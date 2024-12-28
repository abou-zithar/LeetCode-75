# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        current = head
        size = 1
        while current.next != None:
            current = current.next
            size +=1
            

        middle = size//2
       
          # Step 3: Traverse to the node before the middle
        current = head
        index = 0
        while index < middle - 1:
            current = current.next
            index += 1

        # Step 4: Skip the middle node
        current.next = current.next.next

        return head

        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None 
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        
        if prev:
            prev.next = slow.next
        
        return head



        
        
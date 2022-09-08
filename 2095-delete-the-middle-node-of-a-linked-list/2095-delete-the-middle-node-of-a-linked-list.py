# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        curr=head
        n=0
        while curr:
            n+=1
            curr=curr.next
        
        
        
        dummy=ListNode(0,head)
        
        prev,curr=dummy,head
        
        
        if n==1:
            return None
        
        for i in range(n//2):
            
            
            prev=curr
            curr=curr.next
            
        prev.next=curr.next
        
        return head
            
            
            
            
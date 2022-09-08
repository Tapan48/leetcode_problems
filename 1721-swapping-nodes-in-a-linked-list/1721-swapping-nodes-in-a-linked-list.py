# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        curr=head
        n=0
        while curr:
            n+=1
            
            curr=curr.next
            
        f,s=head,head    
        for i in range(k-1):
            f=f.next
            
        for i in range(n-k):
            
            s=s.next
            
        temp=f.val
        
        f.val=s.val
        s.val=temp
        
        return head
            
            
            
            
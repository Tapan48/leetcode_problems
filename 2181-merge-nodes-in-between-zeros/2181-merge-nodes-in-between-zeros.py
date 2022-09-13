# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        dummy=ListNode(0,head)
        arr=[]
        curr=head
        while curr:
            
            while  curr and curr.val==0:
                curr=curr.next
            ts=0    
            while curr and  curr.val!=0  :
                ts+=curr.val
                curr=curr.next
                
            if curr:    
                arr.append(ts)
            
        
        n=len(arr)
        curr2=head
        prev=dummy
        for i in range(n):
            prev=curr2
            curr2.val=arr[i]
            curr2=curr2.next
        
        prev.next=None
        return head
       """
        dummy=ListNode(0,head)
        prevprev=dummy
        prev=head
        curr=head.next
        
        while curr:
            ts=0
            while curr and curr.val!=0:
                ts+=curr.val
                curr=curr.next
            curr=curr.next
            prev.val=ts
            prevprev=prev
            prev=prev.next
        prevprev.next=None     
        return head    
            
            
            
            
        
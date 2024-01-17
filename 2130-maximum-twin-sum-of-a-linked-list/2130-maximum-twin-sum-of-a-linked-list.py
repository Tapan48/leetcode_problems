# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        
        
        ptr=head
        arr=[]
        while ptr:
            
            arr.append(ptr.val)
            
            ptr=ptr.next
            
        maxsum=0
        n=len(arr)
        for i in range((n//2)+1):
            
            cursum=arr[i]+arr[n-1-i]
            maxsum=max(maxsum,cursum)
        return maxsum    
            
            
            
            
            
            
            
            
            
            
            
        
        
            
            
            
        
        
            
            
            
            
            
        
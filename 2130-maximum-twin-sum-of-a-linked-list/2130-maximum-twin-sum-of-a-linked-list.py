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
        
        l,r=0,n-1
        
        while l<r:
            
            cursum=arr[l]+arr[r]
            maxsum=max(cursum,maxsum)
            
            l+=1
            r-=1
        return maxsum     
            
            
       
            
            
            
            
            
            
            
            
            
            
            
        
        
            
            
            
        
        
            
            
            
            
            
        
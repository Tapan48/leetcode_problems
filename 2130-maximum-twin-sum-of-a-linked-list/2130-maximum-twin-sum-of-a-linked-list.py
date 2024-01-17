# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res
        
        
#             ptr = head
#             n = 0
#             while ptr:  # found length
#                 n += 1
#                 ptr = ptr.next

#             ptr = head
#             x = n // 2
#             while x:  # found middle half
#                 ptr = ptr.next
#                 x -= 1

#             prev = None  # Reverse the second half
#             while ptr:
#                 next_node = ptr.next
#                 ptr.next = prev
#                 prev = ptr
#                 ptr = next_node

#             y = n // 2

#             maxsum = 0   #### find maximum twin sum
#             while y:
#                 cursum = head.val + prev.val
#                 head = head.next
#                 prev = prev.next

#                 maxsum = max(cursum, maxsum)
#                 y -= 1

#             return maxsum

        
        
        
        
        
        
#         ptr=head
#         arr=[]
#         while ptr:         ### tc o(n)  sc o(n)
            
#             arr.append(ptr.val)
            
#             ptr=ptr.next
            
#         maxsum=0
#         n=len(arr)
        
#         l,r=0,n-1
        
#         while l<r:
            
#             cursum=arr[l]+arr[r]
#             maxsum=max(cursum,maxsum)
            
#             l+=1
#             r-=1
#         return maxsum  





            
            
            
            
            
          
          
          
         
          
            
            
       
            
            
            
            
            
            
            
            
            
            
            
        
        
            
            
            
        
        
            
            
            
            
            
        
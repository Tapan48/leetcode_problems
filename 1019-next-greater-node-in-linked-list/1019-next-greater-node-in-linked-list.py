# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        
        """
        curr=head
        arr=[]
        res=[]
        while curr:
            
            arr.append(curr.val)
            
            curr=curr.next
            
        for i in range(len(arr)):
            
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    
                    res.append(arr[j])
                    break
                elif j==len(arr)-1 and arr[j]<=arr[i]:      
                    res.append(0)
        res.append(0)       
                
        
        
        return res
        """
        
        """                                       ##tc o(n^2)
        curr1=head
        res=[]
        
        while curr1 and curr1.next:
            
            curr2=curr1.next
            
            while curr2:
                if curr2.val>curr1.val:
                    res.append(curr2.val)
                    break
                curr2=curr2.next
                
                if curr2 is None:
                    res.append(0)
                    
            curr1=curr1.next
            
        res.append(0)    
                    
        return res            
           """                  
        prev=None
        curr=head
        
        while curr:
            
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            
        stack=[]
        result=[]
        while prev:
            
            if stack is None:
                result.append(0)
                stack.append(prev.val)
                prev=prev.next
                last=stack[-1]
            
            elif len(stack)==0 or stack[-1]>prev.val:
                if(len(stack)==0):
                    result.append(0)
                else:
                    result.append(stack[-1])
                stack.append(prev.val)
                prev=prev.next
                
            else:
                stack.pop()
                
        result.reverse()
                
        return result
        
        
        
        
        
        
        
        
        
        
        
        
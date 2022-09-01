# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        """
        x=set()
        
        while headA:       ## tc o(m+n)
                            ## sc o(m) 
            x.add(headA)
            
            headA=headA.next
            
        while headB:
            
            if headB in x:
                return headB
            
            headB=headB.next
            
        return None    
            
         """
        """
        curra,currb=headA,headB
        la,lb=0,0
        
        while curra:
            la+=1
            curra=curra.next
            
            
        while currb:
            lb+=1
            currb=currb.next    
            
        
    
            
        
        if la>lb:
            
            for i in range(la-lb):
                headA=headA.next
                
                
        elif la<lb:
            
            for i in range(lb-la):
                headB=headB.next
                
                
        while headA!=headB:
            
            headA=headA.next
            headB=headB.next
            
        return headA    
        """
        
        l1,l2=headA,headB
        
        
        while l1!=l2:
            
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
            
        return l1    
        
        
        
        
   

            
            
            
            
            
                
            
            
        
        
       
    
    
        
        
        
        
        
        
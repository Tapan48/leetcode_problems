class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        res=0
        l=0
        x=set()
        for r in range(len(s)):
            
            
            while s[r]in x:
                x.remove(s[l])
                
                l+=1
            
            x.add(s[r])
            
            res=max(res,r-l+1)
        return res    
            
            
        
        
        
        
#         l,r=0,0
#         res=0
        
#         freq={}
        
#         for r in range(len(s)):
            
            
            
#              freq[s[r]]=freq.get(s[r],0)+1
                 
#              while freq[s[r]]!=1:
                 
#                  freq[s[l]]-=1
                 
#                  if freq[s[l]]==0:
                 
#                     del freq[s[l]]
#                  l+=1
#              res=max(res,r-l+1)
                 
#         return res           
                 
                    
                 
                 
                  
              
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
#         largest=0
#         for i in range(len(s)-1):
#             length=1
#             for j in range(i+1,len(s)):
#                 if s[i]!=s[j]:
#                     length+=1
#                 else:
#                     break 
#             if length>largest:
#                 largest=length
                
#         return largest       
            
            
            
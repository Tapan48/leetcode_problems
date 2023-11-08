class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        l=0
        res,cnt=0,0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        
        
        for r in range(len(s)):
           
            cnt+=1 if s[r]in vowels else 0
            
            if r-l+1>k:
                
                cnt-=(1 if s[l] in vowels else 0)
                l+=1
            res=max(res,cnt)
        return res     
            
            
            
        
#         while r<len(s):      ### ma code 
            
            
#             while (r-l+1)<=k:
                
#                 if s[r] in vowels:
#                     cnt+=1
#                 r+=1
#             res=max(res,cnt)
#             if s[l]in vowels:
#                 cnt-=1
#             l+=1
#         return res         
            
            
            
            
            
            
            
        
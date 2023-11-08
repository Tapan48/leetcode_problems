class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        l,r=0,0
        res,cnt=0,0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        while r<len(s):
            
            
            while (r-l+1)<=k:
                
                if s[r] in vowels:
                    cnt+=1
                r+=1
            res=max(res,cnt)
            if s[l]in vowels:
                cnt-=1
            l+=1
        return res         
            
            
            
            
            
            
            
        
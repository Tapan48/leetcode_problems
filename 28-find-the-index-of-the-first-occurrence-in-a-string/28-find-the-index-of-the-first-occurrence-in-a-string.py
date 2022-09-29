class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        n=len(needle)
        last=len(haystack)-n
        for i in range(0,last+1):
            if haystack[i:i+n]==needle:
                return i
        return -1        
                
   
        
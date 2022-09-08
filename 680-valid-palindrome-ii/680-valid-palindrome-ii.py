class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        
        """
        l,r=0,len(s)-1
        
        if len(s)==1:
            return True
        
        
        for i in range(len(s)):
            
            if i==0:
                
                if s[l+1:]==s[l+1:][::-1]:
                    return True
                
            if i==len(s)-1:
                if s[l:r]==s[l:r][::-1]:
                    return True
                
            else:
                
                ns=s[l:i]+s[i+1:]
                if ns==ns[::-1]:
                    return True
                
                
                
        return False       
        """
        
        l,r=0,len(s)-1
        
        
        while l<r:
            
            if s[l]!=s[r]:
                
                sl=s[l+1:r+1]
                sr=s[l:r]
                
                return (sl==sl[::-1] or sr==sr[::-1])
           
                
            l+=1
            r-=1
            if l>=r:
                return True
                
                        
                    
                    
                    
                    
            
            
            
            
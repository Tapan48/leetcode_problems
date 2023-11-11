class Solution:
    def minFlips(self, s: str) -> int:
        
        
        ### s="111000"111000  doubled string s for type 1 operation
        ###    101010 101010 ### valid string 1
        ###    010101 010101 ## valid string 2
        n=len(s)
        s=s+s
        
        
        string1=""
        string2=""
        
        for i in range(len(s)):
            
            string1+="1"if i%2 else "0"
            string2+="0"if i%2 else "1"
            
        
        l=0
        res=len(s)
        diff1,diff2=0,0
        for r in range(len(s)):
            
            if s[r]!=string1[r]:
                diff1+=1
            if s[r]!=string2[r]:
                diff2+=1
                
            
            if (r-l+1)>n:
                if s[l]!=string1[l]:
                    diff1-=1
                if s[l]!=string2[l]:
                    diff2-=1
                l+=1
            if (r-l+1)==n:
                res=min(res,diff1,diff2)    
        return res         
                
            
            

        
        
        
        
        
        
        
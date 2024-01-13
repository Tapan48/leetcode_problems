class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        g.sort()
        s.sort()
        
        
        cnt=0
        
        gptr,sptr=0,0
        glen=len(g)
        slen=len(s)
        
        while  gptr<glen and sptr<slen:
            
            if s[sptr]>=g[gptr]:
                
                cnt+=1
                sptr+=1
                gptr+=1
            else:
                sptr+=1
        return cnt        
            
        
        
        
        
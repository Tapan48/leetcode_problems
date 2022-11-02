class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        if len(p)>len(s):
            return []
        dicp={}
        for i in range(len(p)):
            
            
            dicp[p[i]]=dicp.get(p[i],0)+1
        
        
        dics={}                    ## problem statement is to check if every string in s 
        for i in range(len(p)):              ## is an anagram of p 
            
            dics[s[i]]=dics.get(s[i],0)+1
            
            
        l=0
        res=[]
        for r in range(len(p)-1,len(s)):
            
            
            if dics==dicp:
                res.append(l)
            
            dics[s[l]]-=1
            
            if dics[s[l]]==0:
                
                 dics.pop(s[l])
            l+=1
            r+=1
            if r<len(s):
                dics[s[r]]=dics.get(s[r],0)+1
            
            
        return res     
            
                
                
                
            
            
            
            
        
        
      
            
            
            
       
        
class Solution:
    def splitString(self, s: str) -> bool:
        
        
        
        def dfs(i,prev):
            
            if i==len(s):
                return True
            
            
            for j in range(i,len(s)): ### construct the integer
                
                integer=int(s[i:j+1])
                
                if  prev-1==integer:
                    
                   
                    if dfs(j+1,integer):
                        return True
            return False
        for i in range(len(s)-1):
            
            prev=int(s[:i+1])
            
            if dfs(i+1,prev):
                return True
        return False   
                
        
                          
                
                    
                
                
                
                
                
                
        
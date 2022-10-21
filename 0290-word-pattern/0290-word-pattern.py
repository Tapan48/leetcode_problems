class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        list1=list(pattern)
        list2=s.split()
        
        
        
        if len(list1)!=len(list2):
            return False
        
        dictt={}
        for i,char in enumerate(list1):
            
            dictt[char]=dictt.get(char,0)
            
            if dictt[char]==0:
                if list2[i] in dictt.values():
                    return False
                dictt[char]=list2[i]

                
            
            else:
                if dictt[char]!=list2[i]:
                    return False
             
                
               
        return True    
            
            
        
        
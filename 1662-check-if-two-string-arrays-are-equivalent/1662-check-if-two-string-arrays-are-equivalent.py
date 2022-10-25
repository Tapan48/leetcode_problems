class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        
        
        
        s1=""
        s2=""
        
        
        for string1 in word1:
            s1+=string1
            
        for string2 in word2:
            s2+=string2
            
        if s1==s2:
            return True
        
        else:
            return False
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        
        
        freqtext=Counter(text)
        freqballon=Counter("balloon")
        
        res=len(text)
        
        for char in freqballon:
            
            ratio=freqtext[char]//freqballon[char]
            res=min(res,ratio)
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
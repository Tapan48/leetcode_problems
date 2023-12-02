class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        
        freqchars=Counter(chars)
        
        res=0
        for word in words:
            
            curword=defaultdict(int)
            
            good=True
            for char in word:
                
                curword[char]+=1
                
                if char not in freqchars or curword[char]>freqchars[char]:
                    good=False
                    break
                
            if good:
                res+=len(word)
        return res        
                
                
        
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        s=""
        for c in paragraph:
                
                if c.isalpha() or c==" ":
                    s+=(c.lower())
                elif c==",":
                    s+=(" ")
        print(s)
        x=s.split()   ## list
        print(x)
        dictt={}
        for word in x:
            
            if word not in banned:
                 
                dictt[word]=dictt.get(word,0)+1
                
        res=max(dictt.items(),key=lambda x:x[1])[0]           ##key of maximum value
        
        return res
                
                
                
                
            
            
        
        
        
        
        
        
        
        
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        
        listwords=sentence.split()
        dictionary.sort(key=len)
        
        for i,successor in enumerate(listwords):
            
            for root in dictionary:
                n=len(root)
                if root ==successor[0:n]:
                    
                    listwords[i]=root
                    break
                    
        s=" ".join(map(str,listwords))
        return s
           
                    
            
            
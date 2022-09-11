class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        
   
        arr=[]
      
                
        freqlet={}
        
        for char in licensePlate:
            
            
            if char.isalpha():
                char=char.lower()
                freqlet[char]=freqlet.get(char,0)+1
         
        
        
        for word in words:
            cnt=0
            
            for key in freqlet:
                if freqlet[key]<=word.count(key):
                    cnt+=1
                else:
                    break
                    
            if cnt==len(freqlet):
                arr.append(word)
                
        arr.sort(key=len)
        return arr[0]
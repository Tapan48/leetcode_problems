class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        
        string=""
        arr=[]
        for char in licensePlate:
            
            if char.isalpha():
              
            
                string+=char.lower()
                
        freqlet={}
        
        for char in string:
            
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
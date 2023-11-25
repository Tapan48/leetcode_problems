class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
#         sumt=sums=0
#         for char in t:
#             sumt+=ord(char)
            
            
#         for char in s:
#             sums+=ord(char)
            
#         diff=sumt-sums
        
#         res=chr(diff)
        
#         return res
          hashmaps=Counter(s)
          hashmapt=Counter(t)
    
          for char in t:
            
            scount=hashmaps[char]
            tcount=hashmapt.get(char,0)
            if scount!=tcount:
                return char
            
            
            
            
        
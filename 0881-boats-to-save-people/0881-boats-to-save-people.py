class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        
        people.sort()
        
        
        
        l,r=0,len(people)-1
        
        boats=0
        while l<=r:
            
            remainwt=limit-people[r]
            boats+=1
            r-=1
            
            if remainwt>=people[l]:
                l+=1
                
        return boats        
            
            
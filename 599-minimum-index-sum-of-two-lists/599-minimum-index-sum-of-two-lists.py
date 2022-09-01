class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
            d1={s1:i for i,s1 in enumerate(list1)}
            d2={s2:i for i,s2 in enumerate(list2)}   
            d3=defaultdict(list)
            
            
            for key in d1:
                
                if key in d2:
                    
                    d3[d1[key]+d2[key]].append(key)
                    
            return d3[min(d3.keys())]   
                    
                    
                
                
                    
        
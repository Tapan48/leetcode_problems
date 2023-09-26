class TimeMap:

    def __init__(self):
        
        
        self.dictt={}                #### key---> [[value,timestamp]...]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        
        if key not in self.dictt:
            self.dictt[key]=[]
        
        
        self.dictt[key].append([value,timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        
#         storeval=""
        
#         for keyy,value in self.dictt.items():
            
#             if keyy[0]==key and keyy[1]<=timestamp:
                
#                 storeval=value
#         return storeval   

            values=self.dictt.get(key,[])
            res=""
            l,r=0,len(values)-1
        
            while l<=r:
                
                m=(l+r)//2
                
                if values[m][1]<=timestamp:
                    res=values[m][0]
                    l=m+1
                else:
                    r=m-1
            return res          
                    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
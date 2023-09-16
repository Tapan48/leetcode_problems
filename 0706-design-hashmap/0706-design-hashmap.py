class MyHashMap:

    def __init__(self):
        
        # self.dict={}
        self.array=[-1 for i in range(1000001)]
        

    def put(self, key: int, value: int) -> None:
        
        # self.dict[key]=value
        
        self.array[key]=value
        

    def get(self, key: int) -> int:
        
        # return self.dict[key] if key in self.dict else -1
        
        return self.array[key]
        
        
        

    def remove(self, key: int) -> None:
        
        # self.dict.pop(key) if key in self.dict else self.dict
        self.array[key]=-1
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
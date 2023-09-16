class MyHashMap:

    def __init__(self):
        
        self.dict={}

    def put(self, key: int, value: int) -> None:
        
        self.dict[key]=value
        

    def get(self, key: int) -> int:
        
        return self.dict[key] if key in self.dict else -1
        
        
        

    def remove(self, key: int) -> None:
        
        self.dict.pop(key) if key in self.dict else self.dict
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
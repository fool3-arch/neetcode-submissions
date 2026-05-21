class MyHashMap:

    def __init__(self):
        self.data=[-1]*1000001
        self.value=[]

    def put(self, key: int, value: int) -> None:
        if self.data[key]==-1:
            self.value.append(value)
            self.data[key]=(len(self.value)-1)
        else:
            self.value[self.data[key]]=value

    def get(self, key: int) -> int:
        if self.data[key]!=-1:
            return self.value[self.data[key]]
        return -1
        

    def remove(self, key: int) -> None:
        self.data[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
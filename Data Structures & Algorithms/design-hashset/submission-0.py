class MyHashSet:

    def __init__(self):
        self.data=[False]*100001
    def add(self, key: int) -> None:
        if not self.data[key]:
            self.data[key]=True

    def remove(self, key: int) -> None:
        if self.data[key]:
            self.data[key]=False

    def contains(self, key: int) -> bool:
        if self.data[key]:
            return True
        else :
            return False
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
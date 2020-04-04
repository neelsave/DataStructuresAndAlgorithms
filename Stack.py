class Stack():
    def __init__(self):
        self.items = []
    
    def add(self,item):
        self.items.append(item)
    
    def remove(self):
        self.items.pop()
    
    def get_values(self):
        print(self.items)
        
    def is_empty(self):
        print(self.items == [])
    
    def top(self):
        print(self.items[-1])
    
s = Stack()
s.is_empty()
s.add("a")
s.add("b")
s.add("c")
s.remove()
s.get_values()
s.is_empty()
s.top()

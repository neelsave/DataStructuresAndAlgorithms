class Queue:
    def __init__(self):
        self.items = []
    
    def add(self,data):
        self.items.append(data)
        
    def remove(self):
        return self.items.pop(0)
        
    def print_list(self):
        print(self.items)
        
q = Queue()
q.add("A")
q.add("B")
q.add("C")
q.remove()
q.print_list()

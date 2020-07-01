class Stack:
    def __init__(self):
        self.data = []
        
    def append(self,data):
        self.data.append(data)
        
    def remove(self):
        self.data.pop(-1)
        
    def top_stack(self):
        print(self.data[-1])
        
    def count(self):
        print("count:" + str(len(self.data)))
        
    def reverse_stack(self):
        temp_stack = []
        for i in range(len(self.data)):
            temp = self.data.pop()
            temp_stack.append(temp)
        for i in range(len(temp_stack)):
            temp = temp_stack.pop(0)
            self.data.append(temp)
       
    def print_stack(self):
        print(self.data)
        
s = Stack()
s.append(10)
s.append(15)
s.append(30)
s.reverse_stack()
s.print_stack()
#s.top_stack()
#s.count()


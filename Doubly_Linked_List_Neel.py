class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class LL:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def insert_after(self,key,data):
        new_node = Node(data)
        if self.head.data == key:
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            return
        temp = self.head
        while temp:
            if temp.data == key:
                break
            temp = temp.next
        if temp.next is not None:
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
            return
        else:
            temp.next = new_node
            new_node.prev = temp
            
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            last = temp
            temp = temp.next
        while last:
            print(last.data)
            last = last.prev
            
    
    
ll = LL()
ll.append(20)
ll.append(30)
ll.append(50)
ll.prepend(10)
ll.insert_after(50,60)
ll.insert_after(10,15)
ll.print_list()
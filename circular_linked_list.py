class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Circular_Linked_List:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node = Node(data)
        temp = self.head
        
        new_node.next = self.head
        #if linked list is not none then set the next of last node
        
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
            
        self.head = new_node
        
        
    def print_list(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.data)
            temp = temp.next
        print(temp.data)
    
    
    
    
cll = Circular_Linked_List()
cll.push("10")
cll.push("9")
cll.push("6")
cll.push("3")
cll.print_list()

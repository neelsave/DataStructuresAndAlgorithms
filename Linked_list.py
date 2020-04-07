"""
Linked List Data Structure
"""

class Node:                       #creating a node class
    def __init__(self,data):      #constructor with data input for storing
        self.data = data          #data is putting in to the object.data
        self.next = None          #initially next node address is null
        
        
class LinkedList:                 #creating a linkedlist class
    def __init__(self):           
        self.head = None          #head for storing current address initially it is null

    def print_list(self):         #print function for data printing
        cur_node = self.head      #inital head position
        while cur_node:           #while current node is not null
            print(cur_node.data)  #print the cur_node address data
            cur_node = cur_node.next    #make next node as current node
        
    def append(self,data):        #append function for appending at the last position of LL
        new_node = Node(data)     #creating a object of node class 
        
        if self.head is None:     #if ll is null then append
           self.head = new_node  #newlly created node with self.head
           return
        
        last_node = self.head     #self.head to the last_node
        while last_node.next:     #while next last_node is not null
            last_node = last_node.next #last_node is equal to last_node.next
        last_node.next = new_node #append a new node to null node
      
    def prepend(self,data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
    def num_append(self,data,position):
        new_node = Node(data)
        for i in range(position):
            last_node = self.head.next
            a = last_node.next
        last_node.next = new_node   
        new_node.next = a
        
    def insert_after_node(self, prev_node, data): #still modification required in a insert after node 
        
        if not prev_node:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_node(self,key):
        cur_node = self.head
        
        if cur_node and cur_node.data == key:
            self.head =  cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
            
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
        
llist = LinkedList()    
llist.append("A")
llist.append("B")
llist.append("C")
llist.append(20)
llist.prepend("N")
llist.insert_after_node(llist.head.next,'S')
llist.delete_node("B")
llist.print_list()

# """linked list"""
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Linked_list:
#     def __init__(self):
#         self.head=None

#     def append(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=new_node

#     def display(self):
#         current=self.head
#         if not self.head:
#             print("Empty linked list")
#         else:
#             while current:
#                 print(f"{current.data} -> ", end ='')
#                 current=current.next
#             print("None")

# node=Linked_list()
# node.append(10)
# node.append(20)
# node.append(30)
# node.display()

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def insert_at_beginning(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
            
    def display(self):
        if self.head:
            current = self.head
            while current:
                print(current.data,"-->",end=' ')
                current=current.next
            print("None")
        else:
            print('None')
            
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
l1 = LinkedList()
# l1.display()
l1.append(10)
l1.append(20)
# l1.display()

def reverse(node):
    prev = None
    current = node.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    node.head = prev

# reverse(l1)
# l1.display()
# l1.reverse()
# l1.display()

def cycle(node):
    p1 = node.head
    p2 = node.head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False

def mid_value(node):
    p1 = node.head
    p2 = node.head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    return p1.data

print(cycle(l1))
l1.insert_at_beginning(99)
l1.insert_at_beginning(78)
l1.insert_at_beginning(50)
l1.display()
print(mid_value(l1))

class Dnode():
    def __init__(self, data, prev = None , next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Dnode(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
    
    def display(self):
        current = self.head
        while current:
            print(current.data,'<-->', end=' ')
            current = current.next
        print('None')
        
l2 = DoublyLinkedList()
l2.append(10)
l2.append(20)
l2.append(30)
l2.append(40)
l2.display()
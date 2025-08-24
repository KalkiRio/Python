# """linked list"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def length(self):
        length = 0
        current = self.head
        while current:
            length +=1
            current = current.next
        return length
    
    def insert_at(self, pos, data):
        if pos == 0:
            self.insert(data)
            return
        current = self.head
        idx = 0
        while current and idx < pos-1:
            current=current.next
            idx+=1
            if not current:
                return "index out of range"
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def display(self):
        current = self.head
        if not current:
            return
        while current:
            print(f"{current.data} -> ", end ='')
            current = current.next
        print("None")

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.display()

def reverse_link(node):
    current = node.head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    node.head = prev

reverse_link(l1)
l1.display()

def cycle(node):
    slow = fast = node.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(cycle(l1))

l1.insert(10)
l1.insert_at(3,45)
l1.display()
reverse_link(l1)
l1.display()

def bubble_linked_sort(node):
    if not node.head:
        return
    swapped = True
    while swapped:
        swapped = False
        current = node.head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next

bubble_linked_sort(l1)
l1.display()

def mid_value(node):
    p1 = node.head
    p2 = node.head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    return p1.data

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
"""linked list"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def display(self):
        current=self.head
        if not self.head:
            print("Empty linked list")
        else:
            while current:
                print(f"{current.data} -> ", end ='')
                current=current.next
            print("None")

node=Linked_list()
node.append(10)
node.append(20)
node.append(30)
node.display()
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_lst:
    def __init__(self):
        self.head = Node()
    

    def append(self,data):
        new_node = Node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def show(self):
        current = self.head
        elements = []

        while current.next != None:
            current = current.next
            elements.append(current.data)

        return elements
    
mylist = Linked_lst()
mylist.append(2)
print(mylist.show())
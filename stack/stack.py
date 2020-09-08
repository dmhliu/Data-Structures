from singly_linked_list import Node
"""
singly_linked_list/singly_linked_list.py
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
""""""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass
"""
class Stack:
    def __init__(self):
        self.head = None
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            print(f"push -> head: {self.head.get_value()}, next {self.head.get_next()}")
        else:
            newhead = Node(value)
            newhead.set_next(self.head)
            print(f"setting next on head to {self.head.get_value()}")
            self.head = newhead
    def pop(self):
        if self.head  is None:
            return None
        else: 
            oldhead = self.head
            self.head = self.head.get_next()
            return oldhead.get_value()
    def __len__(self):

        if self.head is None:
            return 0
        else: 
            counter = 1
            curr = self.head
            while curr.get_next():
                counter += 1
                curr = curr.get_next()
            
        return counter

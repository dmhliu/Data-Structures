from singly_linked_list import Node

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
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


    def enqueue(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
            print(f"enque -> head: {self.head.get_value()}, next {self.head.get_next()}")
        else:
            new.set_next(self.head)
            self.head = new
    def dequeue(self):
        if self.head  is None:
            return None
        elif self.head is self.tail:
            val  = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else: 
            stash = self.tail.get_value()
            # remove the last value by traversing from head => tail
            curr = self.head
            next = curr.get_next()
            while next != self.tail :
                curr = curr.get_next()
                next = curr.get_next()
            self.tail = curr
            self.tail.set_next(None)
            return stash

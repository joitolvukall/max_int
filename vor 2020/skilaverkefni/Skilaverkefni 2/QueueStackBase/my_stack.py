from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    
    def __init__(self, _type_):
        self.type = _type_
        if self.type == 'array':
            self.stack = ArrayDeque()
        elif self.type == 'linked':
            self.stack = LinkedList()

    def push(self,value):
        self.stack.push_front(value) 
        

    def pop(self):
        return self.stack.pop_front()
    
    def get_size(self):
        return self.stack.get_size()







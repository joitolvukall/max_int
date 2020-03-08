from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, _type_):
        self.type = _type_
        if self.type == 'array':
            self.queue = ArrayDeque()
        elif self.type == 'linked':
            self.queue = LinkedList()

    def add(self, value):
        self.queue.push_back(value)

    def remove(self):
        return self.queue.pop_front()

    def get_size(self):
        return self.queue.get_size()



    



class Node():
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.next = nextNode


class LinkedList():
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        if head == None:
            self.size = 0
        else:
            self.size = 1
    
    def push_back(self, value):
        if self.head == None and self.tail == None:
            self.head = Node(value)
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = Node(value)
            self.head.next = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1

    def push_front(self, value):
        if self.head == None and self.tail == None:
            self.head = Node(value, self.head)
            self.tail = self.head
        else:
            self.head = Node(value, self.head)
        self.size += 1


    def pop_front(self):
        if self.head == None:
            return None
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ''
        save_head = self.head
        if self.head == None:
            return ''
        while True:
            if self.head.next == None:
                ret_str += str(self.head.data)
                break
            else:
                ret_str += str(self.head.data) + ' '
                self.head = self.head.next
        self.head = save_head
        return ret_str





    
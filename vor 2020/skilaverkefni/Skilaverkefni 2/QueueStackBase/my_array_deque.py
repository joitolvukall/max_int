
class ArrayDeque():
    def __init__(self):
        self.front_index = -1
        self.back_index = 0
        self.size = 0
        self.capacity = 4
        self.deque = [None] * self.capacity

    def push_back(self, value):
        self.resize()
        if self.front_index == -1:#if deque is empty
            self.front_index = 0
            self.back_index = 0
        elif self.back_index == self.capacity - 1: #if backindex is at end
            self.back_index = 0
        else:                       #increment
            self.back_index += 1

        self.deque[self.back_index] = value
        self.size += 1

    def push_front(self, value):
        self.resize()
        if self.front_index == -1: # if deque is empty
            self.front_index = 0
            self.back_index = 0
        elif self.front_index == 0: #move to back
            self.front_index = self.capacity -1 
        else:                   #increment
            self.front_index -= 1

        self.deque[self.front_index] = value 
        self.size += 1


    def pop_back(self):
        if self.empty_check():
            return None
        if self.front_index == self.back_index and self.size == 1: #if deque has 1 value
            var = self.deque[self.front_index]
            self.front_index = -1
            self.back_index = -1
            self.size -= 1
            return var
        elif self.back_index == 0 and self.front_index > 0: # if back index has moved to front
            self.back_index = self.capacity - 1
            self.size -= 1
            return self.deque[0]
        else:
            var = self.deque[self.back_index] # decrement index 
            self.back_index -= 1
            self.size -= 1
            return var
       

    def pop_front(self):
        if self.empty_check():
            return None
        if self.front_index == self.back_index and self.size == 1: #if deque has 1 value
            var = self.deque[self.front_index]
            self.front_index = -1
            self.back_index = -1
            self.size -= 1
            return var
        elif self.front_index == self.capacity -1: #if front index is at end of deque
            self.front_index = 0
            self.size -= 1
            return self.deque[self.capacity-1]
        else:                                       #increment index 
            var = self.deque[self.front_index] 
            self.front_index += 1
            self.size -= 1
            return var 

    def resize(self):
        if self.front_index == 0 and self.back_index == self.capacity -1: #normal resize no need to shuffle only copy
            self.capacity *=2
            new_deque = [None]*self.capacity
            for i in range(self.back_index+1):
                new_deque[i] = self.deque[i]
            self.deque = new_deque
        elif self.size == self.capacity and self.back_index+1 == self.front_index:# need to move front to front and vice versa
            self.capacity *=2
            new_deque = [None]*self.capacity
            for i in range(self.size):
                if i < self.front_index: #when i is less then frontindex we move the front from the back of the array to the front
                    new_deque[i + (self.size - self.front_index)] = self.deque[i]
                else: #move back behind front
                    new_deque[i - self.front_index] = self.deque[i]
            self.deque = new_deque
            self.front_index = 0
            self.back_index = self.size-1

    def get_size(self):
        return self.size

    def empty_check(self):
        return self.front_index == -1


    def __str__(self):
        ret_str = ''
        for i in range(self.size):
            if i + self.front_index < self.capacity:
                ret_str += str(self.deque[i+self.front_index]) + ' ' #get front values 
            else:
               ret_str += str(self.deque[i-(self.capacity-self.front_index)]) + ' ' #get back values
        return ret_str.strip()




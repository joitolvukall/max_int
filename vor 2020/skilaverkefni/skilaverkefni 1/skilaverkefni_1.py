class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.user_array = [0] * self.capacity
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        if self.size == 0:
            return return_string
        for i in range(self.size):
            if i+1 == self.size:
                return_string += str(self.user_array[i])
            else:
                return_string += str(self.user_array[i]) + ", "
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        for i in range(self.size + 1):
            if i == self.size:
                self.user_array[0] = value
                self.size += 1
            else:
                self.user_array[(self.size)-i] = self.user_array[(self.size - 1) - i]


    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index >= self.size:
            raise IndexOutOfBounds()
        else:
            for i in range(self.size + 1):
                if (self.size)-i == index:
                    self.user_array[index] = value
                    self.size += 1
                    break
                else:
                    self.user_array[(self.size)-i] = self.user_array[(self.size - 1) - i]
        

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.user_array[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index >= self.size:
            raise IndexOutOfBounds()      
        else:
            self.user_array[index] = value  

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        else:
            return(self.user_array[0])

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index >= self.size:
            raise IndexOutOfBounds()
        else:
            return(self.user_array[index])

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        else:
            return(self.user_array[self.size - 1])

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity = (self.capacity * 2)
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.user_array[i]
        self.user_array = new_array

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index >= self.size:
            raise IndexOutOfBounds()
        else:
            for i in range(self.size - index):
                self.user_array[index + i] = self.user_array[index + (i + 1)]
            self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.__init__()

    def is_ordered(self):
        for i in range(self.size - 1):
            if self.user_array[i] > self.user_array[i+1]:
                self.ordered = False
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        self.is_ordered()
        if self.ordered == False:
            raise NotOrdered()
        for i in range(self.size):
            if value > self.user_array[i] and value < self.user_array[i + 1]:
                self.insert(value, i+1)
                break

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        self.is_ordered()
        if self.is_ordered == True:
            return self.binary_search(self.user_array[:(self.size - 1)], value)
        else:
            return self.linear_search(value)
    
    def binary_search(self, bs_array, value, size = self.size):
        if self.user_array[bs_array // 2] == value:
            return 10
        if size == 1:
            raise NotFound()
        else:
            if self.user_array[bs_array // 2] < value:
                return self.binary_search(bs_array[], value, (size // 2))
            else:
                return self.binary_search()

    def linear_search(self, value):
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.append(1)
    arr_lis.append(2)
    arr_lis.prepend(3)
    arr_lis.insert(2, 2)
    arr_lis.set_at(0, 0)
    first_value = arr_lis.get_first()
    get_value_at = arr_lis.get_at(2)
    last_value = arr_lis.get_last()
    arr_lis.resize()
    arr_lis.append(4)
    arr_lis.remove_at(2)
    #arr_lis.clear()
    arr_lis.insert_ordered(3)
    print(last_value)
    print(get_value_at)
    print("fyrsta valueið er: " + str(first_value))
    print(str(arr_lis))
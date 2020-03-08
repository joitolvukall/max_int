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
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        final_str = ""
        for i in range(self.size+1):
            if i == self.size:
                final_str = final_str.strip(", ")
                return final_str
            else:
                final_str += str(self.arr[i]) + ", "
        return final_str

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.resize()
        new_arr = [0] * self.capacity
        new_arr[0] = value
        for i in range(self.size+1):
            if i > 0:
                new_arr[i] = self.arr[i-1]
        self.arr = new_arr 
        self.size += 1

    # Time complexity: O(n) - linear time in size of list
    # def insert(self, value, index):
    #     if index > self.size: #check for index error
    #         raise IndexOutOfBounds()
    #     self.size += 1
    #     self.resize()
    #     new_arr = [0] * self.capacity # make a new array for copying 

    #     for i in range(self.size):
    #         if i < index: # if we have not yet reached our index copy self.arr to new_arr
    #             new_arr[i] = self.arr[i]
    #         elif index == i:
    #             new_arr[index] = value #when index == i we assign the new value into new_arr at the given index 
    #         else:
    #             new_arr[i] = self.arr[i-1] #add the rest of the elements from the the old arr to new_arr
    #     self.arr = new_arr            

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if (index + 1) >= self.size:
            raise IndexOutOfBounds()
        else:
            for i in range(self.size + 1):
                if (self.size - i) == index:
                    self.arr[index] = value
                    self.size += 1
                    break
                else:
                    self.arr[(self.size)-i] = self.arr[(self.size - 1) - i] 


    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index+1 > self.size:
            raise IndexOutOfBounds()
        else:
            self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index+1 > self.size:
            raise IndexOutOfBounds()
        else:
            return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[self.size-1]


    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2 #double capacity
            new_arr = [0] * self.capacity #create new array
            for i in range(self.size):
                new_arr[i] = self.arr[i] # copy old array to new resized array
            self.arr = new_arr # assign 

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        new_arr = [0] * self.capacity # initialize new list for copying
        for i in range(self.size):
            if i < index:
                new_arr[i] = self.arr[i] #copy elements before index of removal
            elif i > index:
                new_arr[i-1] = self.arr[i] #copy elements after index of removal
                #effectively ignoring the element that is removed 
        self.arr = new_arr #assign
        self.size -= 1
                

    #Time complexity: O(1) - constant time
    def clear(self):
        self.__init__()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        self.resize() #check for resize
        self.ordered_checker()
        for i in range(self.size):
            if value < self.arr[0]: # if the value is smaller than the first we prepend it to the array
                self.prepend(value) 
                break # break to avoid any extra iterations
            elif i+1 < self.size: #make sure we dont get an index out of bounds error
                if self.arr[i] <= value and self.arr[i+1] >= value: 
                    self.insert(value, i+1) # use the already ready insert function to insert new value
                    break # break to avoid any extra iterations of this loop
            else:
                self.append(value) # if we cant place the value anywhere in the ordered array it must be larger
                #thus we append it 
                

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value): 
        self.ordered_checker() #we need to find if array is ordered first 
        return self.binary_find(value)

    
    def binary_find(self, value, low = None, high = None):
        if high == None and low == None:
            low = 0
            high = self.size-1
        if low == high and self.arr[high] != value:
            raise NotFound()
        mid = (high-low)//2 + low
        if self.arr[mid] == value:
            return mid
        elif (value > self.arr[mid]):
            return self.binary_find(value, mid+1, high)
        else:
            return self.binary_find(value, low , mid)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        index = self.find(value)
        self.remove_at(index)

    def ordered_checker(self):
        sorted_bool = True
        for i in range(self.size):
            if self.arr[i] < self.arr[i-1]:
                sorted_bool = False
        if sorted_bool == False: #check if array is ordered
            raise NotOrdered()
    

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.append(1)
    arr_lis.append(2)
    arr_lis.append(3)
    arr_lis.append(4)
    arr_lis.append(6)
    arr_lis.append(11)

    arr_lis.insert_ordered(3)
    arr_lis.insert_ordered(2)
    arr_lis.insert_ordered(0)
    arr_lis.insert_ordered(5)

    print(arr_lis.find(11))
    arr_lis.remove_value(3)

    print(str(arr_lis))

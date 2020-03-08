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
        '''Returns the elements of self.arr as a string with commas'''
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
        '''adds a value to the front of arr_lis'''
        self.resize()
        new_arr = [0] * self.capacity
        new_arr[0] = value 
        for i in range(self.size+1):
            if i > 0: #skip first
                new_arr[i] = self.arr[i-1] # copy the other elements
        self.arr = new_arr 
        self.size += 1

        

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        '''inserts a new value into arr_lis at a certain index without overwriting'''
        if index > self.size or index < 0: #check for index error
            raise IndexOutOfBounds()
        self.resize()
        new_arr = [0] * self.capacity # make a new array for copying 

        for i in range(self.size+1):
            if i < index: # if we have not yet reached our index copy self.arr to new_arr
                new_arr[i] = self.arr[i]
            elif index == i:
                new_arr[index] = value #when index == i we assign the new value into new_arr at the given index 
            else:
                new_arr[i] = self.arr[i-1] #add the rest of the elements from the the old arr to new_arr
        self.arr = new_arr     
        self.size += 1       


    #Time complexity: O(1) - constant time
    def append(self, value):
        '''adds a value to the end of arr_lis'''
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        '''sets an index in arr_lis to a given value'''
        if index+1 > self.size or index < 0:
            raise IndexOutOfBounds()
        else:
            self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        '''returns first value in arr_lis'''
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        '''returns value at arr_lis'''
        if index+1 > self.size or index < 0:
            raise IndexOutOfBounds()
        else:
            return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        '''returns the last element in arr_lis'''
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[self.size-1]


    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        '''doubles the size of arr_lis if size is equals or bigger then capacity'''
        if self.size + 1 >= self.capacity:
            self.capacity *= 2 #double capacity
            new_arr = [0] * self.capacity #create new array
            for i in range(self.size):
                new_arr[i] = self.arr[i] # copy old array to new resized array
            self.arr = new_arr # assign 

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        '''removes a certain value at an index'''
        new_arr = [0] * self.capacity # initialize new list for copying
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
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
        '''clears size and values by calling init'''
        self.__init__()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        '''inserts a value into a ordered list if list is ordered'''
        if self.size == 0:
            self.append(value)
        else:
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
        '''Finds a value in an array using either a binary or linear search'''
        try: 
            self.ordered_checker() #we need to find if array is ordered first 
            return self.binary_find(value)
        except NotOrdered:
            return self.linear_find(value)
            
          
    def binary_find(self, value, low = None, high = None):
        '''binary search returns index of value'''
        if high == None and low == None: # assign high and low when not given
            low = 0 #low is lower index margin
            high = self.size-1  #high is the higher index margin
        if low == high and self.arr[high] != value: #check if value not found 
            raise NotFound()
        mid = (high-low)//2 + low #calculate middle value to check 
        if self.arr[mid] == value: 
            return mid
        elif (value > self.arr[mid]): #recur with mid as lower margin
            return self.binary_find(value, mid+1, high)
        else: #recur with mid as higher margin
            return self.binary_find(value, low , mid)
    
    def linear_find(self, value, low = 0):
        '''returns index of value with a recursive linear search'''
        if low + 1 == self.size:
            raise NotFound() 
        if self.arr[low] == value:
            return low
        else:
            return self.linear_find(value, low + 1)

        # for i in range(self.size):
        #     if self.arr[i] == value:
        #         return i
        # raise NotFound()


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        '''removes a value if it is found in an array'''
        index = self.find(value) #find index 
        self.remove_at(index) #remove at index 

    def ordered_checker(self):
        '''checks if array is ordered, raises NotOrdered if array is not ordered'''
        sorted_bool = True
        for i in range(self.size):
            if self.arr[i] < self.arr[i-1]: #when an element at i is smaller then i-1 the list cannot be ordered 
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
    arr_lis.append(5)
    arr_lis.append(7)
    arr_lis.append(8)

    print(arr_lis.find(1))
    


    print(str(arr_lis))

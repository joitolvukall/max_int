class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def palindrome(head):
    is_palindrome_boolean, _ = palindrome_recursion(head, head)
    return is_palindrome_boolean


def palindrome_recursion(back, head):
    #in this function we use head(front) and tail(back) to check if the list is a palindrome
    #this is done by sending head as two seperate values into the recursion
    #in each recursion we increment one of the head values(back) when we have reached the deepest recursive call 'back' will essentially be tail
    #then on the way back we can iterate front to front.next and return that to the next upper function call
    #we then are essentially comparing head - tail and then head.next - tail.prev then head.next.next - tail.prev.prev.  etc...
    #this ensures that the front and back values are equal and that the list/string is a palindrome
    if back == None: #step through all nodes until node == None
        return (True, head) #return True to start check and head as 'front' 
    #Front is iterated on the way back through the recursion

    is_palindrome, front = palindrome_recursion(back.next, head) 

    if not is_palindrome: #check if bool is False then we go out of recursion and return False
        return False, front.next
    
    is_palindrome_bool = front.data == back.data #compare the front node to back node

    return (is_palindrome_bool, front.next) #iterate heat to next 


        


if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
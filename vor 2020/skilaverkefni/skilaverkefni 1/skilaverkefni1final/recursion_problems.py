 # 10 mod 4
def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    '''returns the a mod b'''
    if a < b:
        return a
    var = a - b
    if var > b:
        return modulus(var, b)
    elif var < b:
        return var
    else:
        return 0



def how_many(lis1, lis2):
    '''returns an integer the value of which is how many of the items in ​an element in lis1​ is also in ​lis2​'''
    if len(lis1) == 0:
        return 0
    if lis1[0] in lis2:
        return 1 + how_many(lis1[1:], lis2)
    else:
        return how_many(lis1[1:], lis2)
    


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)
    test_modulus(3,7)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a','a','b','c','f'], ['a','a',"b","c","d","e","f","g"]) 


if __name__ == "__main__":
    run_recursion_program()
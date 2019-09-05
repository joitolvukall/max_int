num_int = int(input("Input a number: "))    # Do not change this line

max_int = []

while num_int > 0:
    max_int.append(num_int)
    num_int = int(input("Input a number: "))

print("The maximum is", max(max_int))    # Do not change this line

n = int(input("Enter the length of the sequence: ")) # Do not change this line

n_sequence = []
new_n = 0


for i in range(1,n+1):
    if 1==i:
        n_sequence.append(i)
        print(i)
    elif 2==i:
        n_sequence.append(i)
        print(i)
    elif 3==i:
        n_sequence.append(i)
        print(i)
    else:
        n_sequence.append(sum(n_sequence[-3:-1])+n_sequence[-1])
        print(n_sequence[-1])
        
        

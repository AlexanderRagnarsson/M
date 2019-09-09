#Ask for input
length = int(input("Enter the length of the sequence: ")) 
#Create variable that remember the last three integers of the sequence
num1 = 1
num2 = 2
num3 = 3
if length >= 1:
    print(num1)
if length >= 2:
    print(num2)
if length >= 3:
    print(num3)

sequence_len = 3
#The boolean checks if the sequence is long enough else run again
while sequence_len < length:
    #Add the last three variables together to create a new integer in the sum
    temporary_variable = num3
    num3 = num1 + num2 + num3
    num1 = num2
    num2 = temporary_variable
    print(num3)
    """if x < y and x < z:
        x = x + y + z
        print(x)
    elif y < x and y < z:
        y = y + x + z
        print(y)
    else:
        z = z + x + y
        print(z)    """
    sequence_len += 1
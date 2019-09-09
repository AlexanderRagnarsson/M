num_int = int(input("Input a number: "))
if num_int > 0:
    max_int = 0

#Have a while loop that asks for repeated inputs as long as the last input was positive
while num_int > 0:
#Check if the input is larger than the maximum input
    if num_int > max_int:
        max_int =  num_int
    num_int = int(input('Input a number: '))


print("The maximum is", max_int)    # Do not change this line
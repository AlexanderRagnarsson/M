my_int = int(input('Give me an int >= 0: '))

quotient = my_int
bin_str = '' #empty string

# Binary numbers can be found by repeatedly dividing by 2
# (floor division so that is is an int) and 
# adding the remainder at each step in front of a string.
# We stop when the quotient is 0 and the string is then the binary number 

while quotient > 0:
    remainder = quotient%2
    #Adding the remainder to the front of the string
    bin_str = str(remainder) + bin_str
    quotient = quotient//2

#Special case as the while loop is not entered when my_int = 0 and the binary of 0 is 0
if my_int == 0:
    bin_str = '0'

print("The binary of", my_int, "is", bin_str)
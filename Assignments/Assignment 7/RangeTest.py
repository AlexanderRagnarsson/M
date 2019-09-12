# The function definition goes here
def range_checker(num):
    if 1 < num < 555:
        return True


num = int(input("Enter a number: "))


if range_checker(num):      
    print(num, 'is in range.')
else:       #num is not in the range
    print(num, 'is outside the range!')
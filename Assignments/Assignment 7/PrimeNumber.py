# is_prime function definition goes here
def is_prime(num):
    """Returns True if a integer input is prime and False otherwise"""
    for i in range(2, num):
        if num%i == 0:  #The number is divisable by i so it is not prime
            return False
    #Only runs if no divisor was found
    return True


num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message

if is_prime(num):
    print(num, 'is a prime')
else:
    print(num, 'is not a prime')
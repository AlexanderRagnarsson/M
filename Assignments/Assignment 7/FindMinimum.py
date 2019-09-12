def find_min(num1, num2):
    """Receive two integer inputs and return the larger integer"""
    if num1 < num2:
        return num1
    else:   #num2 smaller
        return num2

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = find_min(first,second) 

print("Minimum: ", minimum)
# Your function definition goes here
def fibonacci(n):
    """Take a number a returns a string of the fibonacci sequence with as many
     numbers as the input"""
    num1 = 1
    num2 = 0
    fibbonacci_str = ''

    #Add a new number to the fibbonacci sequence every runthorugh and runs through n times
    for i in range(n):
        if num1 > num2:
            #Add the larger number to the string
            fibbonacci_str += str(num1) + ' '
            num2 += num1
        else: #num2 is larger
            #Add the larger number to the string
            fibbonacci_str += str(num2) + ' '
            num1 += num2
    
    return fibbonacci_str


n = int(input("Input the length of Fibonacci sequence (n>=1): "))

print(fibonacci(n))
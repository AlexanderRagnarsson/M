for number in range(10, 100):  
    #Checks if the digit sum squared is equal to the number   
    if (number//10 + number%10)**2 == number:
            print(number)

for number in range(1, 100):
    divisor_count = 0
    #Checks how many divisors number has
    for possible_divisor in range(1, number+1):
        if number%possible_divisor == 0:
            divisor_count += 1
    if divisor_count == 10:
        print(number)
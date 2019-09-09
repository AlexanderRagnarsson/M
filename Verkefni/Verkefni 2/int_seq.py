total = 0
biggest_number = 0
odd_count = 0
even_count = 0
user_input = int(input('Enter an integer: '))

while user_input > 0:
    if user_input > biggest_number:
        biggest_number = user_input
    if user_input > 0:
        total += user_input
        if user_input % 2:  
            odd_count += 1
        else:
            even_count += 1
        print('Cumulative total:', total)

    user_input = int(input('Enter an integer: '))

    if user_input <= 0:
        print('Largest number:', biggest_number)
        print('Count of even numbers:', even_count)
        print('Count of odd numbers:', odd_count)


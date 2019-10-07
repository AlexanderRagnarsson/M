#Not really in assignment 12
def password_count(N):
    """Takes an integer representing number of numbers in a password
    Retruns amount of passwords that fullfill the conditions
    Conditions: There is atleast one instance in the password 
        where there are atleast two of the same number side by side"""
    password = '1' + '0' * (N)
    count = 0
    while int(password) - 10 ** N <= int('9'* N):
        for index, char in enumerate(password[1:-1]):
            if char == password[index+2]:
                count += 1
                break
        password = str(int(password) + 1)
    return count

for i in range(1, 10):
    print('Password Count: {:10} Password length: {}'.format(password_count(i), i))
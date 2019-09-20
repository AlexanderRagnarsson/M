def safe_input(prompt, a_type):
    while True:
        user_input = input(prompt)
        try:
            return(a_type(user_input))
        except ValueError:
            print("Error: please enter a value of", a_type)


print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))
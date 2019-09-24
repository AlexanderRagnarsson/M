# Your functions should appear here
def loop_bool(user_input):
    """Takes a string and return False if the string is exit and True otherwise"""
    if user_input == 'exit':
        return False
    return True

def input_prompt():
    """Asks user for input and return it"""
    user_input = input('Enter value to be added to list: ')
    return user_input

def printer(value_list):
    """Takes a list and print every item in the list a total of three times"""
    value_list *= 3
    for i in value_list:
        print(i)
    
# Main program starts here
value_list = []
user_input = input_prompt()
while loop_bool(user_input):
    value_list.append(user_input)
    user_input = input_prompt()
    
printer(value_list)

# It should mostly be a sequence of function calls


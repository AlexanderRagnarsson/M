def menu_selection():
    """Prints possible operations and asks user for operation choice, returns choice"""
    print('Menu: ')
    choice = input('add(a), remove(r), find(f): ')
    return choice

def add(a_dict):
    """Accepts a dictionary adds a key-value pair to dictionary based on user input. Prints error message if key is in dicitonary.
    Returns nothing"""
    key = input('Key: ')
    value = input('Value: ')
    if key in a_dict:
        print('Error. Key already exists.')
    else:
        a_dict[key] = value

def remove(a_dict):
    """Accepts a dicitonary removes a key-value pair based on user input. Prints error mesage if key was not found
    Returns nothing"""
    key = input('key to remove: ')
    try:
        a_dict.pop(key)
    except KeyError:
        print('Key not found.')

def find(a_dict):
    """Accepts a dicitonary finds a key-value pair and prints value corresponding to key from user input.
    Prints error mesage if key was not found. Returns nothing"""
    key = input('Key to locate: ')
    try:
        print('Value: ', a_dict[key])
    except KeyError:
        print('Key not found.')


def execute_selection(choice, a_dict):
    """Accepts key and dictionary and excecutes the correspponding function on dictionary"""
    if choice == 'a':
        add(a_dict)
    elif choice == 'r':
        remove(a_dict)
    else:
        find(a_dict)

def dict_to_tuples(a_dict):
    """Accepts a dictionary and returns list of tuple containing every key-value pair in the dictionary"""
    return(list(a_dict.items()))

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()
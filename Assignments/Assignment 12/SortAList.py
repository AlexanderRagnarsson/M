# sort_list() function goes here
def sort_list(unsorted_list):
    """Accepts list sorts the argument list"""
    unsorted_list.sort()
# get_list() function goes here
def get_list():
    """Asks user for digits until he enters a character, returns list of integers"""
    return_list = []
    while True:
        user_input = input()
        if user_input.isdigit():
            return_list.append(int(user_input))
        else:
            return return_list

# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()
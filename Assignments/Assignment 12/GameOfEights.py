def eight_checker():
    """Asks user for a input of numbers seperated by commas, 
    returns and Error if there are characters in input, True if there are two 8 in a row 
    and False otherwise"""
    num_list = input('Enter elements of list separated by commas: ').split(',')
    for char in num_list:
        if char.isalpha():
            return 'Error - please enter only integers.'
    for index, char in enumerate(num_list):
        if char == '8':
            try:
                if num_list[index+1] == '8':
                    return True
            except IndexError:
                return False
    return False

print(eight_checker())
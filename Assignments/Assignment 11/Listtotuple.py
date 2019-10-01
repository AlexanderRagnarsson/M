#list_to_tuple function goes here
def list_to_tuple(list):
    """
    Takes a list and puts turn every element in list to integer
    and returns a tuple of those integers. Prints error message and returns empty 
    tuple if there is an element that i not list
    """
    templist = []
    for i in list:
        try:
            templist.append(int(i))
        except ValueError:
            print('Error. Please enter only integers.')
            return ()
    return tuple(templist)
# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)
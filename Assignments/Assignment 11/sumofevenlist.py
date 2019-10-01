def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list
def even_sum(datalist):
    """
    Takes a list of integers and returns the sum of all even integers
    """
    return_list = []
    for i in datalist:
        #check is the int is even
        if int(i) % 2 == 0:
            return_list.append(int(i))
    return sum(return_list)
# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
def adder(size_int):
    """
    Takes a vector size, int, asks users for vector elements and returns corosponding vector as list
    """
    element_list = []
    for i in range(1, size_int +1):
        element_float = float(input('Element no ' + str(i) + ': '))
        element_list.append(element_float)
    return element_list

def input_prompt():
    """
    Asks the user for vector size and returns a list of two lists representing vectors
    """
    size_int = int(input('Input vector size: '))
    
    element_list = []
    element_list.append(adder(size_int))
    element_list.append(adder(size_int))
    
    return element_list

def dot_product(lists_lst):
    """
    Takes a list of two lists representing vectors as input and returns dot product of
    the vectors
    """
    dot_product_int = 0
    counter = 0
    while counter < len(lists_lst[0]):
        dot_product_int += lists_lst[0][counter] * lists_lst[1][counter]
        counter += 1
    return dot_product_int


# Main program starts here
vector_list = input_prompt()
dot_product_value = dot_product(vector_list)
print('Dot product is:', dot_product_value)
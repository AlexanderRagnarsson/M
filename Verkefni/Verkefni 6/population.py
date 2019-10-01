def prompt():
    """
    Asks user for file name returns the opened file
    Returns False if file is not found
    """
    try:
        file_name = input('Enter filename: ')
        data_file = open(file_name, 'r')
        return data_file
    except FileNotFoundError:
        print('Filename', file_name, 'not found!')
        return False

def year(data):
    """
    Takes data, list of strings (representing lines in data file)
    Asks user for year and returns index of year in list of first line of data file
    If year is not found is tells the user Invalid input and asks again for year
    """
    while True:
        year = input('Enter year: ')
        year_index_int = year_index(data, year)
        if year_index_int:
            return year_index_int
        else:
            print('Invalid year!')

def year_index(data, year):
    """
    Takes data, list of strings(representing lines in data file) and year, str
    Finds where ,in a list of the first line, the year is and returns that index
    """ 
    first_line_str = data[0]
    first_line_list = first_line_str.split()
    for index, value in enumerate(first_line_list):
        if str(year) == value:
            return index

def min_max_finder(data_file, index):
    """
    Takes a data file, list of string (representing lines), and index representing what year.
    Returns the max and min population (int) and corresponding state name (list)
    min pop state and max pop state are returned together as one tuple
    """
    first_line_list = data_file[1].split()
    x = len(first_line_list) - len(data_file[0].split()) #Important if state name is larger than 1 word

    pop = int(first_line_list[index+x])
    state = first_line_list[0:1+x]
    max_pop_state = pop,state
    min_pop_state = pop,state
    
    for line in data_file[2:]:
        line_list = line.split()
        x = len(line_list) - len(data_file[0].split())  #Important if state name is larger than 1 word
        if int(line_list[index + x]) > max_pop_state[0]:
            max_pop_state = (int(line_list[index + x]), line_list[0 : 1 + x])
        elif int(line_list[index + x]) < min_pop_state[0]:
            min_pop_state = (int(line_list[index + x]), line_list[0: 1 + x])
    
    return min_pop_state, max_pop_state

def type_conversion(pop_state_tuple):
    """
    Takes a tuple of str and list, representing year and state name
    and returns a tuple with the first value unchanged and all later value made into str
    """
    state_str = ''
    for i in pop_state_tuple[1]:
        state_str += i + ' '
    return pop_state_tuple[0], state_str[:-1]

data_file = prompt()
if data_file:
    data_file_list = data_file.readlines()
    year_index = year(data_file_list)
    min_data, max_data = min_max_finder(data_file_list, year_index)

    min_data = type_conversion(min_data)
    max_data = type_conversion(max_data)

    print('Minimum:', min_data)
    print('Maximum:', max_data)
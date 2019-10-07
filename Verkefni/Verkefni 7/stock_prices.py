"""Assume a csv file with the data as Date,Open,High,Low,Close,Adj Close,Volume """
CLOSE_index = -2
VOLUME_index = -1
DATE_index = 0

def prompt():
    """Asks user for file name and returns open filestream
    Says File not found if it was not found and returns False"""
    try:
        file_name = input('Enter filename: ')
        return open(file_name, 'r')
    except FileNotFoundError:
        print('Filename {} not found!'.format(file_name))
        return False

def get_data_list(data_file):
    """Takes a data file (csv file) and returns a list with same data as in the file"""
    data_list = []
    for line_str in data_file:
        # strip beginning and end of line, split on commas and append to datalist
        data_list.append(line_str.strip().split(','))
    return data_list

def get_monthly_averages(data_list):
    """Accepts list (Data,Open,High,Low,Close,Adj. Close, Volume) of floats
    Returns average prices for each month as tuple (year-month, avg. price)"""
    year_month = data_list[1][DATE_index][:7]
    ViCi_sum = 0
    Vi_sum = 0
    monthly_averages_list = []
    for line in data_list[1:]:  #skip first line
        if line[DATE_index][:7] != year_month:
            to_append_tuple = year_month, ViCi_sum/Vi_sum
            monthly_averages_list.append( to_append_tuple )
            year_month = line[DATE_index][:7]
            ViCi_sum = 0
            Vi_sum = 0
        ViCi_sum += ( float(line[VOLUME_index]) * float(line[CLOSE_index]) )
        Vi_sum += float(line[VOLUME_index])
    #Append one last time as for loop is finished
    to_append_tuple = year_month, ViCi_sum/Vi_sum
    monthly_averages_list.append(to_append_tuple)

    return monthly_averages_list


def get_highest_price(data_list):
    """Accepts list (Data,Open,High,Low,Close,Adj. Close, Volume) of floats
    Returns highest Adj. Close value found in list as tuple (date, price)"""
    highest_price_date_str = data_list[1][DATE_index]
    highest_price_float = float(data_list[1][CLOSE_index])
    for line in data_list[2:]:
        if float(line[CLOSE_index]) > highest_price_float:
            highest_price_date_str = line[DATE_index]
            highest_price_float = float(line[CLOSE_index])
    return highest_price_date_str, highest_price_float

def print_info(monthly_averages_list, highest_price_tuple):
    """Accepts a list of tuples and a tuple both of type(data, price)
    Prints values in tuples in a formatted way"""
    print('{:10s}{:>7s}'.format('Month', 'Price'))
    for data in monthly_averages_list:
        print('{:10s}{:7.2f}'.format(data[0], data[1]))
    print('Highest price {:.2f} on day {}'.format(highest_price_tuple[1], highest_price_tuple[0]))


def main():
    file_name = prompt()
    if not file_name: #File was not found
        return  #Nothing else in main runs
    data_list = get_data_list(file_name)
    file_name.close()   #File stream no longer needed as the list already stores all data
    monthly_averages_list = get_monthly_averages(data_list)
    highest_price_tuple = get_highest_price(data_list)
    print_info(monthly_averages_list, highest_price_tuple)

main()
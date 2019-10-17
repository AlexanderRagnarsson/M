import string

def initial_prompt():
    """ Accepts nothing and returns rows and seats 
        as int based on user input """
    rows_int = int(input('Enter number of rows: '))
    seats_int = int(input('Enter number of seats in each row: '))
    return rows_int, seats_int

def rows_seats_maker(rows, seats):
    """ Accepts row and seats (int) returns list of list """
    seats_list = []
    for letter in string.ascii_uppercase[:seats]:
        seats_list.append(letter)
    
    rows_list = []

    for _ in range(rows):
        rows_list.append(seats_list[:])

    return rows_list

def seats_print(seat_list):
    """ Accepts seat list and prints list of seats """
    for i in range(len(seat_list)):
        print('{:2d}'.format(i+1), end=('   ') )
        for seat_letter in seat_list[i]:
            print(seat_letter, end=(' '))
            if seat_letter == seat_list[i][ len(seat_list[0])//2 -1 ]:  #Checks if it is the seat next to the middle and prints out a space between the seats if that is the case
                print(end='  ')
        print()     #New line


def seat_taker_prompt(rows, seats):
    """ Accepts rows and seats. Returns seat number (row seat) 
    gotten from user input if it is valid. Returns False otherwise """
    seat_input_list = input('Input seat number (row seat): ').split()
    try:
        seat_input_list[0] = int(seat_input_list[0])
    except ValueError:
        print('Seat number is invalid!')
        return False

    if seat_input_list[0] > rows:
        print('Seat number is invalid!')
        return False

    for index, letter in enumerate(string.ascii_uppercase):
        if index + 1 > seats:
            print('Seat number is invalid!')
            return False
        if letter == seat_input_list[-1]:
            return seat_input_list

def seat_list_checker(seat_number_list, seat_list):
    """ Accpets seat number and seat list. Checks to see if seat number is already taken and prints
        a message if thats the case. Returns True if it wast taken and False if not. """
    seats_only_list = seat_list[ int(seat_number_list[0])-1 ]
    if seat_number_list[-1] not in seats_only_list:
        print('That seat is taken!')
        return True
    else:
        return False


def seat_list_changer(seat_number_list, seat_list):
    """ Accepts seat_number and seat_list and returns seat list with
        X in that seat number """
    seats_only_list = seat_list[ int(seat_number_list[0])-1 ]
    for index, seat_letter in enumerate( seats_only_list ):
        if seat_letter == seat_number_list[-1]:
            seats_only_list[index] = 'X'
            return seat_list

def seats_full(seat_list):
    """ Accepts a seat list and return True is seats are all full and False otherwise """
    for row in seat_list:
        for seat in row:
            if seat != 'X':
                return False
    return True

def main():
    rows_int, seats_int = initial_prompt()
    seat_list = rows_seats_maker(rows_int, seats_int)
    seats_print(seat_list)

    continue_str = 'y'
    while continue_str == 'y':
        seat_number = seat_taker_prompt(rows_int, seats_int)
        if not seat_number:     
            continue
        
        seat_taken = seat_list_checker(seat_number, seat_list)
        if seat_taken:
            continue

        seat_list = seat_list_changer(seat_number, seat_list)
        seats_print(seat_list)

        if seats_full(seat_list):   #True if seats are full
            break                   

        continue_str = input('More seats (y/n)? ')

main()
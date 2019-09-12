position_int123 = int(input('Input a position between 1 and 10: '))
loop_boolean = True

def display(position):
    """The position is an integer. Displays where the character is located"""
    print('X' * (position-1)  +  'O'  +  'X' * (10-position))

def move(direction):
    """Direction is a string. Changes the position og the charcter depending on user input 
    and breaks the loop if the input is not r or l"""
    if direction == 'r':
        return 1
    if direction == 'l':
        return -1
    else:
        return False


display(position_int123) #prints current character position

print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting')  


while loop_boolean:
    direction_str = input('Input or your choice: ')
    if type(move(direction_str)) == bool:
        #breaks the loop after the display function is run since the boolean will now be False
        loop_boolean = move(direction_str)
        #Show the position one last time before the break
        display(position_int123)   
    else:
        position_int123 += move(direction_str)
        #Make sure the position is within our string limit
        if position_int123 > 10:   
            position_int123 = 10
        if position_int123 < 1:
            position_int123 = 1
        #Show the current position    
        display(position_int123)
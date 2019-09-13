position_int = int(input('Input a position between 1 and 10: '))
loop_boolean = True

def display(position):
    """The position is an integer. Displays where the character is located"""
    print('x' * (position-1)  +  'o'  +  'x' * (10-position))

def move(direction):
    """Direction is a string. Returns either 1 ('r') or -1 ('l') that will be used to change the position_int 
    depending on user input but it returns False to breaks the loop if the input is not r or l"""
    if direction == 'r':
        return 1
    if direction == 'l':
        return -1
    else:
        return False


display(position_int) #Prints current position

print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting')  


while loop_boolean:
    direction_str = input('Input your choice: ')
    if type(move(direction_str)) == bool:
        #Breaks the loop after the display function is run since the boolean will now be False
        loop_boolean = move(direction_str)
        #Show the position one last time before leaving the while loop
        display(position_int)   
    else:
        position_int += move(direction_str)
        #Make sure the position is within our string limit
        if position_int > 10:   
            position_int = 10
        if position_int < 1:
            position_int = 1
        #Show the current position    
        display(position_int)
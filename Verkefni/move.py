position_int = int(input('Input a position between 1 and 10: '))

def display(position):
    """The position is an integer. Displays where the character is located"""
    print('x' * (position-1)  +  'o'  +  'x' * (10-position))

def move(direction):
    """Direction is a string. Returns either 1 ('r') or -1 ('l') that will be used to change the position_int 
    depending on user input"""
    if direction == 'r':
        return 1
    if direction == 'l':
        return -1


display(position_int) #Prints current position

print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting')  

loop_boolean = True

while loop_boolean:
    direction_str = input('Input your choice: ')
    if direction_str != 'r' and direction_str != 'l':
        #Show the position one last time
        display(position_int)   
        #Makes us leave the while loop
        loop_boolean = False
    else:
        position_int += move(direction_str)
        #Make sure the position is within our string limit
        if position_int > 10:   
            position_int = 10
        if position_int < 1:
            position_int = 1
        #Show the current position    
        display(position_int)
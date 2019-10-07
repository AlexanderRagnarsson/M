def make_new_row(old_row):
    """
    Takes an old row of the Pascal's triangel, list of ints
    and returns the next_row 
    """
    if old_row == []:
        return [1]
    new_row = []
    for i in range(len(old_row)):
        if i == 0:
            new_row.append(1)
        else:
            new_row.append(old_row[i] + old_row[i-1])
    new_row.append(1)
    return new_row
        
    
# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
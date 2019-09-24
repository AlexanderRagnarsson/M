import string

def swapper(word):
    """
    Takes a string as an input and swappes every two 
    characters in the string around and returns a string with the swapped characters
    """
    return_str = ''
    for index in range(0, len(word), 2):
        try:
            return_str += word[index+1] + word[index] 
        except IndexError:
            #Final char of word never added to the return_str if IndexError so we add it
            return_str += word[-1]
    return return_str

def scrambler(word):
    """
    takes string, and returns a string with the first character, last character and punctuation of the string at correct places
    but with every two characters in between swapped around
    """
    new_str = word.strip()

    #nothing to swap in a 1 ir 2 chararcter word
    if len(new_str) == 1 or len(new_str) == 2:
        return new_str

    elif new_str[-1] in string.punctuation: #We have a punctuation at the end
        partial_str = new_str[1:-2]    #Only the char we want to swap around (not first or last or the punctuation)
        return new_str[0] + swapper(partial_str) + new_str[-2:]   #First char, swapped chars, last char and punctuation

    else: #We dont have a punctution at the end
        partial_str = new_str[1:-1]     #Only char we want to swap around (not first or last)
        return new_str[0] + swapper(partial_str) + new_str[-1]    #Last letter at back
    
try:
    user_input = input('Enter name of file: ')
    data_file = open(user_input ,'r')
except FileNotFoundError:
    print('File', user_input, 'not found!')

for word in data_file:
    print(scrambler(word), end=(' '))

#Add new line
print()
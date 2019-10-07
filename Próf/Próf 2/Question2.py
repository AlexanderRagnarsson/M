def file_opener():
    """
    Asks user for file name and returns opened file
    Returns None (False bool value) and prints file not found if file was not found
    """
    file_name = input('Enter filename: ')
    try:
        return open(file_name, 'r') #Has True bool value
    except FileNotFoundError:
        print('File', file_name, 'not found!')

def word_count(data):
    """
    Takes a file of words and counts how many words and punctuations are in a file
    Returns count
    """
    punctuations = (',', '.', '!', '?')
    count = 0
    for line in data:
        word_list = line.split()
        for word in word_list:
            count += 1
            if word[-1] in punctuations:    #Counts as one extra word
                count += 1
    return count

#Main programs
file_name = file_opener()
if file_name:   #File was found
    print(word_count(file_name))
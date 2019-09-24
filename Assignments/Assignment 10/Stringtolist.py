def word_splitter(word):
    """
    Takes a string and splits is up into words which it appends to a list
    when there is a space or comma and then returns the list
    """
    return_list = []
    append_word = ''
    #Appends word to list whenever there is a space or comma next
    for char in word:
        if char == ',' or char == ' ':
            return_list.append(append_word)
            append_word = ''
        else:
            append_word += char
    #We never append the word if we dont end with a space or comma so lets append it the the list
    if word[-1] != ' ' or word[-1] != ',':
        return_list.append(append_word)
    return return_list
# The main program starts here
the_string = input("Enter the string: ")
# call your function here
the_list = word_splitter(the_string)
print(the_list)
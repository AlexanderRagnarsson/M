import string

def finder(user_input):
    """Takes a string and returns every unique letter of the string
    in correct order"""
    return_list = []
    
    for char in user_input.strip():
        #We dont want any repetition, punctuation or spaces
        if char in return_list or char in string.punctuation or char == ' ':
            continue
        else:
            return_list.append(char)
    
    return return_list


sentence = input("Input a sentence: ")

unique_letters = str(finder(sentence))

print("Unique letters:", unique_letters)
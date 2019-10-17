import string

def get_word_list(data):
    """Accepts file stream and returns list of words in file (no punctuations and all lower case)"""
    return_list = []
    for line in data:
        line_list = line.split()
        for word in line_list:
            word = word.strip().strip(string.punctuation)
            return_list.append(word.lower())
    return return_list

def word_list_to_counts(word_list):
    """Accepts word list and returns dictionary containing word as key and number of times it appears as value"""
    return_dict = {}
    for word in word_list:
        try:
            return_dict[word] += 1
        except KeyError:
            return_dict[word] = 1
    return return_dict

def dict_to_tuple(word_count_dict):
    """Accepts dict and returns a list of tuple where tuple are (key, value)"""
    return(list(word_count_dict.items()))

def main():
    filename = input("Name of file: ")
    # Get a file stream
    fstream = open(filename)
    # Get a list of words from the stream
    word_list = get_word_list(fstream) 
    fstream.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()
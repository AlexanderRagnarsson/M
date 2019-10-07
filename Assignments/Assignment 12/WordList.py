import string

def punctuation_remover(word):
    """Accepts word returns word with removed punctuations of ends of word"""
    for punctuation in word:
        word.strip(punctuation)
    return word
    
def add_to_list(data_file):
    """Accepsts file containing sentances,
    returns an alphabetized list of words (removes all punctuation)"""
    word_list = []
    for line in data_file:
        line_list = line.split()
        for word in line_list:
            word.strip(string)
            word_list.append(punctuation_remover(word))
    return sorted(word_list)

def make_list_unique(word_list):
    """Accepts a list of words and returns list containing only unique words"""
    unique_list = []
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

#Main program
file_name = open(input('Enter filename: '), 'r')
word_list = add_to_list(file_name)
unique_list = make_list_unique(word_list)

print(unique_list)
import string

def open_file(filename):
    try:
        return open(filename)
    except FileNotFoundError:
        return False

def make_paragraph_word_list(filestream):
    """ Accepts a filestream and returns a list of lists where
        each inner list is all the words in a paragraph """
    return_word_list = []
    paragraph_word_list = []

    for line in filestream:
        if line == '\n':
            return_word_list.append(paragraph_word_list)
            paragraph_word_list = []

        line_list = line.split()
        for word in line_list:
            word = word.strip().strip(string.punctuation).lower()
            if word not in paragraph_word_list:
                paragraph_word_list.append(word)
    return_word_list.append(paragraph_word_list)
    return return_word_list


def make_paragraph_dict(paragraph_word_list):
    """ Accepts a list of lists (inner list contains strings) and returns a 
        dictionary where word is the key and inner lists it apears in is the value """
    paragraph_word_dict = {}

    for paragraph_number in range(1, len(paragraph_word_list) + 1):
        paragraph = paragraph_word_list[paragraph_number - 1]
        
        for word in paragraph:
            if word in paragraph_word_dict:
                paragraph_word_dict[word] = paragraph_word_dict[word] + ', ' + str(paragraph_number)
            else:
                paragraph_word_dict[word] = str(paragraph_number)
    return paragraph_word_dict


def make_count_dic(filestream):
    """ Accepts a filestream and returns a dictionary where key is word and
        value is the number of times it appears """
    count_dict = {}

    for line in filestream:
        for word in line.split():
            word = word.strip().strip(string.punctuation).lower()
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
    return count_dict


def sorted_dict_print(dictionary):
    """ Accepts a dictionary and prints ever key value pair in sorted order """
    for k, v in sorted(dictionary.items()):
        print(k, v)
    print() #New line


def fancy_dict_print(dict_list):
    """ Accepts a list of tuples. Prints values in tuples seperated by : and a space
        one tuple in each line. Returns None """
    for k, v in dict_list:
        print(k + ':', v)


def main():
    filename = input('Enter filename: ')
    filestream = open_file(filename)  

    if not filestream:
        print('Filename', filename, 'not found!')
        return                              #Nothing else runs
    
    file_list = filestream.readlines()      #List of all lines in file
    filestream.close()

    paragraph_word_list = make_paragraph_word_list(file_list)
    paragraph_word_dict = make_paragraph_dict(paragraph_word_list)

    count_dict = make_count_dic(file_list)
    count_list_alphabetized = sorted(count_dict.items())
    count_list = sorted(count_list_alphabetized, key=lambda x: x[1], reverse=True)

    print('The paragraph index: ')
    sorted_dict_print(paragraph_word_dict)

    print('The highest 10 counts: ')
    fancy_dict_print(count_list[:10])
    print()                                 #New line
    print('The highest 20 counts: ')
    fancy_dict_print(count_list[:20])

main()
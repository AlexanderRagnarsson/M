import string
from operator import itemgetter

def word_list_maker(filestream):
    """ Accepts a filestream and returns a list of lowerscased words 
        where puncutations and whitespace have been stripped """
    word_list = []

    for line in filestream:
        line_list = line.split()
        for word in line_list:
            word = word.strip().strip(string.punctuation).lower()
            
            word_list.append(word)

    return word_list

def bigram_count(word_list):
    """ Accepts a word list and returns a dictionary with count of bigrams """
    
    bigram_count_dict = {}
    for index, word in enumerate(word_list[:-1]):
        next_word = word_list[index + 1]
        if (word, next_word) in bigram_count_dict:
            bigram_count_dict[(word, next_word)] += 1
        else:
            bigram_count_dict[(word, next_word)] = 1
    return bigram_count_dict


def main():
    filestream = open(input('Enter name of file: '))
    word_list = word_list_maker(filestream)
    bigram_count_dict = bigram_count(word_list)
    bigram_count_list = sorted(bigram_count_dict.items(), key=itemgetter(1) , reverse=True) 
    print(bigram_count_list[:10])

main()
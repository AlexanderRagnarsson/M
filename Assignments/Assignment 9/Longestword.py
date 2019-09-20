filename = input('Enter filename: ')

data_file = open(filename)


longest_word = ''
longest_length = 0
for word in data_file:
    word = word.strip()
    if len(word) > longest_length:
        longest_length = len(word)
        longest_word = word

print("Longest word is '" + longest_word + "' of length", longest_length)

data_file.close()
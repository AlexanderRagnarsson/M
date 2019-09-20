filename = input('Enter filename: ')

read_file = open(filename)
write_file = open("sentences.txt", 'w')

sentence = ''
for line in read_file:
    
    #If there is a newline a new sentance starts so we print out the sentence
    if line == '\n':
        if sentence != '':     #we only want to print if we have words
            print(sentence.strip())
            print(sentence.strip(), file=write_file)
            sentence = ''
        continue    #get next word and skip rest of for
    stripped = line.strip()
    if stripped == '.':
        sentence += stripped #no space before a dot 
    elif stripped == ',':
        sentence += stripped #no space before a comma
    else:
        sentence += ' ' + stripped 
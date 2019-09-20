read_file = open("test.txt")

for line in read_file:
    for word in line:
        print(word.strip(), end=(''))

read_file.close()   
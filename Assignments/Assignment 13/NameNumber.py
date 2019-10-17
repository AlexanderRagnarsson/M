dict = {}
more = 'y'  #so we enter the while loop
while more == 'y':
    name = input('Name: ')
    number = input('Number: ')
    dict[name] = number
    more = input('More data (y/n)? ')

dict_list = list(dict.items())

print(sorted(dict_list))

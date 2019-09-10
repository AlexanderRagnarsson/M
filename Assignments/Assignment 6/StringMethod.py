name = input("Input a name: ")
#The last name includes ','
last_name, first_name = name.split()

#We do not want to print the ',' in the last_name so we skip the last character
print(first_name[0].capitalize() + '. ' + last_name[:-1].capitalize())
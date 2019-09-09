population = 307357870

years = input('Years: ')
while years.isdigit() == False:      #years.isdigit() er True ef years er 0 eða jákvæð heiltala
    print('Invalid input!')
    years = input('Years: ')
years_int = int(years)

seconds = years_int * 365 * 24 * 60 * 60

population_new = population + seconds//7 - seconds//13 + seconds//35

print('New population after', years,'years is', population_new)

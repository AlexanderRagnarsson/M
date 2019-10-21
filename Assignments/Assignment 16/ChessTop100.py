RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3

def open_file(file_name):
    try:
        return open(file_name)
    except FileNotFoundError:
        return False

def create_players_dict(filestream):
    """ Accepts a filestream with player data in every line
        Returns a dictionary with name as key and other data as value """
    player_dict = {}
    for line in filestream:
        rank, name, country, rating, byear = line.split('; ')   #Depilhögg
        lastname, firstname = name.split(', ')

        key = '{} {}'.format(firstname, lastname)               #Set key as the name
        value = ( int(rank), country, int(rating), int(byear) )

        player_dict[key] = value
    
    return player_dict

def create_item_dict(players_dict, index):
    """ Accepts a filestream with player data in every line
        Returns a dictionary with birth year as key and other data as value """
    item_dict = {}
    for chess_player, chess_player_data in players_dict.items():
        item = chess_player_data[index]
        if item in item_dict:
            name_list = item_dict[item]
            name_list.append(chess_player)
        else:
            item_dict[item] = [chess_player]
    
    return item_dict

def print_sorted(item_dict, players_dict):
    """ Prints with correct formatting """
    sorted_dict_list = sorted(item_dict.items())
    for key, players in sorted_dict_list:
        average_rating = get_average_rating(players, players_dict)
        print('{} ({}) ({:.1f}):'.format(key, len(players), average_rating))
        for player in players:
            rating = players_dict[player][RATING]
            print('{:>40} {:>9d}'.format(player,rating))

def get_average_rating(players, players_dict):
    total = 0
    for player in players:
        total += players_dict[player][RATING]
    return total/len(players)

def print_header(header):
    print(header)
    print('-'*len(header))

#--------------------------------------------------------------------------------------
def main():
    file_name = input('Enter filename: ')
    filestream = open_file(file_name)
    if not filestream:
        print('File not found')
        return      #File was not opened so we dont run the rest of the program
    
    player_dict = create_players_dict(filestream)
    country_dict = create_item_dict(player_dict, COUNTRY)
    byear_dict = create_item_dict(player_dict, BYEAR)

    header = 'Players by country:'
    print_header(header)
    print_sorted(country_dict, player_dict)

    print()

    header = 'Players by birth year:'
    print_header(header)
    print_sorted(byear_dict, player_dict)
    
main()
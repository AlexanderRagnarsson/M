def common_letters_list(name_list):
    """Accepts name list (first, last) and returns a list of common letters in first and last name"""
    common_list = []
    for char in name_list[0]:
        if char in name_list[1] and char not in common_list:
            common_list.append(char)
    return common_list


def common_letters_sets(name_list):
    """Accepts name list (first, last) and returns a set of common letters in first and last name """ 
    first_set = set(name_list[0])
    last_set = set(name_list[1])
    return first_set & last_set

def print_sorted_lists(common_list, common_set):
    """ Accepts a list and a set and prints the sorted list and set """
    print(sorted(common_list))
    print(sorted(common_set))

def main():
    name_list = input('Enter name: ').lower().split()
    common_list = common_letters_list(name_list)
    common_set = common_letters_sets(name_list)
    print_sorted_lists(common_list, common_set)

main()
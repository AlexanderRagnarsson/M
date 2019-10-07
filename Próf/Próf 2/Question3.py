def prompt():
    return input('Enter elements of a list separated by space: ')

def list_from_string(str_list):
    return str_list.split()

def type_converter(num_list):
    """
    Takes a list of integers as type strings and returns list of same intgers as int type
    """
    return [int(i) for i in num_list]
    

def set_from_list(num_list):
    """
    Takes a list of ints and returns a corresponmding set
    """
    num_list.sort()
    set_list = []
    for i in num_list:
        if i not in set_list:
            set_list.append(i)
    return set_list

def intersection(set_1, set_2):
    """
    Takes two sets (lists) and returns an intersection of the sets (list)
    """
    return [i for i in set_1 if i in set_2]


def union(set_1, set_2):
    """
    Takes two sets (lists) and returns a union of the sets (list)
    """
    union_list = [i for i in set_1]+[i for i in set_2]
    return set_from_list(union_list)


list1_str_list = list_from_string(prompt())
list2_str_list = list_from_string(prompt())

list1 = type_converter(list1_str_list)
list2 = type_converter(list2_str_list)

set1 = set_from_list(list1)
set2 = set_from_list(list2)

print('Set 1:', set1)
print('Set 2:', set2)
print('Intersection:', intersection(set1, set2))
print('Union:', union(set1, set2))
def merge_lists(list1, list2):
    """Accepts two lists of strings and returns a sorted merged list containing no duplicates"""
    merge_list = list1 + list2
    unique_list = []
    for word in merge_list:
        if word not in unique_list:
            unique_list.append(word)
    return sorted(unique_list) 

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))

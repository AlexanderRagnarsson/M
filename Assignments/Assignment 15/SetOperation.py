def set_input():
    """Prompts user to enter numbers separated by commas and returns a sorted se tof those numbers"""
    list1 = input('Input a list of integers separated with a comma: ').split(',')
    return {int(num) for num in sorted(list1)}
    

def operator(set1, set2, choice):
    """Accepts two sets and a choice, performs an operation on sets based on choice 
        and returns resulting set"""
    if choice == '1':
        return set1 & set2
    elif choice == '2':
        return set1 | set2
    else:   #choice == '3'
        return set1 - set2
    
def operation_prompt():
    """Prints input possibilites and returns user choice"""
    print('1. Intersection\n2. Union\n3. Difference\n4. Quit')
    return input('Set operation: ')

def main():
    set1 = set_input()
    set2 = set_input()
    print(set1)
    print(set2)
    while True:
        choice = operation_prompt()
        if choice == '4':
            break
        print(operator(set1, set2, choice))

main()
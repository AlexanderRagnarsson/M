# palindrome function definition goes here
def palindrome(sentance):
    """Checks if a sentance is a Palindrome"""
    sentance_lowered = sentance.lower()
    sentance_compare = ''

    #Makes a string without all spaces and punctuation that is all lower case
    for char in sentance_lowered:
        if char.islower():
            sentance_compare += char
    #Checks if the string is the same as when it is reversed
    if sentance_compare == sentance_compare[::-1]:
        return True

in_str = input("Enter a string: ")

#Call the function and print out the appropriate message
if palindrome(in_str): #
    print('"' + in_str + '"' + ' is a palindrome.')
else:
    print('"' + in_str + '"' + ' is not a palindrome.')
def get_emails():
    """
    Asks user for emails, one at a time, until he enters 'q'
    Returns list of emails
    """
    email_list = []
    input_q = False
    while not input_q:
        email = input('Email address: ')
        if email == 'q':
            input_q = True
        else:
            email_list.append(email)
    return email_list

def get_names_and_domains(emails):
    """
    Takes a list of emails and returns list of tuple 
    where tuples are names and domains of emails
    """
    return_list = []
    for email in emails:
        #strips whitespace in email, split into lists at the @, turns list into tuple and appends the tuple to the return_list
        return_list.append(tuple(email.strip().split('@')))
    return return_list

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)
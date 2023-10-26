
def add(contacts):
    print ("Input Name and phone number, separated with a space:")
    input_str = input ()
    input_list = input_str.split()
    if len (input_list) == 2:
        contacts[input_list[0]] = input_list[1]
        message = "added successfully"
    else:
        message = "The name and phone number should be separated with a space"
    return contacts, message 
        
def change(contacts):
    print ("Input Name and phone number, separated with a space:")
    input_str = input ()
    input_list = input_str.split()
    if len (input_list) == 2:
        contacts[input_list[0]] = input_list[1]
        message = "changed successfully" 
    else:
        message = "The name and phone number should be separated with a space"
    return contacts, message 

def phone(contacts):
    print ("Input Name:")
    input_str = input ()
    if contacts.get (input_str):
        message = f"Phone: {contacts[input_str]}"
    else:
        message = "Can't find such a contact"
    return contacts, message


def main():
    contacts = {}
    while True:
        VCBLRY = {
            "Hello":"How can I help you?",
            "good bye":"Good bye!",
            "close":"Good bye!",
            "exit":"Good bye!" }
        ACTION = ["add", "change", "phone", "show all"]
        input_str = input ()
        input_str = input_str.lower()
        if input_str == ".":
            break
        if VCBLRY.get(input_str):
            print (VCBLRY[input_str])
            break
        try:
            index = ACTION.index(input_str)
        except ValueError:
            index = 10
            print ("I don't understand this command")
        if index == 0: 
            contacts, message = add(contacts)
            print (message)
        if index == 1: 
            contacts, message = change(contacts)
            print (message)
        if index == 2: 
            contacts, message = phone()
            print (message)
        if index == 3: 
            print (contacts)
main()
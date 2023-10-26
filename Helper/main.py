
def add():
    print ("Input Name and phone number, separated with a space:")
    input_str = input ()
    input_list = input_str.split()
    if len (input_list) == 2:
        contacts[input_list[0]] = input_list[1]
        return "added successfully"
    else:
        return "The name and phone number should be separated with a space"
        
def change():
    print ("Input Name and phone number, separated with a space:")
    input_str = input ()
    input_list = input_str.split()
    if len (input_list) == 2:
        contacts[input_list[0]] = input_list[1]
        return "changed successfully"
    else:
        return "The name and phone number should be separated with a space"

def phone():
    print ("Input Name:")
    input_str = input ()
    if contacts.get (input_str):
        return f"Phone: {contacts[input_str]}"
    else:
        return "Can't find such a contact"

contacts = {}
def main():
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
            print (add())
        if index == 1: 
            print (change())
        if index == 2: 
            print (phone())
        if index == 3: 
            print (contacts)
main()
def add(contacts, input_str):
    input_list = input_str.split()
    if len (input_list) == 2:
        contacts[input_list[0]] = input_list[1]
        message = "added successfully"
    else:
        raise KeyError
    return contacts, message

def change(contacts, input_str):
    input_list = input_str.split()
    if len (input_list) == 2:
        contacts[input_list[0]] = input_list[1]
        message = "changed successfully" 
    else:
        raise KeyError
    return contacts, message 

def phone(contacts, input_str):
    if contacts.get (input_str):
        message = f"Phone: {contacts[input_str]}"
    else:
        raise IndexError
    return contacts, message


def input_error(main_func):

    def inner():
        try:
            main_func ()
        except ValueError:
            print ("I don't understand this command")
            input_error (main())
        except KeyError:
            print ("The name and phone number should be separated with a space")
            input_error (main())
        except IndexError:
            print ("Can't find such a contact")
            input_error (main())

    return inner

@input_error
def main():
    contacts = {}
    message =""
    while True:
        VCBLRY = {
            "hello":"How can I help you?",
            "good bye":"Good bye!",
            "close":"Good bye!",
            "exit":"Good bye!" }
        ACTION = ["add", "change", "phone", "show all"]
        input_str = input ()
        input_str = input_str.lower()
        if input_str == ".":
            break
        if input_str == "hello":
            print (VCBLRY[input_str])
            continue
        elif VCBLRY.get(input_str):
            print (VCBLRY[input_str])
            break
        index = ACTION.index(input_str)
        if index == 0:
            message ="Input Name and phone number, separated with a space:"
            print (message)
            input_str = input ()
            contacts, message = add(contacts, input_str)
            print (message)
        if index == 1:
            message ="Input Name and phone number, separated with a space:"
            print (message)
            input_str = input ()
            contacts, message = change(contacts, input_str)
            print (message)
        if index == 2: 
            message ="Input Name:"
            print (message)
            input_str = input ()
            contacts, message = phone()
            print (message)
        if index == 3: 
            print (contacts)



input_error (main())
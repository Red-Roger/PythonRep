def input_error(func):

    def inner(contacts, input_str):
        try:
            contacts, message = func (contacts, input_str)
        except ValueError:
            message = "Telephone number is not correct"
        except KeyError:
            message = "The name and phone number should be separated with a space"
        except IndexError:
            message = "Can't find such a contact"
        return contacts, message
    return inner


@input_error
def add(contacts, input_str):
    input_list = input_str.split()
    if len (input_list) == 2:
        name = input_list[0]
        phone_number = input_list[1]
        if phone_number[0] == "+":
            phone_number = phone_number[1:]
        if phone_number.isdigit() == False:
            raise ValueError
        else:
            contacts[name] = phone_number
            message = "added successfully"
    else:
        raise KeyError
    return contacts, message


@input_error 
def change(contacts, input_str):
    input_list = input_str.split()
    if len (input_list) == 2:
        name = input_list[0]
        phone_number = input_list[1]
        if phone_number[0] == "+":
            phone_number = phone_number[1:]
        if phone_number.isdigit() == False:
            raise ValueError
        else:
            contacts[name] = phone_number
            message = "changed successfully" 
    else:
        raise KeyError
    return contacts, message 


@input_error 
def phone(contacts, input_str):
    if contacts.get (input_str):
        message = f"Phone: {contacts[input_str]}"
    else:
        raise IndexError
    return contacts, message


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
        allowed_action = "("
        for i in range (len(ACTION)):
            allowed_action = allowed_action + ACTION[i] +", "
        allowed_action = allowed_action [:-2]
        allowed_action += ")"
        input_str = input (f"use command {allowed_action}: ")
        input_str = input_str.lower()


        if input_str == ".":
            break
        if input_str == "hello":
            print (VCBLRY[input_str])
            continue
        elif VCBLRY.get(input_str):
            print (VCBLRY[input_str])
            break
        if input_str in ACTION:
            index = ACTION.index(input_str)
        else:
            index = 100
            print ("I don't understand this command")
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
            contacts, message = phone(contacts, input_str)
            print (message)
        if index == 3:
            if contacts:
                print (contacts)
            else:
                print ("No contacts saved yet")

if __name__ == "__main__":
    main()
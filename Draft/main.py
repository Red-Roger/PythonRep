class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for value in self.contacts:
            if value["id"] == id:
                return value
        return None

    def remove_contacts(self, id):
        for value in self.contacts:
            if value["id"] == id:
                index = self.contacts.index(value)
                self.contacts.pop(index)

con = Contacts()
con.add_contacts("Tolia","+380505056980","email",True)
print (con.get_contact_by_id (1))


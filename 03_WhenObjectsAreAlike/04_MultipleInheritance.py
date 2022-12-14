class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class MailSender:
    def send_mail(self, massage):
        print('Sending Mail to ' + self.email)
        # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
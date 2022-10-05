class ContacatList(list):
    def search(self, name):
        '''Return all contact that contain the search value in their name'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContacatList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
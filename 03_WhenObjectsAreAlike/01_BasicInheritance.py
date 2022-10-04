class Contact:
    all_contact = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
            "{} order to {}".format(order, self.name))
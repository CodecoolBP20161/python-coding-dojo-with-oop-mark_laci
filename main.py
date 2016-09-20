
class ContactList(list):
    @classmethod
    def search(cls, name):
        

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


class Supplier(Contact):
    all_orders = {}

    def order(self, order):
        if self.email not in Supplier.all_orders.keys():
            Supplier.all_orders[self.email] = [order]
        else:
            Supplier.all_orders[self.email].append(order)

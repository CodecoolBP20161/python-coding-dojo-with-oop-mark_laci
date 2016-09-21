
class ContactList(list):

    def search(self, name):
        return_list = []
        for contact in self:
            if name in contact.name:
                return_list.append(contact)
        return return_list

    def longest_name(self):
        if len(self) > 0:
            longest = Contact("", "")
            for contact in self:
                if len(contact.name) > len(longest.name):
                    longest = contact
            return longest.name
        else:
            return None


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = ContactList()


class Supplier(Contact):
    all_orders = {}

    def order(self, order):
        if self.email not in Supplier.all_orders.keys():
            Supplier.all_orders[self.email] = [order]
        else:
            Supplier.all_orders[self.email].append(order)

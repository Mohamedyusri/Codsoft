class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts[name] = new_contact
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}\n")

    def search_contact(self, name=None, phone_number=None):
        if name:
            if name in self.contacts:
                contact = self.contacts[name]
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
            else:
                print("Contact not found.")
        elif phone_number:
            for contact in self.contacts.values():
                if contact.phone_number == phone_number:
                    print(f"Name: {contact.name}")
                    print(f"Phone Number: {contact.phone_number}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    return
            print("Contact not found.")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name].phone_number = phone_number
            if email:
                self.contacts[name].email = email
            if address:
                self.contacts[name].address = address
            print(f"Contact {name} updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            print("Search by:")
            print("1. Name")
            print("2. Phone Number")
            search_choice = input("Enter your choice: ")
            if search_choice == "1":
                name = input("Enter name: ")
                contact_book.search_contact(name=name)
            elif search_choice == "2":
                phone_number = input("Enter phone number: ")
                contact_book.search_contact(phone_number=phone_number)
        elif choice == "4":
            name = input("Enter name: ")
            phone_number = input("Enter new phone number (optional): ")
            email = input("Enter new email (optional): ")
            address = input("Enter new address (optional): ")
            contact_book.update_contact(name, phone_number or None, email or None, address or None)
        elif choice == "5":
            name = input("Enter name: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()



class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))

    def view_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}: {contact.phone}")

    def search_contact(self):
        name = input("Enter name or phone number: ")
        for contact in self.contacts:
            if name in contact.name or name in contact.phone:
                print(f"{contact.name}: {contact.phone}")

    def update_contact(self):
        name = input("Enter name: ")
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")

    def delete_contact(self):
        name = input("Enter name: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)

def main():
    contact_manager = ContactManager()
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



    
           
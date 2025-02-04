contacts = {}

def add_contact():
    print()
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email : ")
    address = input("Enter address : ")
    
    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print(f"Contact {name} added successfully!\n")

def view_contacts():
    print()
    if not contacts:
        print("No contacts available.\n")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
        print()

def search_contact():
    print()
    name = input("Enter name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}\n")
    else:
        print("Contact not found!\n")

def delete_contact():
    print()
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!\n")
    else:
        print("Contact not found!\n")

while True:
    print("\n Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Enter a valid choice! \n")

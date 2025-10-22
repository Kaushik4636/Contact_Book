def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Please select an option (1-5): ")
    return choice

def add_contact(contact_book):
    name = input("Enter the contact's name: ")
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contact_book[name] = {'Phone': phone, 'Email': email}
    print(f"Contact for {name} added successfully!")

def view_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    for name, details in contact_book.items():
        print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

def update_contact(contact_book):
    name = input("Enter the name of the contact you want to update: ")
    if name not in contact_book:
        print("Contact not found!")
        return
    phone = input(f"Enter new phone number for {name}: ")
    email = input(f"Enter new email address for {name}: ")
    contact_book[name] = {'Phone': phone, 'Email': email}
    print(f"Contact for {name} updated successfully!")

def delete_contact(contact_book):
    name = input("Enter the name of the contact you want to delete: ")
    if name not in contact_book:
        print("Contact not found!")
        return
    del contact_book[name]
    print(f"Contact for {name} deleted successfully!")

def main():
    contact_book = {}
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            update_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

contacts = {}
def add_contact():
    name = input("\nEnter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("\nContact added successfully!")
def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return
    print("\n===== CONTACT LIST =====")
    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("Address:", details["address"])
def search_contact():
    search = input("\nEnter name or phone number to search: ").lower()
    found = False
    for name, details in contacts.items():
        if search in name.lower() or search in details["phone"]:
            print("\nContact Found!")
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])
            found = True
    if not found:
        print("\nContact not found.")
def update_contact():
    name = input("\nEnter the name of the contact to update: ")
    if name in contacts:
        print("\nEnter new details:")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("\nContact updated successfully!")
    else:
        print("\nContact not found.")
def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("\nContact deleted successfully!")
    else:
        print("\nContact not found.")
while True:
    print("\n==============================")
    print("       CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break
    else:
        print("\nInvalid choice. Please try again.")

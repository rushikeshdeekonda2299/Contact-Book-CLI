
import csv
import os

CONTACTS_FILE = "contacts.csv"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ["Name", "Phone", "Email", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}")

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if keyword in c["Name"].lower() or keyword in c["Phone"]]
    if found:
        for c in found:
            print(f"{c['Name']} - {c['Phone']} - {c['Email']} - {c['Address']}")
    else:
        print("No matching contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contact["Phone"] = input("Enter new Phone: ")
            contact["Email"] = input("Enter new Email: ")
            contact["Address"] = input("Enter new Address: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    contacts = [c for c in contacts if c["Name"].lower() != name.lower()]
    save_contacts(contacts)
    print("Contact deleted successfully (if it existed).")

def main():
    while True:
        print("\n==== Contact Book ====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

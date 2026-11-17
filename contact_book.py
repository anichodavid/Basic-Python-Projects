import json

def load_contact():
    contacts = {
    "David": {"Phone": "09177777777", "E-mail": "david@gmail.com \n"}
}
    try:
        with open("contact.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        pass
    return contacts

def save_contact(contacts):
    with open ("contact.json", "w") as f:
        json.dump(contacts, f, indent=2)


    

def show_menu():
    print ("\n" + "=" * 40)
    print("Welcome to Contact Book!")
    print ("=" * 40)
    print ("1. Add Contact")
    print ("2. View Contacts")
    print ("3. Search by name")
    print ("4. Edit Contact")
    print ("5. Delete Contact")
    print ("6. Exit")
    

def add_contacts(contacts):

    while True:
        name = input("Name: ").strip().lower()

        if not name.isalpha():
            print("Only letters allowed.")
            continue
    
        
        name_exists = False
        for key in contacts:
            if key.lower() == name:
                name_exists = True
                break
    
        if name_exists:
            print("Name already exists! Enter a different name.")
            continue

        break

    
    while True:
        phone = input("Phone Number: ").strip()
        if not phone.isdigit() or len(phone) != 11:
            print("Enter an 11-digit phone number.")
            continue

        phone_exists = False
        for details in contacts.values():
            if details["Phone"] == phone:
                phone_exists = True
                continue

        if phone_exists:
            print("Phone number already exists! Enter a different one.")
            continue
        break

    
    while True:
        email = input("E-mail: ").strip().lower()
        if "@" not in email or "." not in email:
            print("Enter a valid email (lowercase, with @ and .).")
            continue

        email_exists = False
        for details in contacts.values():
            if details["E-mail"] == email:
                email_exists = True
                continue

        if email_exists:
            print("Email already exists! Enter a different one.")
            continue
        break

    
    contacts[name] = {"Phone": phone, "E-mail": email}
    save_contact(contacts)
    print(f"✅ Contact '{name}' added.")



def view_contacts(contacts):
    if not contacts:
        print("Contact list is empty.")
        return

    print("\nYour contacts:")
    for i, (name, details) in enumerate(contacts.items(), 1):
        print(f"{i}. {name} — {details['Phone']} — {details['E-mail']} \n\n")



def search_contacts(contacts):
    search = input ("Enter the name to search: ").strip().lower()
    while not search.isalpha():
             name = input("Enter a valid name: ")
    if search not in contacts:
        print("Name not found in contacts!")
    else: 
        print(contacts[search])



def edit_contacts(contacts):
    old_name = input("Enter the contact name to edit: ").strip().lower()
    while not old_name.isalpha():
       old_name = input("Enter a valid name to edit: ").strip().lower()

    actual_key = None
    for key in contacts:
        if key.lower() == old_name:
          actual_key = key
          break

    if actual_key is None:
        print ("Name not found in contacts!")
        return

    print (contacts[actual_key])
    print ("\n" + "="*40 )

    update = input("\n1. Name \n 2. Phone Number \n 3. E-mail \n\n Select the option of what you want to edit: ")

    if update == "1":
        new_name = input ("Enter new name: ").strip().lower()
        while not new_name.isalpha():
               new_name = input("Enter a valid new name to edit: ").strip().lower()
        if new_name in contacts:
            print ("Name already exists!")
            return
        contacts[new_name] = contacts.pop(actual_key)
        save_contact(contacts)
        print (f"Renamed: '{actual_key}' to '{new_name}'.")

    elif update == "2":
        contacts[actual_key]["Phone"] = input("New Phone Number: ").strip()
        while not contacts[actual_key]["Phone"].isdigit() or len(contacts[actual_key]["Phone"]) != 11:
            contacts[actual_key]["Phone"] = input("Enter a valid new 11-digit phone number: ").strip()
        save_contact(contacts)
        print("Phone updated!")

    elif update == "3":
        contacts[actual_key]["E-mail"] = input ("New E-mail: ")
        while "@" not in contacts[actual_key]["E-mail"] or "." not in contacts[actual_key]["E-mail"]:
            contacts[actual_key]["E-mail"] = input("Enter a valid email (lowercase, with @ and .): ").strip()
        save_contact(contacts)
        print ("Email Updated")

    else:
        print ("Invalid option")


def delete_contacts(contacts):
    old_name = input("Enter the contact name to delete: ").strip().lower()
    while not old_name.isalpha():
        old_name = input("Enter a valid name to delete: ").strip().lower()
    
    actual_key = None
    for key in contacts:
        if key.lower() == old_name:
            actual_key = key
            break
    
    if actual_key is None:
        print ("Name not found in contacts!")
        return
    
    removed = contacts.pop(actual_key)
    save_contact(contacts)
    print (f"Contact '{actual_key}' Deleted!")

def main():
    contacts = load_contact()

    while True:

        show_menu()
        option = input("Enter an option: ")
        if option == "1":
            add_contacts(contacts)
        elif option == "2":
            view_contacts(contacts)
        elif option == "3":
            search_contacts(contacts)
        elif option == "4":
            edit_contacts(contacts)
        elif option == "5":
            delete_contacts(contacts)
        elif option == "6":
            print ("Exited the Contact book! Good bye!!!!")
            break
        else: 
            print ("Invalid Choice!!")

if __name__ == "__main__":
    main()
        



    














 
    

              


  
    
    








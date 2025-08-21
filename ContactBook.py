contact = {}
def add_contact():
    name=input("Enter the contact name::")
    phone=input("Enter the contact number (digits only)::")
    if not phone.isdigit():
        print(" Invalid phone number! Please enter only digits.")
        return
    contact[name]=phone
    print(f" Contact '{name}' added successfully!")

def search_contact():
        search_name=input("Enter the contact name::")
        if search_name in contact:
            # print(search_name,"s contact number is",contact[search_name])
            print(f"{search_name}'s contact number is {contact[search_name]}")
        else:
            print("Not found in the contact book")
  
def show_contacts():
        if not contact:
            print(" Empty contact book")
        else:
            print("Name\tContact Number")
            for key in contact:
                print(f"{key}\t{contact[key]}")
   
def delete_contact():
        del_contact=input("Enter the contact name to be deleted::")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact Y/N?")
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                print(f"Contact '{del_contact}' deleted successfully!")   
        else:
            print("Name is not found in contact book")
  
def contact_book():
    while True:
        print("Welcome to the contact book program")
        print("--------------------------------------")
        print("Choose an operation:")
        print("1=Add")
        print("2=Search")
        print("3=Display")
        print("4=Delete")
        print("5=Exit")
        print("--------------------------------------")
        choice=(input("Enter the operation::"))

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
             show_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book...")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    contact_book()
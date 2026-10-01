from .contacts import show_contacts, find_contact, count_contacts, add_contact, remove_contact, edit_contact

# This dictionary stores the contact data used by the whole application.
# The key is the contact name and the value is the phone number.
contact_dictionary = {"john": "336-555-123", "mary": "336-789-4585", "david": "336-555-9999", "johnson": "336-567-896"}

# The main loop keeps the program running until the user chooses to exit.
def main():
    while True:
        # Display the available actions to the user.
        print("CONTACT MANAGER")
        print("1. Show all contacts")
        print("2. Find a contact")
        print("3. Add a contact")
        print("4. Remove a contact")
        print("5. Count contacts")
        print("6. Edit a contact")
        print("7. Exit")

        # Read the user's menu selection.
        choice = input("\nChoose an option: ").strip()
        print("")

        match choice:
            # Show every contact currently in the contact dictionary.
            case "1":
                contacts = show_contacts(contact_dictionary)
                if not contacts:
                    print("No contacts found.")
                else:
                    for name, phone_number in contacts:
                        print(f"Contact Information: {name.title()} ({phone_number})")
                print("")

            # Find a contact by name and display its phone number if it exists.
            case "2":
                contact_name = input("Enter the contact name you want to find: ").strip()
                phone_number = find_contact(contact_dictionary, contact_name)

                if phone_number is not None:
                    print(f"The contact phone number for: {contact_name.title()} is {phone_number}")
                else:
                    print(f"The contact name: {contact_name} is not found")
                print("")

            # Add a new contact after confirming the user did not cancel.
            case "3":
                new_contact_name = input("Enter the new contact name (or type cancel): ").strip()
                if not new_contact_name or new_contact_name.lower() == "cancel":
                    print("Adding contact canceled.")
                    print("")
                    continue

                new_contact_phone = input("Enter the new contact phone number: ").strip()
                if add_contact(contact_dictionary, new_contact_name, new_contact_phone):
                    print(f"Contact {new_contact_name.title()} added successfully.")
                else:
                    print(f"Contact {new_contact_name.title()} already exists.")
                print("")

            # Remove a contact after confirming the user did not cancel.
            case "4":
                remove_contact_name = input("Enter the contact name you want to remove: ").strip()
                if not remove_contact_name or remove_contact_name.lower() == "cancel":
                    print("Removing contact canceled.")
                    print("")
                    continue

                if remove_contact(contact_dictionary, remove_contact_name):
                    print(f"Contact {remove_contact_name.title()} removed successfully.")
                else:
                    print(f"Contact {remove_contact_name.title()} not found. No contact removed.")
                print("")

            # Display the total number of contact entries currently in the dictionary.
            case "5":
                total_contacts = count_contacts(contact_dictionary)
                print(f"There are: {total_contacts} contacts")
                print("")

            # Edit an existing contact's phone number if the contact exists.
            case "6":
                contact_name = input("Enter the contact name you want to edit (or type cancel): ").strip()
                if not contact_name or contact_name.lower() == "cancel":
                    print("Editing contact canceled.")
                    print("")
                    continue

                new_contact_phone = input("Enter the new contact phone number: ").strip()
                if edit_contact(contact_dictionary, contact_name, new_contact_phone):
                    print(f"Contact {contact_name.title()} updated successfully.")
                else:
                    print(f"Contact {contact_name.title()} not found. No contact updated.")
                print("")

            # End the loop and close the application.
            case "7":
                break

            # If the user enters anything else, show a helpful error message.
            case _:
                print("Invalid option. Choose a number from 1 to 7.\n")

if __name__ == "__main__":
    main()
from contacts import show_contacts, find_contact, count_contacts, add_contact, remove_contact, edit_contact

contact_dictionary = {"john": "336-555-123", "mary": "336-789-4585", "david": "336-555-9999", "johnson": "336-567-896"}

while True:
	print("CONTACT MANAGER")
	print("1. Show all contacts")
	print("2. Find a contact")
	print("3. Add a contact")
	print("4. Remove a contact")
	print("5. Count contacts")
	print("6. Edit a contact")
	print("7. Exit")

	choice = input("\nChoose an option: ").strip()
	print("")

	match choice:
		case "1":
			print("")
			show_contacts(contact_dictionary)
		case "2":
			contact_name = input("Enter the contact name you want to find: ").strip()
			find_contact(contact_dictionary, contact_name)
		case "3":
			new_contact_name = input("Enter the new contact name (or type cancel): ").strip()
			if new_contact_name.lower() == "cancel" or new_contact_name == "":
				print("Adding contact canceled.")
				print("")
				continue

			new_contact_phone = input("Enter the new contact phone number: ").strip()
			add_contact(contact_dictionary, new_contact_name, new_contact_phone)
		case "4":
			remove_contact_name = input("Enter the contact name you want to remove: ").strip()
			if remove_contact_name.lower() == "cancel" or remove_contact_name == "":
				print("Removing contact canceled.")
				print("")
				continue
			remove_contact(contact_dictionary, remove_contact_name)
		case "5":
			count_contacts(contact_dictionary)
		case "6":
			contact_name = input("Enter the contact name you want to edit (or type cancel): ").strip()
			if contact_name.lower() == "cancel" or contact_name == "":
				print("Editing contact canceled.\n")
				continue

			new_contact_phone = input("Enter the new contact phone number: ").strip()
			edit_contact(contact_dictionary, contact_name, new_contact_phone)
		case "7":
			break
		case _:
			print("Invalid option. Choose a number from 1 to 7.\n")
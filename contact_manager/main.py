from contacts import show_contacts, find_contact, count_contactss, add_contact, remove_contact

contact_dictionary = {"john": "336-555-123", "Mary": "336-789-4585", "David": "336-555-9999", "Johnson": "336567-896"}

while True:
	print("CONTACT MANAGER")
	print("1. Show all contacts")
	print("2. Find a contact")
	print("3. Add a contact")
	print("4. Remove a contact")
	print("5. Count contacts")
	print("6. Exit")

	choice = input("\nChoose an option: ").strip()
	print("")

	match choice:
		case "1":
			print("")
			show_contacts(contact_dictionary)
			print("")
		case "2":
			contact_name = input("Enter the contact name you want to find: ").strip()
			find_contact(contact_dictionary, contact_name)
		case "3":
			new_contact_name = input("Enter the new contact name: ").strip()
			new_contact_phone = input("Enter the new contact phone number: ").strip()
			add_contact(contact_dictionary, new_contact_name, new_contact_phone)
		case "4":
			remove_contact_name = input("Enter the contact name you want to remove: ").strip()
			remove_contact(contact_dictionary, remove_contact_name)
		case "5":
			count_contactss(contact_dictionary)
		case "6":
			break
		case _:
			print("Invalid option. Choose a number from 1 to 6.\n")
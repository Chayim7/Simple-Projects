#It shows all the contcts we have
def show_contacts(contactsDict):
    
    for contacts in contactsDict:
        print("contact information: ", contacts)
    print("")
    

#find specific contacts
def find_contact(contactsDicts_finder, contact_name):
    if contact_name in contactsDicts_finder:
        print("The contact phone number for: ",contact_name,"is",contactsDicts_finder[contact_name])
        print("")
    else:
        print(f"The contact name: {contact_name} is not found")
        print("")


#counts how many contacts we have
def count_contactss(contactsDict):
    count_contacts = 0
    
    
    for contacts in contactsDict:
        count_contacts = count_contacts + 1
    print(f"There are: {count_contacts} contacts")
    print("")


#add new contact to the dictionary
def add_contact(contacts_dict, contact_name, contact_number):
    contacts_dict[contact_name] = contact_number #create a keyname <Name of the new contact> and assign it a value pair <phone number>
    print(f"Contact {contact_name} added successfully.")
    print("")


#remove contact from dictionary
def remove_contact(contacts_dict, contact_name):
    
    if contact_name in contacts_dict:
        del contacts_dict[contact_name] #delete the keyname <Name of the contact> and its value pair <phone number>
        print(f"Contact {contact_name} removed successfully.")
        print("")
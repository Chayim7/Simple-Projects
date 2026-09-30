#It shows all the contcts we have
def show_contacts(contactsDict):
    
    for contacts in contactsDict:
        print("contact information: ", contacts)
    print("")
    

#find specific contacts
def find_contact(contactsDicts_finder, contact_name):
    if contact_name in contactsDicts_finder:
        print("The contact phone number for:",contact_name,"is",contactsDicts_finder[contact_name])
    else:
        print(f"The contact name: {contact_name} is not found")
    
    
#counts how many contacts we have
def count_contactss(contactsDict):
    count_contacts = 0
    
    
    for contacts in contactsDict:
        count_contacts = count_contacts + 1
    print(f"There are: {count_contacts} contacts")
    print("")
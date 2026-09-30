from contacts import show_contacts, find_contact, count_contactss

#Dictionaries
show_contacts_dictionary = {"john": "555-123", "Mary": "336-789", "David": "555-9999", "Johnson": "567-896"}
find_contacts_dictionary = {"john": "336-555-1234", "Mary": "336-789-8916", "David": "336-555-9999", "Johnson": "336-567-8960"}
count_contacts_dictionary = {"john": "555-123", "Mary": "336-789", "David": "555-9999", "Johnson": "567-896"}

#finding specific contacts.
contact_name = "David"

#Calling Functions
show_contacts(show_contacts_dictionary)
find_contact(find_contacts_dictionary, contact_name)
count_contactss(count_contacts_dictionary)
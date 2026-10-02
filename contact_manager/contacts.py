# This helper makes every name consistent before we use it in the dictionary.
# Example: "  David " becomes "david" so name lookups are not case-sensitive.
def normalize_name(contact_name):
    return contact_name.strip().lower()


# Return the contact list in a predictable order so the menu can print it neatly.
# sorted(contacts_dict.items()) gives us a list like [("david", "336-555-9999"), ...].
def show_contacts(contacts_dict):
    return sorted(contacts_dict.items())


# Search for a contact by name.
# If the name exists, return its phone number; otherwise, return None.
def find_contact(contacts_dict, contact_name):
    normalized_name = normalize_name(contact_name)
    return contacts_dict.get(normalized_name)


# Count how many contacts are currently stored in the dictionary.
def count_contacts(contacts_dict):
    return len(contacts_dict)


# Add a new contact only if that name is not already in the dictionary.
# If the name does already exist, do not overwrite it.
def add_contact(contacts_dict, contact_name, contact_number):
    normalized_name = normalize_name(contact_name)

    # If the name already exists, do not replace the existing contact.
    if normalized_name in contacts_dict:
        return False

    # Store the contact using a lowercase, trimmed name as the key.
    contacts_dict[normalized_name] = contact_number.strip()
    return True


# Remove a contact only if the name exists in the dictionary.
# If the name does not exist, do not remove it.
def remove_contact(contacts_dict, contact_name):
    normalized_name = normalize_name(contact_name)

    # If the name does not exist, do not remove it.
    if normalized_name not in contacts_dict:
        return False

    # Delete the contact from the dictionary.
    del contacts_dict[normalized_name]
    return True


# Update a contact's phone number if the contact already exists.
# If the name is missing, do not create a new one or change anything.
def edit_contact(contacts_dict, contact_name, new_contact_number):
    normalized_name = normalize_name(contact_name)

    # If the contact is not found, do not update anything.
    if normalized_name not in contacts_dict:
        return False

    # Replace the phone number for the existing contact.
    contacts_dict[normalized_name] = new_contact_number.strip()
    return True
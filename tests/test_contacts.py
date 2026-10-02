from contact_manager.contacts import (
    show_contacts,
    find_contact,
    count_contacts,
    add_contact,
    remove_contact,
    edit_contact,
)


# Add a contact and verify that the dictionary was updated correctly.
def test_add_contact():
    contacts = {}

    result_alice = add_contact(contacts, "alice", "754-856-7898")
    result_bob = add_contact(contacts, "bob", "987-782-8964")

    assert result_alice is True
    assert result_bob is True
    assert contacts["alice"] == "754-856-7898"
    assert contacts["bob"] == "987-782-8964"


# If the same contact name is added twice, do not overwrite the original.
def test_add_duplicate_contact():
    contacts = {"alice": "754-856-7898"}

    result = add_contact(contacts, "alice", "111-111-1111")

    assert result is False
    assert contacts["alice"] == "754-856-7898"


# Names should be normalized before being stored or looked up.
def test_add_contact_normalizes_name():
    contacts = {}

    result = add_contact(contacts, "  Alice  ", "754-856-7898")

    assert result is True
    assert "alice" in contacts
    assert "  Alice  " not in contacts


# find_contact returns the phone number when the contact exists.
def test_find_contact():
    #Arrange
    contacts = {"alice": "754-856-7898"}

    #Act
    results = find_contact(contacts, "alice")

    
    #Assert
    assert results == "754-856-7898"
    assert find_contact(contacts, "bob") is None


# The name lookup should work even if the user enters different casing.
def test_find_contact_normalizes_name():
    contacts = {"alice": "754-856-7898"}

    assert find_contact(contacts, "  ALICE  ") == "754-856-7898"


# count_contacts should return the number of contacts, not print it.
def test_count_contacts():
    #Arrange
    contacts = {"bob": "987-782-8964", "alice": "754-856-7898"}

    #Act
    result = count_contacts(contacts)

    #Assert
    assert result == 2


# An empty dictionary should count as zero contacts.
def test_count_empty_contacts():
    contacts = {}

    assert count_contacts(contacts) == 0


# show_contacts should return a sorted list of key/value pairs.
def test_show_contacts():
    contacts = {"bob": "987-782-8964", "alice": "754-856-7898"}

    result = show_contacts(contacts)

    assert result == [
        ("alice", "754-856-7898"),
        ("bob", "987-782-8964"),
    ]


# An empty dictionary should return an empty list for display.
def test_show_empty_contacts():
    contacts = {}

    assert show_contacts(contacts) == []


# Editing an existing contact should update the phone number.
def test_edit_contact_updates_number():
    
    #Arrange
    contacts = {"alice": "754-856-7898", "bob": "987-782-8964"} #test- isolation

    #Act
    result = edit_contact(contacts, "alice", "123-456-7890")

    #Assert
    assert result is True
    assert contacts["alice"] == "123-456-7890"
    assert contacts["bob"] == "987-782-8964"


# Editing a missing contact should not change the dictionary.
def test_edit_missing_contact_leaves_contacts_unchanged():
    contacts = {"alice": "754-856-7898"}

    result = edit_contact(contacts, "bob", "123-456-7890")

    assert result is False
    assert contacts == {"alice": "754-856-7898"}


# Removing an existing contact should delete it from the dictionary.
def test_remove_contact():

    #Arrange
    contacts = {"bob": "987-782-8964", "alice": "754-856-7898"}

    #Act
    result = remove_contact(contacts, "alice")

    #Assert
    assert result is True
    assert "alice" not in contacts
    assert "bob" in contacts


# Removing a missing contact should leave the dictionary unchanged.
def test_remove_missing_contact_leaves_contacts_unchanged():
    contacts = {"alice": "754-856-7898"}

    result = remove_contact(contacts, "bob")

    assert result is False
    assert contacts == {"alice": "754-856-7898"}
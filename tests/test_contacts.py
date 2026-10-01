from contact_manager.contacts import show_contacts, find_contact, count_contacts, add_contact, remove_contact, edit_contact

#testing the add_contacts function to ensure it adds contacts correctly to the dictionary
def test_add_contact():
    contacts = {}

    #we add two test contacts to the dictionary
    add_contact(contacts, "alice", "754-856-7898")
    add_contact(contacts, "bob", "987-782-8964")

    #we verify that the contacts were added correctly to the dictionary
    assert contacts["alice"] == "754-856-7898"
    assert contacts["bob"] == "987-782-8964"


def test_find_contact():
    contacts = {}

    add_contact(contacts, "alice", "754-856-7898")

    #we verify that the find_contact function returns the correct phone number
    assert find_contact(contacts, "alice") == "754-856-7898"
    assert find_contact(contacts, "bob") is None  # Contact does not exist


def test_count_contacts(capsys):
    contacts = {}

    #we add two test contacts to the dictionary
    add_contact(contacts, "alice", "754-856-7898")
    add_contact(contacts, "bob", "987-782-8964")

    capsys.readouterr()
    count_contacts(contacts)
    assert capsys.readouterr().out == "There are: 2 contacts\n\n"


def test_show_contacts(capsys):
    contacts = {"alice": "754-856-7898", "bob": "987-782-8964"}

    show_contacts(contacts)

    output = capsys.readouterr().out
    assert "alice" in output
    assert "(754-856-7898)" in output
    assert "bob" in output
    assert "(987-782-8964)" in output


def test_edit_contact_updates_number():
     contact = {}

     add_contact(contact, "alice", "754-856-7898")

     #we verify that the edit_contact function updates the phone number correctly
     edit_contact(contact, "alice", "123-456-7890")
     assert contact["alice"] == "123-456-7890"

     #we verify that the edit_contact function does not affect other contacts
     add_contact(contact, "bob", "987-782-8964")
     assert contact["bob"] == "987-782-8964"
     assert contact["alice"] == "123-456-7890"  # Ensure alice's number was updated correctly


def test_edit_missing_contact_leaves_contacts_unchanged():
    contacts = {"alice": "754-856-7898"}

    edit_contact(contacts, "bob", "123-456-7890")

    assert contacts == {"alice": "754-856-7898"}


def test_remove_contact():
    contacts = {}

    add_contact(contacts, "alice", "754-856-7898")
    add_contact(contacts, "bob", "987-782-8964")

    #We verify that the remove_contact function removes the contact correctly
    remove_contact(contacts, "alice")

    #we verify that the contact was removed correctly
    assert "alice" not in contacts
    assert "bob" in contacts  # Ensure bob's contact was not removed


def test_remove_missing_contact_leaves_contacts_unchanged():
    contacts = {"alice": "754-856-7898"}

    remove_contact(contacts, "bob")

    assert contacts == {"alice": "754-856-7898"}
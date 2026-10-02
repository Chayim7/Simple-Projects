# Contact Manager Project

This project is a small Python contact manager built to teach the fundamentals of:
- dictionaries
- functions
- user input
- conditional logic
- return values
- separation between business logic and user interaction

## Project structure

- `contact_manager/contacts.py` contains the business logic.
- `contact_manager/main.py` contains the menu and user interaction.

## Contact logic functions

### `normalize_name(contact_name)`
Normalizes a name before using it as a dictionary key.
- removes leading/trailing spaces
- converts the name to lowercase

This makes lookups case-insensitive.
Example:
```python
" David " -> "david"
```

### `show_contacts(contacts_dict)`
Returns all contacts in a sorted order so they can be displayed neatly in the menu.

### `find_contact(contacts_dict, contact_name)`
Looks up a contact by name.
- returns the phone number if the contact exists
- returns `None` if the contact is not found

### `count_contacts(contacts_dict)`
Returns the total number of contacts currently stored in the dictionary.

### `add_contact(contacts_dict, contact_name, contact_number)`
Adds a new contact if the name does not already exist.
- returns `True` if the contact was added
- returns `False` if the contact already exists

### `remove_contact(contacts_dict, contact_name)`
Removes a contact if it exists.
- returns `True` if the contact was removed
- returns `False` if the contact was not found

### `edit_contact(contacts_dict, contact_name, new_contact_number)`
Updates an existing contact's phone number.
- returns `True` if the update was successful
- returns `False` if the contact was not found

## Menu behavior

`main.py` handles all user interaction:
- prints the menu
- reads the user's choice
- prompts for names and phone numbers
- displays messages to the user

The menu calls the functions from `contacts.py` and then reports success or failure to the user.

## Running and importing the program

The `main()` function contains the menu loop. The guard at the bottom of `main.py` calls it only when the file is run directly:

```python
if __name__ == "__main__":
	main()
```

Run the contact manager from the project root with:

```bash
python -m contact_manager.main
```

If another Python file imports `main.py` as a module, Python does not call `main()` automatically, so the menu loop does not start. The other file can choose to call `main()` explicitly when appropriate.

## How the pytest tests work

The tests are in `tests/test_contacts.py`. Pytest finds files named `test_*.py` and runs functions whose names begin with `test_`. Run the suite from the project root with:

```bash
python -m pytest -v
```

Each test is a small example of expected behavior. For instance, `test_edit_contact_updates_number()` checks what should happen when Alice's number is changed:

```python
contacts = {
	"alice": "754-856-7898",
	"bob": "987-782-8964",
}

result = edit_contact(contacts, "alice", "123-456-7890")

assert result is True
assert contacts["alice"] == "123-456-7890"
assert contacts["bob"] == "987-782-8964"
```

This test follows **Arrange, Act, Assert**:

1. **Arrange:** Create the starting dictionary with Alice and Bob. This gives the test a known starting state; it does not depend on data from the application or from another test.
2. **Act:** Call `edit_contact()` to change Alice's number. The returned success value is saved in `result`.
3. **Assert:** Check the expected result and dictionary contents.

Each assertion checks a different part of the behavior:

- `result is True` checks that the function reports a successful edit. By itself, this does not prove that the number changed.
- `contacts["alice"] == "123-456-7890"` checks that Alice's number actually changed to the expected value.
- `contacts["bob"] == "987-782-8964"` checks that editing Alice did not accidentally change Bob's number.

The whole test function is one test case, and it can contain multiple assertions. If an assertion fails, pytest reports the test as failed and shows which expectation did not match. Other tests check different cases, such as editing a missing contact, normalizing names, and adding duplicate contacts.

## Learning idea

This project is designed to teach how to separate:
- data logic (what the program should do)
- user interface (how the user interacts with the program)

That separation is a very important beginner programming concept.

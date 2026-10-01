import os
import sys

print("CWD =", os.getcwd()) # Print the current working directory
print("PYTHON =", sys.executable) # Print the path to the Python executable
print("CONTACT_MANAGER_EXISTS =", os.path.isdir("contact_manager")) # Check if the contact_manager directory exists

try: # Attempt to import the contact_manager module
    import contact_manager
    print("IMPORT_OK =", contact_manager)
except Exception as e:             # Print the type of exception and the error message if the import fails
    print("IMPORT_ERROR =", type(e).__name__, e)
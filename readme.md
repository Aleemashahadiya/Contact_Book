📒 Contact Book (Python)

This is a function-based command-line contact book built in Python.
It allows users to add, search, display, and delete contacts through a menu-driven system.
The program runs continuously until the user chooses to exit.

🖥 Technologies Used

Language: Python 3

IDE: Visual Studio Code (VS Code) / Any Python-supported editor

Libraries Used: None (only Python built-ins)

Input Method: input() function

Looping: while True with break for exit

Data Structure: Dictionary ({name: phone})

Functions: Modularized (add_contact(), search_contact(), show_contacts(), delete_contact())

✨ Features

➕ Add Contact – Store a new contact with digit-only phone numbers

🔍 Search Contact – Look up a contact by name

📑 Display Contacts – View all saved contacts in tabular format

❌ Delete Contact – Remove an existing contact (with delete confirmation)

🚪 Exit – Quit the program gracefully

⚠️ Error Handling –

Rejects non-digit phone numbers

Handles invalid menu choices

Handles empty contact book

🛠 What I Did

Created separate functions for each operation (add, search, display, delete).

Used dictionary to manage contacts (name: number).

Validated phone number input to ensure digits only.

Added confirmation prompt before deleting contacts.

Structured program with an entry point (if __name__ == "__main__":).

Tested the program in VS Code.

🚀 How to Run

Save the file as contact_book.py.

Open a terminal in VS Code or Command Prompt in the file’s folder.

Run:

python ContactBook.py
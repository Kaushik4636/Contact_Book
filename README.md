# Contact Book (In-Memory) in Python

Welcome to the **Contact Book** project! This is a simple Python application that lets you manage contacts right from your terminal. You can add, view, update, or delete contacts—all in memory (no database required). Whether you're learning Python or just want a handy tool to store your contacts, this little project has you covered.

## Features:

* **Add a new contact** with their name, phone number, and email address.
* **View all your contacts** in a clear, organized list.
* **Update contact information**, such as phone number or email address.
* **Delete contacts** you no longer need.
* A simple, text-based **menu interface** that’s easy to use.

## Why This Project?

This project is a great way to practice Python concepts like:

* **Dictionaries**: Storing contact details.
* **Functions**: To handle different actions like adding or viewing contacts.
* **Input validation**: To make sure users are entering valid information.
* **Loops and control flow**: For a dynamic user interface.

It's a solid project to add to your portfolio or just a fun tool to keep around!

## Installation

To run this project locally, follow these steps:

### Prerequisites:

* Python 3.x (any version should work)

### Steps:

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/contact-book.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd contact-book
   ```

3. **Run the contact book**:

   ```bash
   python contact_book.py
   ```

   You’ll see a simple text menu to interact with the contact book.

## How to Use:

When you run the program, you’ll be presented with a menu of options. Here’s a quick overview of how you can interact with the contact book:

1. **Add New Contact**: Enter a contact’s name, phone number, and email to add them to the contact book.
2. **View All Contacts**: See a list of all stored contacts.
3. **Update Contact**: Update a contact’s phone number or email if they change.
4. **Delete Contact**: Remove a contact if you no longer need their details.
5. **Exit**: Exit the application when you’re done.

### Example Interaction:

```
--- Contact Book ---
1. Add New Contact
2. View All Contacts
3. Update Contact
4. Delete Contact
5. Exit
Please select an option (1-5): 1
Enter the contact's name: John Doe
Enter the contact's phone number: 123-456-7890
Enter the contact's email address: johndoe@example.com
Contact for John Doe added successfully!

--- Contact Book ---
1. Add New Contact
2. View All Contacts
3. Update Contact
4. Delete Contact
5. Exit
Please select an option (1-5): 2
--- Contact List ---
Name: John Doe, Phone: 123-456-7890, Email: johndoe@example.com
```

## Code Overview:

The script is fairly simple, with the main functions being:

* **`show_menu()`**: Displays the main menu.
* **`add_contact()`**: Adds a new contact to the contact book.
* **`view_contacts()`**: Displays all stored contacts.
* **`update_contact()`**: Allows you to update contact details.
* **`delete_contact()`**: Deletes a contact from the book.

The data is stored in an **in-memory dictionary** so that when the program ends, the data is lost. It's designed to be simple and easy to extend if you ever want to add more features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, submit issues, or make pull requests. Contributions are always welcome! If you have suggestions for features or improvements, don’t hesitate to reach out.

## Contact:

If you have any questions, suggestions, or just want to say hello, feel free to reach out to me at:
**Email**: [madhavankaushik3@gmail.com](mailto:madhavankaushik3@gmail.com)
**GitHub**: [github.com/Kaushik4636](https://github.com/Kaushik4636)

Thanks for checking out the Contact Book project, and happy coding!

---

### Notes:

* Don’t forget to replace `your-username` with your actual GitHub username in the `git clone` URL and GitHub link.
* If you want to add any new features or tweak the code, you’re free to contribute! I’d love to see what you build.



import tkinter as tk
from tkinter import messagebox, simpledialog

# Global contact list (Dictionary to store contacts)
contacts = {}

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        self.root.config(bg="lightblue")
        
        # Title Label
        self.title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 20), bg="lightblue")
        self.title_label.pack(pady=20)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, width=20, height=2, bg="lightgreen", font=("Helvetica", 12))
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, width=20, height=2, bg="lightyellow", font=("Helvetica", 12))
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, width=20, height=2, bg="lightcoral", font=("Helvetica", 12))
        self.search_button.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, width=20, height=2, bg="lightblue", font=("Helvetica", 12))
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, width=20, height=2, bg="lightpink", font=("Helvetica", 12))
        self.delete_button.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:", parent=self.root)
        if name:
            phone = simpledialog.askstring("Input", f"Enter phone number for {name}:", parent=self.root)
            email = simpledialog.askstring("Input", f"Enter email for {name}:", parent=self.root)
            if name and phone and email:
                contacts[name] = (phone, email)
                messagebox.showinfo("Success", f"Contact {name} added successfully!")
            else:
                messagebox.showwarning("Input Error", "All fields must be filled!")
        
    def view_contacts(self):
        if contacts:
            contact_list = "\n".join([f"{name}: {info[0]}, {info[1]}" for name, info in contacts.items()])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts available.")
    
    def search_contact(self):
        name = simpledialog.askstring("Input", "Enter the name to search:", parent=self.root)
        if name:
            if name in contacts:
                phone, email = contacts[name]
                messagebox.showinfo("Contact Found", f"{name}: {phone}, {email}")
            else:
                messagebox.showwarning("Not Found", f"No contact found for {name}.")
    
    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:", parent=self.root)
        if name:
            if name in contacts:
                new_phone = simpledialog.askstring("Input", f"Enter new phone number for {name}:", parent=self.root)
                new_email = simpledialog.askstring("Input", f"Enter new email for {name}:", parent=self.root)
                if new_phone and new_email:
                    contacts[name] = (new_phone, new_email)
                    messagebox.showinfo("Success", f"Contact {name} updated successfully!")
                else:
                    messagebox.showwarning("Input Error", "Both phone and email must be provided.")
            else:
                messagebox.showwarning("Not Found", f"No contact found for {name}.")
    
    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:", parent=self.root)
        if name:
            if name in contacts:
                del contacts[name]
                messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
            else:
                messagebox.showwarning("Not Found", f"No contact found for {name}.")

# Main function to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

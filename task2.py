import tkinter as tk
from tkinter import ttk, messagebox

class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class ContactListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact List App")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('calibri', 12, 'bold'), foreground='blue')
        style.configure('TLabel', font=('calibri', 12))

        ttk.Label(self.master, text="Name:").grid(row=0, column=0, sticky="e")
        ttk.Label(self.master, text="Email:").grid(row=1, column=0, sticky="e")
        ttk.Label(self.master, text="Phone:").grid(row=2, column=0, sticky="e")
        ttk.Label(self.master, text="Address:").grid(row=3, column=0, sticky="e")

        self.name_entry = ttk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='we')
        self.email_entry = ttk.Entry(self.master)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5, sticky='we')
        self.phone_entry = ttk.Entry(self.master)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky='we')
        self.address_entry = ttk.Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky='we')

        ttk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10, sticky='we')
        ttk.Button(self.master, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10, sticky='we')

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        if name and email and phone and address:
            contact = Contact(name, email, phone, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_contacts(self):
        if self.contacts:
            view_window = tk.Toplevel(self.master)
            view_window.title("Contacts")

            style = ttk.Style()
            style.configure('Treeview', font=('calibri', 11))
            style.configure('Treeview.Heading', font=('calibri', 11, 'bold'))

            search_frame = ttk.Frame(view_window)
            search_frame.pack(pady=5)

            search_label = ttk.Label(search_frame, text="Search Contact:")
            search_label.grid(row=0, column=0, padx=5, pady=5)

            search_entry = ttk.Entry(search_frame)
            search_entry.grid(row=0, column=1, padx=5, pady=5)

            search_button = ttk.Button(search_frame, text="Search", command=lambda: self.search_contact(self.contacts_tree, search_entry.get()))
            search_button.grid(row=0, column=2, padx=5, pady=5)

            self.contacts_tree = ttk.Treeview(view_window, columns=('Name', 'Email', 'Phone', 'Address'), show='headings')
            self.contacts_tree.heading('Name', text='Name')
            self.contacts_tree.heading('Email', text='Email')
            self.contacts_tree.heading('Phone', text='Phone')
            self.contacts_tree.heading('Address', text='Address')

            for contact in self.contacts:
                self.contacts_tree.insert('', 'end', values=(contact.name, contact.email, contact.phone, contact.address))

            self.contacts_tree.pack(expand=True, fill='both')

            # Delete functionality
            def delete_contact():
                selected_item = self.contacts_tree.selection()
                if selected_item:
                    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
                    if confirmation:
                        for item in selected_item:
                            contact_index = int(self.contacts_tree.index(item))
                            del self.contacts[contact_index]
                            self.contacts_tree.delete(item)
                            messagebox.showinfo("Success", "Contact deleted successfully!")
                else:
                    messagebox.showinfo("Info", "Please select a contact to delete.")

            delete_button = ttk.Button(view_window, text="Delete Contact", command=delete_contact)
            delete_button.pack(pady=5)

            # Update functionality
            def update_contact():
                selected_item = self.contacts_tree.selection()
                if selected_item:
                    contact_index = int(self.contacts_tree.index(selected_item[0]))
                    selected_contact = self.contacts[contact_index]

                    # Create a new window for updating contact
                    update_window = tk.Toplevel(view_window)
                    update_window.title("Update Contact")

                    ttk.Label(update_window, text="Name:").grid(row=0, column=0, sticky="e")
                    ttk.Label(update_window, text="Email:").grid(row=1, column=0, sticky="e")
                    ttk.Label(update_window, text="Phone:").grid(row=2, column=0, sticky="e")
                    ttk.Label(update_window, text="Address:").grid(row=3, column=0, sticky="e")

                    name_var = tk.StringVar(update_window, value=selected_contact.name)
                    email_var = tk.StringVar(update_window, value=selected_contact.email)
                    phone_var = tk.StringVar(update_window, value=selected_contact.phone)
                    address_var = tk.StringVar(update_window, value=selected_contact.address)

                    name_entry = ttk.Entry(update_window, textvariable=name_var)
                    name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='we')
                    email_entry = ttk.Entry(update_window, textvariable=email_var)
                    email_entry.grid(row=1, column=1, padx=5, pady=5, sticky='we')
                    phone_entry = ttk.Entry(update_window, textvariable=phone_var)
                    phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky='we')
                    address_entry = ttk.Entry(update_window, textvariable=address_var)
                    address_entry.grid(row=3, column=1, padx=5, pady=5, sticky='we')

                    # Function to update contact
                    def update_contact_info():
                        new_name = name_var.get()
                        new_email = email_var.get()
                        new_phone = phone_var.get()
                        new_address = address_var.get()

                        # Update contact details
                        self.contacts[contact_index].name = new_name
                        self.contacts[contact_index].email = new_email
                        self.contacts[contact_index].phone = new_phone
                        self.contacts[contact_index].address = new_address

                                                # Update treeview
                        self.contacts_tree.item(selected_item, values=(new_name, new_email, new_phone, new_address))

                        messagebox.showinfo("Success", "Contact updated successfully!")
                        update_window.destroy()

                    ttk.Button(update_window, text="Update Contact", command=update_contact_info).grid(row=4, column=0, columnspan=2, pady=10, sticky='we')

                else:
                    messagebox.showinfo("Info", "Please select a contact to update.")

            # Add the "Update Contact" button to the view_contacts method
            update_button = ttk.Button(view_window, text="Update Contact", command=update_contact)
            update_button.pack(pady=5)

        else:
            messagebox.showinfo("Info", "No contacts to display.")

    def search_contact(self, contacts_tree, query):
        for item in contacts_tree.get_children():
            contacts_tree.delete(item)

        found_contacts = [contact for contact in self.contacts if (query.lower() in contact.name.lower()) or (query.lower() in contact.phone.lower())]
        
        if found_contacts:
            for contact in found_contacts:
                contacts_tree.insert('', 'end', values=(contact.name, contact.email, contact.phone, contact.address))
        else:
            messagebox.showinfo("Search Result", "No contacts found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

    def get_contacts(self):
        return self.contacts

    def search_contact(self, query):
        return [contact for contact in self.contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]

    def update_contact(self, index, name, phone, email, address):
        self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}

    def delete_contact(self, index):
        del self.contacts[index]


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact_book.add_contact(name, phone, email, address)
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

def display_contacts():
    contacts_list.delete(0, tk.END)
    for i, contact in enumerate(contact_book.get_contacts()):
        contacts_list.insert(tk.END, f"{i + 1}. {contact['name']} ({contact['phone']})")

def search_contact():
    query = search_entry.get()
    results = contact_book.search_contact(query)

    contacts_list.delete(0, tk.END)
    for i, contact in enumerate(results):
        contacts_list.insert(tk.END, f"{contact['name']} ({contact['phone']})")

    if not results:
        messagebox.showinfo("Search Results", "No contacts found matching your query.")

def update_contact():
    selected = contacts_list.curselection()
    if selected:
        index = selected[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone:
            contact_book.update_contact(index, name, phone, email, address)
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_entries()
            display_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")
    else:
        messagebox.showerror("Error", "No contact selected!")

def delete_contact():
    selected = contacts_list.curselection()
    if selected:
        index = selected[0]
        contact_book.delete_contact(index)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        display_contacts()
    else:
        messagebox.showerror("Error", "No contact selected!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Contact Book")
window.geometry("600x400")
window.configure(bg="#FF4500") 

contact_book = ContactBook()
button_style = {
    "bg": "#B22222", 
    "fg": "white",
    "font": ("Arial", 10, "bold"),
    "relief": "raised",
    "bd": 4,
    "activebackground": "#8B0000",  
    "activeforeground": "#FFFFFF",
    "width": 15
}
shadow_style = {
    "highlightbackground": "#333333",
    "highlightthickness": 2
}
label_style = {"bg": "#FF4500", "font": ("Arial", 10, "bold")}
entry_shadow_style = {
    "highlightbackground": "#555555",
    "highlightthickness": 2
}

tk.Label(window, text="Name:", **label_style).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(window, **entry_shadow_style)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Phone:", **label_style).grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(window, **entry_shadow_style)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Email:", **label_style).grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(window, **entry_shadow_style)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Address:", **label_style).grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(window, **entry_shadow_style)
address_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Search:", **label_style).grid(row=4, column=0, padx=10, pady=5)
search_entry = tk.Entry(window, **entry_shadow_style)
search_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Button(window, text="Add Contact", command=add_contact, **button_style, **shadow_style).grid(row=5, column=0, pady=10)
tk.Button(window, text="Update Contact", command=update_contact, **button_style, **shadow_style).grid(row=5, column=1, pady=10)
tk.Button(window, text="Delete Contact", command=delete_contact, **button_style, **shadow_style).grid(row=6, column=0, pady=10)
tk.Button(window, text="Search", command=search_contact, **button_style, **shadow_style).grid(row=6, column=1, pady=10)
tk.Button(window, text="Clear", command=clear_entries, **button_style, **shadow_style).grid(row=7, column=0, pady=10)

tk.Label(window, text="Contacts:", **label_style).grid(row=0, column=2, padx=10, pady=5)
contacts_list = tk.Listbox(window, width=40, height=15, font=("Arial", 10))
contacts_list.grid(row=1, column=2, rowspan=6, padx=10, pady=5)

window.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("300x200")

        self.length_var = tk.IntVar(value=12)
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Label for the prompt
        prompt_label = ttk.Label(main_frame, text="Enter the desired length of the password:", foreground="blue")
        prompt_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Entry for the password length
        length_label = ttk.Label(main_frame, text="Password Length:")
        length_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        length_entry = ttk.Entry(main_frame, textvariable=self.length_var)
        length_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to generate password
        generate_button = ttk.Button(main_frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Label to display generated password
        password_label = ttk.Label(main_frame, text="Generated Password:", foreground="black")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, state="readonly")
        password_entry.grid(row=3, column=1, padx=5, pady=5)

    def generate_password(self):
        length = self.length_var.get()
        if length <= 0:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

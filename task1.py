import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
from datetime import datetime

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.load_previous_tasks()

        # Background Image
        bg_image = Image.open("tt3.jpg")
        bg_image = bg_image.resize((800, 800), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(bg_image)
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Current Date and Time Label
        self.datetime_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="darkblue")
        self.datetime_label.place(relx=0.5, rely=0.02, anchor=tk.CENTER)
        self.update_datetime()

        # Create widgets with custom styles
        self.task_entry = tk.Entry(root, width=40, bg="light yellow", font=("Arial", 12))
        self.task_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.task_entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="light green", font=("Arial", 12))
        self.add_button.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

        self.task_listbox = tk.Listbox(root, width=50, height=15, bg="grey", font=("Arial", 12))
        self.task_listbox.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed, bg="light coral", font=("Arial", 12))
        self.complete_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="light coral", font=("Arial", 12))
        self.delete_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, bg="light coral", font=("Arial", 12))
        self.quit_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

        self.priority_var = tk.IntVar()
        self.priority_var.set(1)
        self.priority_radio1 = tk.Radiobutton(root, text="Priority 1", variable=self.priority_var, value=1, font=("Arial", 12))
        self.priority_radio1.place(relx=0.1, rely=0.1, anchor=tk.CENTER)
        self.priority_radio2 = tk.Radiobutton(root, text="Priority 2", variable=self.priority_var, value=2, font=("Arial", 12))
        self.priority_radio2.place(relx=0.1, rely=0.2, anchor=tk.CENTER)

        self.update_task_listbox()

    def update_datetime(self):
        now = datetime.now()
        formatted_datetime = now.strftime("%A, %d %B %Y %I:%M:%S %p")
        self.datetime_label.config(text=formatted_datetime)
        self.root.after(1000, self.update_datetime)

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            priority = self.priority_var.get()
            if priority not in [1, 2]:
                messagebox.showwarning("Warning", "Please set task priority as 1 or 2.")
                return
            self.tasks.append({"task": task, "completed": False, "priority": priority})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_completed(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            for index in selected_indices:
                self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            for index in sorted(selected_indices, reverse=True):
                del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            priority_str = "Priority 1" if task["priority"] == 1 else "Priority 2"
            task_text = f"{status} {task['task']} ({priority_str})"
            if task["completed"]:
                task_text = f"{task_text}"
            self.task_listbox.insert(tk.END, task_text)

    def load_previous_tasks(self):
        # Load previous tasks from a file/database
        # Example: self.tasks = load_tasks_from_file("tasks.txt")
        pass

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.geometry("1000x700")
    root.mainloop()

if __name__ == "__main__":
    main()


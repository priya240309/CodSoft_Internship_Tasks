import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, dashboard):
        self.root = dashboard
        self.root.title("To-Do List - Task Tracker")
        self.root.geometry("420x470")
        self.task_storage = []

        # header app
        self.title_banner = tk.Label(self.root, text="TO-DO LIST", font=("Verdana", 16, "bold"))
        self.title_banner.pack(pady=12)

        # entry field
        self.task_input = tk.Entry(self.root, font=("Helvetica", 12))
        self.task_input.pack(ipady=6, ipadx=4, padx=20)

        # area
        self.add_btn = tk.Button(self.root, text="+ Add Task", width=15, command=self.add_new_task)
        self.add_btn.pack(pady=6)

        self.remove_btn = tk.Button(self.root, text="Delete Task", width=15, command=self.remove_selected_task)
        self.remove_btn.pack(pady=6)

        self.show_btn = tk.Button(self.root, text=" View Tasks", width=15, command=self.display_all_tasks)
        self.show_btn.pack(pady=6)

        # List of Tasks
        self.task_box = tk.Listbox(self.root, width=42, height=12, bg= "#f8f8f8", font=("Consolas", 11))
        self.task_box.pack(pady=12)

    # Add a task
    def add_new_task(self):
        note = self.task_input.get().strip()
        if note == "":
            messagebox.showwarning("Input Missing", "Please enter a task.")
        else:
            self.task_storage.append(note)
            self.task_input.delete(0, tk.END)
            self.display_all_tasks()
            messagebox.showinfo("Success", "Task added to your list!")

    # Show all the  tasks
    def display_all_tasks(self):
        self.task_box.delete(0, tk.END)
        for num, t in enumerate(self.task_storage, start=1):
            self.task_box.insert(tk.END, f"{num}. {t}")

    # Delete a task
    def remove_selected_task(self):
        selected_task = self.task_box.curselection()
        if not selected_task:
            messagebox.showerror("No Selection", "Please select a task to delete.")
        else:
            task_id = selected_task[0]
            deleted_item = self.task_storage.pop(task_id)
            self.display_all_tasks()
            messagebox.showinfo("Removed", f"Deleted: {deleted_item}")

#  GUI App
if __name__ == "__main__":
    app_window = tk.Tk()
    todo_app = ToDoList(app_window)
    app_window.mainloop()

import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To‑Do List App")
        self.root.geometry("500x400")
        self.tasks = []

        # Entry + Add button
        self.task_entry = tk.Entry(root, width=40, font=('Arial', 14))
        self.task_entry.pack(pady=10)
        tk.Button(root, text="Add Task", command=self.add_task,
                  font=('Arial', 12), bg="#2ecc71", fg="#ecf0f1").pack(pady=5)

        # Tasks listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10,
                                       font=('Arial', 12), bg="#ecf0f1", fg="#2c3e50",
                                       selectbackground="#3498db")
        self.task_listbox.pack(pady=10)

        # Remove / Complete buttons
        frm = tk.Frame(root)
        frm.pack(pady=5)
        tk.Button(frm, text="Remove Task", command=self.remove_task,
                  font=('Arial', 12), bg="#e74c3c", fg="#ecf0f1").pack(side="left", padx=5)
        tk.Button(frm, text="Complete Task", command=self.complete_task,
                  font=('Arial', 12), bg="#f39c12", fg="#ecf0f1").pack(side="left", padx=5)

        # Double-click to complete
        self.task_listbox.bind('<Double-Button-1>', lambda e: self.complete_task())

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        sel = self.task_listbox.curselection()
        if sel:
            self.tasks.pop(sel[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to remove.")

    def complete_task(self):
        sel = self.task_listbox.curselection()
        if sel:
            task = self.tasks.pop(sel[0])
            self.tasks.append(f"[Done] {task}")
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to complete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for t in self.tasks:
            self.task_listbox.insert(tk.END, t)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

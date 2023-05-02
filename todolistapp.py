import tkinter as tk
import tkinter.ttk as ttk

# Function to add a task to the list
def add_task():
    task = new_task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        new_task_entry.delete(0, tk.END)

# Function to remove a selected task from the list
def remove_task():
    tasks_listbox.delete(tk.ANCHOR)

# Create the app window
window = tk.Tk()
window.title("To-Do List")

# Create the label and entry for adding a new task
new_task_label = ttk.Label(window, text="New Task:")
new_task_label.pack(padx=10, pady=10)
new_task_entry = ttk.Entry(window, font=("Helvetica", 14))
new_task_entry.pack(padx=10, pady=5)

# Create the button to add a task
add_task_button = ttk.Button(window, text="Add Task", command=add_task)
add_task_button.pack(padx=10, pady=5)

# Create the button to remove a task
remove_task_button = ttk.Button(window, text="Remove Selected Task", command=remove_task)
remove_task_button.pack(padx=10, pady=5)

# Create the listbox to display the tasks
tasks_listbox = tk.Listbox(window, font=("Helvetica", 14), highlightthickness=0, selectbackground="light blue", selectforeground="white")
tasks_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a scrollbar for the listbox
scrollbar = ttk.Scrollbar(tasks_listbox, orient=tk.VERTICAL, command=tasks_listbox.yview)
tasks_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the app
window.mainloop()

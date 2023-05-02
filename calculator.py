import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Colorful Calculator")

# create a variable to store the current value
value = tk.StringVar()

# create a function to update the value when a button is clicked
def update_value(btn_value):
    current_value = value.get()
    if current_value == "0":
        current_value = ""
    value.set(current_value + btn_value)

# create a function to clear the value
def clear_value():
    value.set("0")

# create a function to calculate the result
def calculate_result():
    try:
        result = eval(value.get())
        value.set(str(result))
    except:
        value.set("Error")

# create the display label
display_label = tk.Label(root, textvariable=value, font=("Arial", 24), anchor="e", bg="white", fg="black", width=20)
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# create the number buttons
for i in range(10):
    btn = tk.Button(root, text=str(i), font=("Arial", 16), bg="yellow", fg="black", width=4, height=2, command=lambda x=i: update_value(str(x)))
    btn.grid(row=1 + (i-1)//3, column=(i-1)%3, padx=5, pady=5)

# create the operation buttons
btn_add = tk.Button(root, text="+", font=("Arial", 16), bg="orange", fg="white", width=4, height=2, command=lambda: update_value("+"))
btn_add.grid(row=4, column=0, padx=5, pady=5)
btn_sub = tk.Button(root, text="-", font=("Arial", 16), bg="orange", fg="white", width=4, height=2, command=lambda: update_value("-"))
btn_sub.grid(row=4, column=1, padx=5, pady=5)
btn_mul = tk.Button(root, text="*", font=("Arial", 16), bg="orange", fg="white", width=4, height=2, command=lambda: update_value("*"))
btn_mul.grid(row=4, column=2, padx=5, pady=5)
btn_div = tk.Button(root, text="/", font=("Arial", 16), bg="orange", fg="white", width=4, height=2, command=lambda: update_value("/"))
btn_div.grid(row=4, column=3, padx=5, pady=5)

# create the utility buttons
btn_clear = tk.Button(root, text="C", font=("Arial", 16), bg="red", fg="white", width=4, height=2, command=clear_value)
btn_clear.grid(row=5, column=0, padx=5, pady=5)
btn_dot = tk.Button(root, text=".", font=("Arial", 16), bg="yellow", fg="black", width=4, height=2, command=lambda: update_value("."))
btn_dot.grid(row=5, column=1, padx=5, pady=5)
btn_equal = tk.Button(root, text="=", font=("Arial", 16), bg="green", fg="white", width=4, height=2, command=calculate_result)
btn_equal.grid(row=5, column=2, padx=5, pady=5)

# run the main loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 18), borderwidth=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    b = tk.Button(root, text=button, font=('Arial', 18), relief=tk.RAISED, borderwidth=2)
    b.grid(row=row, column=col, sticky="nsew")
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text="C", font=('Arial', 18), relief=tk.RAISED, borderwidth=2, command=clear)
clear_button.grid(row=row, column=col, sticky="nsew")

equal_button = tk.Button(root, text="=", font=('Arial', 18), relief=tk.RAISED, borderwidth=2, command=calculate)
equal_button.grid(row=row, column=col+1, sticky="nsew")

root.mainloop()

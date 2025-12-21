import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("268x250")

entry = tk.Entry(root, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

operator = ""

# ---------- functions ----------
def press_num(num):
    entry.insert(tk.END, num)

def press_operator(op):
    global operator
    operator = op
    entry.insert(tk.END, op)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()

        if operator == "+":
            n1, n2 = expression.split("+")
            result = float(n1) + float(n2)

        elif operator == "-":
            n1, n2 = expression.split("-")
            result = float(n1) - float(n2)

        elif operator == "*":
            n1, n2 = expression.split("*")
            result = float(n1) * float(n2)

        elif operator == "/":
            n1, n2 = expression.split("/")
            if float(n2) == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                clear()
                return
            result = float(n1) / float(n2)

        elif operator == "%":
            n1, n2 = expression.split("%")
            result = float(n1) % float(n2)

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# ---------- number buttons ----------
nums = [
    ("7",1,0), ("8",1,1), ("9",1,2),
    ("4",2,0), ("5",2,1), ("6",2,2),
    ("1",3,0), ("2",3,1), ("3",3,2),
    ("0",4,1)
]

for (text, r, c) in nums:
    tk.Button(root, text=text, width=5,
              command=lambda t=text: press_num(t)).grid(row=r, column=c, padx=5, pady=5)

# ---------- operator buttons ----------
tk.Button(root, text="+", width=5, bg="red",
          command=lambda: press_operator("+")).grid(row=1, column=3)

tk.Button(root, text="-", width=5, bg="red",
          command=lambda: press_operator("-")).grid(row=2, column=3)

tk.Button(root, text="*", width=5, bg="red",
          command=lambda: press_operator("*")).grid(row=3, column=3)

tk.Button(root, text="/", width=5, bg="red",
          command=lambda: press_operator("/")).grid(row=4, column=3)

tk.Button(root, text="%", width=5, bg="red",
          command=lambda: press_operator("%")).grid(row=4, column=0)

# ---------- equals & clear ----------
tk.Button(root, text="=", width=5, bg="blue",
          command=calculate).grid(row=4, column=2)

tk.Button(root, text="CLEAR", width=15, bg="orange",
          command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()

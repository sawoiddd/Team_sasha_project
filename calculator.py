import tkinter as tk

root = tk.Tk()

root.geometry("260x340")

root.resizable(False, False)

root.title("Calculator")

line = ""


def insert_symbol(symbol):
    if len(entry.get()) == 0:
        entry.insert(0, symbol)
    else:
        entry.insert(len(entry.get()) + 1, symbol)

    global line
    if symbol == "÷":
        line = line + "/"
    elif symbol == "×":
        line = line + "*"
    elif symbol == "ⁿ":
        line = line + "**"
    elif symbol == "%":
        line = line + "/100*"
    else:
        line = line + symbol


def insert_symbol_1():
    insert_symbol("1")


def insert_symbol_2():
    insert_symbol("2")


def insert_symbol_3():
    insert_symbol("3")


def insert_symbol_4():
    insert_symbol("4")


def insert_symbol_5():
    insert_symbol("5")


def insert_symbol_6():
    insert_symbol("6")


def insert_symbol_7():
    insert_symbol("7")


def insert_symbol_8():
    insert_symbol("8")


def insert_symbol_9():
    insert_symbol("9")


def insert_symbol_0():
    insert_symbol("0")


def insert_symbol_plus():
    insert_symbol("+")


def insert_symbol_minus():
    insert_symbol("-")


def insert_symbol_div():
    insert_symbol("÷")


def insert_symbol_mult():
    insert_symbol("×")


def insert_symbol_dot():
    insert_symbol(".")


def insert_symbol_degree():
    insert_symbol("ⁿ")


def insert_symbol_percent():
    insert_symbol("%")


def insert_result():
    global line
    if line == "":
        line = entry.get()
    delete_entry()

    entry.insert(0, eval(line))


def delete_entry_line():
    entry.delete(0, "end")
    global line
    line = ""


def delete_entry():
    entry.delete(0, "end")


def delete_line():
    global line
    line = ""


entry = tk.Entry(root, font=("Times New Romance", 20, "bold"), width=10)
entry.grid(column=0, row=0, sticky=tk.EW, columnspan=4)

#number buttons
button_1 = tk.Button(root, text="1", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_1)
button_1.grid(column=0, row=2, padx=5, pady=1, sticky=tk.W)

button_4 = tk.Button(root, text="4", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_4)
button_4.grid(column=0, row=3, padx=5, pady=1, sticky=tk.W)

button_7 = tk.Button(root, text="7", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_7)
button_7.grid(column=0, row=4, padx=5, pady=1, sticky=tk.W)

button_2 = tk.Button(root, text="2", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_2)
button_2.grid(column=1, row=2, sticky=tk.W, padx=5, pady=1)

button_5 = tk.Button(root, text="5", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_5)
button_5.grid(column=1, row=3, sticky=tk.W, padx=5, pady=1)

button_8 = tk.Button(root, text="8", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_8)
button_8.grid(column=1, row=4, sticky=tk.W, padx=5, pady=1)

button_3 = tk.Button(root, text="3", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_3)
button_3.grid(column=2, row=2, sticky=tk.W, padx=5, pady=1)

button_6 = tk.Button(root, text="6", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_6)
button_6.grid(column=2, row=3, sticky=tk.W, padx=5, pady=1)

button_9 = tk.Button(root, text="9", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_9)
button_9.grid(column=2, row=4, sticky=tk.W, padx=5, pady=1)

button_0 = tk.Button(root, text="0", font=("Times New Roman", 20),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_0)
button_0.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=1, columnspan=2)

#special buttons
button_division = tk.Button(root, text="÷", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_div)
button_division.grid(column=3, row=1, sticky=tk.W, padx=5, pady=1)

button_multiplication = tk.Button(root, text="×", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_mult)
button_multiplication.grid(column=3, row=2, sticky=tk.W, padx=5, pady=1)

button_minus = tk.Button(root, text="-", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_minus)
button_minus.grid(column=3, row=3, sticky=tk.W, padx=5, pady=1)

button_plus = tk.Button(root, text="+", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_plus)
button_plus.grid(column=3, row=4, sticky=tk.W, padx=5, pady=1)

button_equal = tk.Button(root, text="=", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_result)
button_equal.grid(column=3, row=5, sticky=tk.W, padx=5, pady=1)

button_dot = tk.Button(root, text=".", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_dot)
button_dot.grid(column=2, row=5, sticky=tk.W, padx=5, pady=1)

button_c = tk.Button(root, text="C", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=delete_entry_line)
button_c.grid(column=0, row=1, padx=5, pady=1, sticky=tk.W)

button_degree = tk.Button(root, text="ⁿ", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_degree)
button_degree.grid(column=1, row=1, sticky=tk.W, padx=5, pady=1)

button_percent = tk.Button(root, text="%", font=("Times New Roman", 20, "bold"),
                     height=2, width=2, bg="black", fg="black", command=insert_symbol_percent)
button_percent.grid(column=2, row=1, sticky=tk.W, padx=5, pady=1)


root.mainloop()

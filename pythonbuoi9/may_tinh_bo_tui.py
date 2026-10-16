import tkinter as tk
root = tk.Tk()
root.title("Máy tính đơn giản")
root.geometry("260x320")
root.resizable(False, False)
entry = tk.Entry(root, width=16, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def click(val):
    entry.insert(tk.END, str(val))
def clear():
    entry.delete(0, tk.END)
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Lỗi")
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]
for (text, r, c) in buttons:
    if text == 'C':
        cmd = clear
    elif text == '=':
        cmd = calculate
    else:
        cmd = lambda t=text: click(t)  
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 12), command=cmd).grid(row=r, column=c, padx=3, pady=3)
root.mainloop()
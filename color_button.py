from tkinter import *
from tkinter import ttk

def apply_color():
    if entry_hex.get():
        canvas.itemconfig(rect, fill=entry_hex.get())
    else:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.itemconfig(rect, fill=color)
root = Tk()
root.title("colors.com")
root.geometry("300x400")

Label(root, text="#(HEX):").pack()
entry_hex = Entry(root)
entry_hex.pack()

Label(root, text="r(0-255):").pack()
entry_r = Entry(root)
entry_r.pack()

Label(root, text="g(0-255):").pack()
entry_g = Entry(root)
entry_g.pack()

Label(root, text="b(0-255):").pack()
entry_b = Entry(root)
entry_b.pack()

btn = (ttk.Button(text="color",command=apply_color))
btn.pack(pady=10)

canvas = Canvas(root, width=200,height=100)
canvas.pack()
rect = canvas.create_rectangle(5,5,195,95, fill="white")
root.mainloop()с
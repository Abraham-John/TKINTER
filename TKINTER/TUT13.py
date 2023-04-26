import tkinter as tk
root= tk.Tk()
root.geometry("300x200")

def change_title():
    root.title(f"{title_change.get()}")

title_change = tk.StringVar()

tk.Label(root, text="TITLE",padx=20,pady=15).grid()
tk.Entry(root,textvariable=title_change).grid(row=0,column=1)

tk.Button(root,text="submit", command=change_title).grid(row=1,column=1)

root.mainloop()
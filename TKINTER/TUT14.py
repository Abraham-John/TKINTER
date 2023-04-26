import tkinter as tk
root = tk.Tk()
root.geometry("300x200")

def submit():
    print(radio.get())
    print(check.get())

tk.Label(root,text="DID YOU WASH YOUR ASs TODAY?",padx=20,pady=15).pack()

radio = tk.StringVar()
radio.set("r")

check = tk.IntVar()

tk.Radiobutton(root, text="YES", variable= radio, value="AS YOU SHOULD BISH").pack()
tk.Radiobutton(root, text="NO", variable= radio, value="WTF EWWW").pack()
tk.Checkbutton(root, text="confirm",variable= check).pack

tk.Button(root, text= "submit" ,command=submit).pack()

root.mainloop()
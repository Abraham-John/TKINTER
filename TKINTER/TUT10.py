import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

def submit():
    with open("data.csv" , "a") as f:
        f.write(f"Name : {nameEntry.get()} , Email: {emailEntry.get()},Password: {passwordEntry.get()} ,Phone: {phoneEntry.get()}\n")


tk.Label(root, text="Contact me " , padx=20,pady=15).grid()

tk.Label(root, text="Name: ").grid(row=1,column=0) 
tk.Label(root, text="Email: ").grid(row=2,column=0) 
tk.Label(root, text="Password: ").grid(row=3,column=0) 
tk.Label(root, text="Phone: ").grid(row=4,column=0)

name = tk.StringVar
email = tk.StringVar
password= tk.StringVar
phone= tk.StringVar

nameEntry = tk.Entry(root , textvariable=name)
emailEntry = tk.Entry(root , textvariable=email)
passwordEntry = tk.Entry(root , textvariable=password)
phoneEntry = tk.Entry(root , textvariable=phone)

nameEntry.grid(row=1,column=1)
emailEntry.grid(row=2,column=1)
passwordEntry.grid(row=3,column=1)
phoneEntry.grid(row=4,column=1)

tk.Button(text="submit", command=submit).grid(row=5,column=1)


root.mainloop()


import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

def click():
    with open("click.csv" , "a") as f:
        f.write(f"name : {nameEntry.get()}")

tk.Label(root,text="Name",padx=15,pady=10).grid()

tk.Label(root,text="Enter name").grid(row=1,column=0)

name = tk.StringVar()

nameEntry = tk.Entry(root,textvariable= name)
nameEntry.grid(row=1,column=1)

tk.Button(root,text="submit",command=click).grid(row=5,column=1)
root.mainloop()
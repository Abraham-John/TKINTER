import tkinter as tk
root = tk.Tk()
root.geometry("500x500")


def submit():
    print(f"Name: {nameEntry.get()}") 
    print(f"class:  {class_Entry.get()}")
    print(f"Section:  {sectionEntry.get()}")
    print(f"Roll no.:  {roll_noEntry.get()}")


tk.Label(root, text="Details" , padx=20,pady=15).grid()

tk.Label(root,text= "Name  :").grid(row=1,column=0)
tk.Label(root,text= "Class :").grid(row=2,column=0)
tk.Label(root,text= "Section  :").grid(row=3,column=0)
tk.Label(root,text= "Roll No.  :").grid(row=4,column=0)

name = tk.StringVar
class_ = tk.StringVar
section = tk.StringVar
Roll_No = tk.StringVar

nameEntry = tk.Entry(root,textvariable=name)
class_Entry = tk.Entry(root,textvariable=class_)
sectionEntry = tk.Entry(root,textvariable=section)
roll_noEntry = tk.Entry(root,textvariable=Roll_No)

nameEntry.grid(row=1 ,column= 1)
class_Entry.grid(row=2 ,column= 1)
sectionEntry.grid(row=3 ,column= 1)
roll_noEntry.grid(row=4 ,column= 1) 




tk.Button(root, text="submit",command=submit).grid(row=5,column=1)



root.mainloop()


